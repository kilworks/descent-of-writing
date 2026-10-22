# -*- coding: utf-8 -*-
"""Write GUIDE.md, a readable reference generated from out/dataset.json.

The plate is a picture and the CSV is a table. The guide is the same data as
prose a reader can follow: what kinds of script exist, how the links are
drawn, every family tree from its root, and one entry per script with its
parent, the kind of link, the source it rests on, and the languages a source
records it for. It is generated, never edited by hand, so it cannot drift
from the plate; verify.py fails if it is stale.
"""
import os, sys, json, collections

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "out")
GUIDE = os.path.join(BASE, "GUIDE.md")

TYPES = [
    ("logographic", "signs stand for words or morphemes, usually with phonetic "
     "components alongside. Every independent invention of writing began here."),
    ("syllabary", "one sign per syllable, with no shared shape between syllables "
     "that share a consonant (Cherokee, kana, Linear B)."),
    ("abjad", "letters for consonants only, vowels left to the reader or marked "
     "optionally (Phoenician, Hebrew, Arabic). The term is Daniels' (1990)."),
    ("abugida", "a consonant letter carries an inherent vowel, and other vowels "
     "are marks attached to it (Brahmi and its descendants, Ge'ez). Also Daniels'."),
    ("alphabet", "consonants and vowels written as letters of equal standing "
     "(Greek, Latin, Cyrillic, and many twentieth-century inventions)."),
    ("featural", "the shapes encode articulatory features, so related sounds "
     "look related (Hangul, Visible Speech, SignWriting). The term is Sampson's (1985)."),
    ("semasiographic", "signs carry meaning without fixing the words that "
     "express it (Naxi Dongba, Blissymbols)."),
    ("undeciphered", "the type cannot be stated because the script is not read."),
    ("variant", "a registry code for a style or tradition of another script."),
    ("composite", "a registry code bundling several scripts used together."),
    ("symbols", "a registry code for a symbol set that is not a writing system."),
]

EDGES = [
    ("attested", "direct graphical descent: the letter shapes were inherited."),
    ("contested", "a descent claimed in the literature and disputed there. "
     "The entry names both sides."),
    ("stimulus", "a named script lent the idea of writing, or a structure such as "
     "letter order, an inherent vowel or a syllabic layout; the letters were drawn fresh."),
    ("invented", "made on purpose with no ancestor at all. The script is placed "
     "under the one its makers already wrote; that is a placement, not a descent."),
    ("variant", "the same script in another style or orthographic tradition."),
    ("composite", "a registry code that bundles several scripts, not a script."),
]


