"""U-IN-05 — non-zero duplicate validation RED skeleton (Report/09)."""

from __future__ import annotations

import pytest

from src.boundary.boundary_validator import BoundaryValidator


class TestDuplicateValueValidation:
    """AC-FR01-04 — non-zero values must be unique."""

    def test_u_in_05_nonzero_duplicate_returns_e005(self) -> None:
        """U-IN-05: duplicate non-zero → E005 failure envelope."""
        # Given: 4x4, exactly two blanks, duplicate 8 in non-zero cells
        # When: BoundaryValidator.validate(matrix)
        # Then: error.code E005; Domain execute 0회
        pytest.fail("RED: U-IN-05 — non-zero duplicate → E005")
