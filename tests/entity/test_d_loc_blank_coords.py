"""D-LOC-01 — find_blank_coords RED skeleton (Report/09, FR-02)."""

from __future__ import annotations

import pytest

from src.entity.empty_cell_locator import find_blank_coords

# Domain Mock 금지 — no patch of peer domain functions.


class TestFindBlankCoords:
    """AC-FR02-02/03 — row-major blank coordinates (0-index internal)."""

    def test_d_loc_01_g1_row_major_two_positions(self) -> None:
        """D-LOC-01: G1 → [(1,1), (2,2)] 0-index row-major."""
        # Given: G1_placeholder
        # When: find_blank_coords(matrix)
        # Then: [(1, 1), (2, 2)]
        pytest.fail("RED: D-LOC-01 — G1 blanks row-major (1,1),(2,2)")
