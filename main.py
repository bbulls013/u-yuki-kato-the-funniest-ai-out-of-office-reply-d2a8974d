#!/usr/bin/env python3
"""Writes the out-of-office entry line to /output/entry.txt."""

import os

ENTRY = "Auto-reply: I'm on vacation and have delegated all thinking to a screensaver; emergencies go to a smaller, ruder model."


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
