#!/usr/bin/env python3
"""Build CS146S-notes-zh.pdf / CS146S-notes-en.pdf from the notes, in learning-path order.

Usage: python3 scripts/build_pdf.py [outdir]   (BOOK=1 builds the textbook from book/{lang}/)
         (needs: pip install weasyprint markdown pygments fonttools; run scripts/fetch_fonts.py first)
Only our own notes are included; no course slides or transcripts.
Fonts (all SIL OFL): Inter, Source Serif 4, JetBrains Mono, Noto Sans SC, loaded from .fonts/.
"""
import datetime, glob, html, os, re, sys
import markdown
from pygments.formatters import HtmlFormatter
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_URL = "https://github.com/FL-Bin/stanford-ai-course/blob/main/"
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist")
FONT_DIR = os.environ.get("FONT_DIR", os.path.join(ROOT, ".fonts"))

TEXT = {
    "zh": dict(title="斯坦福 AI 课程", title2="中英双语笔记", course="Stanford CS146S · The Modern Software Developer",
               term="2026 秋季 · 中文版",
               notice="非官方学习笔记，与斯坦福大学及课程团队无任何关联。课件、文字稿等原始材料版权归原作者，本书只包含我们自己写的笔记和附出处的简短引用，原始材料请通过文中链接访问官方地址。",
               lic="笔记内容采用 CC BY-NC-SA 4.0 许可（不含任何被链接的原始材料）。", built="生成日期", toc="目录",
               src="源仓库", path="LEARNING_PATH.md", book="教材", notes="按周笔记", chap="第 {n} 章", week="第 {n} 周",
               intro="导读", fonts="字体：Inter、Source Serif 4、JetBrains Mono、Noto Sans SC（SIL Open Font License 1.1）。",
               imprint="版权与说明", official="课程官网"),
    "en": dict(title="Stanford AI Course", title2="Bilingual Study Notes", course="Stanford CS146S · The Modern Software Developer",
               term="Fall 2026 · English edition",
               notice="Unofficial study notes, not affiliated with Stanford University or the course staff. Slides, transcripts and other original materials belong to their authors; this book contains only our own notes and short attributed quotes. Use the links to reach the official sources.",
               lic="Notes licensed under CC BY-NC-SA 4.0 (linked original materials are not covered).", built="Built", toc="Contents",
               src="Source", path="LEARNING_PATH.en.md", book="Textbook", notes="Weekly Notes", chap="Chapter {n}", week="Week {n}",
               intro="Overview", fonts="Typeset in Inter, Source Serif 4, JetBrains Mono and Noto Sans SC (SIL Open Font License 1.1).",
               imprint="Notice", official="Course site"),
}

BOOK = os.environ.get("BOOK") == "1"  # build the textbook (book/{lang}/) instead of the weekly notes

def note_files(lang):
    if BOOK:
        return sorted(glob.glob(os.path.join(ROOT, "book", lang, "*.md")))
    files = []
    for wk in sorted(glob.glob(os.path.join(ROOT, "weeks", "week*"))):
        files += sorted(glob.glob(os.path.join(wk, lang, "*.md")))
    return files

SWITCH = re.compile(r"^\s*(\*\*中文\*\*\s*\|\s*\[English\]\([^)]*\)|\[中文\]\([^)]*\)\s*\|\s*\*\*English\*\*|\*\*简体中文\*\*.*|\[简体中文\].*)\s*$")

def mermaid(text):
    """Swap ```mermaid blocks for the pre-rendered PNGs in book/assets (see render_diagrams.py)."""
    import hashlib
    def rep(m):
        src = m.group(1)
        img = os.path.join(ROOT, "book", "assets", "mermaid-%s.png" % hashlib.sha1(src.encode()).hexdigest()[:12])
        if os.path.exists(img):
            return '\n<div class="diagram"><img src="file://%s"/></div>\n' % img
        print("warning: diagram not pre-rendered, run scripts/render_diagrams.py", file=sys.stderr)
        return "```text\n" + src + "```"
    return re.sub(r"```mermaid\n(.*?)```", rep, text, flags=re.S)

