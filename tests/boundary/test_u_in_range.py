"""U-IN-04a/b — value range validation (Report/09)."""

from __future__ import annotations

from src.boundary.boundary_validator import BoundaryValidator
from tests.conftest import assert_out_of_range_failure


class TestValueRangeValidation:
    """AC-FR01-03 — values must be 0 or 1..16."""

    def test_u_in_04a_below_range_returns_e004(
        self, grid_below_range: list[list[int]]
    ) -> None:
        """U-IN-04a: -1 in grid → E004 failure envelope."""
        # AC-FR-01-03
        # Given: 4x4, two blanks, [0][0] = -1
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E004; message exact at GREEN
        validator = BoundaryValidator()

        result = validator.validate(grid_below_range)

        assert_out_of_range_failure(result, label="grid_below_range")

    def test_u_in_04b_above_range_returns_e004(
        self, grid_above_range: list[list[int]]
    ) -> None:
        """U-IN-04a: 17 in grid → E004 failure envelope."""
        # AC-FR-01-03
        # Given: 4x4, two blanks, cell value 17
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E004
        validator = BoundaryValidator()

        result = validator.validate(grid_above_range)

        assert_out_of_range_failure(result, label="grid_above_range")
