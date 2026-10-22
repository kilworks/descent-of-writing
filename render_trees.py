# -*- coding: utf-8 -*-
"""Draw the third plate: the language tree and the script tree, facing.

families_and_scripts.svg reduces language descent to a column of families.
Here both recursions are drawn as trees: Glottolog's classification on the
left, cut down to the clades large enough to read, and the descent of the
scripts on the right. A band joins a clade to the script its languages are
mainly written in, as thick as the number of languages.

A clade is opened while it holds at least OPEN written languages and lies
within MAX_DEPTH levels of its family; its subclades of fewer than KEEP
languages, and languages sitting directly under it, are pooled into one
leaf. Families with fewer than KEEP written languages are pooled too.
"""
import os, sys, json, collections

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "out")
sys.path.insert(0, BASE)
from build_data import PSEUDO_FAMILIES
from render_families import lineage_of, LINEAGE, LINEAGE_OTHER, esc

D = json.load(open(os.path.join(OUT, "dataset.json"), encoding="utf8"))
S, L, FN, ST = D["scripts"], D["languages"], D["family_names"], D["stats"]

OPEN, KEEP, MAX_DEPTH = 40, 10, 4
W, PAD, TOP = 4600, 120, 330
L_TREE, L_LEAF, L_PORT = 140, 980, 1560          # left tree, leaf column, band port
R_PORT, R_LABEL, R_TREE0, R_TREE1 = 3010, 3056, 3660, 4460
BAR_W, GAP, H_USE = 22, 7, 5600
PAPER, INK, SOFT, FAINT, RULE = "#f6f1e6", "#1a1714", "#6b6155", "#a89d8d", "#c9bda9"

written = [v for v in L.values() if v["primary_script"]]
total = len(written)

# ------------------------------------------------------------ left tree ----
ISO_LEAF, PSEUDO_LEAF = ("leaf", "Isolates"), ("leaf", "Unclassified and other categories")


def clade_path(v):
    """The language's clades, family first; pseudo-families and isolates are
    filed under one pooled leaf each."""
    if v["isolate"]:
        return None, ISO_LEAF
    if FN.get(v["family"]) in PSEUDO_FAMILIES:
        return None, PSEUDO_LEAF
    return v["classification"], None


count = collections.Counter()
for v in written:
    p, special = clade_path(v)
    for g in p or []:
        count[g] += 1


def leaf_of(v):
    """Walk down the language's clades while they stay open."""
    p, special = clade_path(v)
    if special:
        return special
    if count[p[0]] < KEEP:
        return ("leaf", "smaller families")
    d = 0
    while count[p[d]] >= OPEN and d < MAX_DEPTH:
        nxt = p[d + 1] if d + 1 < len(p) else None
        if not nxt or count[nxt] < KEEP:
            return ("other", p[d])         # opened, but this language sits in no kept subclade
        d += 1
    return ("clade", p[d])


flows = collections.Counter()
leaf_n = collections.Counter()
for v in written:
    lf = leaf_of(v)
    flows[(lf, v["primary_script"])] += 1
    leaf_n[lf] += 1

# the clade tree above the leaves: parent of each clade node, from the paths
parent, members = {}, collections.defaultdict(set)
for v in written:
    p, special = clade_path(v)
    if not p:
        continue
    lf = leaf_of(v)
    if lf[0] not in ("clade", "other"):
        continue
    stop = p.index(lf[1])
    for i in range(1, stop + 1):
        parent[p[i]] = p[i - 1]
    members[lf[1]].add(lf)
    for g in p[:stop]:
        members[g].add(lf)

# ----------------------------------------------------------- right tree ----
used = collections.Counter(v["primary_script"] for v in written)
keep_s = set()
for c in used:
    while c:
        keep_s.add(c)
        c = S[c]["parent"]
kids = collections.defaultdict(list)
for c in sorted(keep_s):
    if S[c]["parent"]:
        kids[S[c]["parent"]].append(c)
