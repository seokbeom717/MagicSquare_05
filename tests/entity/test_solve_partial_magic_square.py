"""SolvePartialMagicSquare.execute — domain entry point (FR-05)."""

from __future__ import annotations

from src.entity.solve_partial_magic_square import SolvePartialMagicSquare


class TestSolvePartialMagicSquare:
    """Domain execute delegates to solution() SSOT."""

    def test_execute_returns_step_a_solution(
        self, grid_g4_step_a_only: list[list[int]]
    ) -> None:
        """execute() returns Step A int[6] when Step A alone is magic."""
        resolver = SolvePartialMagicSquare()

        result = resolver.execute(grid_g4_step_a_only)

        assert result == [3, 2, 6, 3, 3, 7]

    def test_execute_matches_solution_ssot(
        self, grid_g2_reverse_success: list[list[int]]
    ) -> None:
        """execute() matches two_cell_solver.solution for the same grid."""
        from src.entity.two_cell_solver import solution

        resolver = SolvePartialMagicSquare()

        assert resolver.execute(grid_g2_reverse_success) == solution(
            grid_g2_reverse_success
        )
