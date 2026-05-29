"""Boundary-track fixtures (PyQt session app)."""

from __future__ import annotations

import sys

import pytest


@pytest.fixture(scope="session")
def qapp() -> object:
    """Shared QApplication for GUI widget tests (skipped without PyQt6)."""
    pytest.importorskip("PyQt6.QtWidgets")
    from PyQt6.QtWidgets import QApplication

    application = QApplication.instance()
    if application is None:
        application = QApplication(sys.argv)
    return application
