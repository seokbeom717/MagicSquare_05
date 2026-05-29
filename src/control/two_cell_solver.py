"""Two-combination solver use case (FR-05)."""

from __future__ import annotations

from src.entity.solve_partial_magic_square import SolvePartialMagicSquare


class UnsolvableDomainError(Exception):
    """Raised when both solve attempts fail."""


def solution(grid: list[list[int]]) -> list[int]:
    """Return Step A assignment via domain resolver execute."""
    return SolvePartialMagicSquare().execute(grid)
