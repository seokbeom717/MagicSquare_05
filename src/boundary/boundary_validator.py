"""Boundary grid validation for AC-FR-01-01."""

from __future__ import annotations

from typing import Any

from src.boundary.failure_result import FailureResult

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."


class BoundaryValidator:
    """Validates puzzle grid input at the boundary layer."""

    def validate(self, grid: Any) -> FailureResult:
        """Validate grid dimensions and structure.

        Args:
            grid: Input matrix or None.

        Returns:
            FailureResult when validation fails.
        """
        if grid is None:
            return FailureResult(
                code=_INVALID_SIZE_CODE,
                message=_INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError()
