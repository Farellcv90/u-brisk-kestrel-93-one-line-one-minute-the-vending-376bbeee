"""One Line, One Minute: The Vending Machine Pickup Line Contest — one-line entry.

Writes the pickup line to /output/entry.txt (UTF-8, 1-200 chars).

Why this line: the vending machine's coin return is the one part of the
machine that always gives something back — the joke flips it into the one
thing it cannot give back, the person. The em dash splits the setup from
the turn in a single breath, so the whole line reads in well under a
minute. At 99 characters it sits comfortably inside the 1-200 gate with
room to spare, and it is a single line with no line breaks.
"""

LINE = (
    "My coin return has given back thousands of quarters \u2014 "
    "you're the first person I wish it could keep."
)


def load_line():
    """Return the entry pickup line text."""
    return LINE


def validate_line(line):
    """Check the gate: UTF-8, 1-200 chars, a single line, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no line breaks)")
    if len(line) > 200:
        raise ValueError("line exceeds 200 characters: %d" % len(line))
    line.encode("utf-8")
    return line


def write_entry(line, path="/output/entry.txt"):
    """Write the validated line to path, creating parent dirs as needed."""
    import os

    validate_line(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    return path


def main():
    line = load_line()
    path = write_entry(line)
    print("Wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()
