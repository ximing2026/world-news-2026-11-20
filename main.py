#!/usr/bin/env python3
"""Place the bundled poster image at /output/entry.png."""

import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST = os.path.join("/output", "entry.png")


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open(SOURCE, "rb") as handle:
        magic = handle.read(len(PNG_SIGNATURE))
    if magic != PNG_SIGNATURE:
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) > MAX_BYTES:
        print("entry.png is larger than 1 MiB", file=sys.stderr)
        return 1
    shutil.copyfile(SOURCE, DEST)
    print("wrote /output/entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
