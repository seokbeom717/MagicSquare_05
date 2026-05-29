"""U-IN-03a/b — blank count validation RED skeleton (Report/09)."""

from __future__ import annotations

import pytest

from src.boundary.boundary_validator import BoundaryValidator

# SUT alias: InputValidator.validate (Report/09 When notation)


class TestBlankCountValidation:
    """AC-FR01-02 — blank count must be exactly 2."""

    def test_u_in_03a_zero_blanks_returns_e002(self) -> None:
        """U-IN-03a: no zero cells → E002 failure envelope."""
        # Given: G0_placeholder (4x4, no blanks)
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E002; execute 0회 (orchestration — GREEN)
        pytest.fail("RED: U-IN-03a — zero blanks → E002")

    def test_u_in_03b_three_blanks_returns_e002(self) -> None:
        """U-IN-03b: three zero cells → E002 failure envelope."""
        # Given: 4x4 with three zeros (Report/09 design example)
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E002; no exception
        pytest.fail("RED: U-IN-03b — three blanks → E002")
