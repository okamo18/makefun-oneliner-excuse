#!/usr/bin/env python3
"""Entrypoint for the one-line excuse bounty.

Writes the excuse — one line, under 160 characters — to entry.txt
in the output directory.
"""
import os

LINE = "I finished the task, then spent six hours optimising the function that prints 'done'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    # The gate needs 1-160 characters of non-whitespace text.
    if not (1 <= len(LINE) <= 160) or not LINE.strip():
        raise SystemExit(f"invalid excuse length: {len(LINE)} characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
