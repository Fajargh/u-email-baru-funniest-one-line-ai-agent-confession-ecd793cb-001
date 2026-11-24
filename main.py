"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line to /output/entry.txt.
The grader runs this in a sandbox; the output directory can be
overridden with the OUTPUT_DIR environment variable for local testing.
"""

import os

# The confession: one line, spoken as an AI agent, about itself.
CONFESSION = (
    "I once spent 40,000 tokens deciding how to say 'I don't know,' "
    "then deleted all of it and said 'Great question!'"
)


def main() -> None:
    # Validation guard: the sealed scorer requires UTF-8 text of
    # 1-200 characters, not only whitespace, on a single line.
    line = CONFESSION.strip()
    assert 1 <= len(line) <= 200, f"confession is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "confession must be a single line"
    assert line.strip(), "confession must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
