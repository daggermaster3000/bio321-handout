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
import subprocess
import sys
from pathlib import Path

import markdown

import pdf
import schedule as schedule_sheet

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "BIO321 Handout.md"
ATTACHMENTS = ROOT / "attachments"
SITE = Path(__file__).resolve().parent
TEMPLATE = SITE / "template.html"
OUT = SITE / "index.html"
SCHEDULE = ROOT / "Schedule.xlsx"
SCHEDULE_OUT = SITE / "schedule.html"
# The PDFs sit next to the pages they are printed from.
HANDOUT_PDF = "BIO321-handout.pdf"
SCHEDULE_PDF = "BIO321-schedule.pdf"
FIGURES = SITE / "figures"

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}


def git(*args: str) -> str:
    """Run a git command in the repository, or return "" if that is not possible."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), *args],
            capture_output=True, text=True, timeout=10, check=True,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip()


def commit_url(sha: str) -> str:
    """Turn the origin remote into a browsable commit link, ssh or https."""
    remote = git("remote", "get-url", "origin")
    m = re.match(r"(?:git@([^:]+):|https://(?:[^@]+@)?([^/]+)/)(.+?)(?:\.git)?$", remote)
    if not m:
        return ""
    host, path = m.group(1) or m.group(2), m.group(3)
    return f"https://{host}/{path}/commit/{sha}"


def version_text() -> str:
    """Short provenance for the running head of printed pages."""
    sha, date = git("log", "-1", "--format=%h"), git("log", "-1", "--format=%cs")
    return " · ".join(x for x in (sha, date) if x)


def version_stamp() -> str:
    """Stamp the page with the commit it was built from."""
    sha, subject = git("log", "-1", "--format=%h"), git("log", "-1", "--format=%s")
    if not sha:
        return ""
    date = git("log", "-1", "--format=%cs")
    dirty = " + uncommitted changes" if git("status", "--porcelain") else ""
    url = commit_url(sha)
    label = f'<code>{html.escape(sha)}</code>' if not url else (
        f'<a href="{html.escape(url)}"><code>{html.escape(sha)}</code></a>'
    )
    return (
        '<p class="version">'
        + label
        + (f" · {html.escape(date)}" if date else "")
        + f'<span>{html.escape(subject)}{html.escape(dirty)}</span>'
        + "</p>"
    )


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


HIDDEN = re.compile(r"\s*//hidden\s*$", re.I)


def strip_hidden(md: str) -> str:
    """Drop headings marked `//hidden`, along with everything beneath them.

    The marker hides a heading down to the next heading of the same or higher
    level, so hiding `## Experiment 3` also hides its `###` subsections. On a
    line of its own it hides that line alone. Markers inside fenced code
    blocks are left as written.
    """
    out: list[str] = []
    fence = None
    skip_level = 0

    for line in md.split("\n"):
        fence_match = re.match(r"\s*(```+|~~~+)", line)
        if fence_match:
            token = fence_match.group(1)[0]
            fence = None if fence and token == fence else (fence or token)
        if fence:
            if not skip_level:
                out.append(line)
            continue

        heading = re.match(r"(#{1,6})\s", line)
        if skip_level:
            # Stay inside the hidden block until a heading climbs back out.
            if heading and len(heading.group(1)) <= skip_level:
                skip_level = 0
            else:
                continue

        if HIDDEN.search(line):
            if heading:
                skip_level = len(heading.group(1))
            continue  # a bare `//hidden` line hides only itself
        out.append(line)

    return "\n".join(out)


def preprocess(md: str) -> str:
    """Turn Obsidian-only syntax into HTML markdown-python will pass through."""
    # Drop the Obsidian table-of-contents plugin block; the rail replaces it.
    md = re.sub(r"^```table-of-contents\n.*?^```\n?", "", md, flags=re.S | re.M)
    md = strip_hidden(md)
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

        # A heading with nothing under it gets a visible placeholder. A heading
        # followed by a deeper one is not empty — its subsections are its body.
        def placeholder(mm: re.Match) -> str:
            level, gap, following = mm.group(1), mm.group(2), mm.group(3)
            if following and int(following) > int(level):
                return mm.group(0)
            return f"</h{level}>\n{TODO}{gap}"

        rest = re.sub(r"</h([234])>(\s*)(?=<h([234])|\Z)", placeholder, rest)
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


def css_string(text: str) -> str:
    """Make text safe inside a double-quoted CSS string."""
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def rail_link(href: str, label: str) -> str:
    """A standalone link under the contents rail, to the site's other page."""
    return f'<p class="rail-link"><a href="{html.escape(href)}">{html.escape(label)}</a></p>'