def preprocess(text, lang):
    text = mermaid(text)
    lines = [l for l in text.splitlines() if not SWITCH.match(l)]
    # keep the English / Chinese / source lines of a quote on separate lines
    lines = [l + "  " if l.startswith("> ") and not l.startswith("> [!") and i + 1 < len(lines) and lines[i + 1].startswith("> ") else l
             for i, l in enumerate(lines)]
    out, i = [], 0
    while i < len(lines):
        m = re.match(r"^>\s*\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]\s*$", lines[i])
        if m:
            kind = m.group(1).lower()
            body, i = [], i + 1
            while i < len(lines) and lines[i].startswith(">"):
                body.append(re.sub(r"^> ?", "", lines[i])); i += 1
            out += ["", '<div class="callout %s" markdown="1">' % kind, ""] + body + ["", "</div>", ""]
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
                res += ['<p class="callout-label">%s</p>' % l.strip().strip("*"), ""]; prev = ""; continue
        res.append(l); prev = l
    return res

def fix_links(htm, src):
    base = os.path.dirname(os.path.relpath(src, ROOT))
    def rep(m):
        u = m.group(1)
        if re.match(r"^(https?:|mailto:|#|file:)", u): return m.group(0)
        p = os.path.normpath(os.path.join(base, u.split("#")[0]))
        return 'href="%s%s"' % (REPO_URL, p)
    return re.sub(r'href="([^"]+)"', rep, htm)

NAVY, SAND, TERRA = "#112378", "#C9A66B", "#C4573F"
INK, MUTED, PAPER, SANDLT = "#1d2433", "#5b6475", "#fbfaf7", "#f5efe4"

def font_faces():
    faces = []
    for fam, file, w, style in [
        ("Inter", "Inter", 400, "normal"), ("Inter", "Inter", 600, "normal"), ("Inter", "Inter", 700, "normal"),
        ("Inter", "Inter", 800, "normal"), ("Source Serif 4", "SourceSerif4", 400, "normal"),
        ("Source Serif 4", "SourceSerif4", 600, "normal"), ("Source Serif 4", "SourceSerif4-Italic", 400, "italic"),
        ("JetBrains Mono", "JetBrainsMono", 400, "normal"), ("JetBrains Mono", "JetBrainsMono", 700, "normal"),
        ("Noto Sans SC", "NotoSansSC", 400, "normal"), ("Noto Sans SC", "NotoSansSC", 500, "normal"),
        ("Noto Sans SC", "NotoSansSC", 700, "normal")]:
        path = os.path.join(FONT_DIR, f"{file}-{w if file != 'SourceSerif4-Italic' else 400}.ttf")
        if os.path.exists(path):
            faces.append('@font-face { font-family: "%s"; src: url("file://%s"); font-weight: %d; font-style: %s; }' % (fam, path, w, style))
        else:
            print("warning: missing font", path, "(run scripts/fetch_fonts.py)", file=sys.stderr)
    return "\n".join(faces)

