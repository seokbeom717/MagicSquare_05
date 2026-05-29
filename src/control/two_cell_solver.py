"""Two-combination solver use case (FR-05)."""

from __future__ import annotations

from src.entity.blank_locator import find_blank_coords
from src.entity.missing_number_finder import find_missing_numbers


class UnsolvableDomainError(Exception):
    """Raised when both solve attempts fail."""


def solution(grid: list[list[int]]) -> list[int]:
    """Return Step A assignment as 1-index int[6] for a validated grid."""
    blanks = find_blank_coords(grid)
    missing = find_missing_numbers(grid)
    small, large = missing[0], missing[1]
    (row_a, col_a), (row_b, col_b) = blanks
    return [row_a + 1, col_a + 1, small, row_b + 1, col_b + 1, large]
