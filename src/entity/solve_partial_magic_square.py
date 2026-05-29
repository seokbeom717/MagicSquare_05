"""Domain resolver entry point for partial magic square grids."""

from __future__ import annotations

from src.entity.two_cell_solver import solution


class SolvePartialMagicSquare:
    """Executes the two-cell assignment use case on a validated grid."""

    def execute(self, grid: list[list[int]]) -> list[int]:
        """Return Step A/B assignment as 1-index int[6] via domain solver SSOT."""
        return solution(grid)
