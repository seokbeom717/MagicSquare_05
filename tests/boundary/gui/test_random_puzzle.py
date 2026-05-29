"""random_puzzle pure-function tests (no widget required)."""

from __future__ import annotations

import random

from src.boundary.gui.random_puzzle import (
    _flip_horizontal,
    _random_variant,
    _rotate_90,
    generate_random_puzzle,
)


class TestRandomPuzzle:
    """Random puzzle generator for GUI sample loading."""

    def test_rotate_90_preserves_size(self) -> None:
        """Rotation keeps 4x4 dimensions."""
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

        rotated = _rotate_90(grid)

        assert len(rotated) == 4
        assert all(len(row) == 4 for row in rotated)

    def test_flip_horizontal_reverses_rows(self) -> None:
        """Horizontal flip mirrors each row."""
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

        flipped = _flip_horizontal(grid)

        assert flipped[0] == [4, 3, 2, 1]

    def test_generate_random_puzzle_has_two_blanks(self) -> None:
        """Generated puzzle has exactly two blank cells."""
        rng = random.Random(42)

        puzzle = generate_random_puzzle(rng=rng)

        blank_count = sum(cell == 0 for row in puzzle for cell in row)
        assert blank_count == 2
        assert all(0 <= cell <= 16 for row in puzzle for cell in row)

    def test_random_variant_is_deterministic_with_seed(self) -> None:
        """Same seed yields the same transformed magic square."""
        base = [
            [16, 3, 2, 13],
            [5, 10, 11, 8],
            [9, 6, 7, 12],
            [4, 15, 14, 1],
        ]
        rng_a = random.Random(7)
        rng_b = random.Random(7)

        assert _random_variant(base, rng_a) == _random_variant(base, rng_b)
