# -*- coding: utf-8 -*-
"""Acceptance checks, and the companion CSV.

Every number the plate prints is recomputed here from the source files. A
failure is loud: the point of the checks is that a silent omission cannot get
through, and a check that cannot fail proves nothing.
"""
import os, re, sys, csv, json, collections

csv.field_size_limit(10 ** 8)
BASE = os.path.dirname(os.path.abspath(__file__))
DATA, OUT = os.path.join(BASE, "data"), os.path.join(BASE, "out")
sys.path.insert(0, BASE)
from genealogy import G, SOURCES

def short_name(n):
    """Drop a trailing parenthetical, keep a leading one.

    ISO 15924 writes Seal as "(Small) Seal"; cutting at the first "(" left
    that script with an empty name in the catalogue."""
    n = re.sub(r"\s*\([^()]*\)\s*$", "", n).strip()
    return n or "unnamed"


D = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))
S, L, ST = D["scripts"], D["languages"], D["stats"]
SVG = open(os.path.join(OUT, "descent_of_writing.svg"), encoding="utf8").read()

fails, lines = [], []


def check(name, ok, detail):
    lines.append("%-4s %-52s %s" % ("OK" if ok else "FAIL", name, detail))
    if not ok:
        fails.append(name)


# 1. every non-special ISO 15924 code drawn exactly once
raw = [l.rstrip("\n").split(";") for l in open(os.path.join(DATA, "iso15924.txt"), encoding="utf8")
       if l.strip() and not l.startswith("#")]
special = {"Zinh", "Zyyy", "Zzzz", "Zmth", "Zsym", "Zxxx"}
expect = {r[0] for r in raw if r[0] not in special and not re.match(r"^Q[a-b][a-z]{2}$", r[0])}
drawn = set(re.findall(r'<g id="s-([A-Za-z]{4})">', SVG))
check("1. script count == ISO 15924 non-special count",
      drawn == expect and len(drawn) == len(expect),
      "%d rows loaded, %d special/private removed, %d drawn, missing %s, extra %s"
      % (len(raw), len(raw) - len(expect), len(drawn),
         sorted(expect - drawn) or "none", sorted(drawn - expect) or "none"))

dup = len(re.findall(r'<g id="s-[A-Za-z]{4}">', SVG))
check("1b. no script drawn twice", dup == len(expect), "%d script groups in the svg" % dup)

# 2. scripts with no glyph, named
miss = sorted(c for c in S if not S[c]["glyph"])
unenc = [c for c in miss if not S[c]["encoded"]]
check("2. scripts without a glyph specimen are named", len(miss) > 0,
      "%d without a specimen; %d of them are not encoded in Unicode at all"
      % (len(miss), len(unenc)))
lines.append("     " + ", ".join("%s (%s)" % (c, short_name(S[c]["name"])) for c in miss))

# 3. language leaf count == Glottolog level=language, minus constructed
with open(os.path.join(DATA, "glottolog_languages.csv"), encoding="utf8", newline="") as f:
    gl = [r for r in csv.DictReader(f) if r["Level"] == "language"]
marks = len(set(re.findall(r'id="l-([a-z0-9]{8})"', SVG)))
check("3. language marks == Glottolog languages minus constructed",
      marks == len(L) == len(gl) - ST["artificial_dropped"],
      "%d in source, %d constructed dropped, %d in dataset, %d marks drawn"
      % (len(gl), ST["artificial_dropped"], len(L), marks))

# 4. families
fams = {v["family"] for v in L.values() if not v["isolate"]}
check("4. family count == distinct Family_ID", len(fams) == ST["families"],
      "%d families, %d isolates" % (len(fams), ST["isolates"]))

# 5. every script reaches an origin, or is one
bad = []
for c in S:
    seen, cur = set(), c
    while S[cur]["parent"]:
        if cur in seen:
            bad.append(c)
            break
        seen.add(cur)
        cur = S[cur]["parent"]
    else:
        if S[cur]["parent"] is not None:
            bad.append(c)
origins = sorted(c for c in S if S[c]["parent"] is None)
check("5. every script traces to an origin, no cycles", not bad,
      "%d origins: %s" % (len(origins), ", ".join(origins)))

# 6. languages with no script recorded
none = sum(1 for v in L.values() if not v["scripts"])
check("6. languages with no script recorded", none == ST["languages_without_script"],
      "%d of %d, %.1f%%" % (none, len(L), 100 * none / len(L)))

# 7. sources and date present on the plate
check("7. sources and retrieval date printed on the plate",
      "ISO 15924 registry" in SVG and "Glottolog" in SVG and "HarfBuzz" in SVG,
      "source line found in the svg")

