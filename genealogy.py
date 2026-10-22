# -*- coding: utf-8 -*-
"""Curated descent of every ISO 15924 script.

Wikidata P144 covers barely half the registry and disagrees with itself on the
Semitic chain, so descent is curated here against palaeographic scholarship and
the Unicode encoding proposals. Every edge that is not plain attested descent
carries its authority in SOURCES below, and verify.py fails if one is missing.

Row = code: (parent, edge, type, direction, start, end, status)
  parent    ISO 15924 code, or None for a root
  edge      attested | contested | stimulus | invented | variant | composite
              attested  = direct graphical descent, uncontroversial
              contested = descent claimed but disputed in the literature
              stimulus  = a named script supplied the idea of writing, or a
                          structure (letter order, inherent vowel, syllabic
                          layout), but the glyphs were invented fresh
              invented  = created on purpose with no genetic relationship to
                          any script; drawn under the script its makers
                          already wrote, which is a placement, not a descent
              variant   = same script, different style/orthographic tradition
              composite = registry code bundling several scripts, not a script
  type      logographic | syllabary | abjad | alphabet | abugida | featural
            | semasiographic | undeciphered | composite | variant | symbols
  direction ltr | rtl | ttb | boustrophedon | varies
  start     first attestation, year (negative = BCE); for a modern invention,
            the year it was devised
  end       last use, year, or None if still in current use
  status    living | historical | revived | undeciphered | constructed | fictional

A root (parent None) means no ancestor is known among ISO 15924 codes. It is
not a claim of independent invention: only Pcun, Egyp, Hani and Maya are
widely held to be that, and Egyp is argued over (see SOURCES).
"""

G = {}

# ------------------------------------------------------------------ ROOTS ----
# No known ancestor among ISO 15924 codes.
G["Pcun"] = (None, None, "logographic", "varies", -3300, -2900, "historical")
G["Egyp"] = (None, None, "logographic", "varies", -3250, 400, "historical")
G["Hani"] = (None, None, "logographic", "varies", -1250, None, "living")
G["Maya"] = (None, None, "logographic", "ltr", -300, 1600, "historical")
G["Inds"] = (None, None, "undeciphered", "rtl", -2600, -1900, "undeciphered")
G["Roro"] = (None, None, "undeciphered", "boustrophedon", 1864, 1864, "undeciphered")
G["Lina"] = (None, None, "undeciphered", "ltr", -1800, -1450, "undeciphered")
G["Hluw"] = (None, None, "logographic", "boustrophedon", -1400, -700, "historical")
G["Nkdb"] = (None, None, "semasiographic", "ltr", 1200, None, "living")

# ------------------------------------------------------------- MESOPOTAMIA ---
G["Xsux"] = ("Pcun", "attested", "logographic", "ltr", -2900, 75, "historical")
G["Pelm"] = ("Pcun", "stimulus", "undeciphered", "rtl", -3050, -2900, "undeciphered")
G["Xpeo"] = ("Xsux", "stimulus", "syllabary", "ltr", -520, -330, "historical")

# ------------------------------------------------------------------ EGYPT ----
G["Egyh"] = ("Egyp", "attested", "logographic", "rtl", -3200, 300, "historical")
G["Egyd"] = ("Egyh", "attested", "logographic", "rtl", -650, 500, "historical")
G["Mero"] = ("Egyp", "attested", "abugida", "rtl", -300, 400, "historical")
G["Merc"] = ("Egyd", "attested", "abugida", "rtl", -300, 400, "historical")
G["Psin"] = ("Egyp", "attested", "abjad", "varies", -1900, -1400, "historical")

# -------------------------------------------------- PROTO-SINAITIC / SEMITIC --
G["Ugar"] = ("Psin", "stimulus", "abjad", "ltr", -1250, -1190, "historical")
G["Phnx"] = ("Psin", "attested", "abjad", "rtl", -1050, 100, "historical")
G["Samr"] = ("Phnx", "attested", "abjad", "rtl", -600, None, "living")
G["Sarb"] = ("Psin", "attested", "abjad", "boustrophedon", -900, 600, "historical")
G["Narb"] = ("Psin", "attested", "abjad", "varies", -600, 400, "historical")
G["Ethi"] = ("Sarb", "attested", "abugida", "ltr", -100, None, "living")
G["Tfng"] = ("Phnx", "contested", "abjad", "varies", -138, None, "living")

# ----------------------------------------------------------------- ARAMAIC ---
G["Armi"] = ("Phnx", "attested", "abjad", "rtl", -900, -100, "historical")
G["Hebr"] = ("Armi", "attested", "abjad", "rtl", -300, None, "living")
G["Nbat"] = ("Armi", "attested", "abjad", "rtl", -200, 400, "historical")
G["Palm"] = ("Armi", "attested", "abjad", "rtl", -100, 300, "historical")
G["Hatr"] = ("Armi", "attested", "abjad", "rtl", -100, 300, "historical")
G["Syrc"] = ("Armi", "attested", "abjad", "rtl", 100, None, "living")
G["Syre"] = ("Syrc", "variant", "variant", "rtl", 100, None, "living")
G["Syrj"] = ("Syrc", "variant", "variant", "rtl", 400, None, "living")
G["Syrn"] = ("Syrc", "variant", "variant", "rtl", 400, None, "living")
G["Mand"] = ("Armi", "attested", "abjad", "rtl", 200, None, "living")
G["Mani"] = ("Syrc", "contested", "abjad", "rtl", 250, 1000, "historical")
G["Elym"] = ("Armi", "attested", "abjad", "rtl", -100, 300, "historical")
G["Chrs"] = ("Armi", "attested", "abjad", "rtl", -100, 800, "historical")
G["Prti"] = ("Armi", "attested", "abjad", "rtl", -250, 250, "historical")
G["Phli"] = ("Armi", "attested", "abjad", "rtl", -100, 900, "historical")
G["Phlp"] = ("Phli", "attested", "abjad", "rtl", 600, 800, "historical")
G["Phlv"] = ("Phli", "attested", "abjad", "rtl", 400, 1100, "historical")
G["Avst"] = ("Phlv", "attested", "alphabet", "rtl", 400, 1000, "historical")
G["Sogo"] = ("Armi", "attested", "abjad", "rtl", -100, 400, "historical")
G["Sogd"] = ("Sogo", "attested", "abjad", "varies", 400, 1000, "historical")
G["Ougr"] = ("Sogd", "attested", "abjad", "ttb", 800, 1800, "historical")
G["Mong"] = ("Ougr", "attested", "abjad", "ttb", 1204, None, "living")
G["Orkh"] = ("Sogd", "contested", "alphabet", "rtl", 700, 1000, "historical")
G["Hung"] = ("Orkh", "contested", "alphabet", "rtl", 900, None, "revived")
G["Yezi"] = ("Syrc", "contested", "alphabet", "rtl", 1200, None, "living")

