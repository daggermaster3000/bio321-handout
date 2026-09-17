#!/usr/bin/env python3
"""Print built pages to PDF with headless Chrome.

Pagination, running heads and page numbers come from the page's own print
stylesheet (`@page` in template.html), so the PDF matches what a reader gets
from the browser's print dialog.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


def find_chrome() -> str | None:
    env = os.environ.get("CHROME")
    for name in ([env] if env else []) + CANDIDATES:
        path = name if os.path.isabs(name) else shutil.which(name)
        if path and os.path.exists(path):
            return path
    return None


def render(page: Path, out: Path, chrome: str) -> None:
    """Print `page` to `out`. Waits for images and the KaTeX CDN to settle."""
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--no-first-run",
                f"--user-data-dir={profile}",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=20000",
                "--no-pdf-header-footer",
                "--generate-pdf-document-outline",
                f"--print-to-pdf={out}",
                page.resolve().as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=180,
        )
    if not out.exists() or out.stat().st_size == 0:
        raise RuntimeError(f"Chrome produced no PDF for {page.name}")
