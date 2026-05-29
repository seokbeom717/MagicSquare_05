"""Boundary failure result model for AC-FR-01-01."""

from __future__ import annotations

from pydantic import BaseModel


class FailureResult(BaseModel):
    """Dimension and input validation failure payload."""

    code: str
    message: str
