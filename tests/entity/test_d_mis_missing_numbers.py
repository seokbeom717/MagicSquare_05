"""D-MIS-01 — find_missing_numbers (Report/09, FR-03)."""

from __future__ import annotations

from src.entity.missing_number_finder import find_missing_numbers

# Domain Mock 금지.


class TestFindMissingNumbers:
    """AC-FR03-01/02 — two missing numbers, ascending order."""

    def test_d_mis_01_g1_returns_7_and_10_ascending(
        self, grid_g1_two_blanks: list[list[int]]
    ) -> None:
        """D-MIS-01: G1 → [7, 10] ascending."""
        # Given: G1_placeholder
        # When: find_missing_numbers(matrix)
        # Then: [7, 10] ascending (I7, I11)
        result = find_missing_numbers(grid_g1_two_blanks)

        assert result == [7, 10]
