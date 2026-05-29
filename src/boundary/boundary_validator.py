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
_DUPLICATE_VALUE_CODE = "E005"
_DUPLICATE_VALUE_MESSAGE = "Non-zero values must be unique."


def _invalid_size_failure() -> FailureResult:
    return FailureResult(
        code=_INVALID_SIZE_CODE,
        message=_INVALID_SIZE_MESSAGE,
    )


def _structure_failure(grid: Any) -> FailureResult | None:
    """Return INVALID_SIZE when grid is not a 4x4 list-of-lists."""
    if grid is None:
        return _invalid_size_failure()
    if not isinstance(grid, list):
        return _invalid_size_failure()
    if len(grid) != _EXPECTED_DIMENSION:
        return _invalid_size_failure()
    for row in grid:
        if not isinstance(row, list) or len(row) != _EXPECTED_DIMENSION:
            return _invalid_size_failure()
    return None


def _non_int_cell_failure(grid: list[list[Any]]) -> FailureResult | None:
    """Return E004 when any cell is not a strict int."""
    for row in grid:
        for cell in row:
            if type(cell) is not int:
                return _out_of_range_failure()
    return None


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


def _has_duplicate_nonzero(grid: list[list[int]]) -> bool:
    seen: set[int] = set()
    for row in grid:
        for cell in row:
            if cell == 0:
                continue
            if cell in seen:
                return True
            seen.add(cell)
    return False


def _duplicate_value_failure() -> FailureResult:
    return FailureResult(
        code=_DUPLICATE_VALUE_CODE,
        message=_DUPLICATE_VALUE_MESSAGE,
    )


class BoundaryValidator:
    """Validates puzzle grid input at the boundary layer."""

    def validate(self, grid: Any) -> FailureResult | None:
        """Validate grid dimensions and structure.

        Args:
            grid: Input matrix or None.

        Returns:
            FailureResult when validation fails, otherwise None.
        """
        structure = _structure_failure(grid)
        if structure is not None:
            return structure
        assert isinstance(grid, list)
        cell_type = _non_int_cell_failure(grid)
        if cell_type is not None:
            return cell_type
        if _count_blanks(grid) != _REQUIRED_BLANK_COUNT:
            return _invalid_blank_count_failure()
        if not _has_valid_value_range(grid):
            return _out_of_range_failure()
        if _has_duplicate_nonzero(grid):
            return _duplicate_value_failure()
        return None
