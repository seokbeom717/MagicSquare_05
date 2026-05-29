"""MagicSquareControl.resolve — direct domain orchestration (FR-05)."""

from __future__ import annotations

from src.control.magic_square_control import MagicSquareControl


class TestMagicSquareControlResolve:
    """Valid grids invoke solution() via resolve()."""

    def test_resolve_returns_int6_for_valid_grid(
        self, grid_g2_reverse_success: list[list[int]]
    ) -> None:
        """resolve() returns Step B success on G2 grid."""
        control = MagicSquareControl()

        result = control.resolve(grid_g2_reverse_success)

        assert result == [1, 1, 16, 1, 2, 3]

    def test_resolve_matches_solution_ssot(
        self, grid_normal_success: list[list[int]]
    ) -> None:
        """resolve() matches entity.two_cell_solver.solution."""
        from src.entity.two_cell_solver import solution

        control = MagicSquareControl()

        assert control.resolve(grid_normal_success) == solution(grid_normal_success)
