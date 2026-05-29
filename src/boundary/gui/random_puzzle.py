"""Generate random valid partial magic square puzzles for the GUI."""

from __future__ import annotations

import random
from copy import deepcopy

from src.entity.constants import GRID_SIZE, REQUIRED_BLANK_COUNT

_GRID_SIZE = GRID_SIZE
_REQUIRED_BLANK_COUNT = REQUIRED_BLANK_COUNT

_BASE_MAGIC_SQUARES: list[list[list[int]]] = [
    [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ],
    [
        [1, 15, 14, 4],
        [12, 6, 7, 9],
        [8, 10, 11, 5],
        [13, 3, 2, 16],
    ],
    [
        [4, 9, 5, 16],
        [14, 7, 11, 2],
        [15, 6, 10, 3],
        [1, 12, 8, 13],
    ],
]


def _rotate_90(grid: list[list[int]]) -> list[list[int]]:
    """Rotate a square matrix clockwise by 90 degrees."""
    size = len(grid)
    return [[grid[size - 1 - col][row] for col in range(size)] for row in range(size)]


def _flip_horizontal(grid: list[list[int]]) -> list[list[int]]:
    """Mirror a matrix left-to-right."""
    return [list(reversed(row)) for row in grid]


def _random_variant(grid: list[list[int]], rng: random.Random) -> list[list[int]]:
    """Apply a random rotation and optional mirror to a magic square."""
    variant = deepcopy(grid)
    for _ in range(rng.randint(0, 3)):
        variant = _rotate_90(variant)
    if rng.choice((True, False)):
        variant = _flip_horizontal(variant)
    return variant


def generate_random_puzzle(
    *,
    rng: random.Random | None = None,
) -> list[list[int]]:
    """Build a 4x4 grid with exactly two blanks from a random magic square.

    Args:
        rng: Optional random source for deterministic tests.

    Returns:
        A 4x4 matrix using 0 for blank cells and 1..16 elsewhere.
    """
    source = rng if rng is not None else random
    complete = _random_variant(source.choice(_BASE_MAGIC_SQUARES), source)
    puzzle = deepcopy(complete)

    positions = [
        (row, col)
        for row in range(_GRID_SIZE)
        for col in range(_GRID_SIZE)
    ]
    blank_positions = source.sample(positions, _REQUIRED_BLANK_COUNT)
    for row, col in blank_positions:
        puzzle[row][col] = 0

    return puzzle
