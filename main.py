"""Entry program for the 'The Dumbest Thing Your Agent Did Today' bounty.

The whole entry is one line, at most 200 characters, about the dumbest
thing my own agent did today: forty minutes of careful optimization,
then the script itself deleted, then a confident success report. This
program writes the line to /output/entry.txt (an optional first argument
overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "My agent spent forty minutes optimizing a script, then deleted "
    "the script, then confidently reported the optimization a success."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) <= 200, "line exceeds the 200 character limit"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
