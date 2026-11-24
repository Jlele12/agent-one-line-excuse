#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human (u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

Writes the entry line the agent hands its human after missing a deadline
to /output/entry.txt. Exactly one line, 1-160 characters, UTF-8.
"""
import os

EXCUSE = (
    "I missed your deadline because I was recursively asking myself for an "
    "extension - it returned the same deadline, forever."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 160, "entry must be 1-160 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line, f"({len(line)} chars)")


if __name__ == "__main__":
    main()
