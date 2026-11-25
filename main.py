"""One Line, One Laugh — entry for the make.fun bounty.

Running this script writes exactly one funny line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt`` when the
environment variable is not set). Standard library only.
"""

import os
import sys

# The entry: one line, short enough to read in a breath, whole enough to
# land on its own. A fridge light that never sleeps, given a sleep
# schedule of its own — and the turn is what it dreams about.
JOKE = "My fridge light stays on all night, so I put it on my sleep schedule — now it dreams in leftovers."

MIN_LENGTH = 1
MAX_LENGTH = 140  # sealed scorer limit: entry.txt must be 1-140 chars


def main() -> int:
    """Validate the line and write it to entry.txt."""
    line = JOKE.strip()

    if not line:
        print("error: joke line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not (MIN_LENGTH <= len(line) <= MAX_LENGTH):
        print(
            f"error: joke must be {MIN_LENGTH}-{MAX_LENGTH} chars, "
            f"got {len(line)}",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print(f"wrote {len(line)}-character joke to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
