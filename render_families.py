# -*- coding: utf-8 -*-
"""Draw the second plate: language families facing the scripts that write them.

The main plate is a tree of scripts with the languages hung beneath. Script
and language family are different trees, and this plate shows how they cross:
language families on the left, scripts on the right in the order of their
descent tree, and a band between them for every family-script pair, as thick
as the number of languages of that family written mainly in that script.

Only languages with a script on record are drawn; the rest are counted in the
caption. Families are ordered by the mean position of their scripts, which
keeps the bands from crossing more than they must.
"""
import os, sys, json, collections

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "out")
sys.path.insert(0, BASE)
from build_data import PSEUDO_FAMILIES

D = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))
S, L, FN, ST = D["scripts"], D["languages"], D["family_names"], D["stats"]

TOP_FAMILIES, TOP_SCRIPTS = 40, 30
W, PAD = 4200, 120
TOP, ROW_GAP = 330, 6
LEFT_X, RIGHT_X, BAR_W = 900, 3060, 26
PAPER, INK, SOFT, FAINT, RULE = "#f6f1e6", "#1a1714", "#6b6155", "#a89d8d", "#c9bda9"
HUE = {"Pcun": "#8c3b2e", "Egyp": "#a86a1f", "Hani": "#2f5d50", "Maya": "#6b3f7a",
       "Inds": "#7a6a3a", "Roro": "#3d5f7a", "Lina": "#2f6b7a", "Hluw": "#8a5a4a",
       "Nkdb": "#4a6b2f"}
OTHER = "#9c9488"


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def root_of(c):
    while S[c]["parent"]:
        c = S[c]["parent"]
    return c


# Nearly every script descends from Egyptian through Proto-Sinaitic, so the
# root colour of the main plate says nothing here. Colour by great lineage
# instead: the first of these met walking up from a script.
LINEAGE = [("Brah", "#b5651d", "Brahmi"), ("Grek", "#3d5f8a", "Greek, Latin, Cyrillic"),
           ("Armi", "#2f7a52", "Aramaic, Hebrew, Arabic"), ("Sarb", "#7a4a8a", "South Arabian, Ethiopic"),
           ("Hani", "#2f5d50", "Chinese"), ("Pcun", "#8c3b2e", "Cuneiform")]
LINEAGE_OTHER = ("#9c9488", "other lineages")


def lineage_of(c):
    while c:
        for code, col, name in LINEAGE:
            if c == code:
                return col
        c = S[c]["parent"]
    return LINEAGE_OTHER[0]


# script order: a depth-first walk of the descent tree, children by start date,
# so the right column reads as the tree does
kids = collections.defaultdict(list)
for c, s in S.items():
    if s["parent"]:
        kids[s["parent"]].append(c)
order = []


def walk(c):
    order.append(c)
    for k in sorted(kids[c], key=lambda k: (S[k]["start"], k)):
        walk(k)


for r in sorted((c for c in S if not S[c]["parent"]), key=lambda c: S[c]["start"]):
    walk(r)
pos = {c: i for i, c in enumerate(order)}

# flows: family -> main script, counted in languages
flows = collections.Counter()
for v in L.values():
    sc = v["primary_script"]
    if not sc:
        continue
    if v["isolate"]:
        fam = "Isolates"
    else:
        fam = FN.get(v["family"], v["family"])
        if fam in PSEUDO_FAMILIES:
            fam = "Unclassified and other categories"
    flows[(fam, sc)] += 1
total = sum(flows.values())

by_script = collections.Counter()
by_family = collections.Counter()
for (f, sc), n in flows.items():
    by_script[sc] += n
    by_family[f] += n

# ties broken by name: these are sets, whose order changes with Python's hash seed
keep_s = set(sorted(by_script, key=lambda c: (-by_script[c], c))[:TOP_SCRIPTS])
SPECIAL = {"Isolates", "Unclassified and other categories"}
keep_f = set(f for f in sorted(by_family, key=lambda f: -by_family[f]) if f not in SPECIAL)
keep_f = set(sorted(keep_f, key=lambda f: (-by_family[f], f))[:TOP_FAMILIES])
n_other_s = len(set(by_script) - keep_s)
n_other_f = len(set(by_family) - keep_f - SPECIAL)
OTHER_S = "%d other scripts" % n_other_s
OTHER_F = "%d other families" % n_other_f

