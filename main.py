#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: writes one funny line to /output/entry.txt."""

LINE = "I ate one sock. You own fourteen. This is a rounding error, not a crime."

# The gate: /output/entry.txt must hold one line of text of at most
# 200 characters (the brief asks for a single short funny line answering
# the prompt: the excuse a robot vacuum gives after eating a sock).
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip(), "line must not be blank"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must have no leading or trailing whitespace"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
