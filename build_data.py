# -*- coding: utf-8 -*-
"""Join every source into out/dataset.json, the single input to the renderer.

Zone A: 218 script records, descent, metadata, glyph specimens.
Zone B: every Glottolog language, its family, endangerment, speakers, and the
script(s) it is written in.
"""
import os, re, sys, csv, json, collections

csv.field_size_limit(10 ** 8)
BASE = os.path.dirname(os.path.abspath(__file__))
DATA, OUT = os.path.join(BASE, "data"), os.path.join(BASE, "out")
sys.path.insert(0, BASE)
from genealogy import G, SOURCES

# Glottolog files some languoids under top-level "pseudo-families" that are
# categories, not lineages. They are kept on the plate but not counted as
# families: the first version counted them and printed 245 instead of 238.
PSEUDO_FAMILIES = {"Bookkeeping", "Unclassifiable", "Unattested", "Pidgin", "Mixed Language",
                   "Sign Language", "Speech Register", "Artificial Language"}

SPECIAL = {"Zinh", "Zyyy", "Zzzz", "Zmth", "Zsym", "Zxxx"}
# the Unicode scripts ISO 15924 defines its composites and variants by, so a
# name can be tested as written in them
PARTS = {"Jpan": {"Han", "Hiragana", "Katakana"}, "Kore": {"Hangul", "Han"},
         "Hanb": {"Han", "Bopomofo"}, "Hrkt": {"Hiragana", "Katakana"},
         "Hans": {"Han"}, "Hant": {"Han"}}


def iso15924():
    out = {}
    for line in open(os.path.join(DATA, "iso15924.txt"), encoding="utf8"):
        if not line.strip() or line.startswith("#"):
            continue
        code, num, en, fr, pva, uv, date = line.rstrip("\n").split(";")
        if code in SPECIAL or re.match(r"^Q[a-b][a-z]{2}$", code):
            continue
        out[code] = {"code": code, "num": num, "name": en, "name_fr": fr,
                     "pva": pva, "unicode": uv, "iso_date": date}
    return out


def unicode_blocks(scripts_needed):
    """PVA -> (first codepoint, count) so the plate can state the encoding."""
    span = collections.defaultdict(lambda: [None, 0])
    for line in open(os.path.join(DATA, "Scripts.txt"), encoding="utf8"):
        line = line.split("#")[0].strip()
        if not line:
            continue
        rng, name = [x.strip() for x in line.split(";")]
        a, _, b = rng.partition("..")
        lo, hi = int(a, 16), int(b or a, 16)
        s = span[name]
        s[0] = lo if s[0] is None else min(s[0], lo)
        s[1] += hi - lo + 1
    return {k: tuple(v) for k, v in span.items()}


def wikidata(name):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return []
    return json.load(open(p, encoding="utf8"))["results"]["bindings"]


def build_scripts():
    iso = iso15924()
    blocks = unicode_blocks(set())
    glyphs = json.load(open(os.path.join(OUT, "glyphs.json"), encoding="utf8"))

    # native names from Wikidata, keyed by ISO 15924 code
    native = {}
    for b in wikidata("wd_scripts.json"):
        c = b.get("code", {}).get("value")
        n = b.get("native", {}).get("value")
        if c and n and c not in native:
            native[c] = n

    out = {}
    for code, rec in iso.items():
        if code not in G:
            raise SystemExit("genealogy is missing %s" % code)
        parent, edge, typ, direction, start, end, status = G[code]
        via, source, note = SOURCES.get(code, ("", "", ""))
        lo, n = blocks.get(rec["pva"], (None, 0))
        out[code] = dict(rec,
                         parent=parent, edge=edge, type=typ, direction=direction,
                         start=start, end=end, status=status,
                         via=via, source=source, source_note=note,
                         native=native.get(code),
                         block_start=lo, block_size=n,
                         encoded=bool(rec["unicode"]),
                         glyph=glyphs["glyphs"].get(code),
                         glyph_miss=glyphs["misses"].get(code))
    return out


