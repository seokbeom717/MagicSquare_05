"""Boundary input validation for AC-FR-01-01."""

from __future__ import annotations

from typing import Any

from src.boundary.schemas import FailureResponse

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."


class InputValidator:
    """Validates puzzle grid input at the boundary layer."""

    @staticmethod
    def validate(grid: Any) -> FailureResponse:
        """Validate grid dimensions and structure.

        Args:
            grid: Input matrix or None.

        Returns:
            FailureResponse when validation fails.
        """
        if grid is None:
            return FailureResponse(
                type="ERROR",
                code=_INVALID_SIZE_CODE,
                message=_INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError()
