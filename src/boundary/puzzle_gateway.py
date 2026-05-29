"""Boundary entry: validate input then delegate to control (ECB)."""

from __future__ import annotations

from typing import Any

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.failure_result import FailureResult
from src.control.magic_square_control import MagicSquareControl


class PuzzleGateway:
    """Validates at the boundary, then invokes control resolution on valid grids."""

    def __init__(self) -> None:
        self._validator = BoundaryValidator()
        self._control = MagicSquareControl()

    def solve(self, grid: Any) -> FailureResult | list[int]:
        """Validate grid; return failure envelope or int[6] solution."""
        failure = self._validator.validate(grid)
        if failure is not None:
            return failure
        return self._control.resolve(grid)
