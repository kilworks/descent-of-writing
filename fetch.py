"""Download every raw source. Nothing derived here, only bytes to disk."""
import os, sys, json, urllib.request, ssl, time

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
CTX = ssl.create_default_context()
UA = {"User-Agent": "writing-genealogy/1.0 (research plate; contact via local)"}

SOURCES = {
    "iso15924.txt":  "https://www.unicode.org/iso15924/iso15924.txt",
    "Scripts.txt":   "https://www.unicode.org/Public/UCD/latest/ucd/Scripts.txt",
    "Blocks.txt":    "https://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt",
    "PropertyValueAliases.txt": "https://www.unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt",
    "DerivedAge.txt": "https://www.unicode.org/Public/UCD/latest/ucd/DerivedAge.txt",
    "DerivedGeneralCategory.txt": "https://www.unicode.org/Public/UCD/latest/ucd/extracted/DerivedGeneralCategory.txt",
    "ReadMe.txt":    "https://www.unicode.org/Public/UCD/latest/ucd/ReadMe.txt",
    "glottolog_languages.csv":  "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/languages.csv",
    "glottolog_values.csv":     "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/values.csv",
    "glottolog_parameters.csv": "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/parameters.csv",
    "glottolog_codes.csv":      "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/codes.csv",
    "glottolog_metadata.json":  "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/cldf-metadata.json",
    # second opinion on which script a language is written in, and the 639-1 to
    # 639-3 bridge CLDR needs to be joined to Glottolog
    "cldr_supplemental.xml":    "https://raw.githubusercontent.com/unicode-org/cldr/main/common/supplemental/supplementalData.xml",
    "iso-639-3.tab":            "https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3.tab",
    # SIL Writing Systems Technology: scripts per language, curated with the
    # Ethnologue script editor, and an explicit flag for unwritten languages
    "langtags.json":            "https://ldml.api.sil.org/langtags.json",
    # Table 6-1, Unicode's typology of scripts, which the type column follows
    "unicode_ch06.html":        "https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-6/",
}


def get(url, dest, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
                body = r.read()
            with open(dest, "wb") as f:
                f.write(body)
            return len(body)
        except Exception as e:
            if i == tries - 1:
                return "FAIL: %s" % e
            time.sleep(2 + 3 * i)


def cldr_script_names(dest):
    """CLDR's name for each script in each base locale, kept per locale as
    published (cldr-localenames-full), with the CLDR version."""
    reg = json.loads(urllib.request.urlopen(urllib.request.Request(
        "https://registry.npmjs.org/cldr-localenames-full/latest", headers=UA), timeout=90, context=CTX).read())
    v, cdn = reg["version"], "https://cdn.jsdelivr.net/npm/%s@%s/%s"

    def load(path):
        try:
            req = urllib.request.Request(cdn % (path[0], v, path[1]), headers=UA)
            with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:       # a locale with no scripts.json names no script
                return None
            raise

    locs = [l for l in load(("cldr-core", "availableLocales.json"))["availableLocales"]["full"] if "-" not in l]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(16) as ex:
        got = ex.map(lambda l: load(("cldr-localenames-full", "main/%s/scripts.json" % l)), locs)
        out = {"version": v, "locales": {l: d["main"][l]["localeDisplayNames"]["scripts"]
                                         for l, d in zip(locs, got) if d}}
    json.dump(out, open(dest, "w", encoding="utf8"), ensure_ascii=False)
    return "%d locales, CLDR %s" % (len(out["locales"]), v)


if __name__ == "__main__":
    os.makedirs(DATA, exist_ok=True)    # data/ is gitignored, so a fresh clone has none
    failed = []
    dest = os.path.join(DATA, "cldr_script_names.json")
    if not os.path.exists(dest):
        try:
            r = cldr_script_names(dest)
        except Exception as e:
            r = "FAIL: %s" % e
        print("%-30s %s" % ("cldr_script_names.json", r))
        if r.startswith("FAIL"):
            failed.append("cldr_script_names.json")
    for name, url in SOURCES.items():
        dest = os.path.join(DATA, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            print("%-30s cached %d b" % (name, os.path.getsize(dest)))
            continue
        r = get(url, dest)
        print("%-30s %s" % (name, r))
        if isinstance(r, str):
            failed.append(name)
    if failed:
        sys.exit("FAILED: %s" % ", ".join(failed))
