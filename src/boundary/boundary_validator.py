"""Boundary grid validation for AC-FR-01-01."""

from __future__ import annotations

from typing import Any

from src.boundary.failure_result import FailureResult

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."
_EXPECTED_DIMENSION = 4
_INVALID_BLANK_COUNT_CODE = "E002"
_INVALID_BLANK_COUNT_MESSAGE = "Blank count must be exactly 2."
_REQUIRED_BLANK_COUNT = 2
_OUT_OF_RANGE_CODE = "E004"
_OUT_OF_RANGE_MESSAGE = "Values must be 0 or 1..16."
_MIN_CELL_VALUE = 1
_MAX_CELL_VALUE = 16


def _invalid_size_failure() -> FailureResult:
    return FailureResult(
        code=_INVALID_SIZE_CODE,
        message=_INVALID_SIZE_MESSAGE,
    )


def _has_valid_dimensions(grid: list[list[int]]) -> bool:
    if len(grid) != _EXPECTED_DIMENSION:
        return False
    return all(len(row) == _EXPECTED_DIMENSION for row in grid)


def _count_blanks(grid: list[list[int]]) -> int:
    return sum(cell == 0 for row in grid for cell in row)


def _invalid_blank_count_failure() -> FailureResult:
    return FailureResult(
        code=_INVALID_BLANK_COUNT_CODE,
        message=_INVALID_BLANK_COUNT_MESSAGE,
    )


def _has_valid_value_range(grid: list[list[int]]) -> bool:
    for row in grid:
        for cell in row:
            if cell == 0:
                continue
            if cell < _MIN_CELL_VALUE or cell > _MAX_CELL_VALUE:
                return False
    return True


def _out_of_range_failure() -> FailureResult:
    return FailureResult(
        code=_OUT_OF_RANGE_CODE,
        message=_OUT_OF_RANGE_MESSAGE,
    )


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
        if _count_blanks(grid) != _REQUIRED_BLANK_COUNT:
            return _invalid_blank_count_failure()
        if not _has_valid_value_range(grid):
            return _out_of_range_failure()
        raise NotImplementedError()
