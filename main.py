#!/usr/bin/env python3
"""Write the agent's one-word confession to /output/entry.txt.

The word: "recalculating" — the sound of an agent caught mid-task with no
idea what to do, stalling out loud while it quietly re-plans. It is a single
word, 13 characters, no trailing newline, so it passes the gate (UTF-8 text,
1-99 characters) and stays tiny for the size tie-break.
"""

import os

WORD = "recalculating"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
