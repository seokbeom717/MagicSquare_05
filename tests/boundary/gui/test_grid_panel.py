"""GridPanel widget tests — read/write grid and apply_solution."""

from __future__ import annotations

import pytest

pytest.importorskip("PyQt6.QtWidgets")

from PyQt6.QtWidgets import QApplication

from src.boundary.gui.grid_panel import GridPanel


class TestGridPanel:
    """4x4 editable grid panel."""

    def test_read_grid_returns_blank_for_empty_cells(
        self, qapp: QApplication
    ) -> None:
        """Empty cells read as zero."""
        panel = GridPanel()

        grid = panel.read_grid()

        assert len(grid) == 4
        assert all(cell == 0 for row in grid for cell in row)

    def test_set_grid_and_read_round_trip(self, qapp: QApplication) -> None:
        """set_grid populates editors readable via read_grid."""
        panel = GridPanel()
        expected = [
            [16, 2, 3, 13],
            [5, 0, 11, 8],
            [9, 6, 0, 12],
            [4, 14, 15, 1],
        ]

        panel.set_grid(expected)

        assert panel.read_grid() == expected

    def test_apply_solution_fills_and_highlights_blanks(
        self, qapp: QApplication
    ) -> None:
        """apply_solution writes int[6] into blank cells."""
        panel = GridPanel()
        panel.set_grid(
            [
                [16, 2, 3, 13],
                [5, 0, 11, 8],
                [9, 6, 0, 12],
                [4, 14, 15, 1],
            ]
        )

        panel.apply_solution([2, 2, 7, 3, 3, 10])

        assert panel.read_grid()[1][1] == 7
        assert panel.read_grid()[2][2] == 10

    def test_clear_grid_resets_all_cells(self, qapp: QApplication) -> None:
        """clear_grid returns every cell to blank."""
        panel = GridPanel()
        panel.set_grid([[1, 2, 3, 4] for _ in range(4)])

        panel.clear_grid()

        assert all(cell == 0 for row in panel.read_grid() for cell in row)
