#!/usr/bin/env python3
"""Copy the bundled poster to /output/entry.png (byte-identical)."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(SRC, "rb") as f:
        magic = f.read(8)
    if magic[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if os.path.getsize(SRC) > 1_048_576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))
    print("wrote /output/entry.png")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