# ------------------------------------------------------------------ ARABIC ---
G["Arab"] = ("Nbat", "attested", "abjad", "rtl", 400, None, "living")
G["Aran"] = ("Arab", "variant", "variant", "rtl", 1400, None, "living")
G["Thaa"] = ("Arab", "stimulus", "abugida", "rtl", 1705, None, "living")
G["Rohg"] = ("Arab", "stimulus", "alphabet", "rtl", 1980, None, "living")
G["Adlm"] = ("Arab", "stimulus", "alphabet", "rtl", 1989, None, "living")
G["Nkoo"] = ("Arab", "stimulus", "alphabet", "rtl", 1949, None, "living")
G["Gara"] = ("Arab", "stimulus", "alphabet", "rtl", 1961, None, "living")
G["Osma"] = ("Arab", "stimulus", "alphabet", "ltr", 1920, None, "living")
G["Bamu"] = ("Arab", "contested", "syllabary", "ltr", 1896, None, "living")
G["Berf"] = ("Arab", "invented", "alphabet", "ltr", 1950, None, "living")

# ------------------------------------------------------------------- GREEK ---
G["Grek"] = ("Phnx", "attested", "alphabet", "ltr", -800, None, "living")
G["Cari"] = ("Grek", "contested", "alphabet", "varies", -700, -300, "historical")
G["Lyci"] = ("Grek", "attested", "alphabet", "ltr", -500, -300, "historical")
G["Lydi"] = ("Grek", "attested", "alphabet", "rtl", -700, -300, "historical")
G["Sidt"] = ("Phnx", "contested", "alphabet", "rtl", -500, -300, "historical")
G["Copt"] = ("Grek", "attested", "alphabet", "ltr", 200, None, "living")
G["Goth"] = ("Grek", "attested", "alphabet", "ltr", 350, 900, "historical")
G["Armn"] = ("Grek", "contested", "alphabet", "ltr", 405, None, "living")
G["Aghb"] = ("Armn", "contested", "alphabet", "ltr", 420, 1000, "historical")
G["Geok"] = ("Grek", "contested", "alphabet", "ltr", 430, 1100, "historical")
G["Geor"] = ("Geok", "attested", "alphabet", "ltr", 1000, None, "living")
G["Glag"] = ("Grek", "contested", "alphabet", "ltr", 863, 1900, "historical")
G["Cyrl"] = ("Grek", "attested", "alphabet", "ltr", 900, None, "living")
G["Cyrs"] = ("Cyrl", "variant", "variant", "ltr", 900, None, "living")
G["Perm"] = ("Cyrl", "stimulus", "alphabet", "ltr", 1372, 1700, "historical")
G["Ital"] = ("Grek", "attested", "alphabet", "varies", -700, -100, "historical")
G["Runr"] = ("Ital", "attested", "alphabet", "boustrophedon", 150, 1500, "historical")
G["Elba"] = ("Grek", "stimulus", "alphabet", "ltr", 1761, 1800, "historical")
G["Vith"] = ("Grek", "contested", "alphabet", "ltr", 1844, 1900, "historical")
G["Todr"] = ("Grek", "stimulus", "alphabet", "ltr", 1750, 1900, "historical")

# ------------------------------------------------------------------- LATIN ---
G["Latn"] = ("Ital", "attested", "alphabet", "ltr", -700, None, "living")
G["Latf"] = ("Latn", "variant", "variant", "ltr", 1150, None, "living")
G["Latg"] = ("Latn", "variant", "variant", "ltr", 700, None, "living")
G["Ogam"] = ("Latn", "stimulus", "alphabet", "varies", 350, 600, "historical")
G["Moon"] = ("Latn", "attested", "alphabet", "boustrophedon", 1845, None, "living")
G["Brai"] = ("Latn", "stimulus", "alphabet", "ltr", 1824, None, "living")
G["Dupl"] = ("Latn", "stimulus", "alphabet", "ltr", 1860, None, "living")
G["Visp"] = ("Latn", "invented", "featural", "ltr", 1867, 1900, "historical")
G["Shaw"] = ("Latn", "invented", "alphabet", "ltr", 1960, None, "constructed")
G["Dsrt"] = ("Latn", "stimulus", "alphabet", "ltr", 1854, 1877, "constructed")
G["Osge"] = ("Latn", "attested", "alphabet", "ltr", 2006, None, "living")
G["Lisu"] = ("Latn", "attested", "alphabet", "ltr", 1915, None, "living")
G["Sunu"] = ("Latn", "stimulus", "alphabet", "ltr", 1942, None, "living")
G["Sgnw"] = ("Latn", "invented", "featural", "ttb", 1974, None, "living")
G["Zsye"] = ("Latn", "composite", "symbols", "ltr", 1999, None, "living")

