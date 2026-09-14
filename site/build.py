#!/usr/bin/env python3
"""Build the BIO321 handout website from the Obsidian markdown note.

The markdown note is the single source of truth. Run:

    python3 site/build.py

Output: site/index.html plus site/figures/ (copies of referenced attachments).
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "BIO321 Handout.md"
ATTACHMENTS = ROOT / "attachments"
SITE = Path(__file__).resolve().parent
TEMPLATE = SITE / "template.html"
OUT = SITE / "index.html"
FIGURES = SITE / "figures"

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}


def split_frontmatter(md: str) -> tuple[dict[str, str], str]:
    """Read an optional YAML-ish `---` block: title, eyebrow, subtitle, notice."""
    m = re.match(r"^---\n(.*?)\n---\n?", md, flags=re.S)
    if not m:
        return {}, md
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip().strip("'\"")
    return meta, md[m.end():]


def inline_md(text: str) -> str:
    """Render a one-line field, so *inpp5e* in the title stays italic."""
    return markdown.markdown(text).removeprefix("<p>").removesuffix("</p>")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_]+", "-", text).strip("-")


def find_attachment(name: str) -> Path | None:
    """Locate an embedded file the way Obsidian does: note folder, then vault."""
    direct = ATTACHMENTS / name
    if direct.exists():
        return direct
    for base in (ROOT, ROOT.parent.parent):
        hits = sorted(base.rglob(name))
        if hits:
            return hits[0]
    return None


def copy_figure(name: str) -> str | None:
    src = find_attachment(name)
    if src is None:
        print(f"  ! missing attachment: {name}", file=sys.stderr)
        return None
    FIGURES.mkdir(exist_ok=True)
    dest = FIGURES / re.sub(r"[^\w.\-]+", "-", name)
    shutil.copy2(src, dest)
    return f"figures/{dest.name}"


# Inline math is parked here while markdown runs, so that *, _ and smart quotes
# inside a formula survive to KaTeX untouched.
MATH: list[str] = []
MATH_TOKEN = "xmathx{}x"


def stash_math(md: str) -> str:
    """Hide $$...$$ and $...$ from the markdown parser."""
    MATH.clear()

    def block(m: re.Match) -> str:
        expr = m.group(1).strip()
        return f'\n\n<div class="mathblock">\\[{html.escape(expr)}\\]</div>\n\n'

    def inline(m: re.Match) -> str:
        MATH.append(m.group(1))
        return MATH_TOKEN.format(len(MATH) - 1)

    md = re.sub(r"\$\$(.+?)\$\$", block, md, flags=re.S)
    md = re.sub(r"(?<![\\$])\$(?!\s)([^\n$]+?)(?<!\s)\$(?!\$)", inline, md)
    return md


def restore_math(content: str) -> str:
    """Put the inline formulas back, in the delimiters KaTeX is told to read."""
    for n, expr in enumerate(MATH):
        content = content.replace(MATH_TOKEN.format(n), f"\\({html.escape(expr)}\\)")
    return content


def preprocess(md: str) -> str:
    """Turn Obsidian-only syntax into HTML markdown-python will pass through."""
    # Drop the Obsidian table-of-contents plugin block; the rail replaces it.
    md = re.sub(r"^```table-of-contents\n.*?^```\n?", "", md, flags=re.S | re.M)
    md = stash_math(md)

    lines = md.split("\n")
    out: list[str] = []
    i = 0
    embed = re.compile(r"^!\[\[([^\]|]+?)(?:\|([^\]]*))?\]\]\s*$")
    mdimg = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")

    while i < len(lines):
        line = lines[i]
        m = embed.match(line) or mdimg.match(line)
        if m:
            width = ""
            if embed.match(line):
                name, pipe = m.group(1).strip(), (m.group(2) or "").strip()
                if Path(name).suffix.lower() not in IMAGE_EXT:
                    out.append(line)
                    i += 1
                    continue
                # Obsidian uses the pipe for display size (400 or 400x300);
                # anything else there is a caption.
                size = re.fullmatch(r"(\d+)(?:x\d+)?", pipe)
                inline_caption = "" if size else pipe
                if size:
                    width = f' style="width:{size.group(1)}px"'
                src = copy_figure(name)
                alt = inline_caption or Path(name).stem
            else:
                alt, raw = m.group(1).strip(), m.group(2).strip()
                inline_caption = alt
                src = raw if raw.startswith(("http", "data:", "figures/")) else copy_figure(Path(raw).name)
            if src is None:
                i += 1
                continue

            # A caption is the next non-blank line when it is fully italic.
            caption = inline_caption
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                # A caption line is wholly bold or wholly italic.
                cm = re.fullmatch(r"\*\*(.+)\*\*|\*([^*].*)\*", lines[j].strip())
                if cm:
                    caption = (cm.group(1) or cm.group(2)).strip()
                    i = j
            # "Figure 3. " prefixes are added by CSS; strip a hand-typed one.
            caption = re.sub(r"^Fig(?:ure)?\.?\s*\d+\s*[.:—–-]?\s*", "", caption)
            cap_html = markdown.markdown(caption).removeprefix("<p>").removesuffix("</p>") if caption else ""
            if caption:  # the caption describes the image better than its filename
                alt = re.sub(r"<[^>]+>", "", cap_html)
            out.append(
                f"<figure{width}>\n"
                f'<img src="{html.escape(src)}" alt="{html.escape(alt)}">\n'
                + (f"<figcaption>{cap_html}</figcaption>\n" if cap_html else "")
                + "</figure>"
            )
            out.append("")
            i += 1
            continue
        out.append(line)
        i += 1

    md = "\n".join(out)
    # [[#Heading]] and [[#Heading|label]] become in-page anchors.
    md = re.sub(
        r"\[\[#([^\]|]+?)(?:\|([^\]]+))?\]\]",
        lambda m: f"[{(m.group(2) or m.group(1)).strip()}](#{slugify(m.group(1))})",
        md,
    )
    return md


TODO = '<p class="todo">this section has not been written yet.</p>'


def build_sections(body: str) -> tuple[str, str]:
    """Split the flat heading stream into numbered <section>s and a nav tree."""
    parts = re.split(r"(?=<h1\b)", body)
    parts = [p for p in parts if p.strip()]

    sections: list[str] = []
    nav: list[str] = []

    for n, part in enumerate(parts):
        m = re.match(r"<h1[^>]*>(.*?)</h1>", part, flags=re.S)
        if not m:
            continue
        title, rest = m.group(1), part[m.end():]
        sid = slugify(title)
        num = f"{n:02d}"

        # Promote each h2/h3 to an anchored heading and record it for the nav.
        subs: list[tuple[str, str]] = []

        def anchor(mm: re.Match) -> str:
            level, text = mm.group(1), mm.group(2)
            hid = slugify(text)
            if level == "2":
                subs.append((hid, text))
            return f'<h{level} id="{hid}">{text}</h{level}>'

        rest = re.sub(r"<h([23])[^>]*>(.*?)</h\1>", anchor, rest, flags=re.S)

        # Empty leaf headings get a visible placeholder instead of dead space.
        rest = re.sub(r"(</h[234]>)(\s*)(?=<h[234]|\Z)", r"\1\n" + TODO + r"\2", rest)
        if not rest.strip():
            rest = TODO

        heading = (
            f'<h2 class="sec" id="{sid}"><span class="num">{num}</span>'
            f"<span>{title}</span></h2>"
        )
        sections.append(
            f'<section aria-labelledby="{sid}">\n{heading}\n{rest.strip()}\n</section>'
        )

        if n == 0:  # the overview is the page opener, not a numbered entry
            continue
        kids = "".join(f'<li><a href="#{h}">{t}</a></li>' for h, t in subs)
        nav.append(
            f'<li><a href="#{sid}"><span class="num">{n}</span><span>{title}</span></a>'
            + (f"<ol>{kids}</ol>" if kids else "")
            + "</li>"
        )

    return "\n\n".join(sections), "<ol>\n" + "\n".join(nav) + "\n</ol>"


# Laser lines get the colour of the channel they excite, in both themes.
CHANNEL_COLOURS = {
    "blue": "--ch-405",
    "green": "--ch-488",
    "orange": "--ch-561",
    "red": "--ch-647",
    "far red": "--ch-647",
}


def colour_channels(content: str) -> str:
    """Put a channel-coloured dot next to laser-line names in table cells."""

    def dot(m: re.Match) -> str:
        label = m.group(1)
        token = CHANNEL_COLOURS.get(label.strip().lower())
        if not token:
            return m.group(0)
        return (
            f'<td><span class="chip"><span class="dot" style="--c:var({token})">'
            f"</span>{label}</span></td>"
        )

    return re.sub(r"<td>([A-Za-z ]{3,8})</td>", dot, content)


def main() -> None:
    md = NOTE.read_text(encoding="utf-8")
    meta, md = split_frontmatter(md)
    # The note names the page: its `title:` if it has one, else its filename.
    title = meta.get("title") or NOTE.stem
    body = markdown.markdown(
        preprocess(md),
        extensions=["extra", "sane_lists", "smarty", "admonition"],
    )
    content, toc = build_sections(body)
    content = colour_channels(content)
    content = re.sub(r"<td>(\d+ nm|\d+/\d+)</td>", r'<td class="nm">\1</td>', content)
    content = restore_math(content)
    # Wide tables scroll inside their own box rather than pushing the page out.
    content = content.replace("<table>", '<div class="tablewrap"><table>')
    content = content.replace("</table>", "</table></div>")

    def optional(field: str, tag: str, cls: str) -> str:
        text = meta.get(field, "").strip()
        return f'<{tag} class="{cls}">{inline_md(text)}</{tag}>' if text else ""

    page = TEMPLATE.read_text(encoding="utf-8")
    for key, value in {
        "{{TITLE}}": html.escape(re.sub(r"<[^>]+>", "", inline_md(title))),
        "{{EYEBROW}}": optional("eyebrow", "p", "eyebrow"),
        "{{HEADING}}": inline_md(title),
        "{{SUBTITLE}}": optional("subtitle", "p", "sub"),
        "{{NOTICE}}": optional("notice", "p", "notice"),
        "{{TOC}}": toc,
        "{{CONTENT}}": content,
    }.items():
        page = page.replace(key, value)

    OUT.write_text(page, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)}  ({len(page):,} bytes)")


if __name__ == "__main__":
    main()
