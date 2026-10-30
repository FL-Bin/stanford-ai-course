#!/usr/bin/env python3
"""Download the open-licensed (SIL OFL 1.1) fonts used by build_pdf.py into .fonts/ as static instances.

Inter (headings/UI), Source Serif 4 (English body), JetBrains Mono (code), Noto Sans SC (Chinese).
Fonts are fetched at build time and not committed. Needs: pip install fonttools
"""
import os, sys, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.environ.get("FONT_DIR", os.path.join(ROOT, ".fonts"))
GF = "https://raw.githubusercontent.com/google/fonts/main/ofl/"
FONTS = [  # (url, out-prefix, weights, extra fixed axes)
    (GF + "inter/Inter%5Bopsz,wght%5D.ttf", "Inter", (400, 600, 700, 800), {"opsz": 24}),
    (GF + "sourceserif4/SourceSerif4%5Bopsz,wght%5D.ttf", "SourceSerif4", (400, 600), {"opsz": 12}),
    (GF + "sourceserif4/SourceSerif4-Italic%5Bopsz,wght%5D.ttf", "SourceSerif4-Italic", (400,), {"opsz": 12}),
    (GF + "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf", "JetBrainsMono", (400, 700), {}),
    ("https://raw.githubusercontent.com/notofonts/noto-cjk/Sans2.004/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf",
     "NotoSansSC", (400, 500, 700), {}),
]

def fetch(url, path):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=120).read()
            open(path, "wb").write(data); return
        except Exception as e:  # retry flaky downloads
            print("retry", url, e, file=sys.stderr)
    raise SystemExit("failed to download " + url)

def main():
    os.makedirs(DEST, exist_ok=True)
    for url, name, weights, fixed in FONTS:
        if all(os.path.exists(os.path.join(DEST, f"{name}-{w}.ttf")) for w in weights):
            continue
        src = os.path.join(DEST, f"_{name}-VF.ttf")
        if not os.path.exists(src):
            fetch(url, src)
        for w in weights:
            f = TTFont(src)
            axes = {a.axisTag for a in f["fvar"].axes}
            loc = {k: v for k, v in dict(fixed, wght=w).items() if k in axes}
            instantiateVariableFont(f, loc, inplace=True, updateFontNames=True)
            f.save(os.path.join(DEST, f"{name}-{w}.ttf"))
            print("wrote", f"{name}-{w}.ttf")
        os.remove(src)

if __name__ == "__main__":
    main()