# ------------------------------------------- AMERICAS AND THE PACIFIC --------
G["Cher"] = ("Latn", "stimulus", "syllabary", "ltr", 1821, None, "living")
G["Cans"] = ("Latn", "stimulus", "abugida", "ltr", 1840, None, "living")
G["Plrd"] = ("Cans", "stimulus", "abugida", "ltr", 1904, None, "living")
G["Wole"] = ("Latn", "stimulus", "syllabary", "ltr", 1905, 1950, "historical")

# --------------------------------------------------------- WEST AFRICA -------
G["Vaii"] = ("Latn", "stimulus", "syllabary", "ltr", 1833, None, "living")
G["Mend"] = ("Vaii", "stimulus", "syllabary", "rtl", 1917, None, "living")
G["Kpel"] = ("Vaii", "stimulus", "syllabary", "ltr", 1930, None, "living")
G["Loma"] = ("Vaii", "stimulus", "syllabary", "ltr", 1930, None, "living")
G["Bass"] = ("Vaii", "stimulus", "alphabet", "ltr", 1907, None, "living")
G["Medf"] = ("Latn", "stimulus", "alphabet", "ltr", 1927, None, "living")
G["Afak"] = ("Latn", "invented", "syllabary", "ltr", 1908, None, "historical")

# ------------------------------------------- MODERN INVENTIONS, SOUTH ASIA ---
G["Olck"] = ("Latn", "invented", "alphabet", "ltr", 1925, None, "living")
G["Nagm"] = ("Olck", "stimulus", "alphabet", "ltr", 1950, None, "living")
G["Onao"] = ("Latn", "invented", "alphabet", "ltr", 1981, None, "living")
G["Wara"] = ("Latn", "invented", "alphabet", "ltr", 1950, None, "living")
G["Tols"] = ("Latn", "invented", "alphabet", "ltr", 1988, None, "living")
G["Toto"] = ("Latn", "invented", "alphabet", "ltr", 2015, None, "living")
G["Chis"] = ("Latn", "invented", "alphabet", "ltr", 1986, None, "living")
G["Tnsa"] = ("Latn", "invented", "alphabet", "ltr", 1990, None, "living")
G["Wcho"] = ("Latn", "invented", "alphabet", "ltr", 2001, None, "living")
G["Mroo"] = ("Latn", "invented", "alphabet", "ltr", 1980, None, "living")
G["Pauc"] = ("Latn", "invented", "alphabet", "ltr", 1902, None, "living")

# ---------------------------------------------------------- HMONG ------------
G["Hmng"] = ("Laoo", "invented", "alphabet", "ltr", 1959, None, "living")
G["Hmnp"] = ("Hebr", "stimulus", "alphabet", "ltr", 1980, None, "living")

# ------------------------------------------------------- BRAHMIC: NORTHERN ---
G["Brah"] = ("Armi", "contested", "abugida", "ltr", -300, 500, "historical")
G["Khar"] = ("Armi", "attested", "abugida", "rtl", -400, 300, "historical")
G["Sidd"] = ("Brah", "attested", "abugida", "ltr", 550, 1200, "historical")
G["Deva"] = ("Sidd", "attested", "abugida", "ltr", 700, None, "living")
G["Shrd"] = ("Brah", "attested", "abugida", "ltr", 800, 1900, "historical")
G["Takr"] = ("Shrd", "attested", "abugida", "ltr", 1500, None, "historical")
G["Dogr"] = ("Takr", "attested", "abugida", "ltr", 1860, None, "historical")
G["Guru"] = ("Shrd", "attested", "abugida", "ltr", 1539, None, "living")
G["Khoj"] = ("Shrd", "attested", "abugida", "ltr", 1500, None, "historical")
G["Mult"] = ("Shrd", "attested", "abugida", "ltr", 1750, 1950, "historical")
G["Sind"] = ("Shrd", "attested", "abugida", "ltr", 1550, None, "historical")
G["Mahj"] = ("Deva", "contested", "abugida", "ltr", 1600, 1950, "historical")
G["Kthi"] = ("Sidd", "attested", "abugida", "ltr", 1550, 1950, "historical")
G["Modi"] = ("Deva", "attested", "abugida", "ltr", 1200, None, "historical")
G["Nand"] = ("Deva", "attested", "abugida", "ltr", 1100, 1800, "historical")
G["Gujr"] = ("Deva", "attested", "abugida", "ltr", 1592, None, "living")
G["Sylo"] = ("Kthi", "attested", "abugida", "ltr", 1500, None, "living")
G["Gong"] = ("Modi", "contested", "abugida", "ltr", 1750, None, "living")
G["Gonm"] = ("Brah", "stimulus", "abugida", "ltr", 1918, None, "living")
G["Beng"] = ("Sidd", "attested", "abugida", "ltr", 1000, None, "living")
G["Tirh"] = ("Sidd", "attested", "abugida", "ltr", 1200, None, "historical")
G["Orya"] = ("Sidd", "attested", "abugida", "ltr", 1050, None, "living")
G["Newa"] = ("Sidd", "attested", "abugida", "ltr", 1100, None, "living")
G["Ranj"] = ("Sidd", "attested", "abugida", "ltr", 1100, None, "living")
G["Bhks"] = ("Brah", "attested", "abugida", "ltr", 1000, 1200, "historical")
G["Mtei"] = ("Brah", "contested", "abugida", "ltr", 1100, None, "living")
G["Cakm"] = ("Mymr", "attested", "abugida", "ltr", 1700, None, "living")
G["Sora"] = ("Brah", "stimulus", "abugida", "ltr", 1936, None, "living")
G["Gukh"] = ("Brah", "stimulus", "abugida", "ltr", 1995, None, "living")