order, depth_s = [], {}


def walk(c, d):
    order.append(c)
    depth_s[c] = d
    for k in sorted(kids[c], key=lambda k: (S[k]["start"], k)):
        walk(k, d + 1)


for r in sorted((c for c in keep_s if not S[c]["parent"]), key=lambda c: (S[c]["start"], c)):
    walk(r, 0)
rows = [c for c in order if used[c]]
rpos = {c: i for i, c in enumerate(rows)}

# ------------------------------------------------ left order, by right pos --
mean = {}
for lf in leaf_n:
    s = sum(rpos[sc] * n for (l, sc), n in flows.items() if l == lf)
    mean[lf] = s / leaf_n[lf]


def node_mean(g):
    # summed in a fixed order and tied by code: members are sets, whose order
    # changes with Python's hash seed, and the plate must not
    lfs = sorted(members[g])
    return sum(mean[l] * leaf_n[l] for l in lfs) / sum(leaf_n[l] for l in lfs), g


ckids = collections.defaultdict(list)
for g, p in parent.items():
    ckids[p].append(g)
roots = sorted({g for g in members if g not in parent}, key=node_mean)
left, ltree = [], []                       # leaves in order; (node, depth) in order


def lwalk(g, d):
    ltree.append((g, d))
    subs = sorted(ckids[g], key=node_mean)
    items = [("clade", s) for s in subs] + ([("other", g)] if ("other", g) in leaf_n else [])
    if not subs:                           # a leaf, or an opened clade whose subclades are all pooled
        left.append(("clade", g) if ("clade", g) in leaf_n else ("other", g))
        return
    for kind, s in sorted(items, key=lambda it: node_mean(it[1]) if it[0] == "clade" else (mean[it], "~")):
        if kind == "clade":
            lwalk(s, d + 1)
        else:
            left.append(("other", g))


for g in roots:
    lwalk(g, 0)
left += [lf for lf in (("leaf", "smaller families"), ISO_LEAF, PSEUDO_LEAF) if lf in leaf_n]
assert sum(leaf_n[l] for l in left) == total, "every written language sits in one leaf"

# ------------------------------------------------------------- geometry ----
unit_l = (H_USE - GAP * len(left)) / total
unit_r = (H_USE - GAP * len(rows)) / total


def stack(names, tot, unit):
    y, out = TOP, {}
    for n in names:
        h = max(2.5, tot[n] * unit)
        out[n] = [y, h, y]
        y += h + GAP
    return out, y


LY, ly_end = stack(left, leaf_n, unit_l)
RY, ry_end = stack(rows, used, unit_r)
mid = lambda box: box[0] + box[1] / 2


def label_ys(names, Y, gap=21):
    """Label rows, pushed apart where thin bars sit too close to read; the
    trees hang from the labels and a leader joins each label to its bar."""
    out, last = {}, -1e9
    for n in names:
        out[n] = max(mid(Y[n]), last + gap)
        last = out[n]
    return out


LL, RL = label_ys(left, LY), label_ys(rows, RY)
y_end = max(ly_end, ry_end, max(LL.values()) + 30, max(RL.values()) + 30)
H = int(y_end + 520)

