"""Golden Master contract assertions for solver output invariants."""

from __future__ import annotations

from typing import Any

from src.boundary.failure_result import FailureResult
from src.entity.blank_locator import find_blank_coords
from src.entity.missing_number_finder import find_missing_numbers

from tests.conftest import U_IN_03_CODE, U_IN_03_MESSAGE, U_IN_05_CODE, U_IN_05_MESSAGE

_GRID_SIZE = 4


def assert_int6_success_format(result: Any, *, label: str) -> list[int]:
    """Assert success envelope is a six-element integer list."""
    assert isinstance(result, list), f"{label}: success must be list[int]"
    assert len(result) == 6, f"{label}: success length must be 6"
    assert all(isinstance(value, int) for value in result), (
        f"{label}: all elements must be int"
    )
    return result


def assert_one_index_coordinate_rule(result: list[int], *, label: str) -> None:
    """Assert r,c coordinates in result are 1-indexed within 1..4."""
    for index in (0, 1, 3, 4):
        coord = result[index]
        assert 1 <= coord <= _GRID_SIZE, (
            f"{label}: coordinate at index {index} must be 1-index in 1..4"
        )


def assert_row_major_blank_order(
    grid: list[list[int]], result: list[int], *, label: str
) -> None:
    """Assert output coordinates follow row-major blank scan order."""
    blanks = find_blank_coords(grid)
    assert len(blanks) == 2, f"{label}: row-major check requires two blanks"
    (row_a, col_a), (row_b, col_b) = blanks
    assert result[0] == row_a + 1 and result[1] == col_a + 1, (
        f"{label}: first blank must be row-major first 0-cell (1-index)"
    )
    assert result[3] == row_b + 1 and result[4] == col_b + 1, (
        f"{label}: second blank must be row-major second 0-cell (1-index)"
    )


def assert_small_first_combination_rule(
    grid: list[list[int]], result: list[int], *, label: str
) -> None:
    """Assert Step A: smaller missing number → first blank, larger → second."""
    missing = find_missing_numbers(grid)
    assert len(missing) == 2, f"{label}: small-first check requires two missing nums"
    small, large = missing[0], missing[1]
    assert small < large, f"{label}: missing numbers must be ascending"
    assert result[2] == small and result[5] == large, (
        f"{label}: Step A small-first assignment expected ({small}, {large})"
    )


def assert_reverse_fallback_assignment(
    grid: list[list[int]], result: list[int], *, label: str
) -> None:
    """Assert Step B: larger missing number → first blank, smaller → second."""
    missing = find_missing_numbers(grid)
    assert len(missing) == 2, f"{label}: reverse check requires two missing nums"
    small, large = missing[0], missing[1]
    assert result[2] == large and result[5] == small, (
        f"{label}: Step B reverse assignment expected ({large}, {small})"
    )


def assert_error_contract(
    result: Any,
    *,
    code: str,
    message: str,
    label: str,
) -> FailureResult:
    """Assert boundary failure DTO matches the canonical error contract."""
    assert isinstance(result, FailureResult), (
        f"{label}: failure must be FailureResult, got {type(result)}"
    )
    assert result.code == code, f"{label}: code must be {code}"
    assert result.message == message, f"{label}: message must match contract"
    return result


def assert_invalid_blank_count_contract(result: Any, *, label: str) -> FailureResult:
    """Assert INVALID_BLANK_COUNT error contract (E002)."""
    return assert_error_contract(
        result,
        code=U_IN_03_CODE,
        message=U_IN_03_MESSAGE,
        label=label,
    )


_NO_VALID_COMBINATION_CODE = "E006"
_NO_VALID_COMBINATION_MESSAGE = (
    "Both solve attempts failed to satisfy magic square invariants."
)


def assert_no_valid_combination_contract(result: Any, *, label: str) -> FailureResult:
    """Assert E006 when both Step A and Step B fail."""
    return assert_error_contract(
        result,
        code=_NO_VALID_COMBINATION_CODE,
        message=_NO_VALID_COMBINATION_MESSAGE,
        label=label,
    )


def assert_duplicate_number_contract(result: Any, *, label: str) -> FailureResult:
    """Assert DUPLICATE_NUMBER error contract (E005)."""
    return assert_error_contract(
        result,
        code=U_IN_05_CODE,
        message=U_IN_05_MESSAGE,
        label=label,
    )
