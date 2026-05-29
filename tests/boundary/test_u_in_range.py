"""U-IN-04a/b — value range validation RED skeleton (Report/09)."""

from __future__ import annotations

import pytest

from src.boundary.boundary_validator import BoundaryValidator


class TestValueRangeValidation:
    """AC-FR01-03 — values must be 0 or 1..16."""

    def test_u_in_04a_below_range_returns_e004(self) -> None:
        """U-IN-04a: -1 in grid → E004 failure envelope."""
        # Given: 4x4, two blanks, [0][0] = -1
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E004; message exact at GREEN
        pytest.fail("RED: U-IN-04a — value -1 → E004")

    def test_u_in_04b_above_range_returns_e004(self) -> None:
        """U-IN-04b: 17 in grid → E004 failure envelope."""
        # Given: 4x4, two blanks, cell value 17
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E004
        pytest.fail("RED: U-IN-04b — value 17 → E004")