# The lineages, as prose. Every count in braces is computed from the dataset
# when the guide is written, so the text cannot disagree with the tree; every
# claim is one the SOURCES table of genealogy.py, or the works named here, makes.
LINEAGES = [
    ("One invention behind most of the world: the alphabet",
     """Of the {n_scripts} scripts in the registry, {d_Egyp} descend from Egyptian hieroglyphs, and {d_Psin} of those through a single step: Proto-Sinaitic. Around {y_Psin}, Semitic speakers working in Egypt and Sinai took a few dozen hieroglyphs and used each for the first consonant of its name in their own language, a house for /b/, water for /m/ (Darnell et al. 2005 on Wadi el-Hol; Hamilton 2006). The result wrote consonants only, and it was the first alphabet.

It split early. A southern branch gave Ancient South Arabian and, from it, Ge'ez; Ancient North Arabian shares that branch's ancestor rather than descending from it (Al-Jallad 2015). A northern branch was standardised as Phoenician by about {y_Phnx}. Ugarit, around {y_Ugar}, kept the idea and the letter order but wrote them in wedges on clay: an alphabet in cuneiform dress."""),
    ("Aramaic, the empire's hand",
     """Aramaic became the administrative script of the Assyrian and then the Persian empires, and so it travelled. {d_Armi} scripts descend from it. Square Hebrew is one; Nabataean, and from it Arabic (first securely dated in Arabic script in {y_Arab}), another; Syriac a third. Eastward, the Middle Iranian scripts (Parthian, the Pahlavis, Avestan) and Sogdian carried it along the Silk Road, where Sogdian became Old Uyghur and Old Uyghur, turned on its side, became the vertical Mongolian script of {y_Mong}. In India, Kharosthi is an Aramaic adaptation, and Brahmi most likely is too, though that is the majority view rather than a settled one (Salomon 1998)."""),
    ("Greek, and the vowel",
     """Around {y_Grek} Greek writers took Phoenician letters for consonants their language lacked and turned them into vowels: aleph became alpha, he became epsilon. Writing every vowel as a full letter is the step that makes an alphabet in the narrow sense. {d_Grek} scripts descend from Greek. A western Greek variety passed to the Etruscans and from them to Latin and the runes; Coptic kept the Greek letters and added six or seven from Demotic for Egyptian sounds; Gothic, Glagolitic and Cyrillic were made for Christian texts. Armenian and Georgian follow Greek order closely, but where their letter shapes came from is still argued."""),
    ("Latin's reach",
     """Latin writes {n_latin_main} of the {n_written} languages that have a script on record, more than every other script together. That is the history of the last five centuries, missionary and colonial orthographies above all, not a property of the letters. It also explains a pattern on the plate: {n_latin_invented} of the scripts hung under Latin are modern inventions with no ancestor at all (the dash-dot links). They sit there because their makers already wrote in Latin, and the plate says that is a placement, not a descent."""),
    ("Brahmi, and the abugida",
     """Brahmi appears fully formed in the edicts of Ashoka around {y_Brah}. Its idea is new: a consonant letter carries an inherent vowel, other vowels are marks attached to it, and a stroke cancels the vowel. {d_Brah} scripts descend from it, against {d_Grek} from Greek: most of the registry's diversity is Brahmic. Through the Gupta script it gave Siddham and the Nagari family (Devanagari, Bengali, Odia, Newar) in the north, Sharada and Landa in the north-west, Tibetan in the Himalaya, and, through the Kadamba script, Kannada and Telugu. Through the Pallava script of south India it crossed the sea: Khmer and from it Thai and Lao, the Mon-Burmese scripts, Cham, and Kawi with the scripts of Java, Bali, Sumatra, Sulawesi and the Philippines."""),
    ("Chinese, and the scripts it prompted",
     """Chinese writing is attested from the oracle bones of about {y_Hani} and is the only one of the old inventions still in daily use. Its characters are mostly compounds of a meaning part and a sound part. In Japan, Chinese characters used for their sound became the two kana syllabaries; in China, simplified components became Bopomofo, and in Hunan, women's writing became Nushu. Other states built writing on the Chinese model without borrowing its characters: Khitan, Tangut, Jurchen. Hangul, of 1443, is a case apart: by its own account of 1446 its consonant shapes draw the speech organs, a Phags-pa model is argued for five or six letters at most, and the plate hangs it from Phags-pa as contested."""),
    ("The other first inventions",
     """Proto-cuneiform appears at Uruk around {y_Pcun}, as book-keeping, and became cuneiform, the script of Sumerian, Akkadian, Hittite, Elamite and a dozen more languages over three thousand years; Proto-Elamite was devised beside it under its stimulus. Egyptian hieroglyphs appear around {y_Egyp}; hieratic and Demotic are their cursive forms, and the two Meroitic scripts of Nubia were made from the hieroglyphs and from Demotic. Mayan writing, from about {y_Maya}, is the one pre-Columbian script of the Americas that can be read today, deciphered over the second half of the twentieth century after Knorozov showed in 1952 that it is partly phonetic. Linear A in Crete, the Indus signs and rongorongo are not read, and the plate says so."""),
    ("Writing made on purpose",
     """{n_modern} of the scripts were devised after 1800, most of them by a person whose name is recorded. Sequoyah's Cherokee syllabary (finished in {y_Cher}) took Latin letter shapes without their values, and James Evans's Cree syllabics turned British shorthand into a syllabary. In West Africa, the Vai syllabary of {y_Vaii} prompted Mende, Kpelle, Loma and Bassa Vah. In India, Burma and Laos, scripts such as Ol Chiki, Warang Citi, Sora Sompeng, Pahawh Hmong and Mro were made for languages with no script of their own, often as the founding act of a religious or cultural movement, and their encoding proposals describe them as unrelated to any earlier script. They are the clearest evidence that writing, once known to exist, can be invented again from the idea alone."""),
]


