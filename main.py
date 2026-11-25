#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes the two-part micro-confession to /output/entry.txt.
Pure stdlib; no third-party imports.
"""

import os

PART_A = "To: Dad\n"
PART_B = (
    "I know about the letter from the hospital. "
    "I found it in your coat pocket in January and put it back. "
    "I listen to your breathing at night now."
)

ENTRY = PART_A + PART_B

assert 1 <= len(ENTRY) <= 260, "entry outside the 1-260 char gate"
assert ENTRY.strip(), "entry is only whitespace"
assert ENTRY.startswith("To: "), "missing To: line"
assert ENTRY.count("\n") == 1, "entry must be exactly two lines"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