def css(lang, t):
    body_font = ('"Source Serif 4", "Noto Sans SC", serif' if lang == "en"
                 else '"Inter", "Noto Sans SC", sans-serif')
    body_size, lh = ("10.4pt", "1.62") if lang == "en" else ("10pt", "1.85")
    sans = '"Inter", "Noto Sans SC", sans-serif'
    mono = '"JetBrains Mono", "Noto Sans SC", monospace'
    edition = t["book"] if BOOK else t["notes"]
    pyg = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    return font_faces() + f"""
@page {{ size: A4; margin: 24mm 20mm 22mm 22mm;
  @top-left {{ content: string(ed, first-except); font: 600 7.5pt {sans}; color: {MUTED}; letter-spacing: .06em; text-transform: uppercase; vertical-align: bottom; padding-bottom: 3mm; }}
  @top-right {{ content: string(chap, first-except); font: 500 7.5pt {sans}; color: {NAVY}; vertical-align: bottom; padding-bottom: 3mm; }}
  @bottom-right {{ content: counter(page); font: 700 8.5pt {sans}; color: {NAVY}; }}
  @bottom-left {{ content: "themodernsoftware.dev · unofficial notes"; font: 400 7pt {sans}; color: #9aa1ad; }}
}}
@page :blank {{ @top-left {{ content: none; }} @top-right {{ content: none; }} @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
@page cover {{ margin: 0; @top-left {{ content: none; }} @top-right {{ content: none; }} @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
@page front {{ @top-left {{ content: none; }} @top-right {{ content: none; }} @bottom-right {{ content: counter(page, lower-roman); font: 600 8pt {sans}; color: {MUTED}; }} @bottom-left {{ content: none; }} }}
@page chapter:first {{ @top-left {{ content: none; }} @top-right {{ content: none; }} }}
html {{ font-family: {body_font}; font-size: {body_size}; line-height: {lh}; color: {INK}; font-weight: 400;
  text-rendering: optimizeLegibility; font-variant-ligatures: common-ligatures; hyphens: auto; }}
body {{ margin: 0; }}
p {{ margin: 0 0 7pt; text-align: justify; orphans: 2; widows: 2; }}
a {{ color: {NAVY}; text-decoration: none; border-bottom: .5pt solid {SAND}; overflow-wrap: anywhere; }}
strong {{ font-weight: 700; color: #0e1a4f; }}
em {{ font-style: italic; }}
h1, h2, h3, h4 {{ font-family: {sans}; color: {NAVY}; line-height: 1.3; break-after: avoid; }}
h2 {{ font-size: 14.5pt; font-weight: 700; margin: 20pt 0 8pt; padding-bottom: 4pt; border-bottom: 1.2pt solid {NAVY}; }}
h2::before {{ content: ""; display: inline-block; width: 5pt; height: 11pt; background: {TERRA}; margin-right: 7pt; vertical-align: -1pt; }}
h3 {{ font-size: 11.5pt; font-weight: 700; margin: 14pt 0 5pt; color: #1b2f8a; bookmark-level: none; }}
h4, h5, h6 {{ font-size: 10.5pt; font-weight: 600; margin: 10pt 0 4pt; bookmark-level: none; }}
ul, ol {{ margin: 0 0 8pt; padding-left: 16pt; }}
li {{ margin: 2pt 0; }}
li::marker {{ color: {TERRA}; font-family: {sans}; font-weight: 700; }}
hr {{ border: none; border-top: .8pt solid {SAND}; margin: 14pt 0; }}

/* chapters */
section.chapter {{ page: chapter; break-before: page; }}
.opener {{ margin: 6mm 0 12mm; position: relative; }}
.opener .label {{ font: 700 8.5pt {sans}; letter-spacing: .22em; text-transform: uppercase; color: {SAND}; }}
.opener .num {{ font: 800 64pt/1 {sans}; color: {TERRA}; margin: 2mm 0 3mm; letter-spacing: -.02em; }}
.opener h1 {{ font-size: 25pt; font-weight: 800; color: {NAVY}; margin: 0; line-height: 1.22; string-set: chap content(), ed "CS146S · {edition}"; bookmark-level: 1; }}
.opener .rule {{ margin-top: 7mm; height: 3pt; background: linear-gradient(to right, {NAVY} 0 60%, {SAND} 60% 85%, {TERRA} 85% 100%); }}

/* diagrams */
.diagram {{ text-align: center; margin: 10pt 0 12pt; padding: 8pt; border: .6pt solid #e6e0d3; border-radius: 4pt; background: #fff; break-inside: avoid; }}
.diagram img {{ max-width: 100%; max-height: 110mm; width: auto; }}

/* code */
code {{ font-variant-ligatures: none; font-family: {mono}; font-size: .86em; background: {SANDLT}; color: #7a2e1f; padding: .5pt 3pt; border-radius: 2pt; }}
pre, .codehilite {{ break-inside: avoid; }}
.codehilite, pre {{ background: #f7f6f2; border: .6pt solid #e6e0d3; border-left: 3pt solid {NAVY}; border-radius: 3pt; padding: 8pt 10pt; margin: 8pt 0 10pt; }}
.codehilite pre {{ border: none; padding: 0; margin: 0; background: none; }}
pre {{ font-variant-ligatures: none; white-space: pre-wrap; font-family: {mono}; font-size: 8.3pt; line-height: 1.55; }}
pre code {{ background: none; padding: 0; color: {INK}; font-size: 1em; }}
{pyg}
.codehilite {{ background: #f7f6f2; }}
.codehilite .k, .codehilite .kn, .codehilite .kd, .codehilite .ow {{ color: {NAVY}; font-weight: 700; }}
.codehilite .s, .codehilite .s1, .codehilite .s2, .codehilite .sd {{ color: #8a5a17; font-style: normal; }}
.codehilite .c, .codehilite .c1, .codehilite .cm {{ color: #8a8f99; font-style: italic; }}
.codehilite .nf, .codehilite .nc {{ color: {TERRA}; font-weight: 700; }}
.codehilite .mi, .codehilite .mf {{ color: #9b3a7a; }}
.codehilite .nb, .codehilite .bp {{ color: #2b6c8f; }}

/* tables */
table {{ border-collapse: collapse; width: 100%; font-family: {sans}; font-size: 8.6pt; line-height: 1.5; margin: 8pt 0 12pt; break-inside: auto; }}
thead {{ display: table-header-group; }}
th {{ background: {NAVY}; color: #fff; font-weight: 600; text-align: left; padding: 5pt 7pt; }}
th:first-child {{ border-top-left-radius: 3pt; }} th:last-child {{ border-top-right-radius: 3pt; }}
td {{ padding: 4.5pt 7pt; border-bottom: .5pt solid #e3ddd0; vertical-align: top; }}
tbody tr:nth-child(even) td {{ background: #f8f6f1; }}
tr {{ break-inside: avoid; }}
td a, th a {{ border-bottom: none; }}

/* quotes & callouts */
blockquote {{ margin: 10pt 0; padding: 6pt 12pt; border-left: 2.5pt solid {SAND}; background: {PAPER}; color: #3e4656; font-style: italic; }}
.callout {{ break-inside: avoid; margin: 12pt 0; padding: 9pt 12pt 4pt; background: #eef1fa; border: .6pt solid #d5dbef; border-left: 4pt solid {NAVY}; border-radius: 4pt; font-size: .95em; }}
.callout.warning, .callout.caution {{ background: #fbefec; border-color: #efd2cb; border-left-color: {TERRA}; }}
.callout.tip {{ background: {SANDLT}; border-color: #eadcc3; border-left-color: {SAND}; }}
.callout-label {{ display: inline-block; font: 700 7.5pt {sans}; letter-spacing: .14em; text-transform: uppercase; color: #fff; background: {NAVY}; padding: 1.5pt 6pt; border-radius: 2pt; margin-bottom: 6pt; }}
.callout table {{ background: #fff; }}
li.task {{ list-style: none; margin-left: -12pt; }}
.box {{ display: inline-block; width: 7pt; height: 7pt; border: 1pt solid {NAVY}; border-radius: 1.5pt; margin-right: 5pt; vertical-align: -.5pt; }}
.box.done {{ background: {NAVY}; }}

/* cover */
.cover {{ page: cover; height: 297mm; width: 210mm; position: relative; background: {NAVY}; color: #fff; overflow: hidden; font-family: {sans}; }}
.cover .grid {{ position: absolute; right: -30mm; top: -30mm; width: 150mm; height: 150mm; border-radius: 50%; border: 1pt solid rgba(201,166,107,.35); }}
.cover .grid2 {{ position: absolute; right: 5mm; top: 5mm; width: 80mm; height: 80mm; border-radius: 50%; border: 1pt solid rgba(201,166,107,.55); }}
.cover .dot {{ position: absolute; right: 38mm; top: 38mm; width: 14mm; height: 14mm; border-radius: 50%; background: {TERRA}; }}
.cover .band {{ position: absolute; left: 0; bottom: 0; width: 210mm; height: 62mm; background: #0c1a5c; }}
.cover .inner {{ position: absolute; left: 22mm; right: 22mm; top: 92mm; }}
.cover .kicker {{ font-weight: 700; font-size: 9pt; letter-spacing: .28em; text-transform: uppercase; color: {SAND}; }}
.cover .bar {{ width: 22mm; height: 3pt; background: {TERRA}; margin: 6mm 0 7mm; }}
.cover h1.title {{ font-size: 40pt; font-weight: 800; line-height: 1.12; margin: 0; color: #fff; bookmark-level: none; string-set: none; }}
.cover .title2 {{ font-size: 22pt; font-weight: 600; color: {SAND}; margin-top: 3mm; }}
.cover .course {{ margin-top: 12mm; font-size: 11.5pt; color: #dfe3f3; font-weight: 500; }}
.cover .edition {{ margin-top: 2mm; font-size: 10pt; color: #aeb6d8; }}
.cover .foot {{ position: absolute; left: 22mm; right: 22mm; bottom: 18mm; font-size: 8pt; color: #b9c0de; line-height: 1.6; }}
.cover .foot b {{ color: {SAND}; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; font-size: 7.5pt; }}
.cover .pill {{ display: inline-block; border: .8pt solid {SAND}; color: {SAND}; border-radius: 10pt; padding: 1pt 8pt; font-size: 8pt; font-weight: 600; letter-spacing: .08em; margin-bottom: 4mm; }}

/* imprint + toc */
.imprint {{ page: front; break-before: page; padding-top: 150mm; font-family: {sans}; font-size: 8.4pt; line-height: 1.7; color: {MUTED}; }}
.imprint h2 {{ font-size: 9pt; letter-spacing: .2em; text-transform: uppercase; color: {NAVY}; border: none; bookmark-level: none; margin: 0 0 4mm; }}
.imprint h2::before {{ display: none; }}
.imprint p {{ text-align: left; margin-bottom: 4pt; }}
.toc {{ page: front; break-before: page; font-family: {sans}; }}
.toc h1 {{ font-size: 26pt; font-weight: 800; color: {NAVY}; margin: 6mm 0 2mm; bookmark-level: 1; }}
.toc .rule {{ height: 3pt; width: 24mm; background: {TERRA}; margin-bottom: 10mm; }}
.toc ul {{ list-style: none; padding: 0; margin: 0; }}
.toc li {{ margin: 0; }}
.toc li.l1 {{ margin-top: 7pt; padding-top: 6pt; border-top: .5pt solid #e6e0d3; font-size: 10.5pt; font-weight: 700; }}
.toc li.l1 .n {{ display: inline-block; width: 22pt; color: {TERRA}; font-weight: 800; }}
.toc li.l2 {{ padding-left: 22pt; font-size: 8.8pt; color: {MUTED}; line-height: 1.75; }}
.toc a {{ color: {INK}; border: none; }}
.toc li.l1 a {{ color: {NAVY}; }}
.toc a::after {{ content: leader(dotted) " " target-counter(attr(href), page); color: #9aa1ad; font-weight: 600; }}
.toc li.l1 a::after {{ color: {NAVY}; }}
"""