# Questions the plate takes a side on, or declines to. Each states the positions,
# what each side rests on, and where the field is now. Works known only through
# another's citation are marked so.
DEBATES = [
    ("Where Brahmi came from",
     """**Semitic origin.** Buhler (*On the Origin of the Indian Brahma Alphabet*, 1898) derived Brahmi from a Semitic, in practice Aramaic, model; Salomon (*Indian Epigraphy*, 1998) keeps this as the leading view. Falk (*Schrift im alten Indien*, 1993; and in 2018) sees a script designed under Ashoka from the two then current in the north-west, Greek and Kharosthi.

**Earlier or indigenous.** Sherds from Anuradhapura in Sri Lanka carry Brahmi letters in layers dated to the early 4th century BCE (Coningham, Allchin, Batt and Lucy, *Cambridge Archaeological Journal* 6, 1996), and Tamil Nadu finds have been dated earlier still; these would put Brahmi before Ashoka. A descent from the Indus signs is sometimes proposed; it cannot be shown while the Indus signs themselves are unread.

**Where it stands.** An Aramaic model is the majority view and the plate draws it, dashed. How the letters were derived is not explained, and Pillai (2023, *Indialogs*) calls the debate far from settled. About seventy scripts hang from this one edge."""),
    ("Whether Egypt invented writing alone",
     """**Independent.** The labels of tomb U-j at Abydos (Dreyer, *Umm el-Qaab I*, 1998), around 3250 BCE, are as early as the first Mesopotamian tablets, and Egyptian writing differs from cuneiform in structure, signs and use (Baines, in Houston ed., *The First Writing*, 2004; Regulski, *Oxford Handbook*, 2014).

**Stimulus.** Petrie, Pope, Ray (1986) and Brewer (all cited in Regulski 2014) argued that the idea of writing reached Egypt from Mesopotamia, through contacts visible in cylinder seals and art.

**Where it stands.** The majority view is independent invention, with stimulus diffusion of the bare idea still possible; Regulski writes that it remains a possibility. The plate keeps Egyptian hieroglyphs as a root and records the argument against it."""),
    ("What Hangul's letters were drawn from",
     """**The speech organs.** The *Hunminjeongeum Haerye* of 1446, written with the script's promulgation, says the five basic consonants picture the organs that make them, the root of the tongue closing the throat for ㄱ, the shape of the mouth for ㅁ, and that further letters add strokes for aspiration or tension. Sampson (*Writing Systems*, 1985) made Hangul his example of a featural script.

**Phags-pa.** Ledyard (*The Korean Language Reform of 1446*, 1966, revised 1998) argued that a handful of base consonants follow the Phags-pa script of the Mongol court, which Korean scholars knew; an earlier court record also says the letters imitate an old seal script.

**Where it stands.** The articulatory design is not disputed. Ledyard's link concerns five or six shapes, and most scholars treat it as a model at most; the plate draws it dashed rather than leave Hangul as a root it is not."""),
    ("Whether the Indus signs are writing",
     """**Not language.** Farmer, Sproat and Witzel (*Electronic Journal of Vedic Studies* 11, 2004) argued that the inscriptions are too short and repetitive to encode language and are better read as emblems. Sproat (*Computational Linguistics* 36, 2010; *Language*, 2014) showed that the entropy measures offered against this cannot separate linguistic from non-linguistic symbol systems.

**Language.** Rao and colleagues (*Science* 324, 2009) found the sign sequences' conditional entropy close to that of natural languages, with positional regularities like a syntax; Parpola and Mahadevan have long read the signs as a logo-syllabic script.

**Where it stands.** Open. Rao and colleagues themselves write that without a decipherment neither thesis can be proved. The plate includes the Indus signs because the registry does, as a root marked undeciphered."""),
    ("How old rongorongo is",
     """**After contact.** No visitor to Rapa Nui reported writing before Eyraud in 1864. Emory (1968) and Fischer (*Rongorongo*, 1997) argued that the islanders invented it after seeing the Spanish annexation document of 1770 (both cited in Wieczorek et al. 2021).

**Before contact.** Ferrara and colleagues (*Scientific Reports* 14, 2024) radiocarbon-dated the wood of four tablets; one, tablet D, was cut around 1493-1509, which would put the script before European arrival if the text is as old as the wood.

**Where it stands.** Open. A wood date only bounds the inscription from below, and Wieczorek and colleagues (*Journal of Island and Coastal Archaeology*, 2021) found no consensus on when the script was used. The plate keeps rongorongo as a root, dated from its first record."""),
    ("Where the Glagolitic letters came from",
     """**Greek cursive.** Taylor and Jagic derived most letters from Greek minuscule, and Cubberley (in Daniels and Bright, *The World's Writing Systems*, 1996) finds most can be derived from Greek cursive in a formally satisfying way.

**Other sources, or none.** Vondrak, Nahtigal and Fortunatov proposed Hebrew, Samaritan or Coptic models for the letters Greek lacks; Chernokhvostov derived the whole set from the cross, the circle and the triangle; Mathiesen (*Slavistica Vilnensis* 65, 2020) traces its look to esoteric alphabets.

**Where it stands.** Cubberley's own verdict is that the search for the formal origins of Glagolitic remains unsolved. The plate draws Glagolitic from Greek, dashed."""),
]


