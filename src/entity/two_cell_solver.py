"""Two-combination domain solver (FR-05)."""

from __future__ import annotations

from src.entity.blank_locator import find_blank_coords
from src.entity.magic_square_validator import is_magic_square
from src.entity.missing_number_finder import find_missing_numbers


class UnsolvableDomainError(Exception):
    """Raised when both solve attempts fail."""


def build_step_a_assignment(grid: list[list[int]]) -> list[int]:
    """Return Step A int[6]: small missing → first blank, large → second (1-index)."""
    return _build_assignment(grid, reverse=False)


def build_step_b_assignment(grid: list[list[int]]) -> list[int]:
    """Return Step B int[6]: large missing → first blank, small → second (1-index)."""
    return _build_assignment(grid, reverse=True)


def _build_assignment(grid: list[list[int]], *, reverse: bool) -> list[int]:
    blanks = find_blank_coords(grid)
    missing = find_missing_numbers(grid)
    small, large = missing[0], missing[1]
    (row_a, col_a), (row_b, col_b) = blanks
    value_a, value_b = (large, small) if reverse else (small, large)
    return [row_a + 1, col_a + 1, value_a, row_b + 1, col_b + 1, value_b]


def _filled_grid(grid: list[list[int]], assignment: list[int]) -> list[list[int]]:
    filled = [row[:] for row in grid]
    placements = (
        (assignment[0] - 1, assignment[1] - 1, assignment[2]),
        (assignment[3] - 1, assignment[4] - 1, assignment[5]),
    )
    for row, col, value in placements:
        filled[row][col] = value
    return filled


def solution(grid: list[list[int]]) -> list[int]:
    """Try Step A then Step B; return int[6] when a filled grid is a magic square."""
    step_a = build_step_a_assignment(grid)
    if is_magic_square(_filled_grid(grid, step_a)):
        return step_a
    step_b = build_step_b_assignment(grid)
    if is_magic_square(_filled_grid(grid, step_b)):
        return step_b
    raise UnsolvableDomainError()
