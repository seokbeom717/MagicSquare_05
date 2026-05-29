"""Magic square invariant validation."""

from __future__ import annotations

from src.entity.constants import GRID_SIZE, MAGIC_CONSTANT, MAX_VALUE, MIN_CELL_VALUE


def is_magic_square(grid: list[list[int]]) -> bool:
    """Return True when all rows, columns, and diagonals sum to MAGIC_CONSTANT."""
    for row in grid:
        if sum(row) != MAGIC_CONSTANT:
            return False
    for col in range(GRID_SIZE):
        if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False
    if sum(grid[i][i] for i in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False
    if sum(grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False
    flat = [cell for row in grid for cell in row]
    if any(cell < MIN_CELL_VALUE or cell > MAX_VALUE for cell in flat):
        return False
    return len(set(flat)) == MAX_VALUE
