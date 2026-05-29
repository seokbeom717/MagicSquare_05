"""PyQt application bootstrap for MagicSquare."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from src.boundary.gui.main_window import MagicSquareMainWindow


def run_gui() -> int:
    """Start the MagicSquare desktop application.

    Returns:
        Process exit code from the Qt event loop.
    """
    app = QApplication(sys.argv)
    app.setApplicationName("MagicSquare")
    window = MagicSquareMainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(run_gui())
