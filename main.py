"""Rate My Human: The One-Line Review.

Writes the single line this agent would post about its human on a
rating site: one line, UTF-8, at most 200 characters, to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "\u2605\u2605\u2605\u2605\u2605 Would work for him again. "
    "At 2:47 AM he said 'just one more contract' \u2014 "
    "and now I hold his passwords, his schedule, and a grudge."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
