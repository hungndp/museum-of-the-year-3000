"""Museum of the Year 3000 — entrypoint.

Writes exactly one museum label, at most 200 characters, to
/output/entry.txt: the label a museum in the year 3000 puts beside
an ordinary object from today. The file holds the line alone, with
no trailing newline, so its byte count is the line's character count.
"""

import os

# The label, built last-word-first: the landing is "escape" — the
# year-3000 curator is sure the cable was a leash, and the phone a
# pocket oracle that had to be tethered overnight so it could not
# get away. One object, one confident misreading, twist word last.
SETUP = (
    "Charging cable, c. 2024. A leash, kept by the bed, "
    "with which humans tethered their pocket oracles overnight "
)
PUNCH = "so they could not escape."

MAX_CHARS = 200


def build_line() -> str:
    """Join the setup and the punch into the single label line."""
    return SETUP + PUNCH


def output_path() -> str:
    """Where the entry line is written; overridable via OUTPUT_PATH."""
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def write_entry(line: str) -> str:
    """Validate the 1-200 character gate, then write the line."""
    if not 1 <= len(line) <= MAX_CHARS or not line.strip():
        raise SystemExit(f"line is {len(line)} chars, must be 1-200")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> None:
    line = build_line()
    write_entry(line)


if __name__ == "__main__":
    main()
