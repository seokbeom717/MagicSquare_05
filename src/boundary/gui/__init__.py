"""PyQt GUI boundary package for MagicSquare."""

from __future__ import annotations

__all__ = ["run_gui"]


def run_gui() -> int:
    """Launch the desktop GUI (lazy import avoids PyQt6 at package import)."""
    from src.boundary.gui.app import run_gui as _run_gui

    return _run_gui()
