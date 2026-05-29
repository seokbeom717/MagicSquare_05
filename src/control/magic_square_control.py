"""Application control for MagicSquare solve orchestration."""

from __future__ import annotations

from typing import Any

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.failure_result import FailureResult
from src.control.two_cell_solver import solution


class MagicSquareControl:
    """Coordinates boundary validation and domain resolution."""

    def __init__(self) -> None:
        self._validator = BoundaryValidator()

    def solve(self, grid: Any) -> FailureResult | list[int]:
        """Validate input and resolve when validation passes."""
        failure = self._validator.validate(grid)
        if failure is not None:
            return failure
        return self.resolve(grid)

    def resolve(self, grid: list[list[int]]) -> list[int]:
        """Invoke domain solver on a validated grid."""
        return solution(grid)
