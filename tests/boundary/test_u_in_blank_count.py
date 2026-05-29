"""U-IN-03a/b — blank count validation (Report/09)."""

from __future__ import annotations

from src.boundary.boundary_validator import BoundaryValidator
from tests.conftest import (
    U_IN_03_CODE,
    U_IN_03_MESSAGE,
    assert_blank_count_failure,
)


class TestBlankCountValidation:
    """AC-FR01-02 — blank count must be exactly 2."""

    def test_u_in_03a_zero_blanks_returns_e002(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """U-IN-03a: no zero cells → E002 failure envelope."""
        # AC-FR-01-02
        # Given: G0_placeholder (4x4, no blanks)
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E002; execute 0회 (orchestration — GREEN)
        validator = BoundaryValidator()

        result = validator.validate(grid_g0_complete)

        assert_blank_count_failure(result, label="grid_g0_complete")

    def test_u_in_03b_three_blanks_returns_e002(
        self, grid_three_blanks: list[list[int]]
    ) -> None:
        """U-IN-03b: three zero cells → E002 failure envelope."""
        # AC-FR-01-02
        # Given: 4x4 with three zeros (Report/09 design example)
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E002; no exception
        validator = BoundaryValidator()

        result = validator.validate(grid_three_blanks)

        assert result.code == U_IN_03_CODE
        assert result.message == U_IN_03_MESSAGE
