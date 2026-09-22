# BIO321 handout — the cerebellum in *inpp5e* mutants

Course handout for the BIO321 practical (University of Zurich). The Obsidian
note `BIO321 Handout.md` is the single source of truth; the website is built
from it.

## Writing

Edit the note. Headings become sections, `[[#Heading]]` becomes an in-page
link, and an `![[image.png|400]]` embed followed by a bold or italic line
becomes a numbered figure with that line as its caption. Figures are numbered
by the page, so inserting one renumbers the rest.

Ending a heading with `//hidden` keeps it out of the built page and the
contents rail, together with everything under it down to the next heading of
the same or higher level — so `## Experiment 3 //hidden` hides its `###`
subsections too. On a line of its own the marker hides just that line. Inside
a fenced code block it is left alone. Nothing is deleted from the note, and
sections renumber around what is hidden.

`//answer` hides the rest of its line, for answers kept in the note but off
the site and PDF: `1) Why MIPs? //answer Smaller files, faster to process`
shows only the question. A line that starts with `//answer` disappears
entirely, so a longer answer can go on its own line(s) under the question.

## Building

```sh
pip install -r site/requirements.txt
python3 site/serve.py     # http://localhost:8321, rebuilds as you write
python3 site/build.py     # one-off build into site/index.html
python3 site/build.py --pdf   # also print both pages to PDF (needs Chrome)
```

The "Download PDF" button serves `site/BIO321-handout.pdf` and
`site/BIO321-schedule.pdf`, printed by headless Chrome from the pages' own
print stylesheet: A4 (the schedule in landscape), each section on a new page,
a running head with the commit, and page numbers. Chrome is found
automatically; set `CHROME=/path/to/chrome` if it is somewhere unusual. Where no
PDF was built, as in `serve.py` previews, the button opens the print dialog
instead.

`site/index.html` and `site/figures/` are generated and not committed.
`$...$` and `$$...$$` in the note are rendered with KaTeX (loaded from a CDN);
wide tables scroll inside their own box rather than pushing the page out.
Layout and colours live in `site/template.html`. The masthead comes from the
note itself: the page title is the note's filename, or a `title:` in an optional
YAML front-matter block, which also takes `eyebrow:`, `subtitle:` and `notice:`.

```yaml
---
title: The cerebellum in *inpp5e* mutants
eyebrow: BIO321 · Practical course 2026 · University of Zurich
subtitle: A whole-mount immunofluorescence and imaging project in larval zebrafish.
notice: "**Draft handout.** The section text is still being written."
---
```

Pushing to `main` rebuilds and redeploys the site to GitHub Pages.
