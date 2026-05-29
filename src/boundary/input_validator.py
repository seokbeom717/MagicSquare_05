"""Boundary input validation — thin delegate to BoundaryValidator (SSOT)."""

from __future__ import annotations

from typing import Any

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.failure_result import FailureResult


class InputValidator:
    """Delegates to BoundaryValidator; returns the same FailureResult envelope."""

    @staticmethod
    def validate(grid: Any) -> FailureResult | None:
        """Validate grid dimensions and structure.

        Args:
            grid: Input matrix or None.

        Returns:
            FailureResult when validation fails, otherwise None.
        """
        return BoundaryValidator().validate(grid)
