# -*- coding: utf-8 -*-
"""Cross-check the language-to-script links against Wiktionary. Report only.

Wiktionary's language data modules list the scripts of each language code and
are edited independently of SIL, so they are the one open, large source that
can test the links resting on SIL langtags alone. They are CC BY-SA, and the
plate is CC-BY, so nothing from them is written into the dataset: this script
only measures agreement and prints it, with the disagreements, for review.

    python crosscheck_wiktionary.py          # writes out/crosscheck_wiktionary.txt
"""
import os, re, json, time, string, collections, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
DATA, OUT = os.path.join(BASE, "data"), os.path.join(BASE, "out")
UA = {"User-Agent": "descent-of-writing/1.0 (research plate; cross-check only)"}
PAGES = ["Module:languages/data/2"] + ["Module:languages/data/3/" + c for c in string.ascii_lowercase] \
        + ["Module:languages/data/exceptional"]


def fetch(title):
    dest = os.path.join(DATA, "wiktionary_" + re.sub(r"[^A-Za-z0-9]+", "_", title) + ".lua")
    if os.path.exists(dest) and os.path.getsize(dest) > 200:
        return open(dest, encoding="utf8").read()
    url = "https://en.wiktionary.org/w/index.php?" + urllib.parse.urlencode({"title": title, "action": "raw"})
    body = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf8")
    open(dest, "w", encoding="utf8").write(body)
    time.sleep(1)
    return body


ENTRY = re.compile(r'^m\["([a-z]{2,3})"\]\s*=\s*\{(.*?)^\}', re.M | re.S)
FIELD = re.compile(r'"((?:[^"\\]|\\.)*)"|(\d+)|(nil)|(\w+)')


def scripts_of(body):
    """Field 4 of each entry: the script list, a string like "Latn, Arab" or a
    variable naming a shared list. Entries with no field 4 have no script."""
    out = {}
    for code, inner in ENTRY.findall(body):
        fields = [m.group(0) for m in FIELD.finditer(inner.split("\n\t[")[0])][:4]
        if len(fields) < 4:
            continue
        f4 = fields[3]
        if f4.startswith('"'):
            out[code] = set()
            for s in f4.strip('"').split(","):
                out[code] |= NORMAL.get(s.strip().split("-")[-1], {s.strip().split("-")[-1]})
    return out


# Wiktionary's own script codes, mapped back to ISO 15924. A language-prefixed
# code (sjo-Mong, as-Beng) is a local style of the script after the prefix.
NORMAL = {"Hants": {"Hans", "Hant"}, "Aran": {"Arab", "Aran"}, "Polyt": {"Grek"},
          "Kore": {"Kore", "Hang", "Hani"}, "Jpan": {"Jpan", "Hani", "Hira", "Kana"}}


def main():
    import urllib.parse  # noqa: F401  (fetch builds the query with it)
    wk = {}
    for t in PAGES:
        try:
            wk.update(scripts_of(fetch(t)))
        except Exception as e:
            print("skip %s: %s" % (t, e))
    D = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))
    L = D["languages"]
    part1 = {}
    import csv
    with open(os.path.join(DATA, "iso-639-3.tab"), encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("Part1"):
                part1[r["Id"]] = r["Part1"]

    def wk_for(iso):
        return wk.get(iso) or wk.get(part1.get(iso, ""))

    tally = collections.Counter()
    disagree = []
    for v in L.values():
        if v["script_sources"] != ["langtags"]:
            continue
        w = wk_for(v["iso"])
        if w is None:
            tally["no Wiktionary entry or no script listed"] += 1
        elif w & set(v["scripts"]):
            tally["agrees on at least one script"] += 1
        else:
            tally["disagrees"] += 1
            disagree.append((v["name"], v["iso"], sorted(v["scripts"]), sorted(w)))
    n = sum(tally.values())
    lines = ["Wiktionary language data (en.wiktionary.org, Module:languages), CC BY-SA 4.0, quoted for review only.",
             "",
             "Cross-check of the %d languages whose script rests on SIL langtags alone," % n,
             "against Wiktionary's language data modules (%d codes with a script list)." % len(wk), ""]
    for k, c in tally.most_common():
        lines.append("%-42s %5d  %5.1f%%" % (k, c, 100 * c / n))
    checked = tally["agrees on at least one script"] + tally["disagrees"]
    if checked:
        lines.append("")
        lines.append("Agreement where both speak: %d of %d (%.1f%%)."
                     % (tally["agrees on at least one script"], checked,
                        100 * tally["agrees on at least one script"] / checked))
    lines.append("")
    lines.append("Disagreements (name, ISO 639-3, langtags, Wiktionary):")
    for row in sorted(disagree):
        lines.append("  %s [%s]  %s  vs  %s" % (row[0], row[1], ",".join(row[2]), ",".join(row[3])))
    text = "\n".join(lines) + "\n"
    open(os.path.join(OUT, "crosscheck_wiktionary.txt"), "w", encoding="utf8", newline="\n").write(text)
    print("\n".join(lines[2:12]))


if __name__ == "__main__":
    main()
