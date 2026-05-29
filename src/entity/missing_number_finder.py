"""Find missing numbers for a partial magic square grid."""

from __future__ import annotations

from src.entity.constants import MAX_VALUE, MIN_CELL_VALUE


def find_missing_numbers(grid: list[list[int]]) -> list[int]:
    """Return sorted ascending values absent from non-zero cells."""
    present = {cell for row in grid for cell in row if cell != 0}
    return [
        value
        for value in range(MIN_CELL_VALUE, MAX_VALUE + 1)
        if value not in present
    ]
