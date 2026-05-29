"""D-VAL-01~06 — is_magic_square RED skeleton (Report/09, FR-04)."""

from __future__ import annotations

import pytest

from src.entity.magic_square_validator import is_magic_square

# Domain Mock 금지.


class TestIsMagicSquare:
    """AC-FR04 — magic square invariants I1~I5 (M=34)."""

    def test_d_val_01_g0_complete_grid_returns_true(self) -> None:
        """D-VAL-01: G0 complete → True."""
        # Given: G0_placeholder
        # When: is_magic_square(matrix)
        # Then: True
        pytest.fail("RED: D-VAL-01 — G0 complete → true")

    def test_d_val_02_row_sum_mismatch_returns_false(self) -> None:
        """D-VAL-02: one row sum ≠ 34 → False (I1)."""
        # Given: G0 with one row sum broken
        # When: is_magic_square(matrix)
        # Then: False
        pytest.fail("RED: D-VAL-02 — row sum mismatch → false")

    def test_d_val_03_col_sum_mismatch_returns_false(self) -> None:
        """D-VAL-03: one column sum ≠ 34 → False (I2)."""
        # Given: G0 with one column sum broken
        # When: is_magic_square(matrix)
        # Then: False
        pytest.fail("RED: D-VAL-03 — column sum mismatch → false")

    def test_d_val_04_diagonal_mismatch_returns_false(self) -> None:
        """D-VAL-04: diagonal sum ≠ 34 → False (I3)."""
        # Given: G0 with main or anti diagonal broken
        # When: is_magic_square(matrix)
        # Then: False
        pytest.fail("RED: D-VAL-04 — diagonal mismatch → false")

    def test_d_val_05_duplicate_or_out_of_range_returns_false(self) -> None:
        """D-VAL-05: duplicate or 17 in complete grid → False (I4)."""
        # Given: full 4x4 without zeros, invalid multiset
        # When: is_magic_square(matrix)
        # Then: False
        pytest.fail("RED: D-VAL-05 — duplicate/range violation → false")

    def test_d_val_06_zero_in_complete_grid_returns_false(self) -> None:
        """D-VAL-06: zero present in intended complete grid → False (I4)."""
        # Given: all cells filled except illegal 0 cell
        # When: is_magic_square(matrix)
        # Then: False
        pytest.fail("RED: D-VAL-06 — zero in complete grid → false")
