"""Shared fixtures for AC-FR-01-01 dimension validation (RED)."""

from __future__ import annotations

from typing import Any

import pytest

# PRD §8.1 contract literals (README / task notation)
AC_FR_01_01_CODE: str = "INVALID_SIZE"
AC_FR_01_01_MESSAGE: str = "Grid must be 4x4."


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
