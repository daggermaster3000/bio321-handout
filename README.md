# BIO321 handout — the cerebellum in *inpp5e* mutants

Course handout for the BIO321 practical (University of Zurich). The Obsidian
note `BIO321 Handout.md` is the single source of truth; the website is built
from it.

## Writing

Edit the note. Headings become sections, `[[#Heading]]` becomes an in-page
link, and an `![[image.png|400]]` embed followed by a bold or italic line
becomes a numbered figure with that line as its caption. Figures are numbered
by the page, so inserting one renumbers the rest.

## Building

```sh
pip install -r site/requirements.txt
python3 site/serve.py     # http://localhost:8321, rebuilds as you write
python3 site/build.py     # one-off build into site/index.html
```

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
