#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one original single-line safety warning label for every human
being to /output/entry.txt. The label is a fixed, hand-written string:
deterministic, no network, no randomness, no input files.
"""

import os

LABEL = (
    "WARNING: This human may, without warning, explain things it has "
    "never actually done."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