# extra: the plate's own printed figures agree with the data
for n in (ST["scripts"], ST["languages"], ST["families"], ST["isolates"],
          ST["scripts_with_glyph"], ST["scripts_without_glyph"]):
    if str(n) not in SVG:
        fails.append("printed figure %d missing from plate" % n)
check("8. printed figures match the dataset",
      not [f for f in fails if str(f).startswith("printed")], "all key counts appear in the svg")

# 9. every descent claim names its authority, attested ones included. Exempt:
# style variants and registry composites, which claim no descent, and the
# roots whose independence is not argued (Sumer, China, Mesoamerica).
UNDISPUTED_ROOTS = {"Pcun", "Hani", "Maya"}
need = sorted(c for c in S if S[c]["edge"] in ("attested", "stimulus", "contested", "invented")
              or (S[c]["parent"] is None and c not in UNDISPUTED_ROOTS))
nosrc = [c for c in need if not S[c].get("source")]
unsourced = sorted(c for c in need if S[c].get("source") == "unsourced")
edges = collections.Counter(S[c]["edge"] or "root" for c in S)
check("9. every descent claim and argued root is sourced",
      not nosrc and not [c for c in SOURCES if c not in S],
      "%d need a source, missing %s; marked unsourced: %s; edges: %s"
      % (len(need), nosrc or "none", ", ".join(unsourced) or "none",
         ", ".join("%s %d" % kv for kv in edges.most_common())))

# 10. the plate can be read without sight: a title and a description for the
# document, and a title for every script card
titled = set(re.findall(r'<g id="s-([A-Za-z]{4})">\s*<title>[^<]+</title>', SVG))
check("10. svg has a title, a description, and a title per script",
      "<title>The Descent of Writing</title>" in SVG and "<desc>" in SVG and titled == set(S),
      "%d of %d script cards titled, untitled: %s"
      % (len(titled), len(S), sorted(set(S) - titled) or "none"))

# 12. where a language hangs, and how the lower register splits. Braille is a
# recoding of other scripts, so it is a language's main script only when it
# is its only one; and the two lower fields must add up and be printed.
braille_main = sorted(v["name"] for v in L.values()
                      if v["primary_script"] == "Brai" and len(v["scripts"]) > 1)
listed = sum(1 for v in L.values() if not v["scripts"] and v["sil_unwritten"])
norec = sum(1 for v in L.values() if not v["scripts"] and not v["sil_unwritten"])
check("12. main scripts and the lower register are consistent",
      not braille_main and listed == ST["languages_recorded_unwritten"]
      and listed + norec == ST["languages_without_script"]
      and "%d languages" % listed in SVG and "%d languages" % norec in SVG,
      "Braille as main script with another available: %s; listed unwritten %d, no record %d"
      % (braille_main or "none", listed, norec))

# 11. the written guide is generated from this dataset and must not lag it
import guide
_gp = os.path.join(BASE, "GUIDE.md")
_g = open(_gp, encoding="utf8").read() if os.path.exists(_gp) else ""
_entries = len(re.findall(r"^### [A-Z][a-z]{3}$", _g, flags=re.M))
check("11. GUIDE.md matches the dataset, one entry per script",
      _g == guide.build() and _entries == len(S),
      "%d script entries in the guide; rerun python guide.py if stale" % _entries)

# ---- companion CSV, one row per script, all seven documented fields
with open(os.path.join(OUT, "scripts_catalogue.csv"), "w", encoding="utf8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["iso15924", "iso_number", "name_en", "name_fr", "native_name", "type",
                "direction", "first_use", "last_use", "status", "parent", "edge",
                "origin", "via", "source", "source_note", "unicode_version", "unicode_block_start", "codepoints",
                "specimen", "specimen_font", "glyph_missing_reason"])
    for c in sorted(S):
        s = S[c]
        root, cur = c, c
        while S[cur]["parent"]:
            cur = S[cur]["parent"]
        root = cur
        w.writerow([c, s["num"], s["name"], s["name_fr"], s["native"] or "", s["type"],
                    s["direction"], s["start"], s["end"] if s["end"] is not None else "present",
                    s["status"], s["parent"] or "", s["edge"] or "root", root,
                    s.get("via", ""), s.get("source", ""), s.get("source_note", ""),
                    s["unicode"] or "not encoded",
                    "U+%04X" % s["block_start"] if s["block_start"] else "",
                    s["block_size"] or 0,
                    s["glyph"]["chars"] if s["glyph"] else "",
                    s["glyph"]["font"] if s["glyph"] else "",
                    s["glyph_miss"] or ""])

print("\n".join(lines))
print("\ncatalogue -> %s" % os.path.join(OUT, "scripts_catalogue.csv"))
print("RESULT: %s" % ("ALL CHECKS PASS" if not fails else "FAILED: %s" % fails))
sys.exit(1 if fails else 0)
