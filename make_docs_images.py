# -*- coding: utf-8 -*-
"""Cut the figures used by the README out of the finished plate.

Crops are taken at 1:1 against the real canvas, so what the README shows is
literally what the SVG contains at that point, not a redrawn illustration.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
OUT, DOCS = os.path.join(BASE, "out"), os.path.join(BASE, "docs")
sys.path.insert(0, BASE)
import rasterize

os.makedirs(DOCS, exist_ok=True)
SVG = os.path.join(OUT, "descent_of_writing.svg")
head = open(SVG, encoding="utf8").read(4000)
W, H = (int(x) for x in re.search(r'width="(\d+)" height="(\d+)"', head).groups())

FIGURES = [
    # name, crop box on the real canvas, or None for the whole plate
    ("plate-full", None, 2400),
    ("detail-origins", (22300, 430, 3900, 660), None),
    ("detail-spine", (10160, 520, 3600, 2250), None),
    ("detail-languages", (200, 4740, 3400, 940), None),
    ("detail-catalogue", (200, 10250, 3200, 900), None),
]

for name, box, full_w in FIGURES:
    dest = os.path.join(DOCS, name + ".png")
    if box is None:
        n = rasterize.render(SVG, dest, full_w, int(full_w * H / W))
    else:
        x, y, w, h = box
        n = rasterize.render(SVG, dest, 0, 0, crop=(W, H, x, y, w, h))
    print("%-20s %8d bytes" % (name, n))

# the families plate is its own artefact too
fp = os.path.join(OUT, "families_and_scripts.svg")
if os.path.exists(fp):
    fw, fh = (int(x) for x in re.search(r'width="(\d+)" height="(\d+)"',
                                        open(fp, encoding="utf8").read(800)).groups())
    print("%-20s %8d bytes" % ("families", rasterize.render(
        fp, os.path.join(DOCS, "families.png"), 2100, round(2100 * fh / fw))))

tp = os.path.join(OUT, "trees_facing.svg")
if os.path.exists(tp):
    tw, th = (int(x) for x in re.search(r'width="(\d+)" height="(\d+)"',
                                        open(tp, encoding="utf8").read(800)).groups())
    print("%-20s %8d bytes" % ("trees", rasterize.render(
        tp, os.path.join(DOCS, "trees.png"), 1800, round(1800 * th / tw))))

# the shaping witness sheet is its own artefact, not a crop of the plate
sc = os.path.join(OUT, "specimen_check.svg")
if os.path.exists(sc):
    print("%-20s %8d bytes" % ("specimens", rasterize.render(
        sc, os.path.join(DOCS, "specimens.png"), 1920, 820)))
