# -*- coding: utf-8 -*-
"""Curated descent of every ISO 15924 script.

Wikidata P144 covers barely half the registry and disagrees with itself on the
Semitic chain, so descent is curated here against palaeographic scholarship and
the Unicode encoding proposals. Every descent edge, attested ones included,
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
            Follows Unicode 17.0 Table 6-1 where it lists the script, except
            the rows in TYPE_EXCEPTIONS below; verify.py check 16 holds this.
            Cans as syllabary is disputed: Bright and Bringhurst say
            alphasyllabary.
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
G["Xsux"] = ("Pcun", "attested", "logographic", "ltr", -2600, 75, "historical")
G["Pelm"] = ("Pcun", "stimulus", "undeciphered", "rtl", -3050, -2900, "undeciphered")
G["Xpeo"] = ("Xsux", "stimulus", "alphabet", "ltr", -520, -330, "historical")

# ------------------------------------------------------------------ EGYPT ----
G["Egyh"] = ("Egyp", "attested", "logographic", "rtl", -2700, 300, "historical")
G["Egyd"] = ("Egyh", "attested", "logographic", "rtl", -650, 500, "historical")
G["Mero"] = ("Egyp", "attested", "alphabet", "rtl", -150, 400, "historical")
G["Merc"] = ("Egyd", "attested", "alphabet", "rtl", -220, 400, "historical")
G["Psin"] = ("Egyp", "attested", "abjad", "varies", -1900, -1400, "historical")

# -------------------------------------------------- PROTO-SINAITIC / SEMITIC --
G["Ugar"] = ("Psin", "stimulus", "alphabet", "ltr", -1250, -1190, "historical")
G["Phnx"] = ("Psin", "attested", "abjad", "rtl", -1000, 100, "historical")
G["Samr"] = ("Phnx", "contested", "abjad", "rtl", 350, None, "living")
G["Sarb"] = ("Psin", "contested", "abjad", "boustrophedon", -800, 600, "historical")
G["Narb"] = ("Psin", "attested", "abjad", "varies", -600, 400, "historical")
G["Ethi"] = ("Sarb", "attested", "abugida", "ltr", 200, None, "living")
G["Tfng"] = ("Phnx", "contested", "alphabet", "varies", -138, None, "living")

# ----------------------------------------------------------------- ARAMAIC ---
G["Armi"] = ("Phnx", "attested", "abjad", "rtl", -900, -100, "historical")
G["Hebr"] = ("Armi", "attested", "abjad", "rtl", -300, None, "living")
G["Nbat"] = ("Armi", "attested", "abjad", "rtl", -95, 400, "historical")
G["Palm"] = ("Armi", "attested", "abjad", "rtl", -44, 300, "historical")
G["Hatr"] = ("Armi", "attested", "abjad", "rtl", -98, 300, "historical")
G["Syrc"] = ("Armi", "attested", "abjad", "rtl", 6, None, "living")
G["Syre"] = ("Syrc", "variant", "variant", "rtl", 100, None, "living")
G["Syrj"] = ("Syrc", "variant", "variant", "rtl", 400, None, "living")
G["Syrn"] = ("Syrc", "variant", "variant", "rtl", 400, None, "living")
G["Mand"] = ("Elym", "contested", "alphabet", "rtl", 350, None, "living")
G["Mani"] = ("Syrc", "contested", "abjad", "rtl", 250, 1000, "historical")
G["Elym"] = ("Armi", "attested", "abjad", "rtl", -150, 300, "historical")
G["Chrs"] = ("Armi", "attested", "abjad", "rtl", -100, 800, "historical")
G["Prti"] = ("Armi", "attested", "abjad", "rtl", -89, 250, "historical")
G["Phli"] = ("Armi", "attested", "abjad", "rtl", 224, 900, "historical")
G["Phlp"] = ("Phli", "attested", "abjad", "rtl", 600, 800, "historical")
G["Phlv"] = ("Phli", "attested", "abjad", "rtl", 619, 1100, "historical")
G["Avst"] = ("Phlv", "attested", "alphabet", "rtl", 500, None, "living")
G["Sogo"] = ("Armi", "attested", "abjad", "rtl", 313, 400, "historical")
G["Sogd"] = ("Sogo", "attested", "abjad", "varies", 600, 1400, "historical")
G["Ougr"] = ("Sogd", "attested", "abjad", "ttb", 800, 1800, "historical")
G["Mong"] = ("Ougr", "attested", "alphabet", "ttb", 1224, None, "living")
G["Orkh"] = ("Sogd", "contested", "alphabet", "rtl", 700, 1000, "historical")
G["Hung"] = ("Orkh", "contested", "alphabet", "rtl", 900, None, "revived")
G["Yezi"] = ("Syrc", "contested", "alphabet", "rtl", 1200, None, "living")

# ------------------------------------------------------------------ ARABIC ---
G["Arab"] = ("Nbat", "attested", "abjad", "rtl", 512, None, "living")
G["Aran"] = ("Arab", "variant", "variant", "rtl", 1400, None, "living")
G["Thaa"] = ("Arab", "stimulus", "alphabet", "rtl", 1705, None, "living")
G["Rohg"] = ("Arab", "stimulus", "alphabet", "rtl", 1980, None, "living")
G["Adlm"] = ("Arab", "stimulus", "alphabet", "rtl", 1989, None, "living")
G["Nkoo"] = ("Arab", "stimulus", "alphabet", "rtl", 1949, None, "living")
G["Gara"] = ("Arab", "stimulus", "alphabet", "rtl", 1961, None, "living")
G["Osma"] = ("Arab", "stimulus", "alphabet", "ltr", 1920, None, "living")
G["Bamu"] = ("Arab", "contested", "syllabary", "ltr", 1896, None, "living")
G["Berf"] = ("Arab", "invented", "alphabet", "ltr", 1950, None, "living")

# ------------------------------------------------------------------- GREEK ---
G["Grek"] = ("Phnx", "attested", "alphabet", "ltr", -750, None, "living")
G["Cari"] = ("Grek", "contested", "alphabet", "varies", -700, -300, "historical")
G["Lyci"] = ("Grek", "attested", "alphabet", "ltr", -500, -300, "historical")
G["Lydi"] = ("Grek", "attested", "alphabet", "rtl", -700, -300, "historical")
G["Sidt"] = ("Phnx", "contested", "alphabet", "rtl", -500, -300, "historical")
G["Copt"] = ("Grek", "attested", "alphabet", "ltr", 100, None, "living")
G["Goth"] = ("Grek", "attested", "alphabet", "ltr", 350, 900, "historical")
G["Armn"] = ("Grek", "contested", "alphabet", "ltr", 405, None, "living")
G["Aghb"] = ("Armn", "contested", "alphabet", "ltr", 420, 1000, "historical")
G["Geok"] = ("Grek", "contested", "alphabet", "ltr", 430, 1100, "historical")
G["Geor"] = ("Geok", "attested", "alphabet", "ltr", 982, None, "living")
G["Glag"] = ("Grek", "contested", "alphabet", "ltr", 863, 1900, "historical")
G["Cyrl"] = ("Grek", "attested", "alphabet", "ltr", 921, None, "living")
G["Cyrs"] = ("Cyrl", "variant", "variant", "ltr", 900, None, "living")
G["Perm"] = ("Cyrl", "stimulus", "alphabet", "ltr", 1372, 1700, "historical")
G["Ital"] = ("Grek", "attested", "alphabet", "varies", -700, -100, "historical")
G["Runr"] = ("Ital", "attested", "alphabet", "varies", 150, 1500, "historical")
G["Elba"] = ("Grek", "stimulus", "alphabet", "ltr", 1761, 1800, "historical")
G["Vith"] = ("Grek", "contested", "alphabet", "ltr", 1844, 1900, "historical")
G["Todr"] = ("Grek", "stimulus", "alphabet", "ltr", 1750, 1900, "historical")

# ------------------------------------------------------------------- LATIN ---
G["Latn"] = ("Ital", "attested", "alphabet", "ltr", -600, None, "living")
G["Latf"] = ("Latn", "variant", "variant", "ltr", 1150, None, "living")
G["Latg"] = ("Latn", "variant", "variant", "ltr", 700, None, "living")
G["Ogam"] = ("Latn", "stimulus", "alphabet", "varies", 350, 600, "historical")
G["Moon"] = ("Latn", "attested", "alphabet", "boustrophedon", 1845, None, "living")
G["Brai"] = ("Latn", "stimulus", "alphabet", "ltr", 1824, None, "living")
G["Dupl"] = ("Latn", "stimulus", "alphabet", "ltr", 1860, None, "living")
G["Visp"] = ("Latn", "invented", "featural", "ltr", 1867, 1900, "historical")
G["Shaw"] = ("Latn", "invented", "alphabet", "ltr", 1960, None, "constructed")
G["Dsrt"] = ("Latn", "stimulus", "alphabet", "ltr", 1854, 1869, "historical")
G["Osge"] = ("Latn", "attested", "alphabet", "ltr", 2006, None, "living")
G["Lisu"] = ("Latn", "attested", "alphabet", "ltr", 1915, None, "living")
G["Sunu"] = ("Latn", "stimulus", "alphabet", "ltr", 1942, None, "living")
G["Sgnw"] = ("Latn", "invented", "featural", "ttb", 1974, None, "living")
G["Zsye"] = ("Latn", "composite", "symbols", "ltr", 1999, None, "living")

# ------------------------------------------- AMERICAS AND THE PACIFIC --------
G["Cher"] = ("Latn", "stimulus", "syllabary", "ltr", 1821, None, "living")
G["Cans"] = ("Latn", "stimulus", "syllabary", "ltr", 1840, None, "living")
G["Plrd"] = ("Cans", "stimulus", "syllabary", "ltr", 1904, None, "living")
G["Wole"] = ("Latn", "stimulus", "syllabary", "ltr", 1905, 1950, "historical")

# --------------------------------------------------------- WEST AFRICA -------
G["Vaii"] = ("Latn", "stimulus", "syllabary", "ltr", 1833, None, "living")
G["Mend"] = ("Vaii", "stimulus", "syllabary", "rtl", 1917, None, "living")
G["Kpel"] = ("Vaii", "stimulus", "syllabary", "ltr", 1930, None, "living")
G["Loma"] = ("Vaii", "stimulus", "syllabary", "ltr", 1930, None, "living")
G["Bass"] = ("Vaii", "stimulus", "alphabet", "ltr", 1907, None, "living")
G["Medf"] = ("Latn", "stimulus", "alphabet", "ltr", 1927, None, "living")
G["Afak"] = ("Latn", "invented", "syllabary", "ltr", 1908, None, "living")

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
G["Brah"] = ("Armi", "contested", "abugida", "ltr", -250, 500, "historical")
G["Khar"] = ("Armi", "attested", "abugida", "rtl", -250, 300, "historical")
G["Sidd"] = ("Brah", "attested", "abugida", "ltr", 588, 1200, "historical")
G["Deva"] = ("Sidd", "attested", "abugida", "ltr", 851, None, "living")
G["Shrd"] = ("Brah", "attested", "abugida", "ltr", 800, 1900, "historical")
G["Takr"] = ("Shrd", "attested", "abugida", "ltr", 1500, 1950, "historical")
G["Dogr"] = ("Takr", "attested", "abugida", "ltr", 1860, 1950, "historical")
G["Guru"] = ("Shrd", "attested", "abugida", "ltr", 1570, None, "living")
G["Khoj"] = ("Shrd", "attested", "abugida", "ltr", 1500, None, "living")
G["Mult"] = ("Shrd", "attested", "abjad", "ltr", 1750, 1950, "historical")
G["Sind"] = ("Shrd", "attested", "abugida", "ltr", 1550, 1910, "historical")
G["Mahj"] = ("Deva", "contested", "alphabet", "ltr", 1600, 1950, "historical")
G["Kthi"] = ("Sidd", "attested", "abugida", "ltr", 1550, 1950, "historical")
G["Modi"] = ("Deva", "attested", "abugida", "ltr", 1600, 1950, "historical")
G["Nand"] = ("Deva", "attested", "abugida", "ltr", 1100, 1800, "historical")
G["Gujr"] = ("Deva", "attested", "abugida", "ltr", 1592, None, "living")
G["Sylo"] = ("Kthi", "attested", "abugida", "ltr", 1500, None, "living")
G["Gong"] = ("Modi", "contested", "abugida", "ltr", 1750, None, "living")
G["Gonm"] = ("Brah", "stimulus", "abugida", "ltr", 1918, None, "living")
G["Beng"] = ("Sidd", "attested", "abugida", "ltr", 1350, None, "living")
G["Tirh"] = ("Sidd", "attested", "abugida", "ltr", 1200, None, "living")
G["Orya"] = ("Sidd", "attested", "abugida", "ltr", 1300, None, "living")
G["Newa"] = ("Sidd", "attested", "abugida", "ltr", 908, None, "living")
G["Ranj"] = ("Newa", "attested", "abugida", "ltr", 1099, None, "living")
G["Bhks"] = ("Brah", "attested", "abugida", "ltr", 1000, 1200, "historical")
G["Mtei"] = ("Brah", "contested", "abugida", "ltr", 1100, None, "living")
G["Cakm"] = ("Mymr", "attested", "abugida", "ltr", 1700, None, "living")
G["Sora"] = ("Brah", "stimulus", "abugida", "ltr", 1936, None, "living")
G["Gukh"] = ("Brah", "stimulus", "abugida", "ltr", 1995, None, "living")

# ------------------------------------------------------- BRAHMIC: TIBETAN ----
G["Tibt"] = ("Brah", "attested", "abugida", "ltr", 650, None, "living")
G["Marc"] = ("Tibt", "contested", "abugida", "ltr", 1000, None, "living")
G["Phag"] = ("Tibt", "attested", "abugida", "ttb", 1269, 1400, "historical")
G["Lepc"] = ("Tibt", "attested", "abugida", "ltr", 1720, None, "living")
G["Limb"] = ("Lepc", "contested", "abugida", "ltr", 1850, None, "living")
G["Krai"] = ("Limb", "contested", "abugida", "ltr", 1925, None, "living")
G["Zanb"] = ("Tibt", "attested", "abugida", "ltr", 1686, 1800, "historical")
G["Soyo"] = ("Ranj", "attested", "abugida", "ltr", 1686, 1800, "historical")

# ------------------------------------------------------- BRAHMIC: SOUTHERN ---
G["Gran"] = ("Brah", "attested", "abugida", "ltr", 600, None, "living")
G["Taml"] = ("Brah", "attested", "abugida", "ltr", 600, None, "living")
G["Mlym"] = ("Gran", "attested", "abugida", "ltr", 1100, None, "living")
G["Tutg"] = ("Gran", "attested", "abugida", "ltr", 1000, None, "living")
G["Saur"] = ("Brah", "contested", "abugida", "ltr", 1880, None, "living")
G["Sinh"] = ("Brah", "attested", "abugida", "ltr", -200, None, "living")
G["Diak"] = ("Gran", "attested", "abugida", "ltr", 900, 1700, "historical")
G["Knda"] = ("Brah", "attested", "abugida", "ltr", 450, None, "living")
G["Telu"] = ("Brah", "attested", "abugida", "ltr", 600, None, "living")

# --------------------------------------------------- BRAHMIC: SOUTHEAST ASIA -
G["Khmr"] = ("Brah", "attested", "abugida", "ltr", 611, None, "living")
G["Thai"] = ("Khmr", "attested", "abugida", "ltr", 1292, None, "living")
G["Laoo"] = ("Thai", "attested", "abugida", "ltr", 1494, None, "living")
G["Tavt"] = ("Thai", "attested", "abugida", "ltr", 1500, None, "living")
G["Tayo"] = ("Thai", "contested", "abugida", "ttb", 1500, None, "living")
G["Mymr"] = ("Brah", "attested", "abugida", "ltr", 1113, None, "living")
G["Leke"] = ("Mymr", "contested", "abugida", "ltr", 1844, None, "living")
G["Kali"] = ("Mymr", "stimulus", "alphabet", "ltr", 1962, None, "living")
G["Lana"] = ("Mymr", "attested", "abugida", "ltr", 1376, None, "living")
G["Talu"] = ("Lana", "attested", "abugida", "ltr", 1955, None, "living")
G["Tale"] = ("Mymr", "attested", "abugida", "ltr", 1407, None, "living")
G["Ahom"] = ("Mymr", "attested", "abugida", "ltr", 1300, None, "revived")
G["Cham"] = ("Brah", "attested", "abugida", "ltr", 400, None, "living")
G["Kawi"] = ("Brah", "attested", "abugida", "ltr", 750, 1500, "historical")
G["Java"] = ("Kawi", "attested", "abugida", "ltr", 1500, None, "living")
G["Bali"] = ("Kawi", "attested", "abugida", "ltr", 914, None, "living")
G["Sund"] = ("Kawi", "contested", "abugida", "ltr", 1400, None, "living")
G["Rjng"] = ("Kawi", "attested", "abugida", "ltr", 1750, None, "living")
G["Batk"] = ("Kawi", "contested", "abugida", "ltr", 1764, None, "living")
G["Bugi"] = ("Kawi", "contested", "abugida", "ltr", 1600, None, "living")
G["Maka"] = ("Rjng", "contested", "abugida", "ltr", 1600, 1900, "historical")
G["Tglg"] = ("Kawi", "contested", "abugida", "ltr", 1550, None, "revived")
G["Hano"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")
G["Buhd"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")
G["Tagb"] = ("Tglg", "contested", "abugida", "ltr", 1600, None, "living")

# ------------------------------------------------------------------ AEGEAN ---
G["Linb"] = ("Lina", "attested", "syllabary", "ltr", -1400, -1200, "historical")
G["Cpmn"] = ("Lina", "attested", "undeciphered", "ltr", -1500, -1050, "undeciphered")
G["Cprt"] = ("Cpmn", "attested", "syllabary", "rtl", -1100, -300, "historical")

# -------------------------------------------------------------------- HAN ----
G["Seal"] = ("Hani", "variant", "variant", "ttb", -800, None, "living")
G["Hans"] = ("Hani", "variant", "variant", "ltr", 1956, None, "living")
G["Hant"] = ("Hani", "variant", "variant", "varies", -200, None, "living")
G["Hira"] = ("Hani", "attested", "syllabary", "varies", 800, None, "living")
G["Kana"] = ("Hani", "attested", "syllabary", "varies", 825, None, "living")
G["Bopo"] = ("Hani", "attested", "syllabary", "varies", 1913, None, "living")
G["Nshu"] = ("Hani", "attested", "syllabary", "ttb", 1850, None, "revived")
G["Tang"] = ("Hani", "stimulus", "logographic", "ltr", 1036, 1500, "historical")
G["Kitl"] = ("Hani", "stimulus", "logographic", "ttb", 920, 1200, "undeciphered")
G["Kits"] = ("Ougr", "stimulus", "logographic", "ttb", 925, 1200, "undeciphered")
G["Jurc"] = ("Kitl", "attested", "logographic", "ttb", 1119, 1500, "historical")
G["Yiii"] = ("Hani", "contested", "syllabary", "ltr", 1485, None, "living")
G["Nkgb"] = ("Nkdb", "contested", "syllabary", "ltr", 1619, None, "living")
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

# Where the type column departs from Unicode 17.0 Table 6-1, and why.
# code: (Table 6-1 type, reason)
TYPE_EXCEPTIONS = {
    "Ethi": ("syllabary", "ch.6 prose: 'traditionally analyzed as an abugida, because the base "
                          "character for each consonantal series is understood as having an inherent vowel'"),
    "Nshu": ("logographic", "ch.18: 'Nushu characters typically represent the phonetic values of "
                            "syllables'; some signs are ideographs"),
    "Lina": ("logographic", "undeciphered: the plate types it by what is known, not by its sign count"),
    "Cpmn": ("syllabary", "undeciphered: the plate types it by what is known, not by its sign count"),
}


# ---------------------------------------------------------------- SOURCES ----
# The authority for every descent edge and every argued root: the parent, the
# kind of link, and the first dated object behind the start year.
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
    "Dsrt": ("Pitman 1847 phonotypy", "Beesley, 'Deseret in Unicode'; Unicode ch.20",
             "Pitman's phonotypy the starting point, then an entirely new set of characters, adopted Dec 1853; not actively promoted after 1869; now of interest to historians and hobbyists"),
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
    "Afak": ("", "Everson, Unicode N4132 (L2/11-297R); Dubelaar 1976; L2/25-078",
             "unrelated to any other script; acrophonic rebus; devised 1908; still taught as grade-1 Afaka among the few literate in it"),
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
             "Aramaic origin after Buhler is the majority view; not settled; earliest securely dated texts the Ashokan edicts, c.250 BCE"),
    "Tirh": ("Gaudi", "Pandey, L2/11-175R, after Salomon 1998; Unicode ch.15",
             "derived from Gaudi (proto-Bengali); a sibling of Bengali, not its child; inscriptions 13th c.; still used for religious and literary manuscripts and personal letters"),
    "Kthi": ("Nagari", "Pandey, Unicode N3389",
             "Kaithi and Devanagari are siblings within the Nagari family"),
    "Mahj": ("Landa", "Pandey, Unicode N4126",
             "often called a derivative of Kaithi or Devanagari; structure resembles Landa"),
    "Saur": ("", "Everson & Krishnamoorty, L2/05-222R2 (Unicode N2969R2)",
             "'of the Brahmic type'; its origin 'is not known' (Ucida, quoted there); "
             "reformed and cast in type by T. M. Rama Ray in the 1880s"),
    "Diak": ("", "Pandey, L2/18-016R",
             "descended from Brahmi through Grantha; closest to medieval Sinhala"),
    "Tibt": ("Late Gupta", "van Schaik 2012, in Tibetan manuscript studies",
             "north Indian and Nepalese late Gupta inscriptions the closest models"),

    # Southeast Asia
    "Tavt": ("Sukhothai", "Thai Research Fund report PDG4810005",
             "Tai Dam script a derivative of Sukhothai script, arriving around the 16th c."),
    "Tayo": ("", "L2/22-289; Ferlus 2006; Unicode ch.16",
             "a common origin with the Tai Dam group; written top to bottom in right-to-left columns; teaching and learning supported by local government and teachers"),
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
    "Xsux": ("", "Unicode ch.11; L2/25-211 (proto-cuneiform)",
             "cuneiform proper from c.2700-2600 BCE (Fara, Abu Salabikh); -2900 is the end of the archaic period"),
    "Egyh": ("", "Regulski, Oxford Handbook of Topics in Archaeology",
             "earliest hieratic on the stone vessels under the Step Pyramid, late 2nd dynasty to Djoser"),
    "Egyd": ("Abnormal Hieratic", "Depauw, A Companion to Demotic Studies",
             "develops out of late hieratic in the 7th c. BCE; the earliest named object is not sourced here"),
    "Mero": ("", "Rilly, UCLA Encyclopedia of Egyptology",
             "created under Taneyidamani, first half of the 2nd c. BCE, from Egyptian hieroglyphs with new values"),
    "Merc": ("", "Rilly, UCLA Encyclopedia of Egyptology; Priese 1973",
             "developed from Demotic; earliest datable object a sistrum handle naming Arnekhamani, c.220 BCE"),
    "Psin": ("", "L2/19-299 (Proto-Sinaitic)",
             "most scholars agree it derives from Egyptian hieroglyphs; first attested 19th c. BCE (Wadi el-Hol)"),
    "Phnx": ("Proto-Canaanite", "Unicode ch.10; Ahiram sarcophagus, KAI 1",
             "first long text the Ahiram sarcophagus, c.1000 BCE on palaeography; its date is disputed"),
    "Samr": ("Paleo-Hebrew", "Barag, in Cambridge History of Judaism; Langlois 2019",
             "a conscious creation of the 4th c. CE; Cross and Purvis argued a Hasmonean branch of paleo-Hebrew"),
    "Sarb": ("Proto-Canaanite", "Hasselbach, in The Semitic Languages; Sass",
             "split off a Proto-Canaanite variant before 1000 BCE; Sass derives it from Phoenician-type letters"),
    "Ethi": ("", "Drewes, RIE III/B; Breton 2019, Cahiers d'etudes africaines",
             "earliest Ge'ez text the Addi Gelemo sceptre, late 2nd to early 3rd c. CE; vocalised under Ezana"),
    "Nbat": ("", "Naveh, The Nabataeans",
             "Elusa inscription early 2nd c. BCE not yet Nabataean in form; Aslah inscription, Petra, 95 BCE"),
    "Palm": ("", "Unicode ch.10",
             "inscriptions from 44 BCE to about 280 CE"),
    "Hatr": ("", "Unicode N4324 (L2/12-312)",
             "inscriptions from 98-97 BCE to about 241 CE"),
    "Syrc": ("", "Healey 2011, Hugoye; Drijvers & Healey As55",
             "the earliest dated Syriac inscription is the Birecik inscription of 6 CE"),
    "Mand": ("", "Encyclopaedia Iranica 'Mandaeans v'; Haberl 2006, BASOR",
             "based on the script of the Elymaean rock inscriptions; Unicode also allows Parthian chancery; bowls 4th-7th c."),
    "Elym": ("", "L2/17-226 (Elymaic); Unicode ch.10",
             "derives from Aramaic; earliest on coins of the 2nd c. BCE"),
    "Chrs": ("", "L2/18-164R2 (Chorasmian)",
             "from Imperial Aramaic; dated cursive from Toprak-Kala, 3rd c. CE; earlier dates in the proposal unresolved"),
    "Prti": ("", "Skjaervo, Encyclopaedia Iranica 'Iran vi.3'; MacKenzie, 'Dates and dating'",
             "Nisa ostraca of the 1st c. BCE, one dated 89 BCE"),
    "Phli": ("", "Humbach, Encyclopaedia Iranica 'Epigraphy i'; Rezakhani 2016",
             "Sasanian inscriptions from 224 CE; descent through the Persis coin script is denied by Rezakhani"),
    "Phlp": ("", "Encyclopaedia Iranica 'Pahlavi Psalter'; Unicode ch.10",
             "6th or 7th c. CE, after 552; more archaic than Book Pahlavi"),
    "Phlv": ("", "Hintze 2014, Kratylos; Cereti",
             "earliest dated witnesses the Elephantine papyri, 619-629 CE; the 4th-c. sarcophagus anchor is Islamic-period"),
    "Avst": ("", "Unicode ch.10; Hoffmann, Encyclopaedia Iranica 'Avestan script'",
             "created about the 5th-6th c. CE for the Avesta; earliest manuscript 1288; still used in Zoroastrian liturgy"),
    "Sogo": ("", "Encyclopaedia Iranica 'Ancient Letters'; Unicode ch.14",
             "Ancient Letters securely dated 312-313 CE; the Kultobe inscriptions possibly earlier"),
    "Sogd": ("", "Unicode ch.14",
             "derived from Old Sogdian, used from the 7th to the 14th c. CE"),
    "Mong": ("", "Unicode ch.13; Brose 2005",
             "adopted 1204 by tradition; earliest surviving text the Stele of Yisungge, c.1224-1225"),
    "Arab": ("", "Hoyland, 'The birth of Arabic in stone'; Robin et al. 2014, CRAI",
             "earliest dated text in Arabic script Zabad, 512; Namara (328) and Jabal Ramm are in Nabataean script"),
    "Khar": ("", "Strauch; Baums 2016; Salomon 1998",
             "no securely dated document before the Ashokan edicts at Shahbazgarhi and Mansehra, mid-3rd c. BCE"),
    "Grek": ("", "Janko, on Methone; Jeffery, Local Scripts of Archaic Greece",
             "Dipylon jug c.740 BCE and Nestor's cup; Gabii c.770 on the traditional chronology; earliest texts right to left"),
    "Copt": ("", "Claremont Coptic Encyclopedia, 'Old Coptic'",
             "Old Coptic papyri of the 1st-2nd c. CE; Greek letters plus six or seven from Demotic"),
    "Geor": ("", "Aleksidze 1983; Typotheque 2023",
             "first Mkhedruli inscription at Ateni Sioni, 982-986"),
    "Cyrl": ("", "Slavica Occitania 12 (2001), after the Kirilo-Metodievska enciklopedija",
             "earliest epigraphy Krepcha 921, a Preslav sherd 931, a dated Dobrudja inscription 943"),
    "Runr": ("", "Unicode TN40; Looijenga 2003; Duwel 2008",
             "thought to come from North Italic; Vimose comb c.150-160; written in either direction"),
    "Latn": ("", "Rocca & Sarullo 2007; CNR 2011 on the Praeneste fibula; Gippert 2020",
             "Lapis Niger and Lapis Satricanus 6th c. BCE; the Praeneste fibula (7th c.) is still argued over"),
    "Linb": ("", "Olivier 2012, in Cline (ed.), Oxford Handbook of the Bronze Age Aegean",
             "Knossos tablets 14th c. BCE on the compromise chronology; 1450 is the high date"),
    "Cpmn": ("", "Olivier 2012; Steele 2014, Kadmos 53",
             "Enkomi tablet of Late Cypriot I, c.1525-1475 BCE; derived from Linear A by sign form"),
    "Cprt": ("", "Olivier 2012",
             "the Palaepaphos obelos (11th c. BCE) may be the last Cypro-Minoan text rather than the first Cypriot one"),
    "Hira": ("Man'yogana", "Unicode ch.18; Seeley 1991, A History of Writing in Japan",
             "a 9th-c. development from cursive man'yogana; no securely dated first object"),
    "Kana": ("Man'yogana", "Whitman 2022; Seeley 1991",
             "Todaiji fujumonko, 824-834, the earliest katakana used for an extended Japanese text"),
    "Bopo": ("", "Ministry of Education, Taiwan; DeFrancis 1950",
             "adopted 1913 from simplified Han forms (Zhang Binglin), promulgated 1918"),
    "Nshu": ("", "UNESCO 2018; Endo, Unicode N4626; UNESCO Courier 2018; Unicode ch.18",
             "no securely dated object before the 19th c.; claims of a Song origin have no object behind them; very few fluent writers left by the late 20th c.; revived by local and national authorities"),
    "Nkgb": ("", "Friedrich 2023; Unicode N3442",
             "some characters from Dongba, some from Yi, Tibetan and Chinese; a dated stele of 1619"),
    "Sidd": ("Gupta", "Salomon 1998, Indian Epigraphy 2.2.5.4",
             "evolved out of the Gupta script in the late 6th c.; Bodh-Gaya inscription of Mahanaman, 588-589"),
    "Deva": ("Nagari", "Salomon 1998, after Sukthankar",
             "no authentic specimen before the Silahara inscriptions at Kanheri, 851 and 877-878"),
    "Shrd": ("Kutila", "Pandey, L2/08-200; Salomon 1998",
             "descended from Gupta through Kutila; Proto-Sarada from the 7th c., Sharada of Kashmir from the 8th"),
    "Takr": ("Devasesha", "Pandey, L2/09-424; Unicode ch.15",
             "from Sharada through Devasesha (14th c.), differentiated in the 16th c.; official in princely states until the mid-20th c.; revival efforts only"),
    "Dogr": ("", "Pandey, L2/15-234; Unicode ch.15; Indian Express 2026",
             "Dogra written from the 17th c.; standardised in the 1860s; no longer used actively, Dogri now in Devanagari; signboard revival begun in Jammu, 2026"),
    "Guru": ("Landa", "Pandey, L2/10-011; Mann 1996, The Goindval Pothis",
             "Landa the model; the Goindval Pothis of the 1570s are the earliest extant source; 1539 was a guruship date"),
    "Khoj": ("Landa", "Pandey, Unicode N3978; Unicode ch.15",
             "a refined form of the Lohanaki variety of Landa, in use by the 16th c.; primers still published in Pakistan; used in Nizari Ismaili ceremonies"),
    "Mult": ("Landa", "Unicode ch.15",
             "related to Gurmukhi; used in the 19th and 20th c.; earlier date unsourced"),
    "Sind": ("Landa", "Pandey, L2/11-022; Unicode ch.15",
             "a Landa-based script related to Sharada; standard form published 1868; now obsolete; Bible Society printing continued past 1900"),
    "Modi": ("Nagari", "Pandey, Unicode N4034; Salomon 1998 n.116; Unicode ch.15; Hindustan Times 2025",
             "a Nagari-family script for continuous writing; earliest extant document early 17th c.; formally discontinued in the 1950s; taught again for reading archives"),
    "Nand": ("Nagari", "Pandey, L2/17-162",
             "a sister of Devanagari within the Nagari family, 11th c."),
    "Gujr": ("Nagari", "Unicode ch.12; Salomon 1998 3.4.3",
             "closely related to Devanagari; texts wholly in Gujarati from the late 15th c.; 1592 unsourced"),
    "Beng": ("Gaudi", "Salomon 1998 2.2.5.5; Unicode ch.15",
             "Gaudi (proto-Bengali) current from the 10th to the 14th c.; a distinct Bengali from the 14th-15th c."),
    "Orya": ("Gaudi", "Salomon 1998 3.4.2",
             "early Oriya texts in Gaudi (Urajam 1051); a distinct Oriya script from the 14th c., of composite origin"),
    "Newa": ("Kutila", "Pandey, Unicode N4184; Unicode ch.13",
             "a distinct Newar script from the 10th c.; Lankavatara Sutra manuscript dated 908"),
    "Ranj": ("", "Pandey, Unicode N4184, after Malla 1981",
             "developed from the Newar (pacumola) model; first in Nepal in 1099"),
    "Bhks": ("", "Unicode ch.14; Dimitrov",
             "used 10th-13th c.; eleven inscriptions and four manuscripts known"),
    "Marc": ("", "West, Unicode N4491; Unicode ch.14",
             "quite different from Tibetan and Lantsa; no early texts known, likely a much more recent innovation; widely used in modern Bon literature and inscriptions"),
    "Phag": ("", "Unicode ch.14",
             "devised for Khubilai and promulgated in 1269; similar to Tibetan"),
    "Lepc": ("", "Unicode ch.13; Everson, Unicode N2947",
             "based directly on Tibetan; invented around 1720"),
    "Limb": ("", "Unicode ch.13; Hall, Unicode N4347",
             "oldest known writings collected in Darjeeling in the 1850s; 18th-c. Sirijanga origin is tradition"),
    "Zanb": ("", "Unicode ch.14; Pandey, L2/14-024",
             "based upon Tibetan; date unknown, believed to precede Soyombo (1686)"),
    "Soyo": ("Lantsa", "Unicode ch.14; Unicode N1855",
             "created in 1686 by Zanabazar on the model of Lantsa, with Tibetan order and shapes"),
    "Gran": ("Pallava", "Francis 2024; Pandey, L2/18-083",
             "Pallava is the ancestor of Grantha; Grantha itself designed around 600 CE"),
    "Taml": ("Pallava", "Francis 2024",
             "a new alphabet for Tamil around the start of the 7th c., a sister of Grantha, not from Vatteluttu"),
    "Mlym": ("Chola Grantha", "ICANN Malayalam LGR 2019",
             "the 830 Vazhappalli plates are in Vatteluttu; Malayalam script texts from about the 12th c."),
    "Tutg": ("Chola Grantha", "L2/17-378; L2/22-031",
             "evolved from the later Chola Grantha to write Sanskrit; in continuous use for ritual purposes such as birth charts and charms"),
    "Knda": ("Kadamba", "Mahadevan, Frontline; Gai",
             "Halmidi inscription, mid-5th c., in Kadamba script; a sister of Telugu"),
    "Telu": ("Kadamba", "Mahadevan, Frontline",
             "Kalamalla inscription of the Renati Cholas, end of the 6th c."),
    "Sinh": ("", "Unicode L2/10-312",
             "Brahmi inscriptions of the 3rd-2nd c. BCE; later influenced by Grantha"),
    "Khmr": ("Pallava", "Zakharov 2019; Unicode ch.16",
             "earliest dated Old Khmer K.557/600, 611; close to the Pallava script of the Coromandel coast"),
    "Cham": ("Pallava", "Unicode ch.16; Filliozat 1969",
             "Old Cham at Dong Yen Chau, c.4th c., in Pallava script"),
    "Kawi": ("Pallava", "de Casparis 1975, Indonesian Palaeography; Pandey, L2/12-125",
             "Plumpungan c.750; de Casparis doubts direct descent from Pallava"),
    "Mymr": ("Old Mon or Pyu", "Unicode ch.16; Aung-Thwin 2005",
             "first inscription 11th c. (Myazedi c.1113); Mon source in Unicode, Pyu argued by Aung-Thwin"),
    "Thai": ("Sukhothai", "Penth 1989, JSS 77",
             "Ram Khamhaeng inscription dated 1292, authenticity disputed; Wat Bang Sanuk 1219 also cited"),
    "Laoo": ("Fakkham", "Lorrillard, 'Scripts and history: the case of Laos'",
             "Fakkham the prototype of Lao script; no direct Khmer transmission; first dated stele 1494 or 1497"),
    "Lana": ("Old Mon", "Apiradee & Grabowsky 2024",
             "developed from the Mon script of Hariphunchai; earliest evidence 1376"),
    "Tale": ("", "Daniels 2012, Journal of Southeast Asian Studies",
             "the Tay borrowed heavily from Burmese before the 15th c.; a Ming scroll of 1407"),
    "Ahom": ("", "Terwiel 1983, JSS 71; Unicode ch.15",
             "brought at the conquest c. early 13th c., apparently on a Mon example; no dated early object; religious use into the 19th c.; modern use from a 1920 dictionary"),
    "Bali": ("", "Unicode ch.17",
             "from Kawi; Belanjong pillar 914, Old Balinese beside Sanskrit"),
    "Sund": ("Pallava", "Unicode ch.17; Pandey, L2/12-125",
             "Unicode derives Old Sundanese from Pallawa, Pandey from Kawi; used 14th-18th c."),
    "Rjng": ("", "Everson, Unicode N3096",
             "first attested about the mid-18th c."),
    "Batk": ("", "Kozok 2000, BKI",
             "no proto-forms found; a manuscript in the British Library by 1764; introduction date unknown"),
    "Bugi": ("", "Everson, Unicode N2588",
             "of the Brahmic type and perhaps related to Javanese"),
    "Java": ("", "Pandey, L2/12-125",
             "Kawi is the ancestor of Javanese and Balinese"),
    "Armi": ("", "Encyclopaedia Iranica 'Aramaic i'; Unicode ch.10",
             "first attested in inscriptions of the 9th-8th c. BCE; distinct from Phoenician by the mid-8th c."),
    "Hebr": ("", "Unicode ch.10; Barag",
             "the square Hebrew script grew out of Imperial Aramaic; Mount Gerizim inscriptions 3rd-2nd c. BCE"),
    "Goth": ("", "Schaffner 2024, Oxford Research Encyclopedia of Linguistics",
             "Wulfila's alphabet on the Greek model, with Latin and runic letters, c.350; manuscripts 5th-6th c."),
    "Ital": ("Euboean Greek", "Everson, L2/00-140; Unicode TN40",
             "from the Euboean Greek of Ischia and Cumae; Marsiliana abecedary 7th c. BCE; mostly right to left"),
    "Lyci": ("", "Adiego 2018; Unicode ch.8",
             "both the letter shapes and the chronology point to a Greek origin; c.500 BCE"),
    "Lydi": ("", "Adiego 2018; Unicode ch.8",
             "Greek or Phrygian model, an open question; late 8th or early 7th c. BCE; mostly right to left"),
    "Moon": ("", "Everson, Unicode N4128 (L2/11-280); Perkins School for the Blind",
             "embossed symbols simplified from Latin letters; developed by William Moon in 1845"),
    "Osge": ("", "Everson, Lookout & Pratt, Unicode N4587",
             "letters in origin modifications or fusions of Latin letters, designed by 2006, revised 2012-2014"),
    "Lisu": ("", "Unicode N3317; Cook, L2/07-294",
             "Sara Ba Thaw and James Fraser modified the shapes of Latin letters, 1908-1914, published 1915"),
    "Ougr": ("", "L2/20-003 (Old Uyghur); Unicode ch.14",
             "believed to derive from Sogdian cursive in the 8th or 9th c."),
    "Sylo": ("", "L2/02-388 (Syloti Nagri); Pandey, Unicode N3389",
             "a form of Kaithi; earliest manuscript dated 1549 or 1774, exact origin unknown"),
    "Cakm": ("", "Everson & Hosken, Unicode N3645 (L2/09-187)",
             "Brahmic, an early offshoot of the Mon-Burmese script; no dated early manuscript found"),
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
