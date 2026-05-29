"""Boundary response schemas."""

from __future__ import annotations

from pydantic import BaseModel


class FailureResponse(BaseModel):
    """Standard failure envelope for boundary validation."""

    type: str
    code: str
    message: str
