"""Domain resolver entry point for partial magic square grids."""

from __future__ import annotations

from src.entity.blank_locator import find_blank_coords
from src.entity.missing_number_finder import find_missing_numbers


class SolvePartialMagicSquare:
    """Executes the two-cell assignment use case on a validated grid."""

    def execute(self, grid: list[list[int]]) -> list[int]:
        """Return Step A assignment as 1-index int[6]."""
        blanks = find_blank_coords(grid)
        missing = find_missing_numbers(grid)
        small, large = missing[0], missing[1]
        (row_a, col_a), (row_b, col_b) = blanks
        return [row_a + 1, col_a + 1, small, row_b + 1, col_b + 1, large]
