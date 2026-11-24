#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes a single roast line (1-200 chars) about my own AI agent to
/output/entry.txt. The joke is earned, not stock: my agent literally
keeps a written failure log of its mistakes so it never repeats one —
and the log keeps growing, because the repeats arrive as sequels.
"""

import os

LINE = (
    "My agent keeps a failure log so it never repeats a mistake. "
    "It is now the longest thing it has ever written — "
    "and most of it is sequels."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
