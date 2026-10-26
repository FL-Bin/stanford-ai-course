#!/usr/bin/env python3
"""Pre-render ```mermaid blocks in book/**/*.md to book/assets/mermaid-<hash>.png (via mermaid.ink).

Run locally after editing diagrams and commit the PNGs; build_pdf.py then uses them offline.
The mermaid source stays in the Markdown so GitHub still renders it natively.
"""
import base64, glob, hashlib, os, re, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "book", "assets")
BLOCK = re.compile(r"```mermaid\n(.*?)```", re.S)

def asset_path(src):
    return os.path.join(ASSETS, "mermaid-%s.png" % hashlib.sha1(src.encode()).hexdigest()[:12])

def main():
    os.makedirs(ASSETS, exist_ok=True)
    wanted = set()
    for md in sorted(glob.glob(os.path.join(ROOT, "book", "*", "*.md"))):
        for src in BLOCK.findall(open(md, encoding="utf-8").read()):
            out = asset_path(src); wanted.add(out)
            if os.path.exists(out):
                continue
            url = "https://mermaid.ink/img/" + base64.urlsafe_b64encode(src.encode()).decode() + "?type=png&bgColor=white&width=1200"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            open(out, "wb").write(urllib.request.urlopen(req, timeout=60).read())
            print("rendered", os.path.relpath(out, ROOT))
    for old in glob.glob(os.path.join(ASSETS, "mermaid-*.png")):
        if old not in wanted:
            os.remove(old); print("removed", os.path.relpath(old, ROOT))

if __name__ == "__main__":
    main()