# ------------------------------------------------------- BRAHMIC: TIBETAN ----
G["Tibt"] = ("Brah", "attested", "abugida", "ltr", 650, None, "living")
G["Marc"] = ("Tibt", "attested", "abugida", "ltr", 1000, None, "historical")
G["Phag"] = ("Tibt", "attested", "abugida", "ttb", 1269, 1400, "historical")
G["Lepc"] = ("Tibt", "attested", "abugida", "ltr", 1700, None, "living")
G["Limb"] = ("Lepc", "attested", "abugida", "ltr", 1700, None, "living")
G["Krai"] = ("Limb", "contested", "abugida", "ltr", 1925, None, "living")
G["Zanb"] = ("Tibt", "attested", "abugida", "ltr", 1686, 1800, "historical")
G["Soyo"] = ("Ranj", "attested", "abugida", "ltr", 1686, 1800, "historical")

# ------------------------------------------------------- BRAHMIC: SOUTHERN ---
G["Gran"] = ("Brah", "attested", "abugida", "ltr", 500, None, "living")
G["Taml"] = ("Gran", "attested", "abugida", "ltr", 700, None, "living")
G["Mlym"] = ("Gran", "attested", "abugida", "ltr", 830, None, "living")
G["Tutg"] = ("Gran", "attested", "abugida", "ltr", 1000, None, "historical")
G["Saur"] = ("Gran", "contested", "abugida", "ltr", 1880, None, "living")
G["Sinh"] = ("Brah", "attested", "abugida", "ltr", -200, None, "living")
G["Diak"] = ("Gran", "attested", "abugida", "ltr", 900, 1700, "historical")
G["Knda"] = ("Brah", "attested", "abugida", "ltr", 500, None, "living")
G["Telu"] = ("Brah", "attested", "abugida", "ltr", 600, None, "living")