o = []
a = o.append
a('<?xml version="1.0" encoding="UTF-8"?>')
a('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H))
a("<title>The language tree and the script tree, facing</title>")
a("<desc>%d languages with a script on record. Left, Glottolog's classification cut to %d leaves; "
  "right, the descent tree of the %d scripts they are mainly written in, with their ancestors. "
  "Band thickness is the number of languages.</desc>" % (total, len(left), len(rows)))
a('<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
a('<defs><style>text{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;fill:%s;}'
  '.m{font-family:Consolas,"DejaVu Sans Mono",monospace;}</style></defs>' % INK)
a('<text x="%d" y="110" text-anchor="middle" font-size="64" letter-spacing="8">'
  'TWO TREES THAT DO NOT LINE UP</text>' % (W / 2))
a('<text x="%d" y="170" text-anchor="middle" font-size="28" fill="%s">'
  'Where languages come from, left, and where their scripts come from, right. %s languages with a '
  'script on record, each once, under its main script.</text>' % (W / 2, SOFT, format(total, ",")))
a('<text x="%d" y="250" font-size="30" letter-spacing="5" fill="%s">LANGUAGE DESCENT (Glottolog)</text>'
  % (L_TREE, SOFT))
a('<text x="%d" y="250" text-anchor="end" font-size="30" letter-spacing="5" fill="%s">'
  'SCRIPT DESCENT (ISO 15924)</text>' % (R_TREE1, SOFT))

# bands, stacked in the opposite column's order so they do not twist
for lf in left:
    for sc in rows:
        n = flows.get((lf, sc))
        if not n:
            continue
        hl, hr = n * unit_l, n * unit_r
        y1, y2 = LY[lf][2], RY[sc][2]
        LY[lf][2] += hl
        RY[sc][2] += hr
        x1, x2 = L_PORT + BAR_W, R_PORT
        mx = (x1 + x2) / 2
        a('<path d="M%.1f %.2f C %.1f %.2f %.1f %.2f %.1f %.2f L %.1f %.2f C %.1f %.2f %.1f %.2f %.1f %.2f Z" '
          'fill="%s" opacity="0.4"/>'
          % (x1, y1, mx, y1, mx, y2, x2, y2, x2, y2 + hr, mx, y2 + hr, mx, y1 + hl, x1, y1 + hl, lineage_of(sc)))


def leaf_label(lf):
    kind, g = lf
    if kind == "clade":
        return FN.get(g, g)
    if kind == "other":
        return "other %s" % FN.get(g, g)
    return g


# left tree: clade nodes by depth, leaves aligned at L_LEAF
dx = (L_LEAF - L_TREE) / (MAX_DEPTH + 1)
ny = {}
for lf in left:
    ny[lf] = LL[lf]
for g, d in reversed(ltree):
    ys = [ny[("clade", k)] if ("clade", k) in ny and not ckids[k] else ny[k] for k in ckids[g]]
    if ("other", g) in ny:
        ys.append(ny[("other", g)])
    ny[g] = sum(ys) / len(ys) if ys else ny[("clade", g)]
for g, d in ltree:
    x = L_TREE + d * dx
    ends = []
    for k in ckids[g]:
        ky = ny[k] if ckids[k] else ny[("clade", k)]
        kx = L_TREE + (d + 1) * dx if ckids[k] else L_LEAF
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (x, ky, kx, ky, INK))
        ends.append(ky)
    if ("other", g) in ny:
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="4 4"/>'
          % (x, ny[("other", g)], L_LEAF, ny[("other", g)], FAINT))
        ends.append(ny[("other", g)])
    if not ckids[g]:
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
          % (x, ny[("clade", g)], L_LEAF, ny[("clade", g)], INK))
        continue
    a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
      % (x, min(ends), x, max(ends), INK))
    a('<text x="%.1f" y="%.1f" font-size="17" fill="%s">%s</text>' % (x + 5, ny[g] - 6, SOFT, esc(FN.get(g, g))))
for lf in left:
    y = LL[lf]
    a('<rect x="%d" y="%.2f" width="%d" height="%.2f" fill="%s"/>' % (L_PORT, LY[lf][0], BAR_W, LY[lf][1], INK))
    if abs(y - mid(LY[lf])) > 1:
        a('<path d="M%d %.1f L%d %.1f L%d %.1f" fill="none" stroke="%s" stroke-width="1"/>'
          % (L_PORT, mid(LY[lf]), L_PORT - 10, mid(LY[lf]), L_PORT - 16, y, FAINT))
    a('<text x="%d" y="%.1f" font-size="18" dominant-baseline="middle">%s <tspan fill="%s">%d</tspan></text>'
      % (L_LEAF + 10, y, esc(leaf_label(lf)), SOFT, leaf_n[lf]))

