"""Screen-facing boundary facade for puzzle solve requests."""

from __future__ import annotations

from typing import Any

from src.boundary.failure_result import FailureResult
from src.boundary.puzzle_gateway import PuzzleGateway


class UiBoundary:
    """Mediates between Screen and Control via PuzzleGateway (E001~E006)."""

    def __init__(self) -> None:
        self._gateway = PuzzleGateway()

    def solve_puzzle(self, grid: Any) -> FailureResult | list[int]:
        """Validate and solve; return FailureResult or int[6] success envelope."""
        return self._gateway.solve(grid)
