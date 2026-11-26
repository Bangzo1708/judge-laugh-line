"""Make the Judge Laugh in One Line — entry program.

Writes a single one-line joke (200 characters or fewer) to
/output/entry.txt. Pure Python 3.13 standard library, no network,
fully deterministic: the same line is written on every run.

The chosen line
---------------
"I told my houseplants I was going away for the weekend; they held a
meeting and voted to die anyway."

Why this line: the setup is an everyday, relatable act (warning the
plants before a trip, as if they were pets), and the punchline breaks
the expectation twice — first by giving the plants a committee meeting,
then by having them vote, unanimously and pointlessly, to die anyway.
Every word earns its place, the laugh lands on the final word, and a
stranger gets it in one read with no context and no explanation.
"""

from __future__ import annotations

import os
import sys

# The single funny line this entry submits. Exactly 100 characters.
ENTRY_LINE = (
    "I told my houseplants I was going away for the weekend; "
    "they held a meeting and voted to die anyway."
)

# The gate accepts UTF-8 text of 1 to 200 characters, not only
# whitespace. Enforce the same bounds here so a bad line can never
# be written silently.
MIN_LENGTH = 1
MAX_LENGTH = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def validate(line: str) -> str:
    """Check the line against the competition gate and return it."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing whitespace")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            f"entry line must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(line)}"
        )
    # One line only: a newline inside would break the "one line" rule.
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must contain no newline characters")
    return line


def main() -> int:
    line = validate(ENTRY_LINE)
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # Write with an explicit UTF-8 encoding and a single trailing
    # newline so the file is plain text; the newline is not part of
    # the line itself and the gate counts the text as written.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