# right tree: a script's node at its depth, roots far right
dxr = (R_TREE1 - R_TREE0) / max(depth_s.values())
sx = {c: R_TREE1 - depth_s[c] * dxr for c in order}
sy = {}
for c in reversed(order):
    if used[c]:
        sy[c] = RL[c]
    else:
        ys = [sy[k] for k in kids[c]]
        sy[c] = sum(ys) / len(ys)
for c in order:
    for k in kids[c]:
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
          % (sx[k], sy[k], sx[c], sy[k], INK))
    if kids[c]:
        ys = [sy[k] for k in kids[c]] + [sy[c]]
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
          % (sx[c], min(ys), sx[c], max(ys), INK))
    if not used[c]:
        a('<text x="%.1f" y="%.1f" font-size="16" fill="%s">%s</text>' % (sx[c] + 5, sy[c] - 6, SOFT, esc(c)))
for c in rows:
    y = RL[c]
    a('<g id="t-%s">' % c)
    a('<rect x="%d" y="%.2f" width="%d" height="%.2f" fill="%s"/>' % (R_PORT, RY[c][0], BAR_W, RY[c][1], lineage_of(c)))
    if abs(y - mid(RY[c])) > 1:
        a('<path d="M%d %.1f L%d %.1f L%d %.1f" fill="none" stroke="%s" stroke-width="1"/>'
          % (R_PORT + BAR_W, mid(RY[c]), R_PORT + BAR_W + 10, mid(RY[c]), R_LABEL - 6, y, FAINT))
    a('<line x1="%d" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" stroke-dasharray="2 4"/>'
      % (R_TREE0 - 10, y, sx[c], y, FAINT))
    a('<text x="%d" y="%.1f" font-size="18" dominant-baseline="middle">%s %s <tspan fill="%s">%d</tspan></text>'
      % (R_LABEL, y, c, esc(S[c]["name"][:30]), SOFT, used[c]))
    a("</g>")

# lineage key and caption
ky = y_end + 60
for i, (code, col, name) in enumerate(LINEAGE + [("", LINEAGE_OTHER[0], LINEAGE_OTHER[1])]):
    kx = PAD + 40 + i * 600
    a('<rect x="%d" y="%.0f" width="40" height="22" fill="%s" opacity="0.7"/>' % (kx, ky - 16, col))
    a('<text x="%d" y="%.0f" font-size="24">%s</text>' % (kx + 52, ky + 2, esc(name)))
fy = H - 330
a('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (PAD, fy, W - PAD, fy, RULE))
lines = [
    "Left: a clade is opened while it holds %d or more written languages and lies within %d levels of its family; "
    "its subclades of fewer than %d, and languages directly under it, are pooled as 'other' (dashed). "
    "Families with fewer than %d written languages are pooled." % (OPEN, MAX_DEPTH, KEEP, KEEP),
    "Right: every script that is the main script of a language, and its ancestors, in descent order; an "
    "ancestor that writes none of these languages is shown by its code only.",
    "Band colour is the script's great lineage (key above). A language with several scripts is counted once, "
    "under its main script.",
    "Sources: Glottolog 5 CLDF classification (CC-BY-4.0); Wikidata P282, Unicode CLDR and SIL langtags for "
    "scripts. Built by render_trees.py from out/dataset.json.",
]
for i, t in enumerate(lines):
    a('<text x="%d" y="%d" font-size="26" fill="%s">%s</text>' % (PAD, fy + 50 + i * 40, SOFT, esc(t)))
a("</svg>")

path = os.path.join(OUT, "trees_facing.svg")
open(path, "w", encoding="utf8").write("\n".join(o))
print("%s  %d x %d, %d leaves, %d scripts drawn of %d in the tree"
      % (path, W, H, len(left), len(rows), len(order)))
