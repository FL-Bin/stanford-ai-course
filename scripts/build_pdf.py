#!/usr/bin/env python3
"""Build CS146S-notes-zh.pdf / CS146S-notes-en.pdf from the notes, in learning-path order.

Usage: python3 scripts/build_pdf.py [outdir]   (needs: pip install weasyprint markdown; Noto Sans SC or fonts-noto-cjk)
Only our own notes are included; no course slides or transcripts.
"""
import datetime, glob, html, os, re, sys
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_URL = "https://github.com/gaibin/stanford-ai-course/blob/main/"
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist")

TEXT = {
    "zh": dict(title="斯坦福 AI 课程（中英双语笔记）", sub="Stanford CS146S · The Modern Software Developer · 中文版",
               notice="非官方学习笔记，与斯坦福大学及课程团队无任何关联。课件、文字稿等原始材料版权归原作者，本书只包含我们自己写的笔记和附出处的简短引用，原始材料请通过文中链接访问官方地址。",
               lic="笔记内容采用 CC BY-NC-SA 4.0 许可（不含任何被链接的原始材料）。", built="生成日期", toc="目录",
               src="源仓库", path="LEARNING_PATH.md"),
    "en": dict(title="斯坦福 AI 课程（中英双语笔记）", sub="Stanford CS146S · The Modern Software Developer · English edition",
               notice="Unofficial study notes, not affiliated with Stanford University or the course staff. Slides, transcripts and other original materials belong to their authors; this book contains only our own notes and short attributed quotes. Use the links to reach the official sources.",
               lic="Notes licensed under CC BY-NC-SA 4.0 (linked original materials are not covered).", built="Built", toc="Contents",
               src="Source", path="LEARNING_PATH.en.md"),
}

def note_files(lang):
    files = []
    for wk in sorted(glob.glob(os.path.join(ROOT, "weeks", "week*"))):
        files += sorted(glob.glob(os.path.join(wk, lang, "*.md")))
    return files

SWITCH = re.compile(r"^\s*(\*\*中文\*\*\s*\|\s*\[English\]\([^)]*\)|\[中文\]\([^)]*\)\s*\|\s*\*\*English\*\*|\*\*简体中文\*\*.*|\[简体中文\].*)\s*$")

def preprocess(text):
    lines = [l for l in text.splitlines() if not SWITCH.match(l)]
    out, i = [], 0
    while i < len(lines):
        if re.match(r"^>\s*\[!NOTE\]\s*$", lines[i]):
            body, i = [], i + 1
            while i < len(lines) and lines[i].startswith(">"):
                body.append(re.sub(r"^> ?", "", lines[i])); i += 1
            out += ["", '<div class="note" markdown="1">', ""] + body + ["", "</div>", ""]
        else:
            out.append(lines[i]); i += 1
    return "\n".join(normalize_lists(out))

LIST = re.compile(r"^(\s*)([-*+]|\d+\.)\s+")

def normalize_lists(lines):
    """GitHub-style lists -> Python-Markdown: blank line before a list, 2-space nesting -> 4."""
    res, prev, fence = [], "", False
    for l in lines:
        if l.lstrip().startswith("```"):
            fence = not fence
        if not fence:
            m = LIST.match(l)
            if m:
                ind = len(m.group(1))
                if ind:
                    l = " " * (ind * 2 if ind < 4 else ind) + l.lstrip()
                if prev.strip() and not LIST.match(prev) and not prev.lstrip().startswith(("<", "|")):
                    res.append("")
            if l.strip() in ("**补充**", "**Supplement**"):
                res += [l, ""]; prev = ""; continue
        res.append(l); prev = l
    return res

