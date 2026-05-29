"""Application control for MagicSquare solve orchestration."""

from __future__ import annotations

from src.entity.two_cell_solver import solution


class MagicSquareControl:
    """Coordinates domain resolution (valid grids only)."""

    def resolve(self, grid: list[list[int]]) -> list[int]:
        """Invoke domain solver SSOT on a validated grid."""
        return solution(grid)