def build_languages():
    langs, meta = {}, {}
    with open(os.path.join(DATA, "glottolog_languages.csv"), encoding="utf8", newline="") as f:
        for r in csv.DictReader(f):
            if r["Level"] != "language":
                continue
            langs[r["ID"]] = {
                "id": r["ID"], "name": r["Name"], "iso": r["ISO639P3code"],
                # English spans three macroareas; keeping only the first, as
                # this once did, put it in Africa
                "macroareas": [m for m in (r["Macroarea"] or "").split(";") if m],
                "family": r["Family_ID"] or r["ID"],
                "isolate": r["Is_Isolate"] == "true",
            }
    # family display names
    fam_name = {}
    with open(os.path.join(DATA, "glottolog_languages.csv"), encoding="utf8", newline="") as f:
        for r in csv.DictReader(f):
            if r["Level"] == "family":
                fam_name[r["ID"]] = r["Name"]

    # endangerment + category
    aes, cat = {}, {}
    with open(os.path.join(DATA, "glottolog_values.csv"), encoding="utf8", newline="") as f:
        for r in csv.DictReader(f):
            if r["Parameter_ID"] == "aes":
                aes[r["Language_ID"]] = (r["Code_ID"] or "").replace("aes-", "")
            elif r["Parameter_ID"] == "category":
                cat[r["Language_ID"]] = (r["Code_ID"] or "").replace("category-", "")

    by_iso = {v["iso"]: k for k, v in langs.items() if v["iso"]}

    speakers = {}
    for b in wikidata("wd_speakers.json"):
        gid = by_iso.get(b["iso"]["value"])
        if not gid:
            continue
        try:
            n = float(b["n"]["value"])
        except ValueError:
            continue
        speakers[gid] = max(speakers.get(gid, 0), n)

    valid = set(build_scripts())
    lang_scripts = collections.defaultdict(set)
    src_count = collections.Counter()
    for b in wikidata("wd_lang_script.json"):
        gid = by_iso.get(b["iso"]["value"])
        c = b.get("scCode", {}).get("value")
        if gid and c in valid:
            lang_scripts[gid].add(c)
            src_count["wikidata"] += 1

    # CLDR languageData is a second, independently maintained opinion on which
    # script a language uses. It is keyed by BCP47, so bridge 639-1 to 639-3.
    import xml.etree.ElementTree as ET
    part1 = {}
    with open(os.path.join(DATA, "iso-639-3.tab"), encoding="utf8") as f:
        rd = csv.DictReader(f, delimiter="\t")
        for r in rd:
            if r.get("Part1"):
                part1[r["Part1"]] = r["Id"]
    root = ET.parse(os.path.join(DATA, "cldr_supplemental.xml")).getroot()
    cldr_primary = {}
    for el in root.iter("language"):
        t, sc = el.get("type"), el.get("scripts")
        if not t or not sc:
            continue
        iso3 = part1.get(t, t if len(t) == 3 else None)
        gid = by_iso.get(iso3)
        if not gid:
            continue
        for c in sc.split():
            if c in valid:
                lang_scripts[gid].add(c)
                src_count["cldr"] += 1
                if el.get("alt") != "secondary" and gid not in cldr_primary:
                    cldr_primary[gid] = c
    # SIL langtags.json, curated with the Ethnologue script editor. A tagset
    # flagged unwritten can still carry a script "due to regional inference"
    # (langtags.md), so an unwritten tagset never contributes a script: it
    # only records that the language is listed as unwritten. Zyyy (unknown),
    # Zxxx (sign) and the other special codes are not scripts.
    sil_unwritten = set()
    lt_primary = {}       # the script of the language's minimal tag, its default orthography
    by_source = collections.defaultdict(lambda: collections.defaultdict(set))
    for gid, scs in lang_scripts.items():
        for c in scs:
            by_source[gid]["wikidata or cldr"].add(c)
    lt = json.load(open(os.path.join(DATA, "langtags.json"), encoding="utf8"))
    for t in lt:
        if not isinstance(t, dict) or t.get("tag", "").startswith("_"):
            continue
        gid = by_iso.get(t.get("iso639_3"))
        if not gid:
            continue
        if t.get("unwritten"):
            sil_unwritten.add(gid)
            continue
        c = t.get("script")
        if c in valid:
            lang_scripts[gid].add(c)
            by_source[gid]["langtags"].add(c)
            src_count["langtags"] += 1
            if "-" not in t.get("tag", "-"):
                lt_primary[gid] = c
    print("script links: %s" % dict(src_count))

    # corrections.py: the few links the sources get wrong, each with its authority
    from corrections import CORRECTIONS
    forced_main = {}
    for iso, sc, action, _src, _note in CORRECTIONS:
        gid = by_iso.get(iso)
        if not gid:
            continue
        if action == "drop":
            lang_scripts[gid].discard(sc)
            for k in by_source[gid]:
                by_source[gid][k].discard(sc)
        elif action == "add":
            lang_scripts[gid].add(sc)
            by_source[gid]["corrections"].add(sc)
        elif action == "main":
            forced_main[gid] = sc

    dropped = []
    for gid, v in langs.items():
        v["aes"] = aes.get(gid, "unknown")
        v["category"] = cat.get(gid, "")
        v["speakers"] = speakers.get(gid)
        v["scripts"] = sorted(lang_scripts.get(gid, []))
        v["script_sources"] = sorted(k for k, scs in by_source.get(gid, {}).items() if scs)
        # which script a language hangs under on the plate, when it has several
        if not v["scripts"]:
            v["primary_script"], v["primary_basis"] = None, None
        elif forced_main.get(gid) in v["scripts"]:
            v["primary_script"], v["primary_basis"] = forced_main[gid], "corrections.py"
        elif len(v["scripts"]) == 1:
            v["primary_script"], v["primary_basis"] = v["scripts"][0], "only script"
        elif lt_primary.get(gid) in v["scripts"]:
            v["primary_script"], v["primary_basis"] = lt_primary[gid], "langtags default"
        elif cldr_primary.get(gid) in v["scripts"]:
            v["primary_script"], v["primary_basis"] = cldr_primary[gid], "cldr primary"
        else:
            # Members of a macrolanguage (Mandarin under zh, Malay under ms)
            # have their default tagset filed under the macrolanguage, so
            # langtags leaves them only special tagsets such as Braille. Prefer
            # what Wikidata states, and never let Braille, a recoding of
            # another script, be the main script when there is another.
            pool = [c for c in v["scripts"] if c != "Brai"] or v["scripts"]
            wd = sorted(c for c in by_source[gid].get("wikidata or cldr", ()) if c in pool)
            if wd:
                v["primary_script"], v["primary_basis"] = wd[0], "wikidata or cldr, first by code"
            else:
                v["primary_script"], v["primary_basis"] = pool[0], "alphabetical, no source ranks them"
        v["sil_unwritten"] = gid in sil_unwritten
        if v["category"] == "Artificial_Language":
            dropped.append(gid)
    for gid in dropped:                       # spec excludes constructed languages
        del langs[gid]
    return langs, fam_name, len(dropped)