def fix_links(htm, src):
    base = os.path.dirname(os.path.relpath(src, ROOT))
    def rep(m):
        u = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", u): return m.group(0)
        p = os.path.normpath(os.path.join(base, u.split("#")[0]))
        return 'href="%s%s"' % (REPO_URL, p)
    return re.sub(r'href="([^"]+)"', rep, htm)

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm;
  @bottom-center { content: counter(page); font-size: 9pt; color: #666; } }
@page cover { @bottom-center { content: none; } }
html { font-family: "Noto Sans SC", "Noto Serif CJK SC", "Noto Sans CJK SC", sans-serif; font-size: 10.5pt; line-height: 1.65; color: #222; font-weight: 400; }
h1, h2, h3, h4 { font-family: "Noto Sans SC", "Noto Sans CJK SC", sans-serif; font-weight: 700; color: #1F5FA8; line-height: 1.3; }
h1 { font-size: 20pt; border-bottom: 2px solid #1F5FA8; padding-bottom: 4pt; }
h2 { font-size: 14pt; } h3 { font-size: 12pt; } h4 { font-size: 11pt; }
h3, h4, h5, h6 { bookmark-level: none; }
.chapter { page-break-before: always; }
a { color: #1F5FA8; text-decoration: none; word-break: break-all; }
code { font-family: "Noto Sans SC", "Noto Sans Mono CJK SC", monospace; font-weight: 400; font-size: 9pt; background: #f3f4f6; padding: 0 2pt; }
pre { background: #f6f8fa; padding: 6pt 8pt; border-radius: 4pt; white-space: pre-wrap; font-size: 8.5pt; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 6pt 0; }
th, td { border: 1px solid #d0d7de; padding: 3pt 5pt; text-align: left; vertical-align: top; }
th { background: #eef3fa; }
blockquote { margin: 8pt 0; padding: 4pt 10pt; border-left: 4px solid #c4c8cc; background: #f4f5f6; color: #555; }
.note { margin: 8pt 0; padding: 6pt 10pt; border-left: 4px solid #1F5FA8; background: #eaf1fa; border-radius: 3pt; }
.note > p:first-child strong { color: #1F5FA8; }
.cover { page: cover; text-align: center; padding-top: 55mm; }
.cover h1 { border: none; font-size: 28pt; bookmark-level: none; }
.cover .sub { font-size: 13pt; color: #1F5FA8; margin-bottom: 30mm; }
.cover .small { font-size: 9.5pt; color: #555; text-align: left; margin: 6pt 10mm; }
.toc { page-break-before: always; }
.toc h1 { bookmark-level: 1; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin: 3pt 0; }
.toc li.l2 { padding-left: 14pt; font-size: 9.5pt; color: #444; }
.toc a { color: #222; }
.toc a::after { content: leader('.') target-counter(attr(href), page); color: #666; }
"""

MD_EXT = ["tables", "fenced_code", "md_in_html", "sane_lists"]

def build(lang):
    t = TEXT[lang]
    files = [os.path.join(ROOT, t["path"])] + note_files(lang)
    chapters, toc = [], []
    for n, f in enumerate(files):
        h = markdown.markdown(preprocess(open(f, encoding="utf-8").read()), extensions=MD_EXT)
        h = fix_links(h, f)
        h = re.sub(r"<li>\s*\[ \]", "<li>☐", h).replace("<li>[x]", "<li>☑")
        k = [0]
        def addid(m):
            k[0] += 1
            hid = "c%d-%d" % (n, k[0])
            title = re.sub(r"<[^>]+>", "", m.group(3))
            if m.group(1) in "12":
                toc.append((m.group(1), hid, title))
            return '<h%s id="%s"%s>%s</h%s>' % (m.group(1), hid, m.group(2), m.group(3), m.group(1))
        h = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", addid, h, flags=re.S)
        chapters.append('<section class="chapter">%s</section>' % h)
    toc_html = "".join('<li class="l%s"><a href="#%s">%s</a></li>' % (lv, i, tt) for lv, i, tt in toc if lv == "1" or lang)
    today = datetime.date.today().isoformat()
    cover = f"""<section class="cover"><h1>{t['title']}</h1><div class="sub">{t['sub']}</div>
<p class="small">{t['notice']}</p><p class="small">{t['lic']}</p>
<p class="small">{t['built']}: {today} · {t['src']}: <a href="https://github.com/gaibin/stanford-ai-course">github.com/gaibin/stanford-ai-course</a> · <a href="https://themodernsoftware.dev/">themodernsoftware.dev</a></p></section>"""
    doc = f"""<!doctype html><html lang="{'zh-CN' if lang=='zh' else 'en'}"><head><meta charset="utf-8">
<title>{html.escape(t['title'])}</title><style>{CSS}</style></head><body>{cover}
<section class="toc"><h1>{t['toc']}</h1><ul>{toc_html}</ul></section>{''.join(chapters)}</body></html>"""
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"CS146S-notes-{lang}.pdf")
    HTML(string=doc, base_url=ROOT).write_pdf(out)
    print("wrote", out)

if __name__ == "__main__":
    for lang in ("zh", "en"):
        build(lang)