def lineage_numbers(S, L):
    """The figures the lineage prose quotes, computed, never typed."""
    import collections as _c
    kids = _c.defaultdict(list)
    for c, s in S.items():
        if s["parent"]:
            kids[s["parent"]].append(c)

    def desc(c):
        return sum(1 + desc(k) for k in kids[c])

    n = {"n_scripts": len(S),
         "n_written": format(sum(1 for v in L.values() if v["scripts"]), ","),
         "n_latin_main": format(sum(1 for v in L.values() if v["primary_script"] == "Latn"), ","),
         "n_latin_invented": sum(1 for k in kids["Latn"] if S[k]["edge"] == "invented"),
         "n_modern": sum(1 for s in S.values() if s["start"] >= 1800
                         and s["edge"] in ("stimulus", "invented") and s["status"] != "fictional")}
    for c in S:
        n["d_" + c] = desc(c)
        n["y_" + c] = yr(S[c]["start"])
    return n


def yr(v):
    if v is None:
        return "present"
    return "%d BCE" % -v if v < 0 else "%d CE" % v


def short(n):
    import re
    n = re.sub(r"\s*\([^()]*\)\s*$", "", n).strip()
    return n or "unnamed"


def build():
    D = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))
    S, L, ST = D["scripts"], D["languages"], D["stats"]
    kids = collections.defaultdict(list)
    for c, s in S.items():
        if s["parent"]:
            kids[s["parent"]].append(c)
    size = {}

    def n_desc(c):
        if c not in size:
            size[c] = 1 + sum(n_desc(k) for k in kids[c])
        return size[c]

    for c in S:
        n_desc(c)
    for p in kids:
        kids[p].sort(key=lambda c: (S[c]["start"], c))
    roots = sorted((c for c in S if not S[c]["parent"]), key=lambda c: -size[c])

    langs_of = collections.defaultdict(list)
    for v in L.values():
        for sc in v["scripts"]:
            langs_of[sc].append(v)

    o = []
    w = o.append
    w("# A guide to the scripts of the world")
    w("")
    w("Generated from `out/dataset.json` by [`guide.py`](guide.py). Do not edit by hand: "
      "change [`genealogy.py`](genealogy.py) or the sources, rebuild, and rerun `guide.py`. "
      "`verify.py` fails if this file is stale.")
    w("")
    w("It covers all %d scripts of the ISO 15924 registry that are not special or private-use codes, "
      "the same set the [plate](out/descent_of_writing.svg) draws, and the %s languages of Glottolog "
      "that a source records a script for (Wikidata, CLDR or SIL langtags). Of the other %s, %s are "
      "listed as unwritten by SIL langtags and %s have no record either way. Neither is proof that a "
      "language is unwritten."
      % (len(S), format(ST["languages"] - ST["languages_without_script"], ","),
         format(ST["languages_without_script"], ","),
         format(ST["languages_recorded_unwritten"], ","),
         format(ST["languages_without_script"] - ST["languages_recorded_unwritten"], ",")))
    w("")
    w("## Contents")
    w("")
    w("- [What kinds of script there are](#what-kinds-of-script-there-are)")
    w("- [How the links are drawn](#how-the-links-are-drawn)")
    w("- [The roots](#the-roots)")
    w("- [The great lineages](#the-great-lineages)")
    w("- [Script and language are two different trees](#script-and-language-are-two-different-trees)")
    w("- [Open questions](#open-questions)")
    w("- [The family trees](#the-family-trees)")
    w("- [Every script, by code](#every-script-by-code)")
    w("")

    w("## What kinds of script there are")
    w("")
    tc = collections.Counter(s["type"] for s in S.values())
    w("| Type | Scripts | What it means |")
    w("|---|---:|---|")
    for t, desc in TYPES:
        w("| %s | %d | %s |" % (t, tc.get(t, 0), desc))
    w("")
    w("A type describes how a script is used, not where it came from. Descent crosses types "
      "freely: the Phoenician abjad gave rise to the Greek alphabet and, through Aramaic, to "
      "the Brahmi abugida.")
    w("")

    w("## How the links are drawn")
    w("")
    ec = collections.Counter(s["edge"] for s in S.values() if s["edge"])
    w("| Link | Count | Meaning |")
    w("|---|---:|---|")
    for e, desc in EDGES:
        w("| %s | %d | %s |" % (e, ec.get(e, 0), desc))
    w("")
    w("Every link names the publication it rests on, attested descent included, in the entry "
      "below and in the `SOURCES` table of `genealogy.py`.")
    w("")

    w("## The roots")
    w("")
    w("A root has no known parent among the registry's codes. That is a weaker claim than an "
      "independent invention of writing: only proto-cuneiform, Chinese and Mayan writing are "
      "held to be that beyond dispute, and Egyptian probably is.")
    w("")
    w("| Root | First attested | Scripts beneath it | Why it is a root |")
    w("|---|---|---:|---|")
    for r in roots:
        s = S[r]
        why = s["source_note"] or "independent invention, not argued"
        w("| [`%s`](#%s) %s | %s | %d | %s |" % (r, r.lower(), short(s["name"]), yr(s["start"]),
                                               size[r] - 1, why))
    w("")

    w("## The great lineages")
    w("")
    nums = lineage_numbers(S, L)
    for title, text in LINEAGES:
        w("### " + title)
        w("")
        w(text.format(**nums))
        w("")

    w("## Script and language are two different trees")
    w("")
    # Glottolog's pseudo-families are filing categories, not lineages
    PSEUDO = {"Bookkeeping", "Unclassifiable", "Unattested", "Pidgin", "Mixed Language",
              "Sign Language", "Speech Register", "Artificial Language"}
    fam_name = D["family_names"]
    fscripts, sfams, members = collections.defaultdict(set), collections.defaultdict(set), collections.Counter()
    for v in L.values():
        f = "isolate:" + v["id"] if v["isolate"] else v["family"]
        if fam_name.get(f) in PSEUDO:
            continue
        members[f] += 1
        for c in v["scripts"]:
            fscripts[f].add(c)
            sfams[c].add(f)
    top_s = sorted(sfams.items(), key=lambda kv: -len(kv[1]))
    top_f = sorted(fscripts.items(), key=lambda kv: -len(kv[1]))
    single = sum(1 for fs in sfams.values() if len(fs) == 1)
    w("The plate draws the descent of scripts as a tree and sorts languages by family inside each "
      "script's field, but the two trees do not line up. A script travels by conquest, religion, "
      "trade and schooling; a language descends by speech. Counting families and isolates as "
      "Glottolog defines them, leaving out its filing categories (%s):" % ", ".join(sorted(PSEUDO)))
    w("")
    w("- %s writes languages of %d families and isolates, %s of %d, %s of %d."
      % tuple([short(S[top_s[0][0]]["name"]), len(top_s[0][1])]
              + sum(([short(S[c]["name"]), len(fs)] for c, fs in top_s[1:3]), [])))
    w("- %s is written in %d scripts, %s in %d, %s in %d."
      % tuple(sum(([fam_name.get(f, f), len(cs)] for f, cs in top_f[:3]), [])))
    w("- Yet %d of the %d scripts recorded for any language serve a single family or isolate: most "
      "scripts were made for one language or a few close ones, and a handful of imperial and "
      "religious scripts carry everything else." % (single, len(sfams)))
    w("")
    w("A second plate could draw the language families as a tree facing this one, linked by "
      "chords; CONTINUE.md keeps it as open work.")
    w("")

    w("## Open questions")
    w("")
    w("Six questions on which the plate takes a side or declines to. Each gives the positions, what "
      "each rests on, and where the field stands; works known here only through another's citation "
      "are marked as cited.")
    w("")
    for title, text in DEBATES:
        w("### " + title)
        w("")
        w(text)
        w("")

    w("## The family trees")
    w("")
    w("Indented by generation. Each line gives the code, the name, the type, the first attestation, "
      "and the link to the parent when it is not attested descent.")
    w("")
    for r in roots:
        w("### %s" % short(S[r]["name"]))
        w("")

        def walk(c, depth):
            s = S[c]
            tag = "" if s["edge"] in (None, "attested") else " *(%s)*" % s["edge"]
            w("%s- [`%s`](#%s) %s, %s, %s%s"
              % ("  " * depth, c, c.lower(), short(s["name"]), s["type"], yr(s["start"]), tag))
            for k in kids[c]:
                walk(k, depth + 1)

        walk(r, 0)
        w("")

    w("## Every script, by code")
    w("")
    for c in sorted(S):
        s = S[c]
        w("### %s" % c)
        w("")
        w("**%s**%s. %s, written %s. First attested %s, %s; status %s."
          % (short(s["name"]), " (%s)" % s["native"] if s["native"] else "",
             s["type"].capitalize(), {"ltr": "left to right", "rtl": "right to left",
                                      "ttb": "top to bottom", "boustrophedon": "boustrophedon",
                                      "varies": "in more than one direction"}[s["direction"]],
             yr(s["start"]), "in use today" if s["end"] is None else "last used %s" % yr(s["end"]),
             s["status"]))
        w("")
        if s["parent"]:
            p = s["parent"]
            w("Parent: [`%s`](#%s) %s%s, link **%s**."
              % (p, p.lower(), short(S[p]["name"]),
                 " through %s" % s["via"] if s["via"] else "", s["edge"]))
        else:
            w("A root: no known parent among the registry's codes.")
        if s["source"]:
            w("Source: %s. %s." % (s["source"], s["source_note"][0].upper() + s["source_note"][1:])
              if s["source_note"] else "Source: %s." % s["source"])
        if kids[c]:
            w("Children: %s." % ", ".join("[`%s`](#%s)" % (k, k.lower()) for k in kids[c]))
        w("")
        ls = sorted(langs_of[c], key=lambda v: -(v["speakers"] or 0))
        main = [v for v in ls if v["primary_script"] == c]
        also = len(ls) - len(main)
        if main:
            top = ", ".join("%s%s" % (v["name"], " (%s speakers)" % format(int(v["speakers"]), ",")
                                      if v["speakers"] else "") for v in main[:5])
            w("Languages written mainly in it: %s. %s%s.%s"
              % (format(len(main), ","), "Largest: " if len(main) > 1 else "", top,
                 " Also recorded as a further script for %s more." % format(also, ",") if also else ""))
        elif ls:
            w("Recorded as a further script for %s language%s, the main script for none."
              % (format(len(ls), ","), "" if len(ls) == 1 else "s"))
        else:
            w("Languages a source records it for: none.")
        w("Unicode: %s." % ("encoded since version %s, block from U+%04X"
                           % (s["unicode"], s["block_start"]) if s["encoded"] and s["block_start"]
                           else "encoded since version %s" % s["unicode"] if s["encoded"]
                           else "not encoded, so no font can show it"))
        w("")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    text = build()
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        cur = open(GUIDE, encoding="utf8").read() if os.path.exists(GUIDE) else ""
        sys.exit(0 if cur == text else "GUIDE.md is stale: run python guide.py")
    open(GUIDE, "w", encoding="utf8", newline="\n").write(text)
    print("%s  %d lines" % (GUIDE, text.count("\n")))
