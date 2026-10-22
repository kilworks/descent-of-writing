# A guide to the scripts of the world

Generated from `out/dataset.json` by [`guide.py`](guide.py). Do not edit by hand: change [`genealogy.py`](genealogy.py) or the sources, rebuild, and rerun `guide.py`. `verify.py` fails if this file is stale.

It covers all 218 scripts of the ISO 15924 registry that are not special or private-use codes, the same set the [plate](out/descent_of_writing.svg) draws, and the 4,569 languages of Glottolog that a source records a script for (Wikidata, CLDR or SIL langtags). Of the other 4,018, 2,857 are listed as unwritten by SIL langtags and 1,161 have no record either way. Neither is proof that a language is unwritten.

## Contents

- [What kinds of script there are](#what-kinds-of-script-there-are)
- [How the links are drawn](#how-the-links-are-drawn)
- [The roots](#the-roots)
- [The great lineages](#the-great-lineages)
- [Script and language are two different trees](#script-and-language-are-two-different-trees)
- [Open questions](#open-questions)
- [The family trees](#the-family-trees)
- [Every script, by code](#every-script-by-code)

## What kinds of script there are

| Type | Scripts | What it means |
|---|---:|---|
| logographic | 13 | signs stand for words or morphemes, usually with phonetic components alongside. Every independent invention of writing began here. |
| syllabary | 18 | one sign per syllable, with no shared shape between syllables that share a consonant (Cherokee, kana, Linear B). |
| abjad | 23 | letters for consonants only, vowels left to the reader or marked optionally (Phoenician, Hebrew, Arabic). The term is Daniels' (1990). |
| abugida | 69 | a consonant letter carries an inherent vowel, and other vowels are marks attached to it (Brahmi and its descendants, Ge'ez). Also Daniels'. |
| alphabet | 68 | consonants and vowels written as letters of equal standing (Greek, Latin, Cyrillic, and many twentieth-century inventions). |
| featural | 3 | the shapes encode articulatory features, so related sounds look related (Hangul, Visible Speech, SignWriting). The term is Sampson's (1985). |
| semasiographic | 2 | signs carry meaning without fixing the words that express it (Naxi Dongba, Blissymbols). |
| undeciphered | 5 | the type cannot be stated because the script is not read. |
| variant | 11 | a registry code for a style or tradition of another script. |
| composite | 5 | a registry code bundling several scripts used together. |
| symbols | 1 | a registry code for a symbol set that is not a writing system. |

A type describes how a script is used, not where it came from. Descent crosses types freely: the Phoenician abjad gave rise to the Greek alphabet and, through Aramaic, to the Brahmi abugida.

## How the links are drawn

| Link | Count | Meaning |
|---|---:|---|
| attested | 99 | direct graphical descent: the letter shapes were inherited. |
| contested | 37 | a descent claimed in the literature and disputed there. The entry names both sides. |
| stimulus | 38 | a named script lent the idea of writing, or a structure such as letter order, an inherent vowel or a syllabic layout; the letters were drawn fresh. |
| invented | 18 | made on purpose with no ancestor at all. The script is placed under the one its makers already wrote; that is a placement, not a descent. |
| variant | 11 | the same script in another style or orthographic tradition. |
| composite | 6 | a registry code that bundles several scripts, not a script. |

Every link names the publication it rests on, attested descent included, in the entry below and in the `SOURCES` table of `genealogy.py`.

## The roots

A root has no known parent among the registry's codes. That is a weaker claim than an independent invention of writing: only proto-cuneiform, Chinese and Mayan writing are held to be that beyond dispute, and Egyptian probably is.

| Root | First attested | Scripts beneath it | Why it is a root |
|---|---|---:|---|
| [`Egyp`](#egyp) Egyptian hieroglyphs | 3250 BCE | 184 | independent Egyptian invention is the majority view; stimulus from Sumer is argued and not excluded |
| [`Hani`](#hani) Han | 1250 BCE | 18 | independent invention, not argued |
| [`Lina`](#lina) Linear A | 1800 BCE | 3 | Linear A grew out of the Cretan hieroglyphic tradition, which has no ISO code |
| [`Pcun`](#pcun) Proto-Cuneiform | 3300 BCE | 3 | independent invention, not argued |
| [`Nkdb`](#nkdb) Naxi Dongba | 1200 CE | 1 | earliest dated manuscripts 13th c.; independence hedged, created amid Chinese and Tibetan literacy |
| [`Hluw`](#hluw) Anatolian Hieroglyphs | 1400 BCE | 0 | Egyptian inspiration unlikely; probably an Anatolian creation from indigenous signs |
| [`Inds`](#inds) Indus | 2600 BCE | 0 | whether the signs encode language at all is disputed |
| [`Maya`](#maya) Mayan hieroglyphs | 300 BCE | 0 | independent invention, not argued |
| [`Roro`](#roro) Rongorongo | 1864 CE | 0 | first recorded 1864 (Eyraud); stimulus from the 1770 Spanish annexation treaty is argued and unresolved |

## The great lineages

### One invention behind most of the world: the alphabet

Of the 218 scripts in the registry, 184 descend from Egyptian hieroglyphs, and 179 of those through a single step: Proto-Sinaitic. Around 1900 BCE, Semitic speakers working in Egypt and Sinai took a few dozen hieroglyphs and used each for the first consonant of its name in their own language, a house for /b/, water for /m/ (Darnell et al. 2005 on Wadi el-Hol; Hamilton 2006). The result wrote consonants only, and it was the first alphabet.

It split early. A southern branch gave Ancient South Arabian and, from it, Ge'ez; Ancient North Arabian shares that branch's ancestor rather than descending from it (Al-Jallad 2015). A northern branch was standardised as Phoenician by about 1000 BCE. Ugarit, around 1250 BCE, kept the idea and the letter order but wrote them in wedges on clay: an alphabet in cuneiform dress.

### Aramaic, the empire's hand

Aramaic became the administrative script of the Assyrian and then the Persian empires, and so it travelled. 114 scripts descend from it. Square Hebrew is one; Nabataean, and from it Arabic (first securely dated in Arabic script in 512 CE), another; Syriac a third. Eastward, the Middle Iranian scripts (Parthian, the Pahlavis, Avestan) and Sogdian carried it along the Silk Road, where Sogdian became Old Uyghur and Old Uyghur, turned on its side, became the vertical Mongolian script of 1224 CE. In India, Kharosthi is an Aramaic adaptation, and Brahmi most likely is too, though that is the majority view rather than a settled one (Salomon 1998).

### Greek, and the vowel

Around 750 BCE Greek writers took Phoenician letters for consonants their language lacked and turned them into vowels: aleph became alpha, he became epsilon. Writing every vowel as a full letter is the step that makes an alphabet in the narrow sense. 55 scripts descend from Greek. A western Greek variety passed to the Etruscans and from them to Latin and the runes; Coptic kept the Greek letters and added six or seven from Demotic for Egyptian sounds; Gothic, Glagolitic and Cyrillic were made for Christian texts. Armenian and Georgian follow Greek order closely, but where their letter shapes came from is still argued.

### Latin's reach

Latin writes 3,652 of the 4,569 languages that have a script on record, more than every other script together. That is the history of the last five centuries, missionary and colonial orthographies above all, not a property of the letters. It also explains a pattern on the plate: 13 of the scripts hung under Latin are modern inventions with no ancestor at all (the dash-dot links). They sit there because their makers already wrote in Latin, and the plate says that is a placement, not a descent.

### Brahmi, and the abugida

Brahmi appears fully formed in the edicts of Ashoka around 250 BCE. Its idea is new: a consonant letter carries an inherent vowel, other vowels are marks attached to it, and a stroke cancels the vowel. 76 scripts descend from it, against 55 from Greek: most of the registry's diversity is Brahmic. Through the Gupta script it gave Siddham and the Nagari family (Devanagari, Bengali, Odia, Newar) in the north, Sharada and Landa in the north-west, Tibetan in the Himalaya, and, through the Kadamba script, Kannada and Telugu. Through the Pallava script of south India it crossed the sea: Khmer and from it Thai and Lao, the Mon-Burmese scripts, Cham, and Kawi with the scripts of Java, Bali, Sumatra, Sulawesi and the Philippines.

### Chinese, and the scripts it prompted

Chinese writing is attested from the oracle bones of about 1250 BCE and is the only one of the old inventions still in daily use. Its characters are mostly compounds of a meaning part and a sound part. In Japan, Chinese characters used for their sound became the two kana syllabaries; in China, simplified components became Bopomofo, and in Hunan, women's writing became Nushu. Other states built writing on the Chinese model without borrowing its characters: Khitan, Tangut, Jurchen. Hangul, of 1443, is a case apart: by its own account of 1446 its consonant shapes draw the speech organs, a Phags-pa model is argued for five or six letters at most, and the plate hangs it from Phags-pa as contested.

### The other first inventions

Proto-cuneiform appears at Uruk around 3300 BCE, as book-keeping, and became cuneiform, the script of Sumerian, Akkadian, Hittite, Elamite and a dozen more languages over three thousand years; Proto-Elamite was devised beside it under its stimulus. Egyptian hieroglyphs appear around 3250 BCE; hieratic and Demotic are their cursive forms, and the two Meroitic scripts of Nubia were made from the hieroglyphs and from Demotic. Mayan writing, from about 300 BCE, is the one pre-Columbian script of the Americas that can be read today, deciphered over the second half of the twentieth century after Knorozov showed in 1952 that it is partly phonetic. Linear A in Crete, the Indus signs and rongorongo are not read, and the plate says so.

### Writing made on purpose

42 of the scripts were devised after 1800, most of them by a person whose name is recorded. Sequoyah's Cherokee syllabary (finished in 1821 CE) took Latin letter shapes without their values, and James Evans's Cree syllabics turned British shorthand into a syllabary. In West Africa, the Vai syllabary of 1833 CE prompted Mende, Kpelle, Loma and Bassa Vah. In India, Burma and Laos, scripts such as Ol Chiki, Warang Citi, Sora Sompeng, Pahawh Hmong and Mro were made for languages with no script of their own, often as the founding act of a religious or cultural movement, and their encoding proposals describe them as unrelated to any earlier script. They are the clearest evidence that writing, once known to exist, can be invented again from the idea alone.

## Script and language are two different trees

The plate draws the descent of scripts as a tree and sorts languages by family inside each script's field, but the two trees do not line up. A script travels by conquest, religion, trade and schooling; a language descends by speech. Counting families and isolates as Glottolog defines them, leaving out its filing categories (Artificial Language, Bookkeeping, Mixed Language, Pidgin, Sign Language, Speech Register, Unattested, Unclassifiable):

- Latin writes languages of 273 families and isolates, Arabic of 23, Braille of 18.
- Indo-European is written in 85 scripts, Sino-Tibetan in 42, Austronesian in 28.
- Yet 143 of the 193 scripts recorded for any language serve a single family or isolate: most scripts were made for one language or a few close ones, and a handful of imperial and religious scripts carry everything else.

The second plate, [`out/families_and_scripts.svg`](out/families_and_scripts.svg), draws this: families on one side, scripts on the other, and a band for every family and script that meet, as thick as the languages they share.

## Open questions

Six questions on which the plate takes a side or declines to. Each gives the positions, what each rests on, and where the field stands; works known here only through another's citation are marked as cited.

### Where Brahmi came from

**Semitic origin.** Buhler (*On the Origin of the Indian Brahma Alphabet*, 1898) derived Brahmi from a Semitic, in practice Aramaic, model; Salomon (*Indian Epigraphy*, 1998) keeps this as the leading view. Falk (*Schrift im alten Indien*, 1993; and in 2018) sees a script designed under Ashoka from the two then current in the north-west, Greek and Kharosthi.

**Earlier or indigenous.** Sherds from Anuradhapura in Sri Lanka carry Brahmi letters in layers dated to the early 4th century BCE (Coningham, Allchin, Batt and Lucy, *Cambridge Archaeological Journal* 6, 1996), and Tamil Nadu finds have been dated earlier still; these would put Brahmi before Ashoka. A descent from the Indus signs is sometimes proposed; it cannot be shown while the Indus signs themselves are unread.

**Where it stands.** An Aramaic model is the majority view and the plate draws it, dashed. How the letters were derived is not explained, and Pillai (2023, *Indialogs*) calls the debate far from settled. About seventy scripts hang from this one edge.

### Whether Egypt invented writing alone

**Independent.** The labels of tomb U-j at Abydos (Dreyer, *Umm el-Qaab I*, 1998), around 3250 BCE, are as early as the first Mesopotamian tablets, and Egyptian writing differs from cuneiform in structure, signs and use (Baines, in Houston ed., *The First Writing*, 2004; Regulski, *Oxford Handbook*, 2014).

**Stimulus.** Petrie, Pope, Ray (1986) and Brewer (all cited in Regulski 2014) argued that the idea of writing reached Egypt from Mesopotamia, through contacts visible in cylinder seals and art.

**Where it stands.** The majority view is independent invention, with stimulus diffusion of the bare idea still possible; Regulski writes that it remains a possibility. The plate keeps Egyptian hieroglyphs as a root and records the argument against it.

### What Hangul's letters were drawn from

**The speech organs.** The *Hunminjeongeum Haerye* of 1446, written with the script's promulgation, says the five basic consonants picture the organs that make them, the root of the tongue closing the throat for ㄱ, the shape of the mouth for ㅁ, and that further letters add strokes for aspiration or tension. Sampson (*Writing Systems*, 1985) made Hangul his example of a featural script.

**Phags-pa.** Ledyard (*The Korean Language Reform of 1446*, 1966, revised 1998) argued that a handful of base consonants follow the Phags-pa script of the Mongol court, which Korean scholars knew; an earlier court record also says the letters imitate an old seal script.

**Where it stands.** The articulatory design is not disputed. Ledyard's link concerns five or six shapes, and most scholars treat it as a model at most; the plate draws it dashed rather than leave Hangul as a root it is not.

### Whether the Indus signs are writing

**Not language.** Farmer, Sproat and Witzel (*Electronic Journal of Vedic Studies* 11, 2004) argued that the inscriptions are too short and repetitive to encode language and are better read as emblems. Sproat (*Computational Linguistics* 36, 2010; *Language*, 2014) showed that the entropy measures offered against this cannot separate linguistic from non-linguistic symbol systems.

**Language.** Rao and colleagues (*Science* 324, 2009) found the sign sequences' conditional entropy close to that of natural languages, with positional regularities like a syntax; Parpola and Mahadevan have long read the signs as a logo-syllabic script.

**Where it stands.** Open. Rao and colleagues themselves write that without a decipherment neither thesis can be proved. The plate includes the Indus signs because the registry does, as a root marked undeciphered.

### How old rongorongo is

**After contact.** No visitor to Rapa Nui reported writing before Eyraud in 1864. Emory (1968) and Fischer (*Rongorongo*, 1997) argued that the islanders invented it after seeing the Spanish annexation document of 1770 (both cited in Wieczorek et al. 2021).

**Before contact.** Ferrara and colleagues (*Scientific Reports* 14, 2024) radiocarbon-dated the wood of four tablets; one, tablet D, was cut around 1493-1509, which would put the script before European arrival if the text is as old as the wood.

**Where it stands.** Open. A wood date only bounds the inscription from below, and Wieczorek and colleagues (*Journal of Island and Coastal Archaeology*, 2021) found no consensus on when the script was used. The plate keeps rongorongo as a root, dated from its first record.

### Where the Glagolitic letters came from

**Greek cursive.** Taylor and Jagic derived most letters from Greek minuscule, and Cubberley (in Daniels and Bright, *The World's Writing Systems*, 1996) finds most can be derived from Greek cursive in a formally satisfying way.

**Other sources, or none.** Vondrak, Nahtigal and Fortunatov proposed Hebrew, Samaritan or Coptic models for the letters Greek lacks; Chernokhvostov derived the whole set from the cross, the circle and the triangle; Mathiesen (*Slavistica Vilnensis* 65, 2020) traces its look to esoteric alphabets.

**Where it stands.** Cubberley's own verdict is that the search for the formal origins of Glagolitic remains unsolved. The plate draws Glagolitic from Greek, dashed.

## The family trees

Indented by generation. Each line gives the code, the name, the type, the first attestation, and the link to the parent when it is not attested descent.

### Egyptian hieroglyphs

- [`Egyp`](#egyp) Egyptian hieroglyphs, logographic, 3250 BCE
  - [`Egyh`](#egyh) Egyptian hieratic, logographic, 2700 BCE
    - [`Egyd`](#egyd) Egyptian demotic, logographic, 650 BCE
      - [`Merc`](#merc) Meroitic Cursive, alphabet, 220 BCE
  - [`Psin`](#psin) Proto-Sinaitic, abjad, 1900 BCE
    - [`Ugar`](#ugar) Ugaritic, alphabet, 1250 BCE *(stimulus)*
    - [`Phnx`](#phnx) Phoenician, abjad, 1000 BCE
      - [`Armi`](#armi) Imperial Aramaic, abjad, 900 BCE
        - [`Hebr`](#hebr) Hebrew, abjad, 300 BCE
          - [`Hmnp`](#hmnp) Nyiakeng Puachue Hmong, alphabet, 1980 CE *(stimulus)*
        - [`Brah`](#brah) Brahmi, abugida, 250 BCE *(contested)*
          - [`Sinh`](#sinh) Sinhala, abugida, 200 BCE
          - [`Cham`](#cham) Cham, abugida, 400 CE
          - [`Knda`](#knda) Kannada, abugida, 450 CE
          - [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā, abugida, 588 CE
            - [`Deva`](#deva) Devanagari, abugida, 851 CE
              - [`Nand`](#nand) Nandinagari, abugida, 1100 CE
              - [`Gujr`](#gujr) Gujarati, abugida, 1592 CE
              - [`Mahj`](#mahj) Mahajani, alphabet, 1600 CE *(contested)*
              - [`Modi`](#modi) Modi, Moḍī, abugida, 1600 CE
                - [`Gong`](#gong) Gunjala Gondi, abugida, 1750 CE *(contested)*
              - [`Tols`](#tols) Tolong Siki, alphabet, 1988 CE *(invented)*
            - [`Newa`](#newa) Newa, Newar, Newari, Nepāla lipi, abugida, 908 CE
              - [`Ranj`](#ranj) Ranjana, abugida, 1099 CE
                - [`Soyo`](#soyo) Soyombo, abugida, 1686 CE
            - [`Tirh`](#tirh) Tirhuta, abugida, 1200 CE
            - [`Orya`](#orya) Oriya, abugida, 1300 CE
              - [`Olck`](#olck) Ol Chiki, alphabet, 1925 CE *(invented)*
                - [`Nagm`](#nagm) Nag Mundari, alphabet, 1950 CE *(stimulus)*
            - [`Beng`](#beng) Bengali, abugida, 1350 CE
              - [`Toto`](#toto) Toto, alphabet, 2015 CE *(invented)*
            - [`Kthi`](#kthi) Kaithi, abugida, 1550 CE
              - [`Sylo`](#sylo) Syloti Nagri, abugida, 1500 CE
          - [`Gran`](#gran) Grantha, abugida, 600 CE
            - [`Diak`](#diak) Dives Akuru, abugida, 900 CE
            - [`Tutg`](#tutg) Tulu-Tigalari, abugida, 1000 CE
            - [`Mlym`](#mlym) Malayalam, abugida, 1100 CE
          - [`Taml`](#taml) Tamil, abugida, 600 CE
          - [`Telu`](#telu) Telugu, abugida, 600 CE
          - [`Khmr`](#khmr) Khmer, abugida, 611 CE
            - [`Thai`](#thai) Thai, abugida, 1292 CE
              - [`Laoo`](#laoo) Lao, abugida, 1494 CE
                - [`Hmng`](#hmng) Pahawh Hmong, alphabet, 1959 CE *(invented)*
              - [`Tavt`](#tavt) Tai Viet, abugida, 1500 CE
              - [`Tayo`](#tayo) Tai Yo, abugida, 1500 CE *(contested)*
          - [`Tibt`](#tibt) Tibetan, abugida, 650 CE
            - [`Marc`](#marc) Marchen, abugida, 1000 CE *(contested)*
            - [`Phag`](#phag) Phags-pa, abugida, 1269 CE
              - [`Hang`](#hang) Hangul, featural, 1443 CE *(contested)*
                - [`Jamo`](#jamo) Jamo, variant, 1443 CE *(variant)*
            - [`Zanb`](#zanb) Zanabazar Square, abugida, 1686 CE
            - [`Lepc`](#lepc) Lepcha, abugida, 1720 CE
              - [`Limb`](#limb) Limbu, abugida, 1850 CE *(contested)*
                - [`Krai`](#krai) Kirat Rai, abugida, 1925 CE *(contested)*
          - [`Kawi`](#kawi) Kawi, abugida, 750 CE
            - [`Bali`](#bali) Balinese, abugida, 914 CE
            - [`Sund`](#sund) Sundanese, abugida, 1400 CE *(contested)*
            - [`Java`](#java) Javanese, abugida, 1500 CE
            - [`Tglg`](#tglg) Tagalog, abugida, 1550 CE *(contested)*
              - [`Buhd`](#buhd) Buhid, abugida, 1600 CE *(contested)*
              - [`Hano`](#hano) Hanunoo, abugida, 1600 CE *(contested)*
              - [`Tagb`](#tagb) Tagbanwa, abugida, 1600 CE *(contested)*
            - [`Bugi`](#bugi) Buginese, abugida, 1600 CE *(contested)*
            - [`Rjng`](#rjng) Rejang, abugida, 1750 CE
              - [`Maka`](#maka) Makasar, abugida, 1600 CE *(contested)*
            - [`Batk`](#batk) Batak, abugida, 1764 CE *(contested)*
          - [`Shrd`](#shrd) Sharada, Śāradā, abugida, 800 CE
            - [`Khoj`](#khoj) Khojki, abugida, 1500 CE
            - [`Takr`](#takr) Takri, Ṭākrī, Ṭāṅkrī, abugida, 1500 CE
              - [`Dogr`](#dogr) Dogra, abugida, 1860 CE
            - [`Sind`](#sind) Khudawadi, Sindhi, abugida, 1550 CE
            - [`Guru`](#guru) Gurmukhi, abugida, 1570 CE
            - [`Mult`](#mult) Multani, abjad, 1750 CE
          - [`Bhks`](#bhks) Bhaiksuki, abugida, 1000 CE
          - [`Mtei`](#mtei) Meitei Mayek, abugida, 1100 CE *(contested)*
          - [`Mymr`](#mymr) Myanmar, abugida, 1113 CE
            - [`Ahom`](#ahom) Ahom, Tai Ahom, abugida, 1300 CE
            - [`Lana`](#lana) Tai Tham, abugida, 1376 CE
              - [`Talu`](#talu) New Tai Lue, abugida, 1955 CE
            - [`Tale`](#tale) Tai Le, abugida, 1407 CE
            - [`Cakm`](#cakm) Chakma, abugida, 1700 CE
            - [`Leke`](#leke) Leke, abugida, 1844 CE *(contested)*
            - [`Kali`](#kali) Kayah Li, alphabet, 1962 CE *(stimulus)*
          - [`Saur`](#saur) Saurashtra, abugida, 1880 CE *(contested)*
          - [`Gonm`](#gonm) Masaram Gondi, abugida, 1918 CE *(stimulus)*
          - [`Sora`](#sora) Sora Sompeng, abugida, 1936 CE *(stimulus)*
          - [`Gukh`](#gukh) Gurung Khema, abugida, 1995 CE *(stimulus)*
        - [`Khar`](#khar) Kharoshthi, abugida, 250 BCE
        - [`Elym`](#elym) Elymaic, abjad, 150 BCE
          - [`Mand`](#mand) Mandaic, Mandaean, alphabet, 350 CE *(contested)*
        - [`Chrs`](#chrs) Chorasmian, abjad, 100 BCE
        - [`Hatr`](#hatr) Hatran, abjad, 98 BCE
        - [`Nbat`](#nbat) Nabataean, abjad, 95 BCE
          - [`Arab`](#arab) Arabic, abjad, 512 CE
            - [`Aran`](#aran) Arabic, variant, 1400 CE *(variant)*
            - [`Thaa`](#thaa) Thaana, alphabet, 1705 CE *(stimulus)*
            - [`Bamu`](#bamu) Bamum, syllabary, 1896 CE *(contested)*
            - [`Osma`](#osma) Osmanya, alphabet, 1920 CE *(stimulus)*
            - [`Nkoo`](#nkoo) N’Ko, alphabet, 1949 CE *(stimulus)*
            - [`Berf`](#berf) Beria Erfe, alphabet, 1950 CE *(invented)*
            - [`Gara`](#gara) Garay, alphabet, 1961 CE *(stimulus)*
            - [`Rohg`](#rohg) Hanifi Rohingya, alphabet, 1980 CE *(stimulus)*
            - [`Adlm`](#adlm) Adlam, alphabet, 1989 CE *(stimulus)*
        - [`Prti`](#prti) Inscriptional Parthian, abjad, 89 BCE
        - [`Palm`](#palm) Palmyrene, abjad, 44 BCE
        - [`Syrc`](#syrc) Syriac, abjad, 6 CE
          - [`Syre`](#syre) Syriac, variant, 100 CE *(variant)*
          - [`Mani`](#mani) Manichaean, abjad, 250 CE *(contested)*
          - [`Syrj`](#syrj) Syriac, variant, 400 CE *(variant)*
          - [`Syrn`](#syrn) Syriac, variant, 400 CE *(variant)*
          - [`Yezi`](#yezi) Yezidi, alphabet, 1200 CE *(contested)*
        - [`Phli`](#phli) Inscriptional Pahlavi, abjad, 224 CE
          - [`Phlp`](#phlp) Psalter Pahlavi, abjad, 600 CE
          - [`Phlv`](#phlv) Book Pahlavi, abjad, 619 CE
            - [`Avst`](#avst) Avestan, alphabet, 500 CE
        - [`Sogo`](#sogo) Old Sogdian, abjad, 313 CE
          - [`Sogd`](#sogd) Sogdian, abjad, 600 CE
            - [`Orkh`](#orkh) Old Turkic, Orkhon Runic, alphabet, 700 CE *(contested)*
              - [`Hung`](#hung) Old Hungarian, alphabet, 900 CE *(contested)*
            - [`Ougr`](#ougr) Old Uyghur, abjad, 800 CE
              - [`Kits`](#kits) Khitan small script, logographic, 925 CE *(stimulus)*
              - [`Mong`](#mong) Mongolian, alphabet, 1224 CE
      - [`Grek`](#grek) Greek, alphabet, 750 BCE
        - [`Cari`](#cari) Carian, alphabet, 700 BCE *(contested)*
        - [`Ital`](#ital) Old Italic, alphabet, 700 BCE
          - [`Latn`](#latn) Latin, alphabet, 600 BCE
            - [`Ogam`](#ogam) Ogham, alphabet, 350 CE *(stimulus)*
            - [`Latg`](#latg) Latin, variant, 700 CE *(variant)*
            - [`Latf`](#latf) Latin, variant, 1150 CE *(variant)*
            - [`Cher`](#cher) Cherokee, syllabary, 1821 CE *(stimulus)*
            - [`Brai`](#brai) Braille, alphabet, 1824 CE *(stimulus)*
            - [`Vaii`](#vaii) Vai, syllabary, 1833 CE *(stimulus)*
              - [`Bass`](#bass) Bassa Vah, alphabet, 1907 CE *(stimulus)*
              - [`Mend`](#mend) Mende Kikakui, syllabary, 1917 CE *(stimulus)*
              - [`Kpel`](#kpel) Kpelle, syllabary, 1930 CE *(stimulus)*
              - [`Loma`](#loma) Loma, syllabary, 1930 CE *(stimulus)*
            - [`Cans`](#cans) Unified Canadian Aboriginal Syllabics, syllabary, 1840 CE *(stimulus)*
              - [`Plrd`](#plrd) Miao, syllabary, 1904 CE *(stimulus)*
            - [`Moon`](#moon) Moon, alphabet, 1845 CE
            - [`Dsrt`](#dsrt) Deseret, alphabet, 1854 CE *(stimulus)*
            - [`Dupl`](#dupl) Duployan shorthand, Duployan stenography, alphabet, 1860 CE *(stimulus)*
            - [`Visp`](#visp) Visible Speech, featural, 1867 CE *(invented)*
            - [`Pauc`](#pauc) Pau Cin Hau, alphabet, 1902 CE *(invented)*
            - [`Wole`](#wole) Woleai, syllabary, 1905 CE *(stimulus)*
            - [`Afak`](#afak) Afaka, syllabary, 1908 CE *(invented)*
            - [`Lisu`](#lisu) Lisu, alphabet, 1915 CE
            - [`Sara`](#sara) Sarati, alphabet, 1919 CE *(invented)*
              - [`Teng`](#teng) Tengwar, alphabet, 1930 CE
            - [`Medf`](#medf) Medefaidrin, alphabet, 1927 CE *(stimulus)*
            - [`Sunu`](#sunu) Sunuwar, alphabet, 1942 CE *(stimulus)*
            - [`Wara`](#wara) Warang Citi, alphabet, 1950 CE *(invented)*
            - [`Shaw`](#shaw) Shavian, alphabet, 1960 CE *(invented)*
            - [`Sgnw`](#sgnw) SignWriting, featural, 1974 CE *(invented)*
            - [`Piqd`](#piqd) Klingon, alphabet, 1979 CE *(invented)*
            - [`Mroo`](#mroo) Mro, Mru, alphabet, 1980 CE *(invented)*
            - [`Onao`](#onao) Ol Onal, alphabet, 1981 CE *(invented)*
            - [`Chis`](#chis) Chisoi, alphabet, 1986 CE *(invented)*
            - [`Tnsa`](#tnsa) Tangsa, alphabet, 1990 CE *(invented)*
            - [`Zsye`](#zsye) Symbols, symbols, 1999 CE *(composite)*
            - [`Wcho`](#wcho) Wancho, alphabet, 2001 CE *(invented)*
            - [`Osge`](#osge) Osage, alphabet, 2006 CE
          - [`Runr`](#runr) Runic, alphabet, 150 CE
            - [`Cirt`](#cirt) Cirth, alphabet, 1930 CE *(stimulus)*
        - [`Lydi`](#lydi) Lydian, alphabet, 700 BCE
        - [`Lyci`](#lyci) Lycian, alphabet, 500 BCE
        - [`Copt`](#copt) Coptic, alphabet, 100 CE
        - [`Goth`](#goth) Gothic, alphabet, 350 CE
        - [`Armn`](#armn) Armenian, alphabet, 405 CE *(contested)*
          - [`Aghb`](#aghb) Caucasian Albanian, alphabet, 420 CE *(contested)*
        - [`Geok`](#geok) Khutsuri, alphabet, 430 CE *(contested)*
          - [`Geor`](#geor) Georgian, alphabet, 982 CE
        - [`Glag`](#glag) Glagolitic, alphabet, 863 CE *(contested)*
        - [`Cyrl`](#cyrl) Cyrillic, alphabet, 921 CE
          - [`Cyrs`](#cyrs) Cyrillic, variant, 900 CE *(variant)*
          - [`Perm`](#perm) Old Permic, alphabet, 1372 CE *(stimulus)*
        - [`Todr`](#todr) Todhri, alphabet, 1750 CE *(stimulus)*
        - [`Elba`](#elba) Elbasan, alphabet, 1761 CE *(stimulus)*
        - [`Vith`](#vith) Vithkuqi, alphabet, 1844 CE *(contested)*
      - [`Sidt`](#sidt) Sidetic, alphabet, 500 BCE *(contested)*
      - [`Tfng`](#tfng) Tifinagh, alphabet, 138 BCE *(contested)*
      - [`Samr`](#samr) Samaritan, abjad, 350 CE *(contested)*
    - [`Sarb`](#sarb) Old South Arabian, abjad, 800 BCE *(contested)*
      - [`Ethi`](#ethi) Ethiopic, abugida, 200 CE
    - [`Narb`](#narb) Old North Arabian, abjad, 600 BCE
  - [`Mero`](#mero) Meroitic Hieroglyphs, alphabet, 150 BCE

### Han

- [`Hani`](#hani) Han, logographic, 1250 BCE
  - [`Seal`](#seal) (Small) Seal, variant, 800 BCE *(variant)*
  - [`Hant`](#hant) Han, variant, 200 BCE *(variant)*
  - [`Hira`](#hira) Hiragana, syllabary, 800 CE
  - [`Hrkt`](#hrkt) Japanese syllabaries, composite, 800 CE *(composite)*
  - [`Jpan`](#jpan) Japanese, composite, 800 CE *(composite)*
  - [`Kana`](#kana) Katakana, syllabary, 825 CE
  - [`Kitl`](#kitl) Khitan large script, logographic, 920 CE *(stimulus)*
    - [`Jurc`](#jurc) Jurchen, logographic, 1119 CE
  - [`Tang`](#tang) Tangut, logographic, 1036 CE *(stimulus)*
  - [`Shui`](#shui) Shuishu, logographic, 1400 CE
  - [`Kore`](#kore) Korean, composite, 1443 CE *(composite)*
  - [`Yiii`](#yiii) Yi, syllabary, 1485 CE *(contested)*
  - [`Nshu`](#nshu) Nüshu, syllabary, 1850 CE
  - [`Hntl`](#hntl) Han (Traditional variant) with Latin, composite, 1900 CE *(composite)*
  - [`Bopo`](#bopo) Bopomofo, syllabary, 1913 CE
  - [`Hanb`](#hanb) Han with Bopomofo, composite, 1913 CE *(composite)*
  - [`Blis`](#blis) Blissymbols, semasiographic, 1949 CE *(stimulus)*
  - [`Hans`](#hans) Han, variant, 1956 CE *(variant)*

### Linear A

- [`Lina`](#lina) Linear A, undeciphered, 1800 BCE
  - [`Cpmn`](#cpmn) Cypro-Minoan, undeciphered, 1500 BCE
    - [`Cprt`](#cprt) Cypriot syllabary, syllabary, 1100 BCE
  - [`Linb`](#linb) Linear B, syllabary, 1400 BCE

### Proto-Cuneiform

- [`Pcun`](#pcun) Proto-Cuneiform, logographic, 3300 BCE
  - [`Pelm`](#pelm) Proto-Elamite, undeciphered, 3050 BCE *(stimulus)*
  - [`Xsux`](#xsux) Cuneiform, Sumero-Akkadian, logographic, 2600 BCE
    - [`Xpeo`](#xpeo) Old Persian, alphabet, 520 BCE *(stimulus)*

### Naxi Dongba

- [`Nkdb`](#nkdb) Naxi Dongba, semasiographic, 1200 CE
  - [`Nkgb`](#nkgb) Naxi Geba, syllabary, 1619 CE *(contested)*

### Anatolian Hieroglyphs

- [`Hluw`](#hluw) Anatolian Hieroglyphs, logographic, 1400 BCE

### Indus

- [`Inds`](#inds) Indus, undeciphered, 2600 BCE

### Mayan hieroglyphs

- [`Maya`](#maya) Mayan hieroglyphs, logographic, 300 BCE

### Rongorongo

- [`Roro`](#roro) Rongorongo, undeciphered, 1864 CE

## Every script, by code

### Adlm

**Adlam** (𞤀𞤣𞤤𞤢𞤥 𞤆𞤵𞤤𞤢𞤪). Alphabet, written right to left. First attested 1989 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: L2/14-219R; Unicode ch.19. Glyphs original; right-to-left direction and optional joining shared with Arabic.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 9.0, block from U+1E900.

### Afak

**Afaka**. Syllabary, written left to right. First attested 1908 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Everson, Unicode N4132 (L2/11-297R); Dubelaar 1976; L2/25-078. Unrelated to any other script; acrophonic rebus; devised 1908; still taught as grade-1 Afaka among the few literate in it.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Aghb

**Caucasian Albanian**. Alphabet, written left to right. First attested 420 CE, last used 1000 CE; status historical.

Parent: [`Armn`](#armn) Armenian, link **contested**.
Source: Everson & Gippert, Unicode N4131R. Attributed by tradition to Mashtots; arrangement close to Armenian; Greek the model for both.

Languages written mainly in it: 1. Aghwan. Also recorded as a further script for 2 more.
Unicode: encoded since version 7.0, block from U+10530.

### Ahom

**Ahom, Tai Ahom**. Abugida, written left to right. First attested 1300 CE, in use today; status revived.

Parent: [`Mymr`](#mymr) Myanmar, link **attested**.
Source: Terwiel 1983, JSS 71; Unicode ch.15. Brought at the conquest c. early 13th c., apparently on a Mon example; no dated early object; religious use into the 19th c.; modern use from a 1920 dictionary.

Languages written mainly in it: 1. Ahom.
Unicode: encoded since version 8.0, block from U+11700.

### Arab

**Arabic** (الكتابة العربية). Abjad, written right to left. First attested 512 CE, in use today; status living.

Parent: [`Nbat`](#nbat) Nabataean, link **attested**.
Source: Hoyland, 'The birth of Arabic in stone'; Robin et al. 2014, CRAI. Earliest dated text in Arabic script Zabad, 512; Namara (328) and Jabal Ramm are in Nabataean script.
Children: [`Aran`](#aran), [`Thaa`](#thaa), [`Bamu`](#bamu), [`Osma`](#osma), [`Nkoo`](#nkoo), [`Berf`](#berf), [`Gara`](#gara), [`Rohg`](#rohg), [`Adlm`](#adlm).

Languages written mainly in it: 150. Largest: Standard Arabic (335,000,000 speakers), Urdu (68,600,000 speakers), Egyptian Arabic (64,600,000 speakers), Western Farsi (52,800,000 speakers), Levantine Arabic (44,000,000 speakers). Also recorded as a further script for 154 more.
Unicode: encoded since version 1.1, block from U+0600.

### Aran

**Arabic** (نَستَعلِیق). Variant, written right to left. First attested 1400 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **variant**.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 1.1.

### Armi

**Imperial Aramaic**. Abjad, written right to left. First attested 900 BCE, last used 100 BCE; status historical.

Parent: [`Phnx`](#phnx) Phoenician, link **attested**.
Source: Encyclopaedia Iranica 'Aramaic i'; Unicode ch.10. First attested in inscriptions of the 9th-8th c. BCE; distinct from Phoenician by the mid-8th c..
Children: [`Hebr`](#hebr), [`Brah`](#brah), [`Khar`](#khar), [`Elym`](#elym), [`Chrs`](#chrs), [`Hatr`](#hatr), [`Nbat`](#nbat), [`Prti`](#prti), [`Palm`](#palm), [`Syrc`](#syrc), [`Phli`](#phli), [`Sogo`](#sogo).

Languages written mainly in it: 1. Imperial Aramaic (700-300 BCE). Also recorded as a further script for 3 more.
Unicode: encoded since version 5.2, block from U+10840.

### Armn

**Armenian** (հայկական). Alphabet, written left to right. First attested 405 CE, in use today; status living.

Parent: [`Grek`](#grek) Greek, link **contested**.
Source: Pifer, Encyclopaedia Iranica 'Mesrop Mastoc'; D'Aiuto 2020. Arranged in Greek order; derivation of the letter shapes from Greek, Iranian or Aramaic still argued.
Children: [`Aghb`](#aghb).

Languages written mainly in it: 4. Largest: Eastern Armenian (6,700,000 speakers), Western Armenian (1,395,240 speakers), Lomavren, Classical-Middle Armenian. Also recorded as a further script for 1 more.
Unicode: encoded since version 1.1, block from U+0531.

### Avst

**Avestan**. Alphabet, written right to left. First attested 500 CE, in use today; status living.

Parent: [`Phlv`](#phlv) Book Pahlavi, link **attested**.
Source: Unicode ch.10; Hoffmann, Encyclopaedia Iranica 'Avestan script'. Created about the 5th-6th c. CE for the Avesta; earliest manuscript 1288; still used in Zoroastrian liturgy.

Languages written mainly in it: 1. Avestan. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.2, block from U+10B00.

### Bali

**Balinese** (ᬅᬓ᭄ᬱᬭᬩᬮᬶ). Abugida, written left to right. First attested 914 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi, link **attested**.
Source: Unicode ch.17. From Kawi; Belanjong pillar 914, Old Balinese beside Sanskrit.

Languages written mainly in it: 1. Kawi. Also recorded as a further script for 2 more.
Unicode: encoded since version 5.0, block from U+1B00.

### Bamu

**Bamum**. Syllabary, written left to right. First attested 1896 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **contested**.
Source: Orosz, Cahiers d'etudes africaines 2013 (journals.openedition.org/etudesafricaines/18002). Arabic via Hausa traders is the most cited stimulus; European and Vai models also proposed.

Languages written mainly in it: 1. Bamun.
Unicode: encoded since version 5.2, block from U+A6A0.

### Bass

**Bassa Vah**. Alphabet, written left to right. First attested 1907 CE, in use today; status living.

Parent: [`Vaii`](#vaii) Vai, link **stimulus**.
Source: Unicode N3941R (L2/10-382R); Unicode ch.19. May have been influenced by Vai; typeset from 1907.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+16AD0.

### Batk

**Batak** (ᯘᯮᯒᯖ᯲ ᯅᯖᯂ᯲). Abugida, written left to right. First attested 1764 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi, link **contested**.
Source: Kozok 2000, BKI. No proto-forms found; a manuscript in the British Library by 1764; introduction date unknown.

Languages written mainly in it: 2. Largest: Batak Mandailing (1,100,000 speakers), Batak Dairi. Also recorded as a further script for 4 more.
Unicode: encoded since version 6.0, block from U+1BC0.

### Beng

**Bengali** (বাংলা-অসমীয়া). Abugida, written left to right. First attested 1350 CE, in use today; status living.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Gaudi, link **attested**.
Source: Salomon 1998 2.2.5.5; Unicode ch.15. Gaudi (proto-Bengali) current from the 10th to the 14th c.; a distinct Bengali from the 14th-15th c..
Children: [`Toto`](#toto).

Languages written mainly in it: 16. Largest: Bengali (300,000,000 speakers), Assamese (15,300,000 speakers), Sylheti (13,980,000 speakers), Chittagonian (13,000,000 speakers), Mundari (1,500,000 speakers). Also recorded as a further script for 30 more.
Unicode: encoded since version 1.1, block from U+0980.

### Berf

**Beria Erfe**. Alphabet, written left to right. First attested 1950 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic through Zaghawa camel brands, link **invented**.
Source: Unicode ch.19; L2/24-004R. Devised in the 1950s by Adam Tajir from livestock brand marks; revised 2004; left to right.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Bhks

**Bhaiksuki** (भैक्षुकी). Abugida, written left to right. First attested 1000 CE, last used 1200 CE; status historical.

Parent: [`Brah`](#brah) Brahmi, link **attested**.
Source: Unicode ch.14; Dimitrov. Used 10th-13th c.; eleven inscriptions and four manuscripts known.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 9.0, block from U+11C00.

### Blis

**Blissymbols**. Semasiographic, written left to right. First attested 1949 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **stimulus**.
Source: Bliss 1949, Semantography; Unicode N5228. An ideographic system inspired by Chinese characters, devised 1942-1949.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Bopo

**Bopomofo** (注音符號). Syllabary, written in more than one direction. First attested 1913 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **attested**.
Source: Ministry of Education, Taiwan; DeFrancis 1950. Adopted 1913 from simplified Han forms (Zhang Binglin), promulgated 1918.

Languages written mainly in it: 3. Largest: Ge, Northern Qiandong Miao, Eastern Qiandong Miao. Also recorded as a further script for 2 more.
Unicode: encoded since version 1.1, block from U+02EA.

### Brah

**Brahmi** (𑀩𑁆𑀭𑀸𑀳𑁆𑀫𑀻). Abugida, written left to right. First attested 250 BCE, last used 500 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **contested**.
Source: Bright 1996, in Daniels & Bright; Salomon 1998, Indian Epigraphy. Aramaic origin after Buhler is the majority view; not settled; earliest securely dated texts the Ashokan edicts, c.250 BCE.
Children: [`Sinh`](#sinh), [`Cham`](#cham), [`Knda`](#knda), [`Sidd`](#sidd), [`Gran`](#gran), [`Taml`](#taml), [`Telu`](#telu), [`Khmr`](#khmr), [`Tibt`](#tibt), [`Kawi`](#kawi), [`Shrd`](#shrd), [`Bhks`](#bhks), [`Mtei`](#mtei), [`Mymr`](#mymr), [`Saur`](#saur), [`Gonm`](#gonm), [`Sora`](#sora), [`Gukh`](#gukh).

Languages written mainly in it: 8. Largest: Tokharian B, Tokharian A, Old Cham, Maharastri Prakrit, Khotanese. Also recorded as a further script for 3 more.
Unicode: encoded since version 6.0, block from U+11000.

### Brai

**Braille**. Alphabet, written left to right. First attested 1824 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin through Barbier's night writing, link **stimulus**.
Source: RNIB; Unicode ch.21. A six-dot recoding of the French Latin alphabet, after Barbier's twelve-dot phonetic code.

Recorded as a further script for 137 languages, the main script for none.
Unicode: encoded since version 3.0, block from U+2800.

### Bugi

**Buginese** (ᨒᨚᨈᨑ). Abugida, written left to right. First attested 1600 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi, link **contested**.
Source: Everson, Unicode N2588. Of the Brahmic type and perhaps related to Javanese.

Recorded as a further script for 6 languages, the main script for none.
Unicode: encoded since version 4.1, block from U+1A00.

### Buhd

**Buhid** (ᝊᝓᝑᝒ). Abugida, written left to right. First attested 1600 CE, in use today; status living.

Parent: [`Tglg`](#tglg) Tagalog, link **contested**.
Source: Unicode ch.17; Miller, Unicode Technical Note 35. Related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting.

Recorded as a further script for 3 languages, the main script for none.
Unicode: encoded since version 3.2, block from U+1740.

### Cakm

**Chakma** (𑄌𑄋𑄴𑄟𑄳𑄦 𑄃𑄧𑄏𑄛𑄖𑄴). Abugida, written left to right. First attested 1700 CE, in use today; status living.

Parent: [`Mymr`](#mymr) Myanmar, link **attested**.
Source: Everson & Hosken, Unicode N3645 (L2/09-187). Brahmic, an early offshoot of the Mon-Burmese script; no dated early manuscript found.

Languages written mainly in it: 2. Largest: Chakma (326,000 speakers), Tangchangya.
Unicode: encoded since version 6.1, block from U+11100.

### Cans

**Unified Canadian Aboriginal Syllabics** (ᓀᐦᐃᔭᐘᓯᓇᐦᐃᑳᑌᐤ). Syllabary, written left to right. First attested 1840 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin through British shorthand, link **stimulus**.
Source: Nichols 1996, in Daniels & Bright. Most characters drawn from British shorthand; Evans knew Devanagari, but no source makes it his model.
Children: [`Plrd`](#plrd).

Languages written mainly in it: 10. Largest: Plains Cree (34,000 speakers), Severn Ojibwa (10,500 speakers), Eastern Canadian Inuktitut, Naskapi, Swampy Cree. Also recorded as a further script for 13 more.
Unicode: encoded since version 3.0, block from U+1400.

### Cari

**Carian**. Alphabet, written in more than one direction. First attested 700 BCE, last used 300 BCE; status historical.

Parent: [`Grek`](#grek) Greek, link **contested**.
Source: Unicode ch.8; Adiego 2018. A development parallel to, and independent of, Greek cannot be ruled out.

Languages written mainly in it: 1. Carian.
Unicode: encoded since version 5.1, block from U+102A0.

### Cham

**Cham** (ꨀꨇꩉ ꨌꩌ). Abugida, written left to right. First attested 400 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Pallava, link **attested**.
Source: Unicode ch.16; Filliozat 1969. Old Cham at Dong Yen Chau, c.4th c., in Pallava script.

Languages written mainly in it: 1. Eastern Cham. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.1, block from U+AA00.

### Cher

**Cherokee** (ᏣᎳᎩ ᏧᏓᏡᎩ ᏚᏃᏴᎬᎢ). Syllabary, written left to right. First attested 1821 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: Unicode ch.20. Sequoyah took letter shapes from Latin print without their Latin values, 1815-1821.

Languages written mainly in it: 1. Cherokee (12,300 speakers).
Unicode: encoded since version 3.0, block from U+13A0.

### Chis

**Chisoi**. Alphabet, written left to right. First attested 1986 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: L2/22-218R3. Invented in 1986 by Jayanta Kumar Mahata from Kurmali ritual and rangoli signs.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Chrs

**Chorasmian** (زڨاک ای خوارزم). Abjad, written right to left. First attested 100 BCE, last used 800 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: L2/18-164R2 (Chorasmian). From Imperial Aramaic; dated cursive from Toprak-Kala, 3rd c. CE; earlier dates in the proposal unresolved.

Languages written mainly in it: 1. Khwarezmian.
Unicode: encoded since version 13.0, block from U+10FB0.

### Cirt

**Cirth**. Alphabet, written left to right. First attested 1930 CE, in use today; status fictional.

Parent: [`Runr`](#runr) Runic, link **stimulus**.
Source: Everson, Unicode N4013. A runiform script built by Tolkien on the model of Germanic runes.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Copt

**Coptic**. Alphabet, written left to right. First attested 100 CE, in use today; status living.

Parent: [`Grek`](#grek) Greek, link **attested**.
Source: Claremont Coptic Encyclopedia, 'Old Coptic'. Old Coptic papyri of the 1st-2nd c. CE; Greek letters plus six or seven from Demotic.

Languages written mainly in it: 2. Largest: Coptic, Old Nubian. Also recorded as a further script for 2 more.
Unicode: encoded since version 4.1, block from U+03E2.

### Cpmn

**Cypro-Minoan**. Undeciphered, written left to right. First attested 1500 BCE, last used 1050 BCE; status undeciphered.

Parent: [`Lina`](#lina) Linear A, link **attested**.
Source: Olivier 2012; Steele 2014, Kadmos 53. Enkomi tablet of Late Cypriot I, c.1525-1475 BCE; derived from Linear A by sign form.
Children: [`Cprt`](#cprt).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 14.0, block from U+12F90.

### Cprt

**Cypriot syllabary**. Syllabary, written right to left. First attested 1100 BCE, last used 300 BCE; status historical.

Parent: [`Cpmn`](#cpmn) Cypro-Minoan, link **attested**.
Source: Olivier 2012. The Palaepaphos obelos (11th c. BCE) may be the last Cypro-Minoan text rather than the first Cypriot one.

Languages written mainly in it: 1. Eteocypriot. Also recorded as a further script for 1 more.
Unicode: encoded since version 4.0, block from U+10800.

### Cyrl

**Cyrillic** (кириллица). Alphabet, written left to right. First attested 921 CE, in use today; status living.

Parent: [`Grek`](#grek) Greek, link **attested**.
Source: Slavica Occitania 12 (2001), after the Kirilo-Metodievska enciklopedija. Earliest epigraphy Krepcha 921, a Preslav sherd 931, a dated Dobrudja inscription 943.
Children: [`Cyrs`](#cyrs), [`Perm`](#perm).

Languages written mainly in it: 99. Largest: Russian (154,000,000 speakers), Ukrainian (26,900,000 speakers), Tajik (14,000,000 speakers), Kazakh (12,900,000 speakers), Bulgarian (9,000,000 speakers). Also recorded as a further script for 41 more.
Unicode: encoded since version 1.1, block from U+0400.

### Cyrs

**Cyrillic**. Variant, written left to right. First attested 900 CE, in use today; status living.

Parent: [`Cyrl`](#cyrl) Cyrillic, link **variant**.

Recorded as a further script for 8 languages, the main script for none.
Unicode: encoded since version 1.1.

### Deva

**Devanagari** (देवनागरी). Abugida, written left to right. First attested 851 CE, in use today; status living.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Nagari, link **attested**.
Source: Salomon 1998, after Sukthankar. No authentic specimen before the Silahara inscriptions at Kanheri, 851 and 877-878.
Children: [`Nand`](#nand), [`Gujr`](#gujr), [`Mahj`](#mahj), [`Modi`](#modi), [`Tols`](#tols).

Languages written mainly in it: 183. Largest: Hindi (341,000,000 speakers), Marathi (83,100,000 speakers), Bhojpuri (52,200,000 speakers), Maithili (33,900,000 speakers), Awadhi (22,000,000 speakers). Also recorded as a further script for 35 more.
Unicode: encoded since version 1.1, block from U+0900.

### Diak

**Dives Akuru** (𑤙𑤱𑤩𑤵𑤭𑤱 𑤀𑤌𑤳𑤧𑤳). Abugida, written left to right. First attested 900 CE, last used 1700 CE; status historical.

Parent: [`Gran`](#gran) Grantha, link **attested**.
Source: Pandey, L2/18-016R. Descended from Brahmi through Grantha; closest to medieval Sinhala.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 13.0, block from U+11900.

### Dogr

**Dogra** (𑠝𑠢𑠳𑠷 𑠖𑠵𑠌𑠤𑠬 𑠀𑠊𑠹𑠋𑠤). Abugida, written left to right. First attested 1860 CE, last used 1950 CE; status historical.

Parent: [`Takr`](#takr) Takri, Ṭākrī, Ṭāṅkrī, link **attested**.
Source: Pandey, L2/15-234; Unicode ch.15; Indian Express 2026. Dogra written from the 17th c.; standardised in the 1860s; no longer used actively, Dogri now in Devanagari; signboard revival begun in Jammu, 2026.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 11.0, block from U+11800.

### Dsrt

**Deseret** (𐐔𐐯𐑅𐐨𐑉𐐯𐐻). Alphabet, written left to right. First attested 1854 CE, last used 1869 CE; status historical.

Parent: [`Latn`](#latn) Latin through Pitman 1847 phonotypy, link **stimulus**.
Source: Beesley, 'Deseret in Unicode'; Unicode ch.20. Pitman's phonotypy the starting point, then an entirely new set of characters, adopted Dec 1853; not actively promoted after 1869; now of interest to historians and hobbyists.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 3.1, block from U+10400.

### Dupl

**Duployan shorthand, Duployan stenography**. Alphabet, written left to right. First attested 1860 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: Unicode L2/10-272R2. A geometric shorthand, letterforms from circles and lines, for writing French.

Languages written mainly in it: 1. Thompson (440 speakers). Also recorded as a further script for 8 more.
Unicode: encoded since version 7.0, block from U+1BC00.

### Egyd

**Egyptian demotic**. Logographic, written right to left. First attested 650 BCE, last used 500 CE; status historical.

Parent: [`Egyh`](#egyh) Egyptian hieratic through Abnormal Hieratic, link **attested**.
Source: Depauw, A Companion to Demotic Studies. Develops out of late hieratic in the 7th c. BCE; the earliest named object is not sourced here.
Children: [`Merc`](#merc).

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Egyh

**Egyptian hieratic**. Logographic, written right to left. First attested 2700 BCE, last used 300 CE; status historical.

Parent: [`Egyp`](#egyp) Egyptian hieroglyphs, link **attested**.
Source: Regulski, Oxford Handbook of Topics in Archaeology. Earliest hieratic on the stone vessels under the Step Pyramid, late 2nd dynasty to Djoser.
Children: [`Egyd`](#egyd).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 5.2.

### Egyp

**Egyptian hieroglyphs**. Logographic, written in more than one direction. First attested 3250 BCE, last used 400 CE; status historical.

A root: no known parent among the registry's codes.
Source: Baines 2004, in Houston (ed.), The First Writing. Independent Egyptian invention is the majority view; stimulus from Sumer is argued and not excluded.
Children: [`Egyh`](#egyh), [`Psin`](#psin), [`Mero`](#mero).

Languages written mainly in it: 1. Egyptian (Ancient).
Unicode: encoded since version 5.2, block from U+13000.

### Elba

**Elbasan**. Alphabet, written left to right. First attested 1761 CE, last used 1800 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **stimulus**.
Source: Everson & Elsie, Unicode N3856. A Greek flavour to some characters, most letters new creations.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+10500.

### Elym

**Elymaic**. Abjad, written right to left. First attested 150 BCE, last used 300 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: L2/17-226 (Elymaic); Unicode ch.10. Derives from Aramaic; earliest on coins of the 2nd c. BCE.
Children: [`Mand`](#mand).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 12.0, block from U+10FE0.

### Ethi

**Ethiopic** (ግዕዝ). Abugida, written left to right. First attested 200 CE, in use today; status living.

Parent: [`Sarb`](#sarb) Old South Arabian, link **attested**.
Source: Drewes, RIE III/B; Breton 2019, Cahiers d'etudes africaines. Earliest Ge'ez text the Addi Gelemo sceptre, late 2nd to early 3rd c. CE; vocalised under Ezana.

Languages written mainly in it: 34. Largest: Amharic (21,900,000 speakers), Tigrinya (7,507,780 speakers), Wolaytta (5,830,000 speakers), Gamo-Gofa-Dawro (2,000,000 speakers), Sebat Bet Gurage (1,480,000 speakers). Also recorded as a further script for 25 more.
Unicode: encoded since version 3.0, block from U+1200.

### Gara

**Garay**. Alphabet, written right to left. First attested 1961 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: Everson, Unicode N4709; Pandey, Unicode N4044. Influences of the Arabic writing system; written right to left.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+10D40.

### Geok

**Khutsuri** (ხუცური). Alphabet, written left to right. First attested 430 CE, last used 1100 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **contested**.
Source: Bolkvadze & Kiziria 2023; Giunashvili on Tsereteli. Greek provenance most widely accepted; Aramaic shapes argued; earliest inscriptions dated 430s, some earlier claims.
Children: [`Geor`](#geor).

Languages written mainly in it: 1. Old Georgian. Also recorded as a further script for 1 more.
Unicode: encoded since version 1.1, block from U+10A0.

### Geor

**Georgian** (ქართული). Alphabet, written left to right. First attested 982 CE, in use today; status living.

Parent: [`Geok`](#geok) Khutsuri, link **attested**.
Source: Aleksidze 1983; Typotheque 2023. First Mkhedruli inscription at Ateni Sioni, 982-986.

Languages written mainly in it: 4. Largest: Georgian (3,700,000 speakers), Mingrelian (345,530 speakers), Svan (15,000 speakers), Bats (3,420 speakers). Also recorded as a further script for 3 more.
Unicode: encoded since version 1.1, block from U+10A0.

### Glag

**Glagolitic** (Ⰽⱛⱃⰺⰾⰾⱁⰲⰺⱌⰰ). Alphabet, written left to right. First attested 863 CE, last used 1900 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **contested**.
Source: Cubberley, 'Slavonic, Old Church: Orthography'; Schenker 1995. The search for the formal origins of Glagolitic remains unsolved.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 4.1, block from U+2C00.

### Gong

**Gunjala Gondi** (గుంజలా గోండి లిపి). Abugida, written left to right. First attested 1750 CE, in use today; status living.

Parent: [`Modi`](#modi) Modi, Moḍī, link **contested**.
Source: Pandey, L2/15-235R. Not genetically related to other scripts, but strongly resembles Modi; c.1750 is a researchers' claim, 1942 the firm evidence.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 11.0, block from U+11D60.

### Gonm

**Masaram Gondi** (𑴤𑴫𑴦𑴱𑴤 𑴎𑴽𑵀𑴘𑴳 𑴧𑴲𑴠𑴲). Abugida, written left to right. First attested 1918 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **stimulus**.
Source: Pandey, L2/15-090R. No genetic relationship to other writing systems, but based upon the Brahmi model.

Languages written mainly in it: 1. Aheri Gondi (150,000 speakers). Also recorded as a further script for 2 more.
Unicode: encoded since version 10.0, block from U+11D00.

### Goth

**Gothic** (𐌰𐌶𐌲𐌰𐌱𐌰𐌹𐍂𐌺𐌰). Alphabet, written left to right. First attested 350 CE, last used 900 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **attested**.
Source: Schaffner 2024, Oxford Research Encyclopedia of Linguistics. Wulfila's alphabet on the Greek model, with Latin and runic letters, c.350; manuscripts 5th-6th c..

Languages written mainly in it: 1. Gothic.
Unicode: encoded since version 3.1, block from U+10330.

### Gran

**Grantha** (𑌗𑍍𑌰𑌨𑍍𑌥𑌲𑌿𑌪𑌿). Abugida, written left to right. First attested 600 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Pallava, link **attested**.
Source: Francis 2024; Pandey, L2/18-083. Pallava is the ancestor of Grantha; Grantha itself designed around 600 CE.
Children: [`Diak`](#diak), [`Tutg`](#tutg), [`Mlym`](#mlym).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+11300.

### Grek

**Greek** (ελληνικό αλφάβητο). Alphabet, written left to right. First attested 750 BCE, in use today; status living.

Parent: [`Phnx`](#phnx) Phoenician, link **attested**.
Source: Janko, on Methone; Jeffery, Local Scripts of Archaic Greece. Dipylon jug c.740 BCE and Nestor's cup; Gabii c.770 on the traditional chronology; earliest texts right to left.
Children: [`Cari`](#cari), [`Ital`](#ital), [`Lydi`](#lydi), [`Lyci`](#lyci), [`Copt`](#copt), [`Goth`](#goth), [`Armn`](#armn), [`Geok`](#geok), [`Glag`](#glag), [`Cyrl`](#cyrl), [`Todr`](#todr), [`Elba`](#elba), [`Vith`](#vith).

Languages written mainly in it: 17. Largest: Modern Greek (15,000,000 speakers), Pontic (778,000 speakers), Rumelian Turkish (464,000 speakers), Kipchak Urum (185,000 speakers), Cappadocian Greek (2,800 speakers). Also recorded as a further script for 11 more.
Unicode: encoded since version 1.1, block from U+0370.

### Gujr

**Gujarati** (ગુજરાતી લિપિ). Abugida, written left to right. First attested 1592 CE, in use today; status living.

Parent: [`Deva`](#deva) Devanagari through Nagari, link **attested**.
Source: Unicode ch.12; Salomon 1998 3.4.3. Closely related to Devanagari; texts wholly in Gujarati from the late 15th c.; 1592 unsourced.

Languages written mainly in it: 7. Largest: Gujarati (56,400,000 speakers), Dhanki, Dhodia-Kukna, Chodri, Gamit. Also recorded as a further script for 11 more.
Unicode: encoded since version 1.1, block from U+0A81.

### Gukh

**Gurung Khema**. Abugida, written left to right. First attested 1995 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **stimulus**.
Source: L2/22-157. An alphasyllabary based upon the Brahmi model, created 1995.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+16100.

### Guru

**Gurmukhi** (گرمکھی). Abugida, written left to right. First attested 1570 CE, in use today; status living.

Parent: [`Shrd`](#shrd) Sharada, Śāradā through Landa, link **attested**.
Source: Pandey, L2/10-011; Mann 1996, The Goindval Pothis. Landa the model; the Goindval Pothis of the 1570s are the earliest extant source; 1539 was a guruship date.

Languages written mainly in it: 1. Eastern Panjabi (125,000,000 speakers). Also recorded as a further script for 2 more.
Unicode: encoded since version 1.1, block from U+0A01.

### Hanb

**Han with Bopomofo**. Composite, written in more than one direction. First attested 1913 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **composite**.

Languages a source records it for: none.
Unicode: encoded since version 1.1.

### Hang

**Hangul** (언서). Featural, written in more than one direction. First attested 1443 CE, in use today; status living.

Parent: [`Phag`](#phag) Phags-pa, link **contested**.
Source: Ledyard 1966; Haerye 1446. Five or six consonant shapes from Phags-pa (Ledyard); the Haerye derives them from the speech organs.
Children: [`Jamo`](#jamo).

Languages written mainly in it: 1. Jejueo (5,000 speakers). Also recorded as a further script for 2 more.
Unicode: encoded since version 1.1, block from U+1100.

### Hani

**Han** (汉字). Logographic, written in more than one direction. First attested 1250 BCE, in use today; status living.

A root: no known parent among the registry's codes.
Children: [`Seal`](#seal), [`Hant`](#hant), [`Hira`](#hira), [`Hrkt`](#hrkt), [`Jpan`](#jpan), [`Kana`](#kana), [`Kitl`](#kitl), [`Tang`](#tang), [`Shui`](#shui), [`Kore`](#kore), [`Yiii`](#yiii), [`Nshu`](#nshu), [`Hntl`](#hntl), [`Bopo`](#bopo), [`Hanb`](#hanb), [`Blis`](#blis), [`Hans`](#hans).

Languages written mainly in it: 20. Largest: Mandarin Chinese (918,000,000 speakers), Eastern Hongshuihe Zhuang (1,200,000 speakers), Sui (300,000 speakers), Lakkia (9,000 speakers), Paekche. Also recorded as a further script for 21 more.
Unicode: encoded since version 1.1, block from U+2E80.

### Hano

**Hanunoo** (ᜱᜨᜳᜨᜳᜢ). Abugida, written left to right. First attested 1600 CE, in use today; status living.

Parent: [`Tglg`](#tglg) Tagalog, link **contested**.
Source: Unicode ch.17; Miller, Unicode Technical Note 35. Related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting.

Recorded as a further script for 6 languages, the main script for none.
Unicode: encoded since version 3.2, block from U+1720.

### Hans

**Han** (简化字). Variant, written left to right. First attested 1956 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **variant**.

Languages written mainly in it: 14. Largest: Wu Chinese (81,400,000 speakers), Min Nan Chinese (50,100,000 speakers), Hakka Chinese (48,200,000 speakers), Jinyu Chinese (46,900,000 speakers), Xiang Chinese (37,300,000 speakers). Also recorded as a further script for 10 more.
Unicode: encoded since version 1.1.

### Hant

**Han** (繁體字). Variant, written in more than one direction. First attested 200 BCE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **variant**.

Languages written mainly in it: 3. Largest: Yue Chinese (73,100,000 speakers), Classical Chinese, Middle Chinese. Also recorded as a further script for 18 more.
Unicode: encoded since version 1.1.

### Hatr

**Hatran**. Abjad, written right to left. First attested 98 BCE, last used 300 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Unicode N4324 (L2/12-312). Inscriptions from 98-97 BCE to about 241 CE.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 8.0, block from U+108E0.

### Hebr

**Hebrew** (אָלֶף־בֵּית עִבְרִי). Abjad, written right to left. First attested 300 BCE, in use today; status living.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Unicode ch.10; Barag. The square Hebrew script grew out of Imperial Aramaic; Mount Gerizim inscriptions 3rd-2nd c. BCE.
Children: [`Hmnp`](#hmnp).

Languages written mainly in it: 20. Largest: Modern Hebrew (9,303,950 speakers), Ladino (137,000 speakers), Judeo-Persian (60,000 speakers), Judeo-Yemeni Arabic (50,300 speakers), Hulaulá (10,000 speakers). Also recorded as a further script for 9 more.
Unicode: encoded since version 1.1, block from U+0591.

### Hira

**Hiragana** (平仮名). Syllabary, written in more than one direction. First attested 800 CE, in use today; status living.

Parent: [`Hani`](#hani) Han through Man'yogana, link **attested**.
Source: Unicode ch.18; Seeley 1991, A History of Writing in Japan. A 9th-c. development from cursive man'yogana; no securely dated first object.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 1.1, block from U+3041.

### Hluw

**Anatolian Hieroglyphs**. Logographic, written boustrophedon. First attested 1400 BCE, last used 700 BCE; status historical.

A root: no known parent among the registry's codes.
Source: van den Hout 2020, A History of Hittite Literacy, ch.7. Egyptian inspiration unlikely; probably an Anatolian creation from indigenous signs.

Languages written mainly in it: 1. Hieroglyphic Luwian.
Unicode: encoded since version 8.0, block from U+14400.

### Hmng

**Pahawh Hmong** (𖬖𖬰𖬝𖬵 𖬄𖬶𖬟 𖬌𖬣𖬵). Alphabet, written left to right. First attested 1959 CE, in use today; status living.

Parent: [`Laoo`](#laoo) Lao, link **invented**.
Source: Unicode ch.16; Smalley, Vang & Yang 1990, Mother of Writing. Devised by Shong Lue Yang in 1959; some letters may recall Lao and Latin.

Languages written mainly in it: 1. Hmong Njua (Retired) (4,000,000 speakers). Also recorded as a further script for 3 more.
Unicode: encoded since version 7.0, block from U+16B00.

### Hmnp

**Nyiakeng Puachue Hmong** (𞄐𞄦𞄲𞄤𞄎𞄫𞄰𞄚𞄧𞄲𞄤𞄔𞄬𞄱). Alphabet, written left to right. First attested 1980 CE, in use today; status living.

Parent: [`Hebr`](#hebr) Hebrew, link **stimulus**.
Source: Everson, Unicode N4780R3. Several consonant letters appear derived from Hebrew characters; 1980s.

Languages written mainly in it: 1. Hmong Njua. Also recorded as a further script for 1 more.
Unicode: encoded since version 12.0, block from U+1E100.

### Hntl

**Han (Traditional variant) with Latin**. Composite, written in more than one direction. First attested 1900 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **composite**.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Hrkt

**Japanese syllabaries** (仮名). Composite, written in more than one direction. First attested 800 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **composite**.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 1.1.

### Hung

**Old Hungarian** (𐲥𐳋𐳓𐳉𐳗-𐲘𐳀𐳎𐳀𐳢 𐲢𐳛𐳮𐳀𐳤). Alphabet, written right to left. First attested 900 CE, in use today; status revived.

Parent: [`Orkh`](#orkh) Old Turkic, Orkhon Runic, link **contested**.
Source: Everson & Szelp, Unicode N3483; Demeczky et al., Unicode N4371. Thought to derive ultimately from Old Turkic; some treat them as distant relatives only.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 8.0, block from U+10C80.

### Inds

**Indus**. Undeciphered, written right to left. First attested 2600 BCE, last used 1900 BCE; status undeciphered.

A root: no known parent among the registry's codes.
Source: Farmer, Sproat & Witzel 2004, EJVS 11-2; Rao et al. 2009, Science 324. Whether the signs encode language at all is disputed.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Ital

**Old Italic**. Alphabet, written in more than one direction. First attested 700 BCE, last used 100 BCE; status historical.

Parent: [`Grek`](#grek) Greek through Euboean Greek, link **attested**.
Source: Everson, L2/00-140; Unicode TN40. From the Euboean Greek of Ischia and Cumae; Marsiliana abecedary 7th c. BCE; mostly right to left.
Children: [`Latn`](#latn), [`Runr`](#runr).

Languages written mainly in it: 6. Largest: Etruscan, Raetic, Venetic, Oscan, Transalpine Gaulish. Also recorded as a further script for 2 more.
Unicode: encoded since version 3.1, block from U+10300.

### Jamo

**Jamo**. Variant, written left to right. First attested 1443 CE, in use today; status living.

Parent: [`Hang`](#hang) Hangul, link **variant**.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 1.1.

### Java

**Javanese**. Abugida, written left to right. First attested 1500 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi, link **attested**.
Source: Pandey, L2/12-125. Kawi is the ancestor of Javanese and Balinese.

Languages written mainly in it: 2. Largest: Osing (300,000 speakers), Tengger. Also recorded as a further script for 9 more.
Unicode: encoded since version 5.2, block from U+A980.

### Jpan

**Japanese** (日本語の文字). Composite, written in more than one direction. First attested 800 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **composite**.

Languages written mainly in it: 4. Largest: Japanese (128,000,000 speakers), Yaeyama (47,600 speakers), Southern Amami-Oshima (1,800 speakers), Yonaguni (400 speakers). Also recorded as a further script for 1 more.
Unicode: encoded since version 1.1.

### Jurc

**Jurchen**. Logographic, written top to bottom. First attested 1119 CE, last used 1500 CE; status historical.

Parent: [`Kitl`](#kitl) Khitan large script, link **attested**.
Source: Kara 1996, in Daniels & Bright; Jinshi 73. Many characters copies or distorted copies of Chinese and Khitan large script.

Languages written mainly in it: 1. Jurchen.
Unicode: not encoded, so no font can show it.

### Kali

**Kayah Li**. Alphabet, written left to right. First attested 1962 CE, in use today; status living.

Parent: [`Mymr`](#mymr) Myanmar, link **stimulus**.
Source: Unicode N3038. Ordering and some shapes show Brahmic relation, most shapes developed independently.

Languages written mainly in it: 3. Largest: Western Kayah (150,000 speakers), Yintale Karen (1,000 speakers), Eastern Kayah.
Unicode: encoded since version 5.1, block from U+A900.

### Kana

**Katakana** (片仮名). Syllabary, written in more than one direction. First attested 825 CE, in use today; status living.

Parent: [`Hani`](#hani) Han through Man'yogana, link **attested**.
Source: Whitman 2022; Seeley 1991. Todaiji fujumonko, 824-834, the earliest katakana used for an extended Japanese text.

Languages written mainly in it: 2. Largest: Central Okinawan (984,000 speakers), Hokkaido Ainu (10 speakers). Also recorded as a further script for 3 more.
Unicode: encoded since version 1.1, block from U+30A1.

### Kawi

**Kawi**. Abugida, written left to right. First attested 750 CE, last used 1500 CE; status historical.

Parent: [`Brah`](#brah) Brahmi through Pallava, link **attested**.
Source: de Casparis 1975, Indonesian Palaeography; Pandey, L2/12-125. Plumpungan c.750; de Casparis doubts direct descent from Pallava.
Children: [`Bali`](#bali), [`Sund`](#sund), [`Java`](#java), [`Tglg`](#tglg), [`Bugi`](#bugi), [`Rjng`](#rjng), [`Batk`](#batk).

Recorded as a further script for 3 languages, the main script for none.
Unicode: encoded since version 15.0, block from U+11F00.

### Khar

**Kharoshthi**. Abugida, written right to left. First attested 250 BCE, last used 300 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Strauch; Baums 2016; Salomon 1998. No securely dated document before the Ashokan edicts at Shahbazgarhi and Mansehra, mid-3rd c. BCE.

Languages written mainly in it: 1. Gandhari. Also recorded as a further script for 4 more.
Unicode: encoded since version 4.1, block from U+10A00.

### Khmr

**Khmer** (អក្សរខ្មែរ). Abugida, written left to right. First attested 611 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Pallava, link **attested**.
Source: Zakharov 2019; Unicode ch.16. Earliest dated Old Khmer K.557/600, 611; close to the Pallava script of the Coromandel coast.
Children: [`Thai`](#thai).

Languages written mainly in it: 5. Largest: Central Khmer (16,600,000 speakers), Somray of Battambang-Somre of Siem Reap, Kaco', Tampuan, Brao. Also recorded as a further script for 5 more.
Unicode: encoded since version 3.0, block from U+1780.

### Khoj

**Khojki** (𑊻𑋧𑋂𑊺𑋢). Abugida, written left to right. First attested 1500 CE, in use today; status living.

Parent: [`Shrd`](#shrd) Sharada, Śāradā through Landa, link **attested**.
Source: Pandey, Unicode N3978; Unicode ch.15. A refined form of the Lohanaki variety of Landa, in use by the 16th c.; primers still published in Pakistan; used in Nizari Ismaili ceremonies.

Recorded as a further script for 5 languages, the main script for none.
Unicode: encoded since version 7.0, block from U+11200.

### Kitl

**Khitan large script** (契丹大字). Logographic, written top to bottom. First attested 920 CE, last used 1200 CE; status undeciphered.

Parent: [`Hani`](#hani) Han, link **stimulus**.
Source: Kane 2009, The Kitan Language and Script. On the basis of Chinese clerical script with modifications; most characters novel.
Children: [`Jurc`](#jurc).

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Kits

**Khitan small script** (契丹小字). Logographic, written top to bottom. First attested 925 CE, last used 1200 CE; status undeciphered.

Parent: [`Ougr`](#ougr) Old Uyghur, link **stimulus**.
Source: Kane 2009. Created after contact with Uighurs; phonetic components, no shared characters with the large script.

Languages written mainly in it: 1. Kitan.
Unicode: encoded since version 13.0, block from U+16FE4.

### Knda

**Kannada** (ಕನ್ನಡ ಲಿಪಿ). Abugida, written left to right. First attested 450 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Kadamba, link **attested**.
Source: Mahadevan, Frontline; Gai. Halmidi inscription, mid-5th c., in Kadamba script; a sister of Telugu.

Languages written mainly in it: 7. Largest: Kannada (43,600,000 speakers), Tulu (2,000,000 speakers), Kodava (200,000 speakers), Sholaga (24,000 speakers), Kudiya. Also recorded as a further script for 8 more.
Unicode: encoded since version 1.1, block from U+0C80.

### Kore

**Korean** (국한문체). Composite, written in more than one direction. First attested 1443 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **composite**.

Languages written mainly in it: 1. Korean (77,300,000 speakers).
Unicode: encoded since version 1.1.

### Kpel

**Kpelle**. Syllabary, written left to right. First attested 1930 CE, in use today; status living.

Parent: [`Vaii`](#vaii) Vai, link **stimulus**.
Source: L2/09-326; Tuchscherer & Hair 2002. Devised in the 1930s by Gbili; stimulated by the syllabic organisation of Vai.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Krai

**Kirat Rai**. Abugida, written left to right. First attested 1925 CE, in use today; status living.

Parent: [`Limb`](#limb) Limbu through Old Kirat lipi, link **contested**.
Source: L2/22-043R. Derived from the Old Kirat script from which Limbu also comes; Sumhung Lipi of the 1920s, redesigned 2000.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+16D40.

### Kthi

**Kaithi** (𑂍𑂶𑂟𑂲). Abugida, written left to right. First attested 1550 CE, last used 1950 CE; status historical.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Nagari, link **attested**.
Source: Pandey, Unicode N3389. Kaithi and Devanagari are siblings within the Nagari family.
Children: [`Sylo`](#sylo).

Recorded as a further script for 8 languages, the main script for none.
Unicode: encoded since version 5.2, block from U+11080.

### Lana

**Tai Tham** (อักษรธรรมล้านนา). Abugida, written left to right. First attested 1376 CE, in use today; status living.

Parent: [`Mymr`](#mymr) Myanmar through Old Mon, link **attested**.
Source: Apiradee & Grabowsky 2024. Developed from the Mon script of Hariphunchai; earliest evidence 1376.
Children: [`Talu`](#talu).

Languages written mainly in it: 5. Largest: Northern Thai (6,029,500 speakers), Khün (120,000 speakers), Samtao, Phuan, Tai Ya. Also recorded as a further script for 2 more.
Unicode: encoded since version 5.2, block from U+1A20.

### Laoo

**Lao** (ອັກສອນລາວ). Abugida, written left to right. First attested 1494 CE, in use today; status living.

Parent: [`Thai`](#thai) Thai through Fakkham, link **attested**.
Source: Lorrillard, 'Scripts and history: the case of Laos'. Fakkham the prototype of Lao script; no direct Khmer transmission; first dated stele 1494 or 1497.
Children: [`Hmng`](#hmng).

Languages written mainly in it: 14. Largest: Lao (5,225,552 speakers), Khmu (480,000 speakers), Kriang-Khlor, Western Katu, Upper Ta'oih. Also recorded as a further script for 14 more.
Unicode: encoded since version 1.1, block from U+0E81.

### Latf

**Latin** (Fraktur). Variant, written left to right. First attested 1150 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **variant**.

Languages written mainly in it: 1. Middle Low German. Also recorded as a further script for 2 more.
Unicode: encoded since version 1.1.

### Latg

**Latin**. Variant, written left to right. First attested 700 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **variant**.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 1.1.

### Latn

**Latin**. Alphabet, written left to right. First attested 600 BCE, in use today; status living.

Parent: [`Ital`](#ital) Old Italic, link **attested**.
Source: Rocca & Sarullo 2007; CNR 2011 on the Praeneste fibula; Gippert 2020. Lapis Niger and Lapis Satricanus 6th c. BCE; the Praeneste fibula (7th c.) is still argued over.
Children: [`Ogam`](#ogam), [`Latg`](#latg), [`Latf`](#latf), [`Cher`](#cher), [`Brai`](#brai), [`Vaii`](#vaii), [`Cans`](#cans), [`Moon`](#moon), [`Dsrt`](#dsrt), [`Dupl`](#dupl), [`Visp`](#visp), [`Pauc`](#pauc), [`Wole`](#wole), [`Afak`](#afak), [`Lisu`](#lisu), [`Sara`](#sara), [`Medf`](#medf), [`Sunu`](#sunu), [`Wara`](#wara), [`Shaw`](#shaw), [`Sgnw`](#sgnw), [`Piqd`](#piqd), [`Mroo`](#mroo), [`Onao`](#onao), [`Chis`](#chis), [`Tnsa`](#tnsa), [`Zsye`](#zsye), [`Wcho`](#wcho), [`Osge`](#osge).

Languages written mainly in it: 3,652. Largest: English (753,359,540 speakers), Spanish (485,000,000 speakers), Portuguese (254,300,000 speakers), French (208,157,220 speakers), Standard Indonesian (198,996,550 speakers). Also recorded as a further script for 212 more.
Unicode: encoded since version 1.1, block from U+0041.

### Leke

**Leke**. Abugida, written left to right. First attested 1844 CE, in use today; status living.

Parent: [`Mymr`](#mymr) Myanmar, link **contested**.
Source: Kato 2026 (user.keio.ac.jp/~kato/LekeScript.pdf); Unicode N4438. Created mid-19th c. with the Leke religion; some borrowing from Old Mon and Burmese.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Lepc

**Lepcha** (ᰕᰧᰵᰶᰙᰳ). Abugida, written left to right. First attested 1720 CE, in use today; status living.

Parent: [`Tibt`](#tibt) Tibetan, link **attested**.
Source: Unicode ch.13; Everson, Unicode N2947. Based directly on Tibetan; invented around 1720.
Children: [`Limb`](#limb).

Languages written mainly in it: 1. Lepcha (75,000 speakers).
Unicode: encoded since version 5.1, block from U+1C00.

### Limb

**Limbu** (ᤕᤰᤌᤢᤱ ᤐᤠᤴ). Abugida, written left to right. First attested 1850 CE, in use today; status living.

Parent: [`Lepc`](#lepc) Lepcha, link **contested**.
Source: Unicode ch.13; Hall, Unicode N4347. Oldest known writings collected in Darjeeling in the 1850s; 18th-c. Sirijanga origin is tradition.
Children: [`Krai`](#krai).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 4.0, block from U+1900.

### Lina

**Linear A**. Undeciphered, written left to right. First attested 1800 BCE, last used 1450 BCE; status undeciphered.

A root: no known parent among the registry's codes.
Source: Salgarella 2020, Aegean Linear Script(s), CUP. Linear A grew out of the Cretan hieroglyphic tradition, which has no ISO code.
Children: [`Cpmn`](#cpmn), [`Linb`](#linb).

Languages written mainly in it: 1. Minoan.
Unicode: encoded since version 7.0, block from U+10600.

### Linb

**Linear B**. Syllabary, written left to right. First attested 1400 BCE, last used 1200 BCE; status historical.

Parent: [`Lina`](#lina) Linear A, link **attested**.
Source: Olivier 2012, in Cline (ed.), Oxford Handbook of the Bronze Age Aegean. Knossos tablets 14th c. BCE on the compromise chronology; 1450 is the high date.

Languages written mainly in it: 1. Achaean Greek. Also recorded as a further script for 1 more.
Unicode: encoded since version 4.0, block from U+10000.

### Lisu

**Lisu**. Alphabet, written left to right. First attested 1915 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **attested**.
Source: Unicode N3317; Cook, L2/07-294. Sara Ba Thaw and James Fraser modified the shapes of Latin letters, 1908-1914, published 1915.

Languages written mainly in it: 1. Lisu. Also recorded as a further script for 3 more.
Unicode: encoded since version 5.2, block from U+A4D0.

### Loma

**Loma**. Syllabary, written left to right. First attested 1930 CE, in use today; status living.

Parent: [`Vaii`](#vaii) Vai, link **stimulus**.
Source: Unicode N3756 (L2/10-005). Devised in the 1930s by Wido Zobo; Vai stimulus, no shared letterforms.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Lyci

**Lycian**. Alphabet, written left to right. First attested 500 BCE, last used 300 BCE; status historical.

Parent: [`Grek`](#grek) Greek, link **attested**.
Source: Adiego 2018; Unicode ch.8. Both the letter shapes and the chronology point to a Greek origin; c.500 BCE.

Languages written mainly in it: 2. Largest: Milyan, Lycian A.
Unicode: encoded since version 5.1, block from U+10280.

### Lydi

**Lydian**. Alphabet, written right to left. First attested 700 BCE, last used 300 BCE; status historical.

Parent: [`Grek`](#grek) Greek, link **attested**.
Source: Adiego 2018; Unicode ch.8. Greek or Phrygian model, an open question; late 8th or early 7th c. BCE; mostly right to left.

Languages written mainly in it: 1. Lydian.
Unicode: encoded since version 5.1, block from U+10920.

### Mahj

**Mahajani** (महाजनी). Alphabet, written left to right. First attested 1600 CE, last used 1950 CE; status historical.

Parent: [`Deva`](#deva) Devanagari through Landa, link **contested**.
Source: Pandey, Unicode N4126. Often called a derivative of Kaithi or Devanagari; structure resembles Landa.

Recorded as a further script for 3 languages, the main script for none.
Unicode: encoded since version 7.0, block from U+11150.

### Maka

**Makasar**. Abugida, written left to right. First attested 1600 CE, last used 1900 CE; status historical.

Parent: [`Rjng`](#rjng) Rejang, link **contested**.
Source: Pandey, L2/15-233; Unicode ch.17. Closest relative Rejang; no evolutionary relationship with Buginese.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 11.0, block from U+11EE0.

### Mand

**Mandaic, Mandaean**. Alphabet, written right to left. First attested 350 CE, in use today; status living.

Parent: [`Elym`](#elym) Elymaic, link **contested**.
Source: Encyclopaedia Iranica 'Mandaeans v'; Haberl 2006, BASOR. Based on the script of the Elymaean rock inscriptions; Unicode also allows Parthian chancery; bowls 4th-7th c..

Languages written mainly in it: 2. Largest: Classical Mandaic, Neo-Mandaic.
Unicode: encoded since version 6.0, block from U+0840.

### Mani

**Manichaean**. Abjad, written right to left. First attested 250 CE, last used 1000 CE; status historical.

Parent: [`Syrc`](#syrc) Syriac, link **contested**.
Source: Unicode ch.10; Everson, Unicode N2544 and N3486. Based on Estrangela Syriac and Palmyrene; also described as a sister of Syriac out of Aramaic.

Recorded as a further script for 5 languages, the main script for none.
Unicode: encoded since version 7.0, block from U+10AC0.

### Marc

**Marchen**. Abugida, written left to right. First attested 1000 CE, in use today; status living.

Parent: [`Tibt`](#tibt) Tibetan, link **contested**.
Source: West, Unicode N4491; Unicode ch.14. Quite different from Tibetan and Lantsa; no early texts known, likely a much more recent innovation; widely used in modern Bon literature and inscriptions.

Languages written mainly in it: 1. Zhangzhung. Also recorded as a further script for 1 more.
Unicode: encoded since version 9.0, block from U+11C70.

### Maya

**Mayan hieroglyphs**. Logographic, written left to right. First attested 300 BCE, last used 1600 CE; status historical.

A root: no known parent among the registry's codes.

Languages written mainly in it: 1. Epigraphic Mayan.
Unicode: not encoded, so no font can show it.

### Medf

**Medefaidrin** (𖹝𖹰𖹯𖹼𖹫 𖹚𖹬𖹾𖹠𖹯). Alphabet, written left to right. First attested 1927 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: L2/16-101R. Strong influence of English orthography, capital and small letters; revealed 1927.

Languages written mainly in it: 1. Medefidrin.
Unicode: encoded since version 11.0, block from U+16E40.

### Mend

**Mende Kikakui**. Syllabary, written right to left. First attested 1917 CE, in use today; status living.

Parent: [`Vaii`](#vaii) Vai, link **stimulus**.
Source: Unicode N4133 (L2/11-301). Syllabic blueprint unquestionably influenced by Vai; right to left.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+1E800.

### Merc

**Meroitic Cursive**. Alphabet, written right to left. First attested 220 BCE, last used 400 CE; status historical.

Parent: [`Egyd`](#egyd) Egyptian demotic, link **attested**.
Source: Rilly, UCLA Encyclopedia of Egyptology; Priese 1973. Developed from Demotic; earliest datable object a sistrum handle naming Arnekhamani, c.220 BCE.

Languages written mainly in it: 1. Meroitic.
Unicode: encoded since version 6.1, block from U+109A0.

### Mero

**Meroitic Hieroglyphs**. Alphabet, written right to left. First attested 150 BCE, last used 400 CE; status historical.

Parent: [`Egyp`](#egyp) Egyptian hieroglyphs, link **attested**.
Source: Rilly, UCLA Encyclopedia of Egyptology. Created under Taneyidamani, first half of the 2nd c. BCE, from Egyptian hieroglyphs with new values.

Languages a source records it for: none.
Unicode: encoded since version 6.1, block from U+10980.

### Mlym

**Malayalam** (മലയാളലിപി). Abugida, written left to right. First attested 1100 CE, in use today; status living.

Parent: [`Gran`](#gran) Grantha through Chola Grantha, link **attested**.
Source: ICANN Malayalam LGR 2019. The 830 Vazhappalli plates are in Vatteluttu; Malayalam script texts from about the 12th c..

Languages written mainly in it: 11. Largest: Malayalam (37,100,000 speakers), Aranadan (200 speakers), Attapady Kurumba, Muduga, Kanikkaran. Also recorded as a further script for 7 more.
Unicode: encoded since version 1.1, block from U+0D00.

### Modi

**Modi, Moḍī**. Abugida, written left to right. First attested 1600 CE, last used 1950 CE; status historical.

Parent: [`Deva`](#deva) Devanagari through Nagari, link **attested**.
Source: Pandey, Unicode N4034; Salomon 1998 n.116; Unicode ch.15; Hindustan Times 2025. A Nagari-family script for continuous writing; earliest extant document early 17th c.; formally discontinued in the 1950s; taught again for reading archives.
Children: [`Gong`](#gong).

Languages written mainly in it: 1. Old Marathi. Also recorded as a further script for 3 more.
Unicode: encoded since version 7.0, block from U+11600.

### Mong

**Mongolian** (ᠮᠣᠩᠭᠣᠯ ᠪᠢᠴᠢᠭ᠌). Alphabet, written top to bottom. First attested 1224 CE, in use today; status living.

Parent: [`Ougr`](#ougr) Old Uyghur, link **attested**.
Source: Unicode ch.13; Brose 2005. Adopted 1204 by tradition; earliest surviving text the Stele of Yisungge, c.1224-1225.

Languages written mainly in it: 5. Largest: China Buriat (65,000 speakers), Xibe (30,000 speakers), Manchu (20 speakers), Middle Mongol, Peripheral Mongolian. Also recorded as a further script for 9 more.
Unicode: encoded since version 3.0, block from U+1800.

### Moon

**Moon**. Alphabet, written boustrophedon. First attested 1845 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **attested**.
Source: Everson, Unicode N4128 (L2/11-280); Perkins School for the Blind. Embossed symbols simplified from Latin letters; developed by William Moon in 1845.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Mroo

**Mro, Mru**. Alphabet, written left to right. First attested 1980 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Unicode N3589. A messianic script of the 1980s with no genetic relationship to existing scripts.

Languages written mainly in it: 1. Mru.
Unicode: encoded since version 7.0, block from U+16A40.

### Mtei

**Meitei Mayek** (ꯃꯩꯇꯩ ꯃꯌꯦꯛ). Abugida, written left to right. First attested 1100 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **contested**.
Source: Everson, Unicode N3158. Earliest use dated 11th-12th c., from the Tibetan group; Tomba 1993 calls the old documents forgeries.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 5.2, block from U+AAE0.

### Mult

**Multani** (ਮੁਲਤਾਨੀ ਲਿਪੀ). Abjad, written left to right. First attested 1750 CE, last used 1950 CE; status historical.

Parent: [`Shrd`](#shrd) Sharada, Śāradā through Landa, link **attested**.
Source: Unicode ch.15. Related to Gurmukhi; used in the 19th and 20th c.; earlier date unsourced.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 8.0, block from U+11280.

### Mymr

**Myanmar** (မွန်မြန်မာအက္ခရာ). Abugida, written left to right. First attested 1113 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Old Mon or Pyu, link **attested**.
Source: Unicode ch.16; Aung-Thwin 2005. First inscription 11th c. (Myazedi c.1113); Mon source in Unicode, Pyu argued by Aung-Thwin.
Children: [`Ahom`](#ahom), [`Lana`](#lana), [`Tale`](#tale), [`Cakm`](#cakm), [`Leke`](#leke), [`Kali`](#kali).

Languages written mainly in it: 31. Largest: Burmese (32,900,000 speakers), S'gaw Karen (4,000,000 speakers), Shan (3,000,000 speakers), Pa'o Karen (860,000 speakers), Mon (850,000 speakers). Also recorded as a further script for 8 more.
Unicode: encoded since version 3.0, block from U+1000.

### Nagm

**Nag Mundari** (𞓗𞓕𞓨𞓚 𞓧𞓟𞓨𞓡𞓚). Alphabet, written left to right. First attested 1950 CE, in use today; status living.

Parent: [`Olck`](#olck) Ol Chiki, link **stimulus**.
Source: L2/21-031R; Unicode ch.13. Organisation modelled on Ol Chiki; developed from the 1950s.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 15.0, block from U+1E4D0.

### Nand

**Nandinagari** (𑧁𑧞𑦿𑧒𑧁𑧑𑦰𑧈𑧓). Abugida, written left to right. First attested 1100 CE, last used 1800 CE; status historical.

Parent: [`Deva`](#deva) Devanagari through Nagari, link **attested**.
Source: Pandey, L2/17-162. A sister of Devanagari within the Nagari family, 11th c..

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 12.0, block from U+119A0.

### Narb

**Old North Arabian**. Abjad, written in more than one direction. First attested 600 BCE, last used 400 CE; status historical.

Parent: [`Psin`](#psin) Proto-Sinaitic, link **attested**.
Source: Al-Jallad 2015, An Outline of the Grammar of the Safaitic Inscriptions; Unicode ch.10. Shares an ancestor with Ancient South Arabian rather than descending from it.

Languages written mainly in it: 1. Ancient North Arabian.
Unicode: encoded since version 7.0, block from U+10A80.

### Nbat

**Nabataean**. Abjad, written right to left. First attested 95 BCE, last used 400 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Naveh, The Nabataeans. Elusa inscription early 2nd c. BCE not yet Nabataean in form; Aslah inscription, Petra, 95 BCE.
Children: [`Arab`](#arab).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+10880.

### Newa

**Newa, Newar, Newari, Nepāla lipi** (𑐣𑐾𑐥𑐵𑐮 𑐮𑐶𑐥𑐶). Abugida, written left to right. First attested 908 CE, in use today; status living.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Kutila, link **attested**.
Source: Pandey, Unicode N4184; Unicode ch.13. A distinct Newar script from the 10th c.; Lankavatara Sutra manuscript dated 908.
Children: [`Ranj`](#ranj).

Recorded as a further script for 5 languages, the main script for none.
Unicode: encoded since version 9.0, block from U+11400.

### Nkdb

**Naxi Dongba**. Semasiographic, written left to right. First attested 1200 CE, in use today; status living.

A root: no known parent among the registry's codes.
Source: Poupard 2019, Written Language & Literacy; Yang & He 2024. Earliest dated manuscripts 13th c.; independence hedged, created amid Chinese and Tibetan literacy.
Children: [`Nkgb`](#nkgb).

Recorded as a further script for 2 languages, the main script for none.
Unicode: not encoded, so no font can show it.

### Nkgb

**Naxi Geba**. Syllabary, written left to right. First attested 1619 CE, in use today; status living.

Parent: [`Nkdb`](#nkdb) Naxi Dongba, link **contested**.
Source: Friedrich 2023; Unicode N3442. Some characters from Dongba, some from Yi, Tibetan and Chinese; a dated stele of 1619.

Recorded as a further script for 2 languages, the main script for none.
Unicode: not encoded, so no font can show it.

### Nkoo

**N’Ko** (ߒߞߏ). Alphabet, written right to left. First attested 1949 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: Unicode ch.19; Oyler 2005; Wyrod 2019, African Studies Review. Kante tried Arabic ajami and Latin before devising N'Ko in 1949; direction and joining as Arabic.

Recorded as a further script for 4 languages, the main script for none.
Unicode: encoded since version 5.0, block from U+07C0.

### Nshu

**Nüshu** (女書). Syllabary, written top to bottom. First attested 1850 CE, in use today; status revived.

Parent: [`Hani`](#hani) Han, link **attested**.
Source: UNESCO 2018; Endo, Unicode N4626; UNESCO Courier 2018; Unicode ch.18. No securely dated object before the 19th c.; claims of a Song origin have no object behind them; very few fluent writers left by the late 20th c.; revived by local and national authorities.

Languages a source records it for: none.
Unicode: encoded since version 10.0, block from U+16FE1.

### Ogam

**Ogham** (᚛ᚑᚌᚐᚋ᚜). Alphabet, written in more than one direction. First attested 350 CE, last used 600 CE; status historical.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: McManus 1991, A Guide to Ogam. The most likely immediate source is Latin; Greek and runes have had adherents.

Languages written mainly in it: 1. Pictish. Also recorded as a further script for 7 more.
Unicode: encoded since version 3.0, block from U+1680.

### Olck

**Ol Chiki** (ᱚᱞ ᱪᱤᱠᱤ). Alphabet, written left to right. First attested 1925 CE, in use today; status living.

Parent: [`Orya`](#orya) Oriya, link **invented**.
Source: Unicode N2505; Zide 1996; Wikipedia 'Raghunath Murmu' (secondary). Alphabetic, sharing none of the syllabic properties of Indic scripts; shapes from familiar objects; Murmu was schooled in Odia, so it hangs under Odia (Santali was also written in Latin, Devanagari, Bengali).
Children: [`Nagm`](#nagm).

Languages written mainly in it: 1. Santali (7,200,000 speakers).
Unicode: encoded since version 5.1, block from U+1C50.

### Onao

**Ol Onal** (𞗘𞗪𞗢𞗑𞗜𞗥𞗰). Alphabet, written left to right. First attested 1981 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: L2/22-151. Invented by Mahendra Nath Sardar between 1981 and 1992; Bhumij was written in Odia, Bengali, Devanagari and Latin.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+1E5D0.

### Orkh

**Old Turkic, Orkhon Runic**. Alphabet, written right to left. First attested 700 CE, last used 1000 CE; status historical.

Parent: [`Sogd`](#sogd) Sogdian, link **contested**.
Source: Everson et al., L2/08-071R2; Shcherbak 1996, Etudes mongoles 27. Aramaic via Iranian scripts is mainstream; a direct Sogdian link is denied by Rona-Tas.
Children: [`Hung`](#hung).

Languages written mainly in it: 1. Old Turkish. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.2, block from U+10C00.

### Orya

**Oriya** (ଓଡ଼ିଆ ଲିପି). Abugida, written left to right. First attested 1300 CE, in use today; status living.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Gaudi, link **attested**.
Source: Salomon 1998 3.4.2. Early Oriya texts in Gaudi (Urajam 1051); a distinct Oriya script from the 14th c., of composite origin.
Children: [`Olck`](#olck).

Languages written mainly in it: 15. Largest: Odia (34,500,000 speakers), Sambalpuri (2,630,000 speakers), Pengo (350,000 speakers), Juang (30,875 speakers), Bondo (9,000 speakers). Also recorded as a further script for 11 more.
Unicode: encoded since version 1.1, block from U+0B01.

### Osge

**Osage**. Alphabet, written left to right. First attested 2006 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **attested**.
Source: Everson, Lookout & Pratt, Unicode N4587. Letters in origin modifications or fusions of Latin letters, designed by 2006, revised 2012-2014.

Languages written mainly in it: 1. Osage.
Unicode: encoded since version 9.0, block from U+104B0.

### Osma

**Osmanya** (𐒍𐒖𐒇𐒂𐒖 𐒋𐒘𐒈𐒑𐒛𐒒𐒕𐒖). Alphabet, written left to right. First attested 1920 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: Unicode ch.19; Tosco, AAP, after Cerulli 1932. Letter order follows Arabic; Latin gave only the direction; no Ethiopic role.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 4.0, block from U+10480.

### Ougr

**Old Uyghur**. Abjad, written top to bottom. First attested 800 CE, last used 1800 CE; status historical.

Parent: [`Sogd`](#sogd) Sogdian, link **attested**.
Source: L2/20-003 (Old Uyghur); Unicode ch.14. Believed to derive from Sogdian cursive in the 8th or 9th c..
Children: [`Kits`](#kits), [`Mong`](#mong).

Languages written mainly in it: 1. Old Turkic. Also recorded as a further script for 1 more.
Unicode: encoded since version 14.0, block from U+10F70.

### Palm

**Palmyrene**. Abjad, written right to left. First attested 44 BCE, last used 300 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Unicode ch.10. Inscriptions from 44 BCE to about 280 CE.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+10860.

### Pauc

**Pau Cin Hau**. Alphabet, written left to right. First attested 1902 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: L2/11-104R. No genetic relationship with any other writing system; revealed 1902, alphabetic form 1931.

Languages written mainly in it: 1. Tedim Chin.
Unicode: encoded since version 7.0, block from U+11AC0.

### Pcun

**Proto-Cuneiform**. Logographic, written in more than one direction. First attested 3300 BCE, last used 2900 BCE; status historical.

A root: no known parent among the registry's codes.
Children: [`Pelm`](#pelm), [`Xsux`](#xsux).

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Pelm

**Proto-Elamite**. Undeciphered, written right to left. First attested 3050 BCE, last used 2900 BCE; status undeciphered.

Parent: [`Pcun`](#pcun) Proto-Cuneiform, link **stimulus**.
Source: Dahl 2005, CDLJ 2005:3; Englund, Encyclopaedia Iranica 'Elam iii'. Unquestionably inspired by proto-cuneiform; numerical systems borrowed, signs largely new.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Perm

**Old Permic**. Alphabet, written left to right. First attested 1372 CE, last used 1700 CE; status historical.

Parent: [`Cyrl`](#cyrl) Cyrillic, link **stimulus**.
Source: Everson, Unicode N4263. Modelled on Greek and Cyrillic, with many glyphs taken from tamga signs.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+10350.

### Phag

**Phags-pa**. Abugida, written top to bottom. First attested 1269 CE, last used 1400 CE; status historical.

Parent: [`Tibt`](#tibt) Tibetan, link **attested**.
Source: Unicode ch.14. Devised for Khubilai and promulgated in 1269; similar to Tibetan.
Children: [`Hang`](#hang).

Recorded as a further script for 4 languages, the main script for none.
Unicode: encoded since version 5.0, block from U+A840.

### Phli

**Inscriptional Pahlavi**. Abjad, written right to left. First attested 224 CE, last used 900 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Humbach, Encyclopaedia Iranica 'Epigraphy i'; Rezakhani 2016. Sasanian inscriptions from 224 CE; descent through the Persis coin script is denied by Rezakhani.
Children: [`Phlp`](#phlp), [`Phlv`](#phlv).

Languages written mainly in it: 1. Pahlavi.
Unicode: encoded since version 5.2, block from U+10B60.

### Phlp

**Psalter Pahlavi**. Abjad, written right to left. First attested 600 CE, last used 800 CE; status historical.

Parent: [`Phli`](#phli) Inscriptional Pahlavi, link **attested**.
Source: Encyclopaedia Iranica 'Pahlavi Psalter'; Unicode ch.10. 6th or 7th c. CE, after 552; more archaic than Book Pahlavi.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+10B80.

### Phlv

**Book Pahlavi**. Abjad, written right to left. First attested 619 CE, last used 1100 CE; status historical.

Parent: [`Phli`](#phli) Inscriptional Pahlavi, link **attested**.
Source: Hintze 2014, Kratylos; Cereti. Earliest dated witnesses the Elephantine papyri, 619-629 CE; the 4th-c. sarcophagus anchor is Islamic-period.
Children: [`Avst`](#avst).

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Phnx

**Phoenician**. Abjad, written right to left. First attested 1000 BCE, last used 100 CE; status historical.

Parent: [`Psin`](#psin) Proto-Sinaitic through Proto-Canaanite, link **attested**.
Source: Unicode ch.10; Ahiram sarcophagus, KAI 1. First long text the Ahiram sarcophagus, c.1000 BCE on palaeography; its date is disputed.
Children: [`Armi`](#armi), [`Grek`](#grek), [`Sidt`](#sidt), [`Tfng`](#tfng), [`Samr`](#samr).

Languages written mainly in it: 3. Largest: Old Aramaic-Sam'alian, Punic, Phoenician. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.0, block from U+10900.

### Piqd

**Klingon** (). Alphabet, written left to right. First attested 1979 CE, in use today; status fictional.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: L2/20-181. Built on ten characters designed for Star Trek: The Motion Picture, 1979.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Plrd

**Miao**. Syllabary, written left to right. First attested 1904 CE, in use today; status living.

Parent: [`Cans`](#cans) Unified Canadian Aboriginal Syllabics, link **stimulus**.
Source: Unicode N3789 (L2/10-093); Lewis & Dorais 2003. Structure adopted from Cree syllabics, with Latin, shorthand and Miao signs.

Languages written mainly in it: 10. Largest: Diandongbei-Large Flowery Miao, Gha-mu, Lipo, Biyo, Kaduo. Also recorded as a further script for 4 more.
Unicode: encoded since version 6.1, block from U+16F00.

### Prti

**Inscriptional Parthian**. Abjad, written right to left. First attested 89 BCE, last used 250 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Skjaervo, Encyclopaedia Iranica 'Iran vi.3'; MacKenzie, 'Dates and dating'. Nisa ostraca of the 1st c. BCE, one dated 89 BCE.

Languages written mainly in it: 1. Parthian.
Unicode: encoded since version 5.2, block from U+10B40.

### Psin

**Proto-Sinaitic**. Abjad, written in more than one direction. First attested 1900 BCE, last used 1400 BCE; status historical.

Parent: [`Egyp`](#egyp) Egyptian hieroglyphs, link **attested**.
Source: L2/19-299 (Proto-Sinaitic). Most scholars agree it derives from Egyptian hieroglyphs; first attested 19th c. BCE (Wadi el-Hol).
Children: [`Ugar`](#ugar), [`Phnx`](#phnx), [`Sarb`](#sarb), [`Narb`](#narb).

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Ranj

**Ranjana**. Abugida, written left to right. First attested 1099 CE, in use today; status living.

Parent: [`Newa`](#newa) Newa, Newar, Newari, Nepāla lipi, link **attested**.
Source: Pandey, Unicode N4184, after Malla 1981. Developed from the Newar (pacumola) model; first in Nepal in 1099.
Children: [`Soyo`](#soyo).

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Rjng

**Rejang** (ꥆꤰ꥓ꤼꤽ ꤽꥍꤺꥏ). Abugida, written left to right. First attested 1750 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi, link **attested**.
Source: Everson, Unicode N3096. First attested about the mid-18th c..
Children: [`Maka`](#maka).

Languages written mainly in it: 1. Lampung Nyo. Also recorded as a further script for 4 more.
Unicode: encoded since version 5.1, block from U+A930.

### Rohg

**Hanifi Rohingya** (𐴌𐴟𐴇𐴥𐴝𐴚𐴒𐴙𐴝 𐴇𐴝𐴕𐴞𐴉𐴞 𐴓𐴠𐴑𐴤𐴝). Alphabet, written right to left. First attested 1980 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: Pandey, L2/16-311. Influenced by Arabic but a modern construction with no direct genetic affiliation; finalised 1980.

Languages written mainly in it: 1. Rohingya (1,800,000 speakers).
Unicode: encoded since version 11.0, block from U+10D00.

### Roro

**Rongorongo**. Undeciphered, written boustrophedon. First attested 1864 CE, last used 1864 CE; status undeciphered.

A root: no known parent among the registry's codes.
Source: Ferrara et al. 2024, Scientific Reports 14:2794; Wieczorek et al. 2021, J. Island & Coastal Arch.. First recorded 1864 (Eyraud); stimulus from the 1770 Spanish annexation treaty is argued and unresolved.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Runr

**Runic** (ᚱᚢᚾᛟ). Alphabet, written in more than one direction. First attested 150 CE, last used 1500 CE; status historical.

Parent: [`Ital`](#ital) Old Italic, link **attested**.
Source: Unicode TN40; Looijenga 2003; Duwel 2008. Thought to come from North Italic; Vimose comb c.150-160; written in either direction.
Children: [`Cirt`](#cirt).

Languages written mainly in it: 2. Largest: Central East Middle German (2,000,000 speakers), Old Norse. Also recorded as a further script for 14 more.
Unicode: encoded since version 3.0, block from U+16A0.

### Samr

**Samaritan**. Abjad, written right to left. First attested 350 CE, in use today; status living.

Parent: [`Phnx`](#phnx) Phoenician through Paleo-Hebrew, link **contested**.
Source: Barag, in Cambridge History of Judaism; Langlois 2019. A conscious creation of the 4th c. CE; Cross and Purvis argued a Hasmonean branch of paleo-Hebrew.

Languages written mainly in it: 1. Samaritan. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.2, block from U+0800.

### Sara

**Sarati**. Alphabet, written left to right. First attested 1919 CE, in use today; status fictional.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Everson, Unicode N4013; Smith 2007, Parma Eldalamberon. Tolkien's first Elvish script, from 1919; the precursor of Tengwar.
Children: [`Teng`](#teng).

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Sarb

**Old South Arabian** (𐩣𐩯𐩬𐩵). Abjad, written boustrophedon. First attested 800 BCE, last used 600 CE; status historical.

Parent: [`Psin`](#psin) Proto-Sinaitic through Proto-Canaanite, link **contested**.
Source: Hasselbach, in The Semitic Languages; Sass. Split off a Proto-Canaanite variant before 1000 BCE; Sass derives it from Phoenician-type letters.
Children: [`Ethi`](#ethi).

Languages written mainly in it: 2. Largest: Hadrami, Sabaic.
Unicode: encoded since version 5.2, block from U+10A60.

### Saur

**Saurashtra** (ꢱꣃꢬꢵꢰ꣄ꢜ꣄ꢬ ꢂꢒ꣄ꢯꢬꢸꢥ꣄). Abugida, written left to right. First attested 1880 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **contested**.
Source: Everson & Krishnamoorty, L2/05-222R2 (Unicode N2969R2). 'of the Brahmic type'; its origin 'is not known' (Ucida, quoted there); reformed and cast in type by T. M. Rama Ray in the 1880s.

Languages written mainly in it: 1. Saurashtra (300,000 speakers).
Unicode: encoded since version 5.1, block from U+A880.

### Seal

**(Small) Seal** (小篆). Variant, written top to bottom. First attested 800 BCE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **variant**.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Sgnw

**SignWriting** (M547x535S10019454x474S10011478x465S2ea04483x501S2ea48461x509S29b0b514x500S15a0a511x471S1eb20523x486). Featural, written top to bottom. First attested 1974 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin through Sutton DanceWriting, link **invented**.
Source: Unicode N4342. Developed in 1974 by Valerie Sutton out of her DanceWriting.

Languages written mainly in it: 9. Largest: Brazilian Sign Language (3,000,000 speakers), British Sign Language (327,000 speakers), American Sign Language (250,000 speakers), Mexican Sign Language, German Sign Language.
Unicode: encoded since version 8.0, block from U+1D800.

### Shaw

**Shavian** (𐑖𐑱𐑝𐑾𐑯). Alphabet, written left to right. First attested 1960 CE, in use today; status constructed.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: University of Reading, Kingsley Read alphabet collection. A 48-character alphabet for English, shapes new, 1960.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 4.0, block from U+10450.

### Shrd

**Sharada, Śāradā** (𑆯𑆳𑆫𑆢𑆳). Abugida, written left to right. First attested 800 CE, last used 1900 CE; status historical.

Parent: [`Brah`](#brah) Brahmi through Kutila, link **attested**.
Source: Pandey, L2/08-200; Salomon 1998. Descended from Gupta through Kutila; Proto-Sarada from the 7th c., Sharada of Kashmir from the 8th.
Children: [`Khoj`](#khoj), [`Takr`](#takr), [`Sind`](#sind), [`Guru`](#guru), [`Mult`](#mult).

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 6.1, block from U+11180.

### Shui

**Shuishu**. Logographic, written right to left. First attested 1400 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **attested**.
Source: L2/14-243 (Shuishu proposal). About half the characters derive from Chinese in mirrored or inverted form.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Sidd

**Siddham, Siddhaṃ, Siddhamātṛkā** (𑖭𑖰𑖟𑖿𑖠𑖽). Abugida, written left to right. First attested 588 CE, last used 1200 CE; status historical.

Parent: [`Brah`](#brah) Brahmi through Gupta, link **attested**.
Source: Salomon 1998, Indian Epigraphy 2.2.5.4. Evolved out of the Gupta script in the late 6th c.; Bodh-Gaya inscription of Mahanaman, 588-589.
Children: [`Deva`](#deva), [`Newa`](#newa), [`Tirh`](#tirh), [`Orya`](#orya), [`Beng`](#beng), [`Kthi`](#kthi).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+11580.

### Sidt

**Sidetic**. Alphabet, written right to left. First attested 500 BCE, last used 300 BCE; status historical.

Parent: [`Phnx`](#phnx) Phoenician, link **contested**.
Source: Pandey, L2/23-019. Origins not clearly known; thought to develop from Phoenician in parallel with Greek.

Languages written mainly in it: 1. Sidetic.
Unicode: not encoded, so no font can show it.

### Sind

**Khudawadi, Sindhi** (खुदाबादी). Abugida, written left to right. First attested 1550 CE, last used 1910 CE; status historical.

Parent: [`Shrd`](#shrd) Sharada, Śāradā through Landa, link **attested**.
Source: Pandey, L2/11-022; Unicode ch.15. A Landa-based script related to Sharada; standard form published 1868; now obsolete; Bible Society printing continued past 1900.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+112B0.

### Sinh

**Sinhala** (සිංහල අක්ෂර මාලාව). Abugida, written left to right. First attested 200 BCE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **attested**.
Source: Unicode L2/10-312. Brahmi inscriptions of the 3rd-2nd c. BCE; later influenced by Grantha.

Languages written mainly in it: 2. Largest: Sinhala (15,300,000 speakers), Veddah (300 speakers). Also recorded as a further script for 3 more.
Unicode: encoded since version 3.0, block from U+0D81.

### Sogd

**Sogdian** (𐼼𐼇𐼄𐼌𐼊𐼋). Abjad, written in more than one direction. First attested 600 CE, last used 1400 CE; status historical.

Parent: [`Sogo`](#sogo) Old Sogdian, link **attested**.
Source: Unicode ch.14. Derived from Old Sogdian, used from the 7th to the 14th c. CE.
Children: [`Orkh`](#orkh), [`Ougr`](#ougr).

Languages written mainly in it: 1. Sogdian. Also recorded as a further script for 2 more.
Unicode: encoded since version 11.0, block from U+10F30.

### Sogo

**Old Sogdian**. Abjad, written right to left. First attested 313 CE, last used 400 CE; status historical.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Encyclopaedia Iranica 'Ancient Letters'; Unicode ch.14. Ancient Letters securely dated 312-313 CE; the Kultobe inscriptions possibly earlier.
Children: [`Sogd`](#sogd).

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 11.0, block from U+10F00.

### Sora

**Sora Sompeng** (𑃐𑃦𑃝𑃗 𑃐𑃦𑃖𑃛𑃣𑃗). Abugida, written left to right. First attested 1936 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi, link **stimulus**.
Source: Everson, Unicode N3647R (L2/09-189R). Of the Brahmic type, consonants with an inherent vowel; revealed 18 June 1936.

Languages written mainly in it: 1. Sora (410,000 speakers).
Unicode: encoded since version 6.1, block from U+110D0.

### Soyo

**Soyombo** (𑪞𑪞). Abugida, written left to right. First attested 1686 CE, last used 1800 CE; status historical.

Parent: [`Ranj`](#ranj) Ranjana through Lantsa, link **attested**.
Source: Unicode ch.14; Unicode N1855. Created in 1686 by Zanabazar on the model of Lantsa, with Tibetan order and shapes.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 10.0, block from U+11A50.

### Sund

**Sundanese** (ᮃᮊ᮪ᮞᮛ ᮞᮥᮔ᮪ᮓ). Abugida, written left to right. First attested 1400 CE, in use today; status living.

Parent: [`Kawi`](#kawi) Kawi through Pallava, link **contested**.
Source: Unicode ch.17; Pandey, L2/12-125. Unicode derives Old Sundanese from Pallawa, Pandey from Kawi; used 14th-18th c..

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 5.1, block from U+1B80.

### Sunu

**Sunuwar** (𑯆𑯑𑯃̃𑯌 𑯎𑯄𑯂𑯒𑯂). Alphabet, written left to right. First attested 1942 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: Pandey, L2/21-157. A linear alphabet whose structure is modelled upon the Latin alphabet.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+11BC0.

### Sylo

**Syloti Nagri** (ꠎꠟꠣꠟꠣꠛꠣꠖꠤ ꠢꠞꠚ (Perso-Arabic origin)). Abugida, written left to right. First attested 1500 CE, in use today; status living.

Parent: [`Kthi`](#kthi) Kaithi, link **attested**.
Source: L2/02-388 (Syloti Nagri); Pandey, Unicode N3389. A form of Kaithi; earliest manuscript dated 1549 or 1774, exact origin unknown.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 4.1, block from U+A800.

### Syrc

**Syriac** (ܐܠܦ ܒܝܬ ܣܘܪܝܝܐ). Abjad, written right to left. First attested 6 CE, in use today; status living.

Parent: [`Armi`](#armi) Imperial Aramaic, link **attested**.
Source: Healey 2011, Hugoye; Drijvers & Healey As55. The earliest dated Syriac inscription is the Birecik inscription of 6 CE.
Children: [`Syre`](#syre), [`Mani`](#mani), [`Syrj`](#syrj), [`Syrn`](#syrn), [`Yezi`](#yezi).

Languages written mainly in it: 8. Largest: Classical Syriac (575,000 speakers), Assyrian Neo-Aramaic (232,300 speakers), Western Neo-Aramaic, Chaldean Neo-Aramaic, Mlahsô. Also recorded as a further script for 4 more.
Unicode: encoded since version 3.0, block from U+0700.

### Syre

**Syriac** (ܐܣܛܪܢܓܠܐ). Variant, written right to left. First attested 100 CE, in use today; status living.

Parent: [`Syrc`](#syrc) Syriac, link **variant**.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 3.0.

### Syrj

**Syriac** (ܣܶܪܛܳܐ). Variant, written right to left. First attested 400 CE, in use today; status living.

Parent: [`Syrc`](#syrc) Syriac, link **variant**.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 3.0.

### Syrn

**Syriac** (ܡܲܕ݂ܢܚܵܝܵܐ). Variant, written right to left. First attested 400 CE, in use today; status living.

Parent: [`Syrc`](#syrc) Syriac, link **variant**.

Languages a source records it for: none.
Unicode: encoded since version 3.0.

### Tagb

**Tagbanwa** (ᝦᝪᝯ). Abugida, written left to right. First attested 1600 CE, in use today; status living.

Parent: [`Tglg`](#tglg) Tagalog, link **contested**.
Source: Unicode ch.17; Miller, Unicode Technical Note 35. Related to Tagalog but may not descend from it; within the range of 17th-c. Philippine handwriting.

Languages written mainly in it: 1. Calamian Tagbanwa. Also recorded as a further script for 2 more.
Unicode: encoded since version 3.2, block from U+1760.

### Takr

**Takri, Ṭākrī, Ṭāṅkrī** (𑚔𑚭𑚊𑚤𑚯). Abugida, written left to right. First attested 1500 CE, last used 1950 CE; status historical.

Parent: [`Shrd`](#shrd) Sharada, Śāradā through Devasesha, link **attested**.
Source: Pandey, L2/09-424; Unicode ch.15. From Sharada through Devasesha (14th c.), differentiated in the 16th c.; official in princely states until the mid-20th c.; revival efforts only.
Children: [`Dogr`](#dogr).

Languages written mainly in it: 1. Hinduri. Also recorded as a further script for 14 more.
Unicode: encoded since version 6.1, block from U+11680.

### Tale

**Tai Le** (ᥘᥤᥐ ᥖᥭᥰ ᥘᥫᥴ). Abugida, written left to right. First attested 1407 CE, in use today; status living.

Parent: [`Mymr`](#mymr) Myanmar, link **attested**.
Source: Daniels 2012, Journal of Southeast Asian Studies. The Tay borrowed heavily from Burmese before the 15th c.; a Ming scroll of 1407.

Languages written mainly in it: 1. Tai Nüa (650,000 speakers). Also recorded as a further script for 4 more.
Unicode: encoded since version 4.0, block from U+1950.

### Talu

**New Tai Lue** (ᦟᦲᧅᦷᦎᦺᦑᦟᦹᧉ). Abugida, written left to right. First attested 1955 CE, in use today; status living.

Parent: [`Lana`](#lana) Tai Tham, link **attested**.
Source: Grabowsky, Manuscript Cultures 3. A simplification of Tai Tham, officially introduced 1955.

Languages written mainly in it: 1. Lü (700,000 speakers).
Unicode: encoded since version 4.1, block from U+1980.

### Taml

**Tamil** (தமிழ்). Abugida, written left to right. First attested 600 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Pallava, link **attested**.
Source: Francis 2024. A new alphabet for Tamil around the start of the 7th c., a sister of Grantha, not from Vatteluttu.

Languages written mainly in it: 12. Largest: Tamil (75,000,000 speakers), Badaga (134,000 speakers), Kurumba, Kannada, Kota (India), Toda. Also recorded as a further script for 5 more.
Unicode: encoded since version 1.1, block from U+0B82.

### Tang

**Tangut** (𗼇𗟲). Logographic, written left to right. First attested 1036 CE, last used 1500 CE; status historical.

Parent: [`Hani`](#hani) Han, link **stimulus**.
Source: Cook, Unicode N3297. Invented by decree with Chinese writing as conceptual model; no shared characters.

Languages written mainly in it: 1. Tangut.
Unicode: encoded since version 9.0, block from U+16FE0.

### Tavt

**Tai Viet**. Abugida, written left to right. First attested 1500 CE, in use today; status living.

Parent: [`Thai`](#thai) Thai through Sukhothai, link **attested**.
Source: Thai Research Fund report PDG4810005. Tai Dam script a derivative of Sukhothai script, arriving around the 16th c..

Languages written mainly in it: 3. Largest: Tai Dam (760,000 speakers), Tai Daeng-Meuay (650,000 speakers), Thai Song. Also recorded as a further script for 2 more.
Unicode: encoded since version 5.2, block from U+AA80.

### Tayo

**Tai Yo**. Abugida, written top to bottom. First attested 1500 CE, in use today; status living.

Parent: [`Thai`](#thai) Thai, link **contested**.
Source: L2/22-289; Ferlus 2006; Unicode ch.16. A common origin with the Tai Dam group; written top to bottom in right-to-left columns; teaching and learning supported by local government and teachers.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Telu

**Telugu** (తెలుగు లిపి). Abugida, written left to right. First attested 600 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Kadamba, link **attested**.
Source: Mahadevan, Frontline. Kalamalla inscription of the Renati Cholas, end of the 6th c..

Languages written mainly in it: 13. Largest: Telugu (82,000,000 speakers), Lambadi (6,000,000 speakers), Konda-Dora (20,000 speakers), Southeastern Kolami, Gorum-Parenga. Also recorded as a further script for 9 more.
Unicode: encoded since version 1.1, block from U+0C00.

### Teng

**Tengwar**. Alphabet, written left to right. First attested 1930 CE, in use today; status fictional.

Parent: [`Sara`](#sara) Sarati, link **attested**.
Source: Everson, Unicode N4013. The featural Tengwar, developed by Tolkien from Sarati.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Tfng

**Tifinagh** (ⵜⴼⵉⵏⵗ). Alphabet, written in more than one direction. First attested 138 BCE, in use today; status living.

Parent: [`Phnx`](#phnx) Phoenician through Libyco-Berber, link **contested**.
Source: British Museum, 'Written in stone'; Chaker & Hachi 2000. Phoenician/Punic origin has the wider support; indigenous and South Arabian origins argued; first dated text 139/138 BCE (Dougga).

Languages written mainly in it: 6. Largest: Tachelhit (8,000,000 speakers), Tagdal (26,900 speakers), Zenaga (200 speakers), Numidian, Western Algerian Berber. Also recorded as a further script for 16 more.
Unicode: encoded since version 4.1, block from U+2D30.

### Tglg

**Tagalog** (ᜊᜌ᜔ᜊᜌᜒᜈ᜔). Abugida, written left to right. First attested 1550 CE, in use today; status revived.

Parent: [`Kawi`](#kawi) Kawi, link **contested**.
Source: Miller 2011, 11-PLC; Unicode ch.17. Kawi, Bugis, Sumatran and Gujarati origins all argued; first verifiably dated text 1593.
Children: [`Buhd`](#buhd), [`Hano`](#hano), [`Tagb`](#tagb).

Recorded as a further script for 4 languages, the main script for none.
Unicode: encoded since version 3.2, block from U+1700.

### Thaa

**Thaana** (ތާނަ). Alphabet, written right to left. First attested 1705 CE, in use today; status living.

Parent: [`Arab`](#arab) Arabic, link **stimulus**.
Source: Maldives National Centre for Linguistic and Historical Research, 'Scripts of Maldives'. First nine letters from Arabic numerals, next nine from Indic numerals; vowel marks from Arabic; earliest records 1705.

Languages written mainly in it: 1. Dhivehi (340,500 speakers).
Unicode: encoded since version 3.0, block from U+0780.

### Thai

**Thai** (อักษรไทย). Abugida, written left to right. First attested 1292 CE, in use today; status living.

Parent: [`Khmr`](#khmr) Khmer through Sukhothai, link **attested**.
Source: Penth 1989, JSS 77. Ram Khamhaeng inscription dated 1292, authenticity disputed; Wat Bang Sanuk 1219 also cited.
Children: [`Laoo`](#laoo), [`Tavt`](#tavt), [`Tayo`](#tayo).

Languages written mainly in it: 23. Largest: Thai (20,700,000 speakers), Northeastern Thai (15,000,000 speakers), Southern Thai (4,500,000 speakers), Northern Khmer (1,400,000 speakers), Kuy (488,900 speakers). Also recorded as a further script for 22 more.
Unicode: encoded since version 1.1, block from U+0E01.

### Tibt

**Tibetan** (བོད་ཡིག་). Abugida, written left to right. First attested 650 CE, in use today; status living.

Parent: [`Brah`](#brah) Brahmi through Late Gupta, link **attested**.
Source: van Schaik 2012, in Tibetan manuscript studies. North Indian and Nepalese late Gupta inscriptions the closest models.
Children: [`Marc`](#marc), [`Phag`](#phag), [`Zanb`](#zanb), [`Lepc`](#lepc).

Languages written mainly in it: 28. Largest: Khams Tibetan (1,500,000 speakers), Tibetan (1,200,000 speakers), Amdo Tibetan (810,000 speakers), Dzongkha (237,080 speakers), Tshangla (175,000 speakers). Also recorded as a further script for 16 more.
Unicode: encoded since version 2.0, block from U+0F00.

### Tirh

**Tirhuta** (𑒧𑒱𑒟𑒱𑒪𑒰𑒏𑓂𑒭𑒩). Abugida, written left to right. First attested 1200 CE, in use today; status living.

Parent: [`Sidd`](#sidd) Siddham, Siddhaṃ, Siddhamātṛkā through Gaudi, link **attested**.
Source: Pandey, L2/11-175R, after Salomon 1998; Unicode ch.15. Derived from Gaudi (proto-Bengali); a sibling of Bengali, not its child; inscriptions 13th c.; still used for religious and literary manuscripts and personal letters.

Recorded as a further script for 2 languages, the main script for none.
Unicode: encoded since version 7.0, block from U+11480.

### Tnsa

**Tangsa** (𖪰𖩵𖪂𖪫𖩸 𖪫𖪏𖪴𖩻𖪇𖪐). Alphabet, written left to right. First attested 1990 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Morey, eScholarship 5nz191bp; L2/13-231. Developed since 1990 by Lakhum Mossang; genetically unrelated to existing scripts.

Languages written mainly in it: 1. Pangwa Naga.
Unicode: encoded since version 14.0, block from U+16A70.

### Todr

**Todhri**. Alphabet, written left to right. First attested 1750 CE, last used 1900 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **stimulus**.
Source: Everson, Unicode N5139R2; Geitler 1883. Derived from Greek and Roman cursive (Geitler); 18th century, author fl. c.1730-1805.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+105C0.

### Tols

**Tolong Siki** (𑶻𑶳𑷑𑶳𑷎 𑷔𑶰𑷊𑶰). Alphabet, written left to right. First attested 1988 CE, in use today; status living.

Parent: [`Deva`](#deva) Devanagari, link **invented**.
Source: Pandey, L2/23-024. Invented in 1988 by Narayan Oraon, published 1999; Oraon also published Kurukh-Hindi primers, so it hangs under Devanagari.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Toto

**Toto** (𞊒𞊪𞊒𞊪 𞊫𞊠𞊐𞊭𞊑𞊦𞊒). Alphabet, written left to right. First attested 2015 CE, in use today; status living.

Parent: [`Beng`](#beng) Bengali, link **invented**.
Source: Anderson & Evans 2024, Nepalese Linguistics 38; L2/19-330. An entirely novel set of letters from everyday objects; launched May 2015; 'the government schooling is in Bangla medium', so it hangs under Bengali.

Languages written mainly in it: 1. Toto.
Unicode: encoded since version 14.0, block from U+1E290.

### Tutg

**Tulu-Tigalari** (𑎡𑎻𑎭𑎻 𑎭𑎹𑎦𑎹). Abugida, written left to right. First attested 1000 CE, in use today; status living.

Parent: [`Gran`](#gran) Grantha through Chola Grantha, link **attested**.
Source: L2/17-378; L2/22-031. Evolved from the later Chola Grantha to write Sanskrit; in continuous use for ritual purposes such as birth charts and charms.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 16.0, block from U+11380.

### Ugar

**Ugaritic**. Alphabet, written left to right. First attested 1250 BCE, last used 1190 BCE; status historical.

Parent: [`Psin`](#psin) Proto-Sinaitic through Proto-Canaanite linear alphabet, link **stimulus**.
Source: Vita, 'Ugaritic' (CSIC 2021); Cross, 'A Ugaritic Abecedary'. Modelled on a linear alphabet of 27 signs; only the wedge medium is Mesopotamian.

Languages written mainly in it: 1. Ugaritic. Also recorded as a further script for 1 more.
Unicode: encoded since version 4.0, block from U+10380.

### Vaii

**Vai** (ꕙꔤ). Syllabary, written left to right. First attested 1833 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: Unicode ch.19; Tuchscherer & Hair 2002, History in Africa 29. Latin, Arabic and possibly Cherokee influence proposed; none established.
Children: [`Bass`](#bass), [`Mend`](#mend), [`Kpel`](#kpel), [`Loma`](#loma).

Languages written mainly in it: 1. Vai.
Unicode: encoded since version 5.1, block from U+A500.

### Visp

**Visible Speech**. Featural, written left to right. First attested 1867 CE, last used 1900 CE; status historical.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Bell 1867, Visible Speech. Symbols built from the vocal organs, not from existing letters.

Languages a source records it for: none.
Unicode: not encoded, so no font can show it.

### Vith

**Vithkuqi**. Alphabet, written left to right. First attested 1844 CE, last used 1900 CE; status historical.

Parent: [`Grek`](#grek) Greek, link **contested**.
Source: Everson, Unicode N5138, quoting Elsie 2017 and von Hahn. Only single letters recall Greek; glyphs resemble cursive Armenian; no source names a model.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 14.0, block from U+10570.

### Wara

**Warang Citi** (𑢹𑣗𑣁𑣜𑣊 𑣏𑣂𑣕𑣂). Alphabet, written left to right. First attested 1950 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Everson, Unicode N4259 (L2/12-118). Devised by Lako Bodra in the 1950s; full vowel letters.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 7.0, block from U+118A0.

### Wcho

**Wancho** (𞋒𞋀𞋉𞋃𞋕 𞋈𞋀𞋜𞋐𞋜). Alphabet, written left to right. First attested 2001 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **invented**.
Source: Unicode N4787. Devised 2001-2012 by Banwang Losu; a simple alphabetic script.

Languages written mainly in it: 1. Wancho Naga (59,154 speakers).
Unicode: encoded since version 12.0, block from U+1E2C0.

### Wole

**Woleai**. Syllabary, written left to right. First attested 1905 CE, last used 1950 CE; status historical.

Parent: [`Latn`](#latn) Latin, link **stimulus**.
Source: Everson, Unicode N4146. One class of signs from Latin letters, the other invented; c.1905-1909.

Recorded as a further script for 1 language, the main script for none.
Unicode: not encoded, so no font can show it.

### Xpeo

**Old Persian**. Alphabet, written left to right. First attested 520 BCE, last used 330 BCE; status historical.

Parent: [`Xsux`](#xsux) Cuneiform, Sumero-Akkadian, link **stimulus**.
Source: Schmitt, Encyclopaedia Iranica 'Cuneiform script'. An independent creation in wedge form for Darius's Bisotun inscription, c. 520 BCE.

Languages written mainly in it: 1. Old Persian (ca. 600-400 B.C.).
Unicode: encoded since version 4.1, block from U+103A0.

### Xsux

**Cuneiform, Sumero-Akkadian**. Logographic, written left to right. First attested 2600 BCE, last used 75 CE; status historical.

Parent: [`Pcun`](#pcun) Proto-Cuneiform, link **attested**.
Source: Unicode ch.11; L2/25-211 (proto-cuneiform). Cuneiform proper from c.2700-2600 BCE (Fara, Abu Salabikh); -2900 is the end of the archaic period.
Children: [`Xpeo`](#xpeo).

Languages written mainly in it: 10. Largest: Sumerian, Elamite, Hattic, Hurrian, Urartian. Also recorded as a further script for 1 more.
Unicode: encoded since version 5.0, block from U+12000.

### Yezi

**Yezidi**. Alphabet, written right to left. First attested 1200 CE, in use today; status living.

Parent: [`Syrc`](#syrc) Syriac, link **contested**.
Source: L2/19-051R (Yezidi proposal); Unicode ch.9. An original consonantal alphabet; manuscripts perhaps 12th-13th c.; no named ancestor.

Recorded as a further script for 1 language, the main script for none.
Unicode: encoded since version 13.0, block from U+10E80.

### Yiii

**Yi** (ꆈꌠꁱꂷ). Syllabary, written left to right. First attested 1485 CE, in use today; status living.

Parent: [`Hani`](#hani) Han, link **contested**.
Source: Bradley 2003; Unicode ch.18. Glyphs independent in form; earliest dated object a bronze bell of 1485.

Languages written mainly in it: 9. Largest: Sichuan Yi (2,000,000 speakers), Southwestern Nisu, Mantsi, Samatao, Sani. Also recorded as a further script for 2 more.
Unicode: encoded since version 3.0, block from U+A000.

### Zanb

**Zanabazar Square** (𑨢𑨆𑨏𑨳𑨋𑨆𑨬𑨳). Abugida, written left to right. First attested 1686 CE, last used 1800 CE; status historical.

Parent: [`Tibt`](#tibt) Tibetan, link **attested**.
Source: Unicode ch.14; Pandey, L2/14-024. Based upon Tibetan; date unknown, believed to precede Soyombo (1686).

Languages a source records it for: none.
Unicode: encoded since version 10.0, block from U+11A00.

### Zsye

**Symbols** (絵文字). Symbols, written left to right. First attested 1999 CE, in use today; status living.

Parent: [`Latn`](#latn) Latin, link **composite**.

Languages a source records it for: none.
Unicode: encoded since version 6.0.

