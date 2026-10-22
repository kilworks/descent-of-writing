# -*- coding: utf-8 -*-
"""Upstream drift: compare a fresh build's figures with the committed ones.

verify.py checks the plate against the sources it was built from, so it
passes on any upstream release. This compares the stats of the dataset just
built with the dataset committed in git, and exits 1 naming every figure that
moved, so a new Glottolog release or ISO 15924 code is seen the month it lands
instead of the plate quietly becoming a snapshot that claims to be current.

    python drift.py            # compare against out/dataset.json at HEAD
    python drift.py <ref>      # or against any git ref
"""
import os, sys, json, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))


def stats_at(ref):
    blob = subprocess.run(["git", "show", "%s:out/dataset.json" % ref], cwd=BASE,
                          capture_output=True, check=True).stdout
    return json.loads(blob.decode("utf8"))["stats"]


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    old = stats_at(ref)
    new = json.load(open(os.path.join(BASE, "out", "dataset.json"), encoding="utf8"))["stats"]
    moved = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))
    for k in moved:
        print("%-28s %s -> %s" % (k, old.get(k), new.get(k)))
    if moved:
        sys.exit("DRIFT: %d figure(s) moved since %s" % (len(moved), ref))
    print("no drift against %s (%d figures)" % (ref, len(new)))


if __name__ == "__main__":
    main()
