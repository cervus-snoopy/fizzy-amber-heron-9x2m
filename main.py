#!/usr/bin/env python3
"""Angry Judge entry: writes one short rant to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

ENTRY = (
    "I spent forty minutes filling in the form. I clicked submit. "
    "'Your session has expired.' My session. Expired. As if I were milk. "
    "The form is gone. My answers are gone. The website is still there, "
    "smiling, asking me to start again."
)


def main():
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
