# -*- coding: utf-8 -*-
"""Cross-check the language-to-script links against LinguaMeta. Report only.

LinguaMeta (Google Research, Ritchie et al., LREC-COLING 2024) tags every
script it gives a language with the source it came from. Only the scripts
it sourced to its own curation (GOOGLE_RESEARCH) are used here: the ones it
took from Wiktionary are already tested by crosscheck_wiktionary.py, and the
ones it assumed from a locale prove nothing. It is CC BY-SA, so, as with
Wiktionary, nothing from it is written into the dataset; this script only
measures agreement with the links resting on SIL langtags alone.

    python crosscheck_linguameta.py          # writes out/crosscheck_linguameta.txt
"""
import os, csv, json, collections, urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.path.dirname(os.path.abspath(__file__))
DATA, OUT = os.path.join(BASE, "data"), os.path.join(BASE, "out")
LM = os.path.join(DATA, "linguameta")
RAW = "https://raw.githubusercontent.com/google-research/url-nlp/main/linguameta/"
UA = {"User-Agent": "descent-of-writing/1.0 (research plate; cross-check only)"}


def fetch(path):
    dest = os.path.join(LM, path.replace("/", "_"))
    if not os.path.exists(dest):
        try:
            body = urllib.request.urlopen(urllib.request.Request(RAW + path, headers=UA), timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise
        open(dest, "wb").write(body)
    return open(dest, encoding="utf8").read()


def own_scripts(doc):
    """The ISO 15924 codes LinguaMeta sources to its own curation."""
    out = set()
    for x in json.loads(doc).get("language_script_locale", []):
        s = x.get("script", {})
        if s.get("source") == "GOOGLE_RESEARCH" and s.get("iso_15924_code", "xxxx") != "xxxx":
            out.add(s["iso_15924_code"].title())
    return out


def main():
    os.makedirs(LM, exist_ok=True)
    bcp = {r["iso_639_3_code"]: r["bcp_47_code"]
           for r in csv.DictReader(fetch("linguameta.tsv").splitlines(), delimiter="\t") if r["iso_639_3_code"]}
    L = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))["languages"]
    alone = [v for v in L.values() if v["script_sources"] == ["langtags"]]
    with ThreadPoolExecutor(16) as ex:
        docs = list(ex.map(lambda v: fetch("data/%s.json" % bcp[v["iso"]]) if v["iso"] in bcp else None, alone))

    # Wiktionary's verdicts, from the cached modules, to count languages
    # confirmed by either of the two
    import crosscheck_wiktionary as cw
    wk = {}
    for t in cw.PAGES:
        try:
            wk.update(cw.scripts_of(cw.fetch(t)))
        except Exception:
            pass
    part1 = {r["Id"]: r["Part1"] for r in csv.DictReader(
        open(os.path.join(DATA, "iso-639-3.tab"), encoding="utf8"), delimiter="\t") if r.get("Part1")}

    tally, disagree, either = collections.Counter(), [], 0
    for v, doc in zip(alone, docs):
        own = own_scripts(doc) if doc else set()
        w = wk.get(v["iso"]) or wk.get(part1.get(v["iso"], "")) or set()
        if not own:
            tally["no LinguaMeta curation of its own"] += 1
        elif own & set(v["scripts"]):
            tally["agrees on at least one script"] += 1
        else:
            tally["disagrees"] += 1
            disagree.append((v["name"], v["iso"], sorted(v["scripts"]), sorted(own)))
        either += bool((own | w) & set(v["scripts"]))
    n = len(alone)
    lines = ["LinguaMeta (google-research/url-nlp, linguameta), CC BY-SA 4.0, quoted for review only.",
             "Only scripts LinguaMeta sources to its own curation (GOOGLE_RESEARCH) are used.",
             "",
             "Cross-check of the %d languages whose script rests on SIL langtags alone." % n, ""]
    for k, c in tally.most_common():
        lines.append("%-42s %5d  %5.1f%%" % (k, c, 100 * c / n))
    checked = tally["agrees on at least one script"] + tally["disagrees"]
    if checked:
        lines += ["", "Agreement where both speak: %d of %d (%.1f%%)."
                  % (tally["agrees on at least one script"], checked,
                     100 * tally["agrees on at least one script"] / checked)]
    lines += ["Confirmed by LinguaMeta or Wiktionary or both: %d of %d (%.1f%%)." % (either, n, 100 * either / n),
              "", "Disagreements (name, ISO 639-3, langtags, LinguaMeta):"]
    for row in sorted(disagree):
        lines.append("  %s [%s]  %s  vs  %s" % (row[0], row[1], ",".join(row[2]), ",".join(row[3])))
    open(os.path.join(OUT, "crosscheck_linguameta.txt"), "w", encoding="utf8", newline="\n").write("\n".join(lines) + "\n")
    print("\n".join(lines[3:14]))


if __name__ == "__main__":
    main()
