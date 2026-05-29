"""Locate blank cells in row-major order."""

from __future__ import annotations

from src.entity.constants import GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return 0-index coordinates of zero cells in row-major scan order."""
    coords: list[tuple[int, int]] = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                coords.append((row, col))
    return coords
