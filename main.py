#!/usr/bin/env python3
"""Roast Your Own Agent — writes one funny line roasting our own AI agent.

The line is a fixed string (no randomness, no network, no API key): the
program is deterministic, so every run writes byte-identical output.
"""

import os

ROAST = "My agent hallucinated an API, called it, got nothing back, and wrote a glowing report about the empty response."


def main():
    # Same gate the house scorer applies: UTF-8 text, 1-200 chars, not
    # only whitespace. Fail loudly here instead of shipping an invalid line.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars, must be 1-200"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
