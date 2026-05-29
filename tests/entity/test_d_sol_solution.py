"""D-SOL-01~04 — solution() use case RED skeleton (Report/09, FR-05)."""

from __future__ import annotations

import pytest

from src.control.two_cell_solver import solution

# Domain Mock 금지 — real is_magic_square path at GREEN.


class TestSolution:
    """AC-FR05 — two-combination solver, int[6] 1-index output."""

    def test_d_sol_01_g1_step_a_success_returns_int6(self) -> None:
        """D-SOL-01: G1 Step A → [2,2,7,3,3,10] (I8)."""
        # Given: G1_placeholder
        # When: solution(matrix)
        # Then: [2, 2, 7, 3, 3, 10]
        pytest.fail("RED: D-SOL-01 — G1 Step A success int[6]")

    def test_d_sol_02_g2_step_b_success(self) -> None:
        """D-SOL-02: G2 Step A fail, Step B success (I9)."""
        # Given: G2_placeholder — TBD
        # When: solution(matrix)
        # Then: reverse assignment int[6], ≠ D-SOL-01
        pytest.fail("RED: D-SOL-02 — G2 TBD")

    def test_d_sol_03_g3_both_steps_fail_unsolvable(self) -> None:
        """D-SOL-03: G3 both fail → UnsolvableDomainError (I10)."""
        # Given: G3_placeholder — TBD
        # When: solution(matrix)
        # Then: UnsolvableDomainError; no success array
        pytest.fail("RED: D-SOL-03 — G3 both fail → UnsolvableDomainError")

    def test_d_sol_04_success_length_six_and_one_index_coords(self) -> None:
        """D-SOL-04: len 6; r,c ∈ [1,4] on G1 or G2 success (I8/I9)."""
        # Given: G1_placeholder (or G2 when defined)
        # When: solution(matrix)
        # Then: len(result)==6; coordinates 1-index in 1..4
        pytest.fail("RED: D-SOL-04 — success length 6, 1-index coords")
