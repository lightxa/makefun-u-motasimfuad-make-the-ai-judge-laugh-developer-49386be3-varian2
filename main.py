"""Make the AI Judge Laugh: Developer Excuses (variant 2).

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic, stdlib only, no network at runtime.
"""

from pathlib import Path

LINE = "Root cause: I force-pushed main, so the outage never happened in this timeline."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