# --------------------------------------------------- BRAHMIC: SOUTHEAST ASIA -
G["Khmr"] = ("Gran", "attested", "abugida", "ltr", 611, None, "living")
G["Thai"] = ("Khmr", "attested", "abugida", "ltr", 1283, None, "living")
G["Laoo"] = ("Khmr", "attested", "abugida", "ltr", 1350, None, "living")
G["Tavt"] = ("Thai", "attested", "abugida", "ltr", 1500, None, "living")
G["Tayo"] = ("Thai", "contested", "abugida", "ttb", 1500, None, "historical")
G["Mymr"] = ("Gran", "attested", "abugida", "ltr", 1000, None, "living")
G["Leke"] = ("Mymr", "contested", "abugida", "ltr", 1844, None, "living")
G["Kali"] = ("Mymr", "stimulus", "alphabet", "ltr", 1962, None, "living")
G["Lana"] = ("Mymr", "attested", "abugida", "ltr", 1300, None, "living")
G["Talu"] = ("Lana", "attested", "abugida", "ltr", 1955, None, "living")
G["Tale"] = ("Mymr", "attested", "abugida", "ltr", 1300, None, "living")
G["Ahom"] = ("Mymr", "attested", "abugida", "ltr", 1300, 1800, "revived")
G["Cham"] = ("Gran", "attested", "abugida", "ltr", 400, None, "living")
G["Kawi"] = ("Gran", "attested", "abugida", "ltr", 750, 1500, "historical")
G["Java"] = ("Kawi", "attested", "abugida", "ltr", 1500, None, "living")
G["Bali"] = ("Kawi", "attested", "abugida", "ltr", 1000, None, "living")
G["Sund"] = ("Kawi", "attested", "abugida", "ltr", 1400, None, "living")
G["Rjng"] = ("Kawi", "attested", "abugida", "ltr", 1700, None, "living")
G["Batk"] = ("Kawi", "attested", "abugida", "ltr", 1300, None, "living")
G["Bugi"] = ("Kawi", "attested", "abugida", "ltr", 1600, None, "living")
G["Maka"] = ("Rjng", "contested", "abugida", "ltr", 1600, 1900, "historical")
G["Tglg"] = ("Kawi", "contested", "abugida", "ltr", 1550, None, "revived")
G["Hano"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")
G["Buhd"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")
G["Tagb"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")

# ------------------------------------------------------------------ AEGEAN ---
G["Linb"] = ("Lina", "attested", "syllabary", "ltr", -1450, -1200, "historical")
G["Cpmn"] = ("Lina", "attested", "undeciphered", "ltr", -1550, -1050, "undeciphered")
G["Cprt"] = ("Cpmn", "attested", "syllabary", "rtl", -1100, -300, "historical")

# -------------------------------------------------------------------- HAN ----
G["Seal"] = ("Hani", "variant", "variant", "ttb", -800, None, "living")
G["Hans"] = ("Hani", "variant", "variant", "ltr", 1956, None, "living")
G["Hant"] = ("Hani", "variant", "variant", "varies", -200, None, "living")
G["Hira"] = ("Hani", "attested", "syllabary", "varies", 800, None, "living")
G["Kana"] = ("Hani", "attested", "syllabary", "varies", 800, None, "living")
G["Bopo"] = ("Hani", "attested", "syllabary", "varies", 1913, None, "living")
G["Nshu"] = ("Hani", "attested", "syllabary", "ttb", 1400, None, "historical")
G["Tang"] = ("Hani", "stimulus", "logographic", "ltr", 1036, 1500, "historical")
G["Kitl"] = ("Hani", "stimulus", "logographic", "ttb", 920, 1200, "undeciphered")
G["Kits"] = ("Ougr", "stimulus", "logographic", "ttb", 925, 1200, "undeciphered")
G["Jurc"] = ("Kitl", "attested", "logographic", "ttb", 1119, 1500, "historical")
G["Yiii"] = ("Hani", "contested", "syllabary", "ltr", 1485, None, "living")
G["Nkgb"] = ("Nkdb", "attested", "syllabary", "ltr", 1600, None, "living")
G["Shui"] = ("Hani", "attested", "logographic", "rtl", 1400, None, "living")
G["Hang"] = ("Phag", "contested", "featural", "varies", 1443, None, "living")
G["Jamo"] = ("Hang", "variant", "variant", "ltr", 1443, None, "living")
G["Blis"] = ("Hani", "stimulus", "semasiographic", "ltr", 1949, None, "living")

# ------------------------------------------------------ COMPOSITE REGISTRY ---
# Not scripts. Registry conveniences bundling several scripts for locale tagging.
G["Jpan"] = ("Hani", "composite", "composite", "varies", 800, None, "living")
G["Kore"] = ("Hani", "composite", "composite", "varies", 1443, None, "living")
G["Hanb"] = ("Hani", "composite", "composite", "varies", 1913, None, "living")
G["Hrkt"] = ("Hani", "composite", "composite", "varies", 800, None, "living")
G["Hntl"] = ("Hani", "composite", "composite", "varies", 1900, None, "living")

# ---------------------------------------------------------------- FICTIONAL --
G["Sara"] = ("Latn", "invented", "alphabet", "ltr", 1919, None, "fictional")
G["Teng"] = ("Sara", "attested", "alphabet", "ltr", 1930, None, "fictional")
G["Cirt"] = ("Runr", "stimulus", "alphabet", "ltr", 1930, None, "fictional")
G["Piqd"] = ("Latn", "invented", "alphabet", "ltr", 1979, None, "fictional")


# ---------------------------------------------------------------- SOURCES ----
# The authority for every edge that is not plain attested descent, and for
# every row whose date or parent departs from what a reader might expect.
# code: (via, source, note)
#   via     the real intermediary when it has no ISO 15924 code, else ""
#   source  the citation the row rests on; "unsourced" is allowed and counted
#   note    what the source says, in one line
#
# "Unicode N####" is an ISO/IEC JTC1/SC2/WG2 document, at
# https://www.unicode.org/wg2/docs/n####.pdf. "L2/yy-nnn" is a UTC document,
# at https://www.unicode.org/L2/L20yy/. "Unicode ch.N" is the core
# specification, version 17.0.
SOURCES = {
    # roots
    "Egyp": ("", "Baines 2004, in Houston (ed.), The First Writing",
             "independent Egyptian invention is the majority view; stimulus from Sumer is argued and not excluded"),
    "Inds": ("", "Farmer, Sproat & Witzel 2004, EJVS 11-2; Rao et al. 2009, Science 324",
             "whether the signs encode language at all is disputed"),
    "Roro": ("", "Ferrara et al. 2024, Scientific Reports 14:2794; Wieczorek et al. 2021, J. Island & Coastal Arch.",
             "first recorded 1864 (Eyraud); stimulus from the 1770 Spanish annexation treaty is argued and unresolved"),
    "Lina": ("Cretan hieroglyphic", "Salgarella 2020, Aegean Linear Script(s), CUP",
             "Linear A grew out of the Cretan hieroglyphic tradition, which has no ISO code"),
    "Hluw": ("", "van den Hout 2020, A History of Hittite Literacy, ch.7",
             "Egyptian inspiration unlikely; probably an Anatolian creation from indigenous signs"),
    "Nkdb": ("", "Poupard 2019, Written Language & Literacy; Yang & He 2024",
             "earliest dated manuscripts 13th c.; independence hedged, created amid Chinese and Tibetan literacy"),

    # Near East and the Mediterranean
    "Pelm": ("", "Dahl 2005, CDLJ 2005:3; Englund, Encyclopaedia Iranica 'Elam iii'",
             "unquestionably inspired by proto-cuneiform; numerical systems borrowed, signs largely new"),
    "Xpeo": ("", "Schmitt, Encyclopaedia Iranica 'Cuneiform script'",
             "an independent creation in wedge form for Darius's Bisotun inscription, c. 520 BCE"),
    "Ugar": ("Proto-Canaanite linear alphabet", "Vita, 'Ugaritic' (CSIC 2021); Cross, 'A Ugaritic Abecedary'",
             "modelled on a linear alphabet of 27 signs; only the wedge medium is Mesopotamian"),
    "Narb": ("", "Al-Jallad 2015, An Outline of the Grammar of the Safaitic Inscriptions; Unicode ch.10",
             "shares an ancestor with Ancient South Arabian rather than descending from it"),
    "Tfng": ("Libyco-Berber", "British Museum, 'Written in stone'; Chaker & Hachi 2000",
             "Phoenician/Punic origin has the wider support; indigenous and South Arabian origins argued; first dated text 139/138 BCE (Dougga)"),
    "Mani": ("", "Unicode ch.10; Everson, Unicode N2544 and N3486",
             "based on Estrangela Syriac and Palmyrene; also described as a sister of Syriac out of Aramaic"),
    "Yezi": ("", "L2/19-051R (Yezidi proposal); Unicode ch.9",
             "an original consonantal alphabet; manuscripts perhaps 12th-13th c.; no named ancestor"),
    "Orkh": ("", "Everson et al., L2/08-071R2; Shcherbak 1996, Etudes mongoles 27",
             "Aramaic via Iranian scripts is mainstream; a direct Sogdian link is denied by Rona-Tas"),
    "Hung": ("", "Everson & Szelp, Unicode N3483; Demeczky et al., Unicode N4371",
             "thought to derive ultimately from Old Turkic; some treat them as distant relatives only"),
    "Thaa": ("", "Maldives National Centre for Linguistic and Historical Research, 'Scripts of Maldives'",
             "first nine letters from Arabic numerals, next nine from Indic numerals; vowel marks from Arabic; earliest records 1705"),
    "Rohg": ("", "Pandey, L2/16-311",
             "influenced by Arabic but a modern construction with no direct genetic affiliation; finalised 1980"),
    "Adlm": ("", "L2/14-219R; Unicode ch.19",
             "glyphs original; right-to-left direction and optional joining shared with Arabic"),
    "Nkoo": ("", "Unicode ch.19; Oyler 2005; Wyrod 2019, African Studies Review",
             "Kante tried Arabic ajami and Latin before devising N'Ko in 1949; direction and joining as Arabic"),
    "Gara": ("", "Everson, Unicode N4709; Pandey, Unicode N4044",
             "influences of the Arabic writing system; written right to left"),
    "Osma": ("", "Unicode ch.19; Tosco, AAP, after Cerulli 1932",
             "letter order follows Arabic; Latin gave only the direction; no Ethiopic role"),
    "Bamu": ("", "Orosz, Cahiers d'etudes africaines 2013 (journals.openedition.org/etudesafricaines/18002)",
             "Arabic via Hausa traders is the most cited stimulus; European and Vai models also proposed"),
    "Berf": ("Zaghawa camel brands", "Unicode ch.19; L2/24-004R",
             "devised in the 1950s by Adam Tajir from livestock brand marks; revised 2004; left to right"),

    # Greek world
    "Cari": ("", "Unicode ch.8; Adiego 2018",
             "a development parallel to, and independent of, Greek cannot be ruled out"),
    "Sidt": ("", "Pandey, L2/23-019",
             "origins not clearly known; thought to develop from Phoenician in parallel with Greek"),
    "Armn": ("", "Pifer, Encyclopaedia Iranica 'Mesrop Mastoc'; D'Aiuto 2020",
             "arranged in Greek order; derivation of the letter shapes from Greek, Iranian or Aramaic still argued"),
    "Aghb": ("", "Everson & Gippert, Unicode N4131R",
             "attributed by tradition to Mashtots; arrangement close to Armenian; Greek the model for both"),
    "Geok": ("", "Bolkvadze & Kiziria 2023; Giunashvili on Tsereteli",
             "Greek provenance most widely accepted; Aramaic shapes argued; earliest inscriptions dated 430s, some earlier claims"),
    "Glag": ("", "Cubberley, 'Slavonic, Old Church: Orthography'; Schenker 1995",
             "the search for the formal origins of Glagolitic remains unsolved"),
    "Perm": ("", "Everson, Unicode N4263",
             "modelled on Greek and Cyrillic, with many glyphs taken from tamga signs"),
    "Elba": ("", "Everson & Elsie, Unicode N3856",
             "a Greek flavour to some characters, most letters new creations"),
    "Vith": ("", "Everson, Unicode N5138, quoting Elsie 2017 and von Hahn",
             "only single letters recall Greek; glyphs resemble cursive Armenian; no source names a model"),
    "Todr": ("", "Everson, Unicode N5139R2; Geitler 1883",
             "derived from Greek and Roman cursive (Geitler); 18th century, author fl. c.1730-1805"),

    # Latin world and modern inventions
    "Ogam": ("", "McManus 1991, A Guide to Ogam",
             "the most likely immediate source is Latin; Greek and runes have had adherents"),
    "Brai": ("Barbier's night writing", "RNIB; Unicode ch.21",
             "a six-dot recoding of the French Latin alphabet, after Barbier's twelve-dot phonetic code"),
    "Dupl": ("", "Unicode L2/10-272R2",
             "a geometric shorthand, letterforms from circles and lines, for writing French"),
    "Visp": ("", "Bell 1867, Visible Speech",
             "symbols built from the vocal organs, not from existing letters"),
    "Shaw": ("", "University of Reading, Kingsley Read alphabet collection",
             "a 48-character alphabet for English, shapes new, 1960"),
    "Dsrt": ("Pitman 1847 phonotypy", "Beesley, 'Deseret in Unicode'",
             "Pitman's phonotypy the starting point, then an entirely new set of characters, adopted Dec 1853"),
    "Sunu": ("", "Pandey, L2/21-157",
             "a linear alphabet whose structure is modelled upon the Latin alphabet"),
    "Sgnw": ("Sutton DanceWriting", "Unicode N4342",
             "developed in 1974 by Valerie Sutton out of her DanceWriting"),
    "Cher": ("", "Unicode ch.20",
             "Sequoyah took letter shapes from Latin print without their Latin values, 1815-1821"),
    "Cans": ("British shorthand", "Nichols 1996, in Daniels & Bright",
             "most characters drawn from British shorthand; Evans knew Devanagari, but no source makes it his model"),
    "Plrd": ("", "Unicode N3789 (L2/10-093); Lewis & Dorais 2003",
             "structure adopted from Cree syllabics, with Latin, shorthand and Miao signs"),
    "Wole": ("", "Everson, Unicode N4146",
             "one class of signs from Latin letters, the other invented; c.1905-1909"),
    "Vaii": ("", "Unicode ch.19; Tuchscherer & Hair 2002, History in Africa 29",
             "Latin, Arabic and possibly Cherokee influence proposed; none established"),
    "Mend": ("", "Unicode N4133 (L2/11-301)",
             "syllabic blueprint unquestionably influenced by Vai; right to left"),
    "Kpel": ("", "L2/09-326; Tuchscherer & Hair 2002",
             "devised in the 1930s by Gbili; stimulated by the syllabic organisation of Vai"),
    "Loma": ("", "Unicode N3756 (L2/10-005)",
             "devised in the 1930s by Wido Zobo; Vai stimulus, no shared letterforms"),
    "Bass": ("", "Unicode N3941R (L2/10-382R); Unicode ch.19",
             "may have been influenced by Vai; typeset from 1907"),
    "Medf": ("", "L2/16-101R",
             "strong influence of English orthography, capital and small letters; revealed 1927"),
    "Afak": ("", "Everson, Unicode N4132 (L2/11-297R); Dubelaar 1976",
             "unrelated to any other script; acrophonic rebus; devised 1908"),
    "Olck": ("", "Unicode N2505; Zide 1996",
             "alphabetic, sharing none of the syllabic properties of Indic scripts; shapes from familiar objects"),
    "Nagm": ("", "L2/21-031R; Unicode ch.13",
             "organisation modelled on Ol Chiki; developed from the 1950s"),
    "Onao": ("", "L2/22-151",
             "invented by Mahendra Nath Sardar between 1981 and 1992; Bhumij was written in Odia, Bengali, Devanagari and Latin"),
    "Wara": ("", "Everson, Unicode N4259 (L2/12-118)",
             "devised by Lako Bodra in the 1950s; full vowel letters"),
    "Tols": ("", "Pandey, L2/23-024",
             "invented in 1988 by Narayan Oraon, published 1999"),
    "Toto": ("", "Anderson & Evans 2024, Nepalese Linguistics 38; L2/19-330",
             "an entirely novel set of letters from everyday objects; launched May 2015"),
    "Chis": ("", "L2/22-218R3",
             "invented in 1986 by Jayanta Kumar Mahata from Kurmali ritual and rangoli signs"),
    "Tnsa": ("", "Morey, eScholarship 5nz191bp; L2/13-231",
             "developed since 1990 by Lakhum Mossang; genetically unrelated to existing scripts"),
    "Wcho": ("", "Unicode N4787",
             "devised 2001-2012 by Banwang Losu; a simple alphabetic script"),
    "Mroo": ("", "Unicode N3589",
             "a messianic script of the 1980s with no genetic relationship to existing scripts"),
    "Pauc": ("", "L2/11-104R",
             "no genetic relationship with any other writing system; revealed 1902, alphabetic form 1931"),
    "Hmng": ("", "Unicode ch.16; Smalley, Vang & Yang 1990, Mother of Writing",
             "devised by Shong Lue Yang in 1959; some letters may recall Lao and Latin"),
    "Hmnp": ("", "Everson, Unicode N4780R3",
             "several consonant letters appear derived from Hebrew characters; 1980s"),
    "Sora": ("", "Everson, Unicode N3647R (L2/09-189R)",
             "of the Brahmic type, consonants with an inherent vowel; revealed 18 June 1936"),
    "Gonm": ("", "Pandey, L2/15-090R",
             "no genetic relationship to other writing systems, but based upon the Brahmi model"),
    "Gong": ("", "Pandey, L2/15-235R",
             "not genetically related to other scripts, but strongly resembles Modi; c.1750 is a researchers' claim, 1942 the firm evidence"),
    "Gukh": ("", "L2/22-157",
             "an alphasyllabary based upon the Brahmi model, created 1995"),
    "Krai": ("Old Kirat lipi", "L2/22-043R",
             "derived from the Old Kirat script from which Limbu also comes; Sumhung Lipi of the 1920s, redesigned 2000"),
    "Mtei": ("", "Everson, Unicode N3158",
             "earliest use dated 11th-12th c., from the Tibetan group; Tomba 1993 calls the old documents forgeries"),
    "Brah": ("", "Bright 1996, in Daniels & Bright; Salomon 1998, Indian Epigraphy",
             "Aramaic origin after Buhler is the majority view; not settled"),
    "Tirh": ("Gaudi", "Pandey, L2/11-175R, after Salomon 1998",
             "derived from Gaudi (proto-Bengali); a sibling of Bengali, not its child; inscriptions 13th c."),
    "Kthi": ("Nagari", "Pandey, Unicode N3389",
             "Kaithi and Devanagari are siblings within the Nagari family"),
    "Mahj": ("Landa", "Pandey, Unicode N4126",
             "often called a derivative of Kaithi or Devanagari; structure resembles Landa"),
    "Saur": ("", "unsourced",
             "Brahmic, exact derivation unknown; Randle 1943 records it printed in 1880"),
    "Diak": ("", "Pandey, L2/18-016R",
             "descended from Brahmi through Grantha; closest to medieval Sinhala"),
    "Tibt": ("Late Gupta", "van Schaik 2012, in Tibetan manuscript studies",
             "north Indian and Nepalese late Gupta inscriptions the closest models"),

    # Southeast Asia
    "Tavt": ("Sukhothai", "Thai Research Fund report PDG4810005",
             "Tai Dam script a derivative of Sukhothai script, arriving around the 16th c."),
    "Tayo": ("", "L2/22-289; Ferlus 2006",
             "a common origin with the Tai Dam group; written top to bottom in right-to-left columns"),
    "Talu": ("", "Grabowsky, Manuscript Cultures 3",
             "a simplification of Tai Tham, officially introduced 1955"),
    "Kali": ("", "Unicode N3038",
             "ordering and some shapes show Brahmic relation, most shapes developed independently"),
    "Leke": ("", "Kato 2026 (user.keio.ac.jp/~kato/LekeScript.pdf); Unicode N4438",
             "created mid-19th c. with the Leke religion; some borrowing from Old Mon and Burmese"),
    "Maka": ("", "Pandey, L2/15-233; Unicode ch.17",
             "closest relative Rejang; no evolutionary relationship with Buginese"),
    "Hano": ("", "Unicode ch.17; Miller, Unicode Technical Note 35",
             "related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting"),
    "Buhd": ("", "Unicode ch.17; Miller, Unicode Technical Note 35",
             "related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting"),
    "Tagb": ("", "Unicode ch.17; Miller, Unicode Technical Note 35",
             "related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting"),
    "Tglg": ("", "Miller 2011, 11-PLC; Unicode ch.17",
             "Kawi, Bugis, Sumatran and Gujarati origins all argued; first verifiably dated text 1593"),

    # East Asia
    "Tang": ("", "Cook, Unicode N3297",
             "invented by decree with Chinese writing as conceptual model; no shared characters"),
    "Kitl": ("", "Kane 2009, The Kitan Language and Script",
             "on the basis of Chinese clerical script with modifications; most characters novel"),
    "Kits": ("", "Kane 2009",
             "created after contact with Uighurs; phonetic components, no shared characters with the large script"),
    "Jurc": ("", "Kara 1996, in Daniels & Bright; Jinshi 73",
             "many characters copies or distorted copies of Chinese and Khitan large script"),
    "Shui": ("", "L2/14-243 (Shuishu proposal)",
             "about half the characters derive from Chinese in mirrored or inverted form"),
    "Yiii": ("", "Bradley 2003; Unicode ch.18",
             "glyphs independent in form; earliest dated object a bronze bell of 1485"),
    "Hang": ("", "Ledyard 1966; Haerye 1446",
             "five or six consonant shapes from Phags-pa (Ledyard); the Haerye derives them from the speech organs"),
    "Blis": ("", "Bliss 1949, Semantography; Unicode N5228",
             "an ideographic system inspired by Chinese characters, devised 1942-1949"),
    "Cirt": ("", "Everson, Unicode N4013",
             "a runiform script built by Tolkien on the model of Germanic runes"),
    "Sara": ("", "Everson, Unicode N4013; Smith 2007, Parma Eldalamberon",
             "Tolkien's first Elvish script, from 1919; the precursor of Tengwar"),
    "Teng": ("", "Everson, Unicode N4013",
             "the featural Tengwar, developed by Tolkien from Sarati"),
    "Piqd": ("", "L2/20-181",
             "built on ten characters designed for Star Trek: The Motion Picture, 1979"),
}

# Sample codepoints for the glyph specimens, keyed by ISO 15924 code.
# Only needed where the Unicode block start is a poor specimen (combining marks,
# format characters, or a block whose first rows are rarely-drawn variants).
SPECIMEN_OVERRIDE = {
    "Arab": "ابجدهو",
    "Hebr": "אבגדהו",
    "Grek": "ΑΒΓΔΕΖ",
    "Cyrl": "АБВГДЕ",
    "Latn": "ABCDEF",
    "Hani": "中文字書写語",
    "Hans": "汉字简体中文",
    "Hant": "漢字繁體中文",
    "Deva": "अआइकखग",
    "Thai": "กขฃคฅฆ",
    "Hang": "가나다라마바",
    "Hira": "あいうえおか",
    "Kana": "アイウエオカ",
    "Ethi": "ሀለሐመሠረ",
    "Armn": "ԱԲԳԴԵԶ",
    "Geor": "აბგდევ",
    "Taml": "அஆஇகஙச",
    "Beng": "অআইকখগ",
    "Telu": "అఆఇకఖగ",
    "Knda": "ಅಆಇಕಖಗ",
    "Mlym": "അആഇകഖഗ",
    "Guru": "ਅਆਇਕਖਗ",
    "Gujr": "અઆઇકખગ",
    "Orya": "ଅଆଇକଖଗ",
    "Sinh": "අආඇකඛග",
    "Mymr": "ကခဂဃငစ",
    "Khmr": "កខគឃងច",
    "Laoo": "ກຂຄງຈຊ",
    "Tibt": "ཀཁགངཅཆ",
    "Mong": "ᠠᠡᠢᠣᠤᠥ",
    "Syrc": "ܐܒܓܕܖܗ",
    "Thaa": "ހށނރބޅ",
    "Nkoo": "ߊߋߌߍߎߏ",
    "Adlm": "\U0001e900\U0001e901\U0001e902\U0001e903\U0001e904\U0001e905",
    "Cher": "ᎠᎡᎢᎣᎤᎥ",
    "Copt": "ⲀⲂⲄⲆⲈⲊ",
    "Egyp": "\U00013000\U00013001\U00013002\U00013003\U00013004\U00013005",
    "Xsux": "\U00012000\U00012001\U00012002\U00012003\U00012004\U00012005",
    "Egyh": "\U00013009\U0001300a\U0001300b\U0001300c\U0001300d\U0001300e",
    "Brai": "⠁⠃⠉⠙⠑⠋",
    # Variant and composite registry codes own no codepoint range, so the
    # specimen is named here and drawn in the face of the script they style.
    "Latf": "ABCDEF",
    "Latg": "ABCDEF",
    "Cyrs": "АБВГДЕ",
    "Aran": "ابجدهو",
    "Syre": "ܐܒܓܕܗܘ",
    "Syrj": "ܐܒܓܕܗܘ",
    "Syrn": "ܐܒܓܕܗܘ",
    "Jamo": "ᄀᄂᄃᄅᄆᄇ",
    "Hrkt": "あいうカキク",
    "Jpan": "日本語かなカ",
    "Kore": "한국어漢字書",
    "Hanb": "漢字ㄅㄆㄇㄈ",
    "Hntl": "漢字ABCD",
    "Bopo": "ㄅㄆㄇㄈㄉㄊ",
    "Zsye": "☺★☂✈♪⚑",
}
