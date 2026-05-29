"""D-SOL-01~04 — solution() use case (Report/09, FR-05)."""

from __future__ import annotations

import pytest

from src.control.two_cell_solver import (
    UnsolvableDomainError,
    build_step_a_assignment,
    solution,
)

# Domain Mock 금지 — real is_magic_square path at GREEN.


class TestSolution:
    """AC-FR05 — two-combination solver, int[6] 1-index output."""

    def test_d_sol_01_g1_step_a_success_returns_int6(
        self, grid_g1_two_blanks: list[list[int]]
    ) -> None:
        """D-SOL-01: G1 Step A assignment → [2,2,7,3,3,10] (I8)."""
        result = build_step_a_assignment(grid_g1_two_blanks)

        assert result == [2, 2, 7, 3, 3, 10]

    def test_d_sol_02_g2_step_b_success(
        self, grid_g2_reverse_success: list[list[int]]
    ) -> None:
        """D-SOL-02: G2 Step A fail, Step B success (I9)."""
        step_a = build_step_a_assignment(grid_g2_reverse_success)

        result = solution(grid_g2_reverse_success)

        assert result == [1, 1, 16, 1, 2, 3]
        assert result != step_a

    def test_d_sol_03_g3_both_steps_fail_unsolvable(
        self, grid_g3_unsolvable: list[list[int]]
    ) -> None:
        """D-SOL-03: G3 both fail → UnsolvableDomainError (I10)."""
        with pytest.raises(UnsolvableDomainError):
            solution(grid_g3_unsolvable)

    def test_d_sol_04_success_length_six_and_one_index_coords(
        self, grid_g2_reverse_success: list[list[int]]
    ) -> None:
        """D-SOL-04: len 6; r,c ∈ [1,4] on G2 success (I8/I9)."""
        result = solution(grid_g2_reverse_success)

        assert len(result) == 6
        for index in (0, 1, 3, 4):
            assert 1 <= result[index] <= 4

    def test_d_sol_05_step_a_only_returns_without_step_b(
        self, grid_g4_step_a_only: list[list[int]]
    ) -> None:
        """D-SOL-05: Step A magic → early return before Step B (L48)."""
        step_a = build_step_a_assignment(grid_g4_step_a_only)

        result = solution(grid_g4_step_a_only)

        assert result == step_a
        assert result == [3, 2, 6, 3, 3, 7]
