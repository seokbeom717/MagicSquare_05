"""D-VAL-01~06 — is_magic_square (Report/09, FR-04)."""

from __future__ import annotations

from src.entity.magic_square_validator import is_magic_square

# Domain Mock 금지.


class TestIsMagicSquare:
    """AC-FR04 — magic square invariants I1~I5 (M=34)."""

    def test_d_val_01_g0_complete_grid_returns_true(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """D-VAL-01: G0 complete → True."""
        assert is_magic_square(grid_g0_complete) is True

    def test_d_val_02_row_sum_mismatch_returns_false(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """D-VAL-02: one row sum ≠ 34 → False (I1)."""
        grid = [row[:] for row in grid_g0_complete]
        grid[0][0] = 1

        assert is_magic_square(grid) is False

    def test_d_val_03_col_sum_mismatch_returns_false(
        self, grid_column_sum_mismatch: list[list[int]]
    ) -> None:
        """D-VAL-03: one column sum ≠ 34 → False (I2)."""
        assert is_magic_square(grid_column_sum_mismatch) is False

    def test_d_val_04_diagonal_mismatch_returns_false(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """D-VAL-04: main diagonal sum ≠ 34 → False (I3)."""
        grid = [row[:] for row in grid_g0_complete]
        grid[0][0] = 1
        grid[1][1] = 20

        assert is_magic_square(grid) is False

    def test_d_val_05_duplicate_or_out_of_range_returns_false(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """D-VAL-05: duplicate or 17 in complete grid → False (I4)."""
        grid = [row[:] for row in grid_g0_complete]
        grid[0][1] = 17

        assert is_magic_square(grid) is False

    def test_d_val_06_zero_in_complete_grid_returns_false(
        self, grid_g0_complete: list[list[int]]
    ) -> None:
        """D-VAL-06: zero present in intended complete grid → False (I4)."""
        grid = [row[:] for row in grid_g0_complete]
        grid[1][1] = 0

        assert is_magic_square(grid) is False
