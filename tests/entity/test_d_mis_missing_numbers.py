"""D-MIS-01 — find_not_exist_nums RED skeleton (Report/09, FR-03)."""

from __future__ import annotations

import pytest

from src.entity.missing_number_finder import find_not_exist_nums

# Domain Mock 금지.


class TestFindNotExistNums:
    """AC-FR03-01/02 — two missing numbers, ascending order."""

    def test_d_mis_01_g1_returns_7_and_10_ascending(self) -> None:
        """D-MIS-01: G1 → {7, 10} or [7, 10]."""
        # Given: G1_placeholder
        # When: find_not_exist_nums(matrix)
        # Then: [7, 10] ascending (I7, I11)
        pytest.fail("RED: D-MIS-01 — G1 missing numbers {7, 10}")