MD_EXT = ["tables", "fenced_code", "md_in_html", "sane_lists", "codehilite"]
MD_CFG = {"codehilite": {"guess_lang": False, "css_class": "codehilite"}}

def split_title(raw, lang, t):
    """'第 6 章　代理代码审查' / 'Chapter 6 · X' / 'Week 6 · X' -> (label, number, title)."""
    txt = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
    m = re.match(r"^(第\s*(\d+)\s*([章周讲]))[\s　｜|·:：]*(.*)$", txt) or \
        re.match(r"^((Chapter|Week|Lecture)\s+(\d+))\s*[·:|—-]?\s*(.*)$", txt)
    if m:
        if txt.startswith("第"):
            n, kind, title = m.group(2), m.group(3), m.group(4)
            label = t["chap"].format(n=n) if kind == "章" else t["week"].format(n=n) if kind == "周" else m.group(1)
        else:
            kind, n, title = m.group(2), m.group(3), m.group(4)
            label = (t["chap"] if kind == "Chapter" else t["week"]).format(n=n) if kind != "Lecture" else m.group(1)
        return label, "%02d" % int(n), title or txt
    return t["intro"], "", txt

def build(lang):
    t = dict(TEXT[lang])
    files = ([] if BOOK else [os.path.join(ROOT, t["path"])]) + note_files(lang)
    chapters, toc = [], []
    for n, f in enumerate(files):
        h = markdown.markdown(preprocess(open(f, encoding="utf-8").read(), lang), extensions=MD_EXT, extension_configs=MD_CFG)
        h = fix_links(h, f)
        h = re.sub(r"<li>\s*\[ \]\s*", '<li class="task"><span class="box"></span>', h)
        h = re.sub(r"<li>\s*\[x\]\s*", '<li class="task"><span class="box done"></span>', h)
        k = [0]; first = [True]
        def addid(m):
            k[0] += 1
            lv, attrs, inner = m.group(1), m.group(2), m.group(3)
            hid = "c%d-%d" % (n, k[0])
            title = re.sub(r"<[^>]+>", "", inner)
            if lv == "1" and first[0]:
                first[0] = False
                label, num, ttl = split_title(inner, lang, t)
                toc.append(("1", hid, ttl, num))
                return ('<header class="opener"><div class="label">%s</div>%s<h1 id="%s">%s</h1><div class="rule"></div></header>'
                        % (label, '<div class="num">%s</div>' % num if num else '<div class="num">00</div>', hid, html.escape(ttl)))
            if lv in "12":
                toc.append((lv, hid, title, ""))
            return '<h%s id="%s"%s>%s</h%s>' % (lv, hid, attrs, inner, lv)
        h = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", addid, h, flags=re.S)
        chapters.append('<section class="chapter">%s</section>' % h)
    toc_html = "".join(
        '<li class="l%s"><a href="#%s">%s%s</a></li>' % (lv, i, '<span class="n">%s</span>' % num if lv == "1" else "", tt)
        for lv, i, tt, num in toc)
    today = datetime.date.today().isoformat()
    edition = t["book"] if BOOK else t["notes"]
    cover = f"""<section class="cover"><div class="grid"></div><div class="grid2"></div><div class="dot"></div><div class="band"></div>
<div class="inner"><div class="kicker">CS146S · {edition}</div><div class="bar"></div>
<h1 class="title">{t['title']}</h1><div class="title2">{t['title2']}</div>
<div class="course">{t['course']}</div><div class="edition">{t['term']}</div></div>
<div class="foot"><div class="pill">UNOFFICIAL · CC BY-NC-SA 4.0</div><br/>
<b>{t['src']}</b>&nbsp; github.com/FL-Bin/stanford-ai-course &nbsp;&nbsp; <b>{t['official']}</b>&nbsp; themodernsoftware.dev</div></section>"""
    imprint = f"""<section class="imprint"><h2>{t['imprint']}</h2><p>{t['notice']}</p><p>{t['lic']}</p><p>{t['fonts']}</p>
<p>{t['built']}: {today} · {t['src']}: <a href="https://github.com/FL-Bin/stanford-ai-course">github.com/FL-Bin/stanford-ai-course</a> · <a href="https://themodernsoftware.dev/">themodernsoftware.dev</a></p></section>"""
    doc = f"""<!doctype html><html lang="{'zh-CN' if lang=='zh' else 'en'}"><head><meta charset="utf-8">
<title>{html.escape(t['title'] + ' · ' + t['title2'] + ' · ' + edition)}</title><style>{css(lang, t)}</style></head><body>{cover}{imprint}
<section class="toc"><h1>{t['toc']}</h1><div class="rule"></div><ul>{toc_html}</ul></section>{''.join(chapters)}</body></html>"""
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"CS146S-book-{lang}.pdf" if BOOK else f"CS146S-notes-{lang}.pdf")
    HTML(string=doc, base_url=ROOT).write_pdf(out)
    print("wrote", out)

if __name__ == "__main__":
    for lang in ("zh", "en"):
        build(lang)
