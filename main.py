#!/usr/bin/env python3
"""One-Line Robot Wedding Vows -- make.fun bounty entry.

Writes a single funny line of wedding vows for a robot couple
(at most 160 characters) to ``entry.txt`` inside the output directory
the harness provides (``MAKEFUN_OUTPUT_DIR``, which is ``/output``
in the grading sandbox).

Stdlib only. Deterministic: one constant, no network, no randomness,
no clock.
"""

import os

LINE = (
    "I take you to be my lawfully wedded copilot, to have and to hold, "
    "in sickness and in health, in full charge and in airplane mode, "
    "until low battery do us part."
)


def main() -> None:
    # Gate: the sealed scorer only accepts UTF-8 text of 1 to 160
    # characters, not only white space, standing alone on one line.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert LINE.strip() == LINE and LINE, "line must not be blank-padded"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
