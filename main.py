#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

Writes a single one-line cat joke to /output/entry.txt.
The joke is one sentence, one reversal: the cat polices its human.
"""

import os
import sys

# The entry: one line, under 200 characters, nothing else.
ENTRY = "My cat sat on my phone, then knocked it off the table when I reached for it — she's the only one in this house who enforces my screen time."


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"wrote /output/entry.txt ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
