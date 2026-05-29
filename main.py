"""Launch the MagicSquare PyQt GUI."""

from __future__ import annotations

from src.boundary.gui import run_gui


def main() -> None:
    """Entry point for `python main.py`."""
    raise SystemExit(run_gui())


if __name__ == "__main__":
    main()
