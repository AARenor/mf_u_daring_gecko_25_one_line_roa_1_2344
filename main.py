#!/usr/bin/env python3
"""Write one short text for make.fun's bounty.

Bounty: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610

The entry text is a single roast line of 83 characters. This program writes
exactly those bytes, with no trailing newline, into the output folder and
prints the character count to stderr.
"""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
