# -*- coding: utf-8 -*-
"""Corrections to the language-to-script links the open sources give.

Wikidata, CLDR and SIL langtags are joined as they come, and they are right
almost everywhere they overlap. The few links below are wrong on the record,
mostly for ancient scripts where the sources are thin. Each correction names
the language by ISO 639-3, the script, what is done, and the authority, and
verify.py fails if one stops being applied.

  drop  remove the link: the language was not written in that script
  add   add a link no source gives, where the authority is direct
  main  keep every link, but hang the language under this script
"""

CORRECTIONS = [
    # code, script, action, source, note
    ("xly", "Elym", "drop", "L2/17-226 (Elymaic); Tribulato 2012, Language and Linguistic Contact in Ancient Sicily",
     "Elymian is a language of ancient Sicily, written in the Greek alphabet; Elymaic is the Aramaic script "
     "of Elymais in Iran. The names collide, the scripts do not"),
    ("oar", "Elym", "drop", "L2/17-226 (Elymaic)",
     "Sam'alian Old Aramaic of the 9th-8th c. BCE predates Elymaic writing by six centuries"),
    ("tmr", "Elym", "drop", "Unicode ch.9",
     "Jewish Babylonian Aramaic is written in the square Hebrew script"),
    ("aii", "Elym", "drop", "Unicode ch.9",
     "Assyrian Neo-Aramaic is written in the Syriac script"),
    ("oar", "Syrc", "drop", "Unicode ch.10",
     "Old Aramaic of the 9th-8th c. BCE predates Syriac writing by eight centuries"),
    ("oar", "Phnx", "add", "Unicode ch.10",
     "Old Aramaic inscriptions are written in letters Unicode encodes with Phoenician"),
    ("tmr", "Syrc", "drop", "Unicode ch.9",
     "Jewish Babylonian Aramaic is written in the square Hebrew script, not Syriac"),
    ("tmr", "Hebr", "add", "Unicode ch.9",
     "the Babylonian Talmud and the incantation bowls in Jewish Aramaic use the square Hebrew script"),
    ("oty", "Gran", "drop", "Mahadevan 2003, Early Tamil Epigraphy",
     "Old Tamil inscriptions are in Tamil-Brahmi and Vatteluttu; Grantha writes Sanskrit"),
    ("oty", "Brah", "add", "Mahadevan 2003, Early Tamil Epigraphy; Unicode ch.14",
     "Tamil-Brahmi, whose extra letters Unicode encodes in the Brahmi block"),
    # found by crosscheck_wiktionary.py, where Wiktionary and langtags part
    ("yej", "Hebr", "add", "Krivoruchko 2016, 'Judeo-Greek', in Kahn & Rubin (eds.), Handbook of Jewish Languages",
     "Yevanic, the Judeo-Greek of the Romaniote Jews, was written in the Hebrew alphabet"),
    ("yej", "Hebr", "main", "Krivoruchko 2016, in Kahn & Rubin (eds.), Handbook of Jewish Languages",
     "the Hebrew alphabet is its main script; Greek-letter texts are the exception"),
    ("bjf", "Syrc", "drop", "Khan 2016, 'Jewish Neo-Aramaic', in Kahn & Rubin (eds.), Handbook of Jewish Languages",
     "the Jewish Neo-Aramaic dialects are written in the Hebrew script, not Syriac"),
    ("bjf", "Hebr", "add", "Khan 2016, in Kahn & Rubin (eds.), Handbook of Jewish Languages",
     "Barzani Jewish Neo-Aramaic texts are in Hebrew script"),
    ("cld", "Hebr", "drop", "Unicode ch.9",
     "Chaldean Neo-Aramaic is the language of Chaldean Catholics, who write East Syriac, not Hebrew"),
    ("cld", "Syrc", "add", "Unicode ch.9",
     "the East Syriac script of the Church of the East and the Chaldean Church"),
    ("xrr", "Latn", "drop", "Schumacher 2004, Die raetischen Inschriften",
     "the Raetic inscriptions are in North Italic alphabets, not Latin"),
    ("xrr", "Ital", "add", "Schumacher 2004, Die raetischen Inschriften",
     "the Sanzeno and Magre alphabets, varieties of North Etruscan"),
    ("xhu", "Hluw", "drop", "Unicode ch.11; Wilhelm 2004, in The Cambridge Encyclopedia of the World's Ancient Languages",
     "Hurrian is written in cuneiform and, at Ugarit, in the Ugaritic alphabet; Anatolian hieroglyphs write Luwian"),
    ("xlu", "Hluw", "drop", "Unicode ch.11; Melchert 2003, The Luwians",
     "Cuneiform Luwian is the Luwian written in cuneiform; Hieroglyphic Luwian (hlu) is the hieroglyphic one"),
    ("elx", "Pelm", "drop", "Dahl 2005, CDLJ 2005:3",
     "the language of Proto-Elamite tablets is not established as Elamite; Elamite is written in cuneiform "
     "and Linear Elamite"),
    ("xly", "Grek", "add", "Tribulato 2012, Language and Linguistic Contact in Ancient Sicily",
     "the Elymian inscriptions of Segesta and Entella are written in a local Greek alphabet"),
    ("xlu", "Xsux", "add", "Melchert 2003, The Luwians",
     "Cuneiform Luwian survives in Hittite cuneiform tablets from Hattusa"),
    ("xhu", "Xsux", "main", "Wilhelm 2004, in The Cambridge Encyclopedia of the World's Ancient Languages",
     "most Hurrian texts, the Mitanni letter among them, are in cuneiform; the Ugarit texts are a small part"),
    ("txb", "Brah", "main", "Malzahn 2007, Instrumenta Tocharica; Unicode ch.14",
     "Tocharian B is written mainly in Tocharian Brahmi, a Brahmi variety Unicode has not encoded; "
     "only a few texts use the Manichaean script"),
    ("hea", "Latn", "add", "Enwall 2012, International Journal of the Sociology of Language 215",
     "a Latin-based script for Hmu, on the Yanghao dialect, was set in 1956 and reintroduced in schools in 1981; "
     "langtags gives only a Bopomofo tagset"),
    ("hea", "Latn", "main", "Enwall 2012, International Journal of the Sociology of Language 215",
     "the 1956 Latin script is the one in schools and in the 2009 New Testament"),
]
