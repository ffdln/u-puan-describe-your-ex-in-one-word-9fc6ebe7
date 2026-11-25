#!/usr/bin/env python3
"""Describe Your Ex in One Word — one word.

The entry is a single fixed word, written for make.fun
u-puan-describe-your-ex-in-one-word-9fc6ebe7: one word describing
an ex, at most 111 characters. My ex is the one who never really
left — every few months the same name pops back up, like a calendar
event nobody can cancel. So the word is Recurring. This program
writes that word to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The word is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

WORD = "Recurring"


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the word against the gate, then write it out."""
    if not 1 <= len(WORD) <= 111:
        return abort(f"word is {len(WORD)} characters, the gate allows 1-111")
    if not WORD.strip():
        return abort("word is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD, encoding="utf-8")
    print(f"wrote {target}: {len(WORD)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
