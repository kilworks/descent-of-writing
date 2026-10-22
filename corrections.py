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
]