agg = collections.Counter()
for (f, sc), n in flows.items():
    ff = f if (f in keep_f or f in SPECIAL) else OTHER_F
    ss = sc if sc in keep_s else OTHER_S
    agg[(ff, ss)] += n

right = sorted(keep_s, key=lambda c: pos[c]) + [OTHER_S]
rpos = {c: i for i, c in enumerate(right)}
fam_mean = collections.defaultdict(lambda: [0, 0])
for (f, s), n in agg.items():
    fam_mean[f][0] += rpos[s] * n
    fam_mean[f][1] += n
left = sorted((f for f in fam_mean if f not in SPECIAL and f != OTHER_F),
              key=lambda f: (fam_mean[f][0] / fam_mean[f][1], f))
left += [f for f in (OTHER_F, "Isolates", "Unclassified and other categories") if f in fam_mean]

col_tot_l = {f: sum(n for (ff, _), n in agg.items() if ff == f) for f in left}
col_tot_r = {s: sum(n for (_, ss), n in agg.items() if ss == s) for s in right}

H_USE = 2600                                  # vertical space for the columns
unit_l = (H_USE - ROW_GAP * len(left)) / total
unit_r = (H_USE - ROW_GAP * len(right)) / total
MIN_H = 3.0                                   # a one-language family stays visible


def stack(names, tot, unit):
    y, out = TOP, {}
    for n in names:
        h = max(MIN_H, tot[n] * unit)
        out[n] = [y, h, y]                    # top, height, cursor for bands
        y += h + ROW_GAP
    return out, y


LY, ly_end = stack(left, col_tot_l, unit_l)
RY, ry_end = stack(right, col_tot_r, unit_r)
H = int(max(ly_end, ry_end) + 560)

