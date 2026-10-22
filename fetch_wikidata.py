"""Wikidata pulls. Saves raw SPARQL JSON to data/. No derivation here."""
import os, sys, json, time, urllib.request, urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
EP = "https://query.wikidata.org/sparql"
UA = {"User-Agent": "writing-genealogy/1.0 (offline research plate; python-urllib)",
      "Accept": "application/sparql-results+json"}

QUERIES = {
    # language (ISO 639-3) -> writing system, with the script's ISO 15924 code
    "wd_lang_script.json": """
SELECT ?iso ?sc ?scCode ?scLabel WHERE {
  ?l wdt:P220 ?iso .
  ?l wdt:P282 ?sc .
  OPTIONAL { ?sc wdt:P506 ?scCode . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}""",

    # language (Glottocode) -> writing system: reaches the languages with no
    # ISO 639-3 code, which every other script source keys on
    "wd_glotto_script.json": """
SELECT ?g ?scCode WHERE {
  ?l wdt:P1394 ?g .
  ?l wdt:P282 ?sc .
  ?sc wdt:P506 ?scCode .
}""",

    # language (ISO 639-3) -> speaker count, keep the max per language downstream
    "wd_speakers.json": """
SELECT ?iso ?n WHERE {
  ?l wdt:P220 ?iso .
  ?l wdt:P1098 ?n .
}""",

    # every label of every script item, in every language: a script's name in
    # the language it mainly writes is its native name when P1705 is missing
    "wd_script_labels.json": """
SELECT ?code ?label WHERE {
  ?sc wdt:P506 ?code .
  ?sc rdfs:label ?label .
}""",

    # every entity carrying an ISO 15924 code, with descent + metadata
    "wd_scripts.json": """
SELECT ?sc ?code ?scLabel ?native ?inception ?based ?basedCode ?dir ?dirLabel ?instLabel WHERE {
  ?sc wdt:P506 ?code .
  OPTIONAL { ?sc wdt:P1705 ?native . }
  OPTIONAL { ?sc wdt:P571  ?inception . }
  OPTIONAL { ?sc wdt:P144  ?based . OPTIONAL { ?based wdt:P506 ?basedCode . } }
  OPTIONAL { ?sc wdt:P1406 ?dir . }
  OPTIONAL { ?sc wdt:P31   ?inst . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}""",
}


def run(q, tries=6):
    # WDQS is rate-limiting to 1 req/min during an outage; back off past that window.
    url = EP + "?" + urllib.parse.urlencode({"query": q, "format": "json"})
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300) as r:
                return json.loads(r.read())
        except Exception as e:
            last = e
            print("     retry %d after %s" % (i + 1, str(e)[:70]), flush=True)
            time.sleep(70)
    raise last


if __name__ == "__main__":
    os.makedirs(DATA, exist_ok=True)
    failed = []
    for name, q in QUERIES.items():
        dest = os.path.join(DATA, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 500:
            d = json.load(open(dest, encoding="utf8"))
            print("%-22s cached %d rows" % (name, len(d["results"]["bindings"])))
            continue
        try:
            d = run(q)
            json.dump(d, open(dest, "w", encoding="utf8"))
            print("%-22s %d rows" % (name, len(d["results"]["bindings"])), flush=True)
        except Exception as e:
            print("%-22s FAIL %s" % (name, str(e)[:160]), flush=True)
            failed.append(name)
        time.sleep(70)
    if failed:
        sys.exit("FAILED: %s" % ", ".join(failed))