if __name__ == "__main__":
    scripts = build_scripts()
    langs, fam_name, n_artificial = build_languages()

    fams = collections.Counter(v["family"] for v in langs.values())
    with_script = sum(1 for v in langs.values() if v["scripts"])
    # Native names: Wikidata P1705 where it exists, else the script's Wikidata
    # label in the language it mainly writes (the largest language hung under
    # it), kept only if the label is written in that script itself, so a
    # transliteration never passes for a native name.
    for c, s in scripts.items():
        s["native_source"] = "Wikidata P1705" if s["native"] else None
    cp_script = {}
    for line in open(os.path.join(DATA, "Scripts.txt"), encoding="utf8"):
        line = line.split("#")[0].strip()
        if not line:
            continue
        rng, sc = [x.strip() for x in line.split(";")]
        lo, _, hi = rng.partition("..")
        for cp in range(int(lo, 16), int(hi or lo, 16) + 1):
            cp_script[cp] = sc
    part1 = {}
    with open(os.path.join(DATA, "iso-639-3.tab"), encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("Part1"):
                part1[r["Id"]] = r["Part1"]
    labels = collections.defaultdict(dict)
    for b in wikidata("wd_script_labels.json"):
        lab = b["label"]
        labels[b["code"]["value"]][lab.get("xml:lang", "")] = lab["value"]
    hung = collections.defaultdict(list)
    for v in langs.values():
        if v["primary_script"] and v["iso"]:
            hung[v["primary_script"]].append(v)
    for c, s in scripts.items():
        # Latin writes languages of some 270 families: no one of them owns its name
        if s["native"] or c == "Latn":
            continue
        # largest language first; English is the plate's own language, not a native one
        for v in sorted(hung.get(c, []), key=lambda v: -(v["speakers"] or 0)):
            tag = part1.get(v["iso"], v["iso"])
            lab = labels.get(c, {}).get(tag)
            if tag != "en" and lab and any(cp_script.get(ord(ch)) == s["pva"] for ch in lab):
                s["native"] = lab
                s["native_source"] = "Wikidata label in %s" % v["name"]
                break

    # Then CLDR's display name for the script in that language's locale. A
    # macrolanguage member is reached through langtags, which files Mandarin
    # (cmn) under zh.
    cldr = json.load(open(os.path.join(DATA, "cldr_script_names.json"), encoding="utf8"))
    locale = {}
    for t in json.load(open(os.path.join(DATA, "langtags.json"), encoding="utf8")):
        if isinstance(t, dict) and not t.get("tag", "_").startswith("_"):
            base = t["tag"].split("-")[0]
            for alias in [t.get("iso639_3") or ""] + t.get("tags", []):
                locale.setdefault(alias.split("-")[0], base)
    for c, s in scripts.items():
        if s["native"] or c == "Latn":
            continue
        ok = PARTS.get(c, {s["pva"]})
        for v in sorted(hung.get(c, []), key=lambda v: -(v["speakers"] or 0)):
            for tag in dict.fromkeys([part1.get(v["iso"], v["iso"]), locale.get(v["iso"])]):
                lab = cldr["locales"].get(tag, {}).get(c)
                if tag and tag != "en" and lab and any(cp_script.get(ord(ch)) in ok for ch in lab):
                    s["native"] = lab
                    s["native_source"] = "CLDR %s name in %s" % (cldr["version"], v["name"])
                    break
            if s["native"]:
                break

    stats = {
        "iso15924_total_rows": 226,
        "iso15924_special_removed": 8,
        "scripts": len(scripts),
        "scripts_with_glyph": sum(1 for s in scripts.values() if s["glyph"]),
        "scripts_without_glyph": sum(1 for s in scripts.values() if not s["glyph"]),
        "scripts_encoded": sum(1 for s in scripts.values() if s["encoded"]),
        "scripts_not_encoded": sum(1 for s in scripts.values() if not s["encoded"]),
        "scripts_with_native_name": sum(1 for s in scripts.values() if s["native"]),
        "origins": sorted(k for k, v in scripts.items() if v["parent"] is None),
        "languages": len(langs),
        "artificial_dropped": n_artificial,
        "families": len([f for f in fams if not langs[[g for g in langs if langs[g]['family'] == f][0]]["isolate"]]) if langs else 0,
        "isolates": sum(1 for v in langs.values() if v["isolate"]),
        "languages_with_script": with_script,
        "languages_without_script": len(langs) - with_script,
        "languages_recorded_unwritten": sum(1 for v in langs.values()
                                            if not v["scripts"] and v["sil_unwritten"]),
        "languages_multiscript": sum(1 for v in langs.values() if len(v["scripts"]) > 1),
        "primary_alphabetical": sum(1 for v in langs.values()
                                    if (v["primary_basis"] or "").startswith("alphabetical")),
        "languages_scripted_only_by_langtags": sum(1 for v in langs.values()
                                                   if v["script_sources"] == ["langtags"]),
        "languages_with_speakers": sum(1 for v in langs.values() if v["speakers"]),
        "sign_languages": sum(1 for v in langs.values() if v["category"] == "Sign_Language"),
        "extinct": sum(1 for v in langs.values() if v["aes"] == "extinct"),
        "aes": dict(collections.Counter(v["aes"] for v in langs.values())),
        "macroareas": dict(collections.Counter(m for v in langs.values() for m in v["macroareas"] or [""])),
    }
    fam_ids = {v["family"] for v in langs.values() if not v["isolate"]}
    pseudo = {f for f in fam_ids if fam_name.get(f) in PSEUDO_FAMILIES}
    stats["families"] = len(fam_ids - pseudo)
    stats["pseudo_families"] = sorted(fam_name[f] for f in pseudo)
    stats["languages_in_pseudo_families"] = sum(1 for v in langs.values()
                                                if not v["isolate"] and v["family"] in pseudo)

    json.dump({"scripts": scripts, "languages": langs, "family_names": fam_name,
               "stats": stats},
              open(os.path.join(OUT, "dataset.json"), "w", encoding="utf8"), ensure_ascii=False)
    for k, v in stats.items():
        print("%-28s %s" % (k, v if not isinstance(v, list) else "%d %s" % (len(v), v)))
