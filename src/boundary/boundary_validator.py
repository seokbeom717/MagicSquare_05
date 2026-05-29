"""Boundary grid validation for AC-FR-01-01."""

from __future__ import annotations

from typing import Any

from src.boundary.failure_result import FailureResult

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."
_EXPECTED_DIMENSION = 4


def _invalid_size_failure() -> FailureResult:
    return FailureResult(
        code=_INVALID_SIZE_CODE,
        message=_INVALID_SIZE_MESSAGE,
    )


def _has_valid_dimensions(grid: list[list[int]]) -> bool:
    if len(grid) != _EXPECTED_DIMENSION:
        return False
    return all(len(row) == _EXPECTED_DIMENSION for row in grid)


class BoundaryValidator:
    """Validates puzzle grid input at the boundary layer."""

    def validate(self, grid: Any) -> FailureResult:
        """Validate grid dimensions and structure.

        Args:
            grid: Input matrix or None.

        Returns:
            FailureResult when validation fails.
        """
        if grid is None:
            return _invalid_size_failure()
        if not isinstance(grid, list) or not _has_valid_dimensions(grid):
            return _invalid_size_failure()
        raise NotImplementedError()
