"""U-IN-05 — non-zero duplicate validation (Report/09)."""

from __future__ import annotations

from src.boundary.boundary_validator import BoundaryValidator
from tests.conftest import assert_duplicate_value_failure


class TestDuplicateValueValidation:
    """AC-FR01-04 — non-zero values must be unique."""

    def test_u_in_05_nonzero_duplicate_returns_e005(
        self, grid_duplicate_eight: list[list[int]]
    ) -> None:
        """U-IN-05: duplicate non-zero → E005 failure envelope."""
        # AC-FR-01-04
        # Given: 4x4, exactly two blanks, duplicate 8 in non-zero cells
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E005; Domain execute 0회
        validator = BoundaryValidator()

        result = validator.validate(grid_duplicate_eight)

        assert_duplicate_value_failure(result, label="grid_duplicate_eight")
