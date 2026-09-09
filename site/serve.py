#!/usr/bin/env python3
"""Serve the handout locally and rebuild whenever the note or template changes.

    python3 site/serve.py          # http://localhost:8321
    python3 site/serve.py 9000     # pick another port
"""
from __future__ import annotations

import functools
import http.server
import socketserver
import sys
import threading
import time
from pathlib import Path

import build

SITE = Path(__file__).resolve().parent
WATCHED = [build.NOTE, build.TEMPLATE, Path(__file__).parent / "build.py"]
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8321


def stamp() -> tuple[float, ...]:
    files = list(WATCHED)
    if build.ATTACHMENTS.exists():
        files += sorted(build.ATTACHMENTS.iterdir())
    return tuple(f.stat().st_mtime for f in files if f.exists())


def watch() -> None:
    last = stamp()
    while True:
        time.sleep(0.7)
        now = stamp()
        if now != last:
            last = now
            try:
                build.main()
            except Exception as exc:  # keep serving the last good build
                print(f"  ! build failed: {exc}", file=sys.stderr)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt: str, *args) -> None:
        pass  # the rebuild lines are the only output worth reading


def main() -> None:
    build.main()
    threading.Thread(target=watch, daemon=True).start()
    handler = functools.partial(Handler, directory=str(SITE))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"serving http://localhost:{PORT}  —  watching for changes, ctrl-C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped")


if __name__ == "__main__":
    main()
