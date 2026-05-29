"""D-LOC-01 — find_blank_coords (Report/09, FR-02)."""

from __future__ import annotations

from src.entity.blank_locator import find_blank_coords

# Domain Mock 금지 — no patch of peer domain functions.


class TestFindBlankCoords:
    """AC-FR02-02/03 — row-major blank coordinates (0-index internal)."""

    def test_d_loc_01_g1_row_major_two_positions(
        self, grid_g1_two_blanks: list[list[int]]
    ) -> None:
        """D-LOC-01: G1 → [(1,1), (2,2)] 0-index row-major."""
        # Given: G1_placeholder
        # When: find_blank_coords(matrix)
        # Then: [(1, 1), (2, 2)]
        result = find_blank_coords(grid_g1_two_blanks)

        assert result == [(1, 1), (2, 2)]