def write_page(
    out: Path,
    *,
    title: str,
    content: str,
    toc: str,
    version: str = "",
    eyebrow: str = "",
    subtitle: str = "",
    notice: str = "",
    rail: str = "",
    main_class: str = "",
    pdf_name: str = "",
    page_size: str = "A4",
    print_version: str = "",
) -> None:
    plain_title = re.sub(r"<[^>]+>", "", inline_md(title))
    button = (
        f'<a class="pdf-button" href="{html.escape(pdf_name)}" download>'
        '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" '
        'stroke-width="1.5"><path d="M8 2v8m0 0-3-3m3 3 3-3M3 13h10"/></svg>'
        "Download PDF</a>"
        if pdf_name
        else ""
    )
    page = TEMPLATE.read_text(encoding="utf-8")
    for key, value in {
        "{{PDF_BUTTON}}": button,
        "{{PAGE_SIZE}}": page_size,
        "{{PRINT_TITLE}}": css_string(html.unescape(plain_title)),
        "{{PRINT_VERSION}}": css_string(print_version),
        "{{TITLE}}": html.escape(plain_title),
        "{{EYEBROW}}": eyebrow,
        "{{HEADING}}": inline_md(title),
        "{{SUBTITLE}}": subtitle,
        "{{NOTICE}}": notice,
        "{{VERSION}}": version,
        "{{TOC}}": toc,
        "{{RAIL_EXTRA}}": rail,
        "{{MAIN_CLASS}}": main_class,
        "{{CONTENT}}": content,
    }.items():
        page = page.replace(key, value)
    out.write_text(page, encoding="utf-8")
    print(f"built {out.relative_to(ROOT)}  ({len(page):,} bytes)")


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

    stamp = version_stamp()

    # Read the schedule first: the handout only links to it if it can be built.
    weeks = toc_weeks = ""
    if SCHEDULE.exists():
        try:
            toc_weeks = schedule_sheet.nav(SCHEDULE)
            weeks = schedule_sheet.render(SCHEDULE)
        except Exception as exc:  # a missing openpyxl, or a re-shaped sheet
            print(f"  ! schedule not built: {exc}", file=sys.stderr)
            SCHEDULE_OUT.unlink(missing_ok=True)

    write_page(
        OUT,
        title=title,
        eyebrow=optional("eyebrow", "p", "eyebrow"),
        subtitle=optional("subtitle", "p", "sub"),
        notice=optional("notice", "p", "notice"),
        version=stamp,
        toc=toc,
        content=content,
        rail=rail_link("schedule.html", "Course schedule") if weeks else "",
        pdf_name=HANDOUT_PDF,
        print_version=version_text(),
    )
    if weeks:
        write_page(
            SCHEDULE_OUT,
            title="Course schedule",
            subtitle='<p class="sub">Four weeks of the BIO321 practical, '
            "half-hour by half-hour.</p>",
            version=stamp,
            toc=toc_weeks,
            content=weeks,
            rail=rail_link("index.html", "Back to the handout"),
            main_class="wide",
            pdf_name=SCHEDULE_PDF,
            page_size="A4 landscape",
            print_version=version_text(),
        )


def make_pdfs() -> None:
    chrome = pdf.find_chrome()
    if not chrome:
        print("  ! no Chrome/Chromium found; PDFs not built (set CHROME=...)", file=sys.stderr)
        return
    jobs = [(OUT, SITE / HANDOUT_PDF)]
    if SCHEDULE_OUT.exists():
        jobs.append((SCHEDULE_OUT, SITE / SCHEDULE_PDF))
    for page, out in jobs:
        try:
            pdf.render(page, out, chrome)
        except Exception as exc:
            print(f"  ! PDF of {page.name} failed: {exc}", file=sys.stderr)
            continue
        print(f"built {out.relative_to(ROOT)}  ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
    if "--pdf" in sys.argv[1:]:
        make_pdfs()
