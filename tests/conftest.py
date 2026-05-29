"""Shared fixtures for AC-FR-01-01 dimension validation (RED)."""

from __future__ import annotations

from typing import Any

import pytest

# PRD §8.1 contract literals (README / task notation)
AC_FR_01_01_CODE: str = "INVALID_SIZE"
AC_FR_01_01_MESSAGE: str = "Grid must be 4x4."

# Report/09 U-IN-03 — blank count contract (PRD §13)
U_IN_03_CODE: str = "E002"
U_IN_03_MESSAGE: str = "Blank count must be exactly 2."
REQUIRED_BLANK_COUNT: int = 2

# Report/09 U-IN-04 — value range contract (PRD §13)
U_IN_04_CODE: str = "E004"
U_IN_04_MESSAGE: str = "Values must be 0 or 1..16."

# Report/09 U-IN-05 — duplicate value contract (PRD §13)
U_IN_05_CODE: str = "E005"
U_IN_05_MESSAGE: str = "Non-zero values must be unique."


@pytest.fixture
def grid_none() -> None:
    """Explicit None grid input."""
    return None


@pytest.fixture
def grid_empty() -> list[list[int]]:
    """Empty list — zero rows."""
    return []


@pytest.fixture
def grid_four_empty_rows() -> list[list[int]]:
    """Four rows with zero columns each."""
    return [[]] * 4


@pytest.fixture
def grid_3x4() -> list[list[int]]:
    """Three rows, four columns — row count mismatch."""
    return [[1, 2, 3, 4] for _ in range(3)]


@pytest.fixture
def grid_g0_complete() -> list[list[int]]:
    """G0_placeholder — complete 4x4 magic square (Report/09 §6.1)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_three_blanks() -> list[list[int]]:
    """4x4 with three zero cells — blank count violation (U-IN-03b)."""
    return [
        [0, 1, 2, 3],
        [4, 0, 6, 7],
        [8, 9, 0, 11],
        [12, 13, 14, 15],
    ]


@pytest.fixture
def grid_g1_two_blanks() -> list[list[int]]:
    """G1_placeholder — two blanks at 0-index (1,1) and (2,2) (Report/09 §6.2)."""
    return [
        [16, 2, 3, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 14, 15, 1],
    ]


@pytest.fixture
def grid_g2_reverse_success() -> list[list[int]]:
    """G2 — Step A fails, Step B succeeds (D-SOL-02, GM reverse_success)."""
    return [
        [0, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g3_unsolvable() -> list[list[int]]:
    """G3 — both steps fail → UnsolvableDomainError (D-SOL-03, GM no_valid_solution)."""
    return [
        [0, 3, 2, 0],
        [5, 10, 15, 8],
        [9, 6, 7, 12],
        [4, 11, 14, 1],
    ]


@pytest.fixture
def grid_below_range() -> list[list[int]]:
    """4x4 with two blanks and -1 at [0][0] (U-IN-04a)."""
    return [
        [-1, 2, 3, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 14, 15, 1],
    ]


@pytest.fixture
def grid_above_range() -> list[list[int]]:
    """4x4 with two blanks and 17 at [0][0] (U-IN-04b)."""
    return [
        [17, 2, 3, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 14, 15, 1],
    ]


@pytest.fixture
def grid_duplicate_eight() -> list[list[int]]:
    """4x4 with two blanks and duplicate 8 in non-zero cells (U-IN-05)."""
    return [
        [16, 2, 3, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 8, 15, 1],
    ]


@pytest.fixture
def expected_failure_payload() -> dict[str, str]:
    """Canonical AC-FR-01-01 failure contract."""
    return {"code": AC_FR_01_01_CODE, "message": AC_FR_01_01_MESSAGE}


# --- Report/09 §6 grid placeholders (RED skeleton — uncomment at GREEN) ---
# G0_placeholder: complete magic square (see tests/entity/conftest.py)
# G1_placeholder: two blanks, missing {7, 10} (see tests/entity/conftest.py)

def assert_invalid_size_failure(result: Any, *, label: str) -> None:
    """Assert standard failure object for dimension violations."""
    assert result is not None, f"{label}: result must not be None"
    assert getattr(result, "code", None) == AC_FR_01_01_CODE, (
        f"{label}: code must be INVALID_SIZE"
    )
    assert getattr(result, "message", None) == AC_FR_01_01_MESSAGE, (
        f"{label}: message must match PRD §8.1 literally"
    )


def assert_blank_count_failure(result: Any, *, label: str) -> None:
    """Assert standard failure object for blank count violations."""
    assert result is not None, f"{label}: result must not be None"
    assert getattr(result, "code", None) == U_IN_03_CODE, (
        f"{label}: code must be E002"
    )
    assert getattr(result, "message", None) == U_IN_03_MESSAGE, (
        f"{label}: message must match PRD §13 literally"
    )


def assert_out_of_range_failure(result: Any, *, label: str) -> None:
    """Assert standard failure object for value range violations."""
    assert result is not None, f"{label}: result must not be None"
    assert getattr(result, "code", None) == U_IN_04_CODE, (
        f"{label}: code must be E004"
    )
    assert getattr(result, "message", None) == U_IN_04_MESSAGE, (
        f"{label}: message must match PRD §13 literally"
    )


def assert_duplicate_value_failure(result: Any, *, label: str) -> None:
    """Assert standard failure object for duplicate non-zero violations."""
    assert result is not None, f"{label}: result must not be None"
    assert getattr(result, "code", None) == U_IN_05_CODE, (
        f"{label}: code must be E005"
    )
    assert getattr(result, "message", None) == U_IN_05_MESSAGE, (
        f"{label}: message must match PRD §13 literally"
    )
