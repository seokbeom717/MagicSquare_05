"""4x4 puzzle grid input panel."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

_GRID_SIZE = 4
_MAX_CELL_VALUE = 16
_BLANK_VALUE = 0
_DEFAULT_STYLE = ""
_ANSWER_STYLE = "color: #1565c0; font-weight: bold;"


class _CellInput(QLineEdit):
    """Single grid cell accepting blank or integers 1..16."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaxLength(2)
        self.setValidator(QIntValidator(_BLANK_VALUE, _MAX_CELL_VALUE, self))
        self.setPlaceholderText("·")
        self.setFixedSize(56, 36)
        self.setClearButtonEnabled(False)
        self.textChanged.connect(self._on_text_changed)

    def _on_text_changed(self) -> None:
        """Remove answer highlight when the user edits the cell."""
        if self.styleSheet():
            self.set_highlighted(False)

    def set_highlighted(self, highlighted: bool) -> None:
        """Mark this cell as a solved answer with blue text."""
        self.setStyleSheet(_ANSWER_STYLE if highlighted else _DEFAULT_STYLE)

    def value(self) -> int:
        """Return parsed cell value; empty text means blank."""
        text = self.text().strip()
        if not text:
            return _BLANK_VALUE
        return int(text)

    def set_value(self, value: int) -> None:
        """Set cell display from a numeric value."""
        if value == _BLANK_VALUE:
            self.clear()
        else:
            self.setText(str(value))


class GridPanel(QWidget):
    """Editable 4x4 grid where empty cells represent blanks."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._cells: list[list[_CellInput]] = []
        self._build_ui()

    def _build_ui(self) -> None:
        """Lay out column headers, row labels, and cell editors."""
        outer = QVBoxLayout(self)
        grid = QGridLayout()
        grid.setSpacing(6)

        corner = QLabel("")
        corner.setFixedWidth(28)
        grid.addWidget(corner, 0, 0)

        for col in range(_GRID_SIZE):
            header = QLabel(str(col + 1))
            header.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header.setFixedWidth(56)
            grid.addWidget(header, 0, col + 1)

        for row in range(_GRID_SIZE):
            row_label = QLabel(str(row + 1))
            row_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            row_label.setFixedWidth(28)
            grid.addWidget(row_label, row + 1, 0)

            row_cells: list[_CellInput] = []
            for col in range(_GRID_SIZE):
                cell = _CellInput()
                grid.addWidget(cell, row + 1, col + 1)
                row_cells.append(cell)
            self._cells.append(row_cells)

        outer.addLayout(grid)

    def read_grid(self) -> list[list[int]]:
        """Return the current grid values as a 4x4 matrix."""
        return [[cell.value() for cell in row] for row in self._cells]

    def set_grid(self, grid: list[list[int]]) -> None:
        """Populate cell editors from a 4x4 matrix."""
        self.clear_highlights()
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                self._cells[row_idx][col_idx].set_value(value)

    def clear_grid(self) -> None:
        """Reset every cell to blank."""
        self.clear_highlights()
        for row in self._cells:
            for cell in row:
                cell.set_value(_BLANK_VALUE)

    def clear_highlights(self) -> None:
        """Remove answer highlighting from all cells."""
        for row in self._cells:
            for cell in row:
                cell.set_highlighted(False)

    def apply_solution(self, result: list[int]) -> None:
        """Fill blank cells from a six-element success result."""
        row_a, col_a, value_a, row_b, col_b, value_b = result
        answer_cells = (
            self._cells[row_a - 1][col_a - 1],
            self._cells[row_b - 1][col_b - 1],
        )
        for cell, value in zip(answer_cells, (value_a, value_b), strict=True):
            cell.blockSignals(True)
            cell.set_value(value)
            cell.blockSignals(False)
            cell.set_highlighted(True)
