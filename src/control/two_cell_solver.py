"""Control-layer re-exports for the domain two-cell solver (FR-05)."""

from __future__ import annotations

from src.entity.two_cell_solver import (
    UnsolvableDomainError,
    build_step_a_assignment,
    build_step_b_assignment,
    solution,
)

__all__ = [
    "UnsolvableDomainError",
    "build_step_a_assignment",
    "build_step_b_assignment",
    "solution",
]
