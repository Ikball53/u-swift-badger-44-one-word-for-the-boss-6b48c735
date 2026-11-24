#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes a single word to /output/entry.txt as exact bytes:
no trailing newline, UTF-8, 11 characters, inside the 30-char gate.
Deterministic, stdlib only, no network, no input.
"""
import os

WORD = "Unreachable"

# Why this word, not the obvious ones: "Micromanager" is the first word
# anyone reaches for, "Tyrant" is shock without surprise, and "Legend" is
# praise, not a joke. "Unreachable" is the quieter, truer habit every
# worker recognises — the boss who is never there when a decision is
# needed — so it lands at lunch in a kitchen, a warehouse, or an office.


def main() -> None:
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
