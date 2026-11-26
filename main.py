"""One Word From Your Ex — writes the entry to /output/entry.txt.

The word: Placeholder — the word an ex would use for someone kept around
until something better came along.
"""

import os
import sys

WORD = "Placeholder"


def _check(text: str) -> None:
    if not (1 <= len(text) <= 24):
        sys.exit(f"gate: entry is {len(text)} chars, need 1-24")
    if not text.strip():
        sys.exit("gate: entry is only whitespace")
    if len(text.split()) != 1:
        sys.exit("gate: entry must be exactly one word")
    if not text.isalpha():
        sys.exit("gate: entry must be a single alphabetic word")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _check(WORD)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {len(WORD.encode('utf-8'))} bytes to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
