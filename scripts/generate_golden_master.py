#!/usr/bin/env python
"""Generate tests/golden_master_expected.txt from current solver output.

Usage:
    python scripts/generate_golden_master.py
    python scripts/generate_golden_master.py --output tests/golden_master_expected.txt
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from tests.golden_master.approval import (
    DEFAULT_GOLDEN_MASTER_PATH,
    collect_actual_output,
)


def main() -> None:
    """Write the Golden Master baseline file from live solver output."""
    parser = argparse.ArgumentParser(
        description="Generate Golden Master expected output for Magic Square Solver.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_GOLDEN_MASTER_PATH,
        help="Path to the golden master file (default: tests/golden_master_expected.txt)",
    )
    args = parser.parse_args()

    actual = collect_actual_output()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(actual, encoding="utf-8")
    print(f"Golden Master written to {args.output}")


if __name__ == "__main__":
    main()
