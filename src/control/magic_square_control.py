"""Application control for MagicSquare solve orchestration."""

from __future__ import annotations

from src.entity.solve_partial_magic_square import SolvePartialMagicSquare


class MagicSquareControl:
    """Coordinates domain resolution (valid grids only)."""

    def __init__(self) -> None:
        self._solver = SolvePartialMagicSquare()

    def resolve(self, grid: list[list[int]]) -> list[int]:
        """Invoke domain resolver execute on a validated grid."""
        return self._solver.execute(grid)