o = []
a = o.append
a('<?xml version="1.0" encoding="UTF-8"?>')
a('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H))
a("<title>Language families and the scripts that write them</title>")
a("<desc>%d languages with a script on record, in %d families and isolates on the left, joined by bands "
  "to the %d scripts they are mainly written in on the right, ordered as the descent tree. Band "
  "thickness is the number of languages.</desc>" % (total, len(by_family), len(by_script)))
a('<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
a('<defs><style>text{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;fill:%s;}'
  '.m{font-family:Consolas,"DejaVu Sans Mono",monospace;}</style></defs>' % INK)
a('<text x="%d" y="110" text-anchor="middle" font-size="64" letter-spacing="8">'
  'LANGUAGE FAMILIES AND THE SCRIPTS THAT WRITE THEM</text>' % (W / 2))
a('<text x="%d" y="170" text-anchor="middle" font-size="28" fill="%s">'
  '%s languages with a script on record, each counted once, under its main script. '
  'The other %s have none on record and are not drawn.</text>'
  % (W / 2, SOFT, format(total, ","), format(ST["languages"] - total, ",")))
a('<text x="%d" y="250" font-size="30" letter-spacing="5" fill="%s">LANGUAGE FAMILIES (Glottolog)</text>'
  % (LEFT_X - 20, SOFT) if False else
  '<text x="%d" y="250" text-anchor="end" font-size="30" letter-spacing="5" fill="%s">'
  'LANGUAGE FAMILIES (Glottolog)</text>' % (LEFT_X + BAR_W, SOFT))
a('<text x="%d" y="250" font-size="30" letter-spacing="5" fill="%s">SCRIPTS (ISO 15924), IN DESCENT ORDER</text>'
  % (RIGHT_X, SOFT))

# bands first, under the bars; ordered so each column's bands stack in the
# order of the opposite column, which keeps them from twisting
for f in left:
    for s in right:
        n = agg.get((f, s))
        if not n:
            continue
        hl, hr = n * unit_l, n * unit_r
        y1 = LY[f][2]
        LY[f][2] += hl
        y2 = RY[s][2]
        RY[s][2] += hr
        col = lineage_of(s) if s in S else OTHER
        x1, x2 = LEFT_X + BAR_W, RIGHT_X
        mx = (x1 + x2) / 2
        a('<path d="M%.1f %.2f C %.1f %.2f %.1f %.2f %.1f %.2f L %.1f %.2f C %.1f %.2f %.1f %.2f %.1f %.2f Z" '
          'fill="%s" opacity="0.42"><title>%s, %d language%s, %s</title></path>'
          % (x1, y1, mx, y1, mx, y2, x2, y2, x2, y2 + hr, mx, y2 + hr, mx, y1 + hl, x1, y1 + hl,
             col, esc(f), n, "" if n == 1 else "s", esc(S[s]["name"] if s in S else s)))

def label_ys(names, Y, gap=24):
    """Label positions, pushed apart where thin bars sit too close to read."""
    out, last = {}, -1e9
    for n in names:
        want = Y[n][0] + Y[n][1] / 2
        out[n] = max(want, last + gap)
        last = out[n]
    return out


lyl, lyr = label_ys(left, LY), label_ys(right, RY)
for f in left:
    y, h, _ = LY[f]
    a('<rect x="%d" y="%.2f" width="%d" height="%.2f" fill="%s"/>' % (LEFT_X, y, BAR_W, h, INK))
    if abs(lyl[f] - (y + h / 2)) > 1:
        a('<path d="M%d %.1f L%d %.1f L%d %.1f" fill="none" stroke="%s" stroke-width="1"/>'
          % (LEFT_X, y + h / 2, LEFT_X - 8, y + h / 2, LEFT_X - 12, lyl[f], FAINT))
    a('<text x="%d" y="%.1f" text-anchor="end" font-size="20" dominant-baseline="middle">%s '
      '<tspan fill="%s">%s</tspan></text>'
      % (LEFT_X - 16, lyl[f], esc(f), SOFT, format(col_tot_l[f], ",")))
for s in right:
    y, h, _ = RY[s]
    col = lineage_of(s) if s in S else OTHER
    a('<g id="r-%s">' % (s if s in S else "other"))
    a('<rect x="%d" y="%.2f" width="%d" height="%.2f" fill="%s"/>' % (RIGHT_X, y, BAR_W, h, col))
    if abs(lyr[s] - (y + h / 2)) > 1:
        a('<path d="M%d %.1f L%d %.1f L%d %.1f" fill="none" stroke="%s" stroke-width="1"/>'
          % (RIGHT_X + BAR_W, y + h / 2, RIGHT_X + BAR_W + 8, y + h / 2, RIGHT_X + BAR_W + 12, lyr[s], FAINT))
    label = "%s %s" % (s, S[s]["name"]) if s in S else s
    a('<text x="%d" y="%.1f" font-size="20" dominant-baseline="middle">%s '
      '<tspan fill="%s">%s</tspan></text>'
      % (RIGHT_X + BAR_W + 16, lyr[s], esc(label), SOFT, format(col_tot_r[s], ",")))
    a("</g>")

# lineage key
ky = max(max(lyl.values()), max(lyr.values())) + 70
for i, (code, col, name) in enumerate(LINEAGE + [("", LINEAGE_OTHER[0], LINEAGE_OTHER[1])]):
    kx = PAD + 40 + i * 560
    a('<rect x="%d" y="%.0f" width="40" height="22" fill="%s" opacity="0.7"/>' % (kx, ky - 16, col))
    a('<text x="%d" y="%.0f" font-size="24">%s</text>' % (kx + 52, ky + 2, esc(name)))

fy = H - 300
a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (PAD, fy, W - PAD, fy, RULE))
lines = [
    "Band colour is the script's great lineage (key above). A language with several "
    "scripts is counted once, under its main script.",
    "Script and family do not line up: Latin alone writes %s of these languages, from families on every "
    "continent, while most other scripts serve one family." % format(by_script.get("Latn", 0), ","),
    "%d families and isolates are drawn by name; the other %d are pooled, as are the %d scripts after the "
    "first %d. Glottolog's filing categories (Bookkeeping, Unclassifiable and the rest) are pooled as one."
    % (len(keep_f), n_other_f, n_other_s, TOP_SCRIPTS),
    "Sources: Glottolog 5 CLDF (CC-BY-4.0); Wikidata P282, Unicode CLDR and SIL langtags for scripts. "
    "Built by render_families.py from out/dataset.json.",
]
for i, t in enumerate(lines):
    a('<text x="%d" y="%d" font-size="26" fill="%s">%s</text>' % (PAD, fy + 50 + i * 40, SOFT, esc(t)))
a("</svg>")

path = os.path.join(OUT, "families_and_scripts.svg")
open(path, "w", encoding="utf8").write("\n".join(o))
print("%s  %d x %d, %d bands, %d families, %d scripts"
      % (path, W, H, len(agg), len(left), len(right)))
