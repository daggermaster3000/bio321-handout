#!/usr/bin/env python3
"""Print built pages to PDF with headless Chrome.

Pagination, running heads and page numbers come from the page's own print
stylesheet (`@page` in template.html), so the PDF matches what a reader gets
from the browser's print dialog.
"""
from __future__ import annotations

import os
import shutil
import signal
import subprocess
import time
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


def render(page: Path, out: Path, chrome: str, timeout: float = 120) -> None:
    """Print `page` to `out`. Waits for images and the KaTeX CDN to settle.

    Chrome sometimes writes the file and then lingers instead of exiting, so a
    PDF that has stopped growing counts as done and the process is killed.
    """
    out.unlink(missing_ok=True)
    proc = subprocess.Popen(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--virtual-time-budget=20000",
            "--no-pdf-header-footer",
            "--generate-pdf-document-outline",
            f"--print-to-pdf={out}",
            page.resolve().as_uri(),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    deadline = time.monotonic() + timeout
    last_size, stable_since = -1, 0.0
    try:
        while proc.poll() is None:
            if time.monotonic() > deadline:
                raise RuntimeError(f"Chrome timed out printing {page.name}")
            size = out.stat().st_size if out.exists() else -1
            if size > 0 and size == last_size:
                if time.monotonic() - stable_since > 3:
                    break
            else:
                last_size, stable_since = size, time.monotonic()
            time.sleep(0.5)
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
    if not out.exists() or out.stat().st_size == 0:
        raise RuntimeError(f"Chrome produced no PDF for {page.name}")
