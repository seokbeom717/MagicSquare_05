"""UiBoundary facade — Screen entry contract."""

from __future__ import annotations

from src.boundary.failure_result import FailureResult
from src.boundary.ui_boundary import UiBoundary
from tests.conftest import assert_invalid_size_failure


class TestUiBoundary:
    """Screen-facing solve envelope (validation + domain)."""

    def test_solve_puzzle_valid_returns_int6(
        self, grid_normal_success: list[list[int]]
    ) -> None:
        """Valid grid returns six-element success list."""
        boundary = UiBoundary()

        result = boundary.solve_puzzle(grid_normal_success)

        assert isinstance(result, list)
        assert len(result) == 6

    def test_solve_puzzle_invalid_returns_failure_result(
        self, grid_none: None
    ) -> None:
        """Invalid grid returns FailureResult without raising."""
        boundary = UiBoundary()

        result = boundary.solve_puzzle(grid_none)

        assert_invalid_size_failure(result, label="ui_boundary_none")

    def test_solve_puzzle_unsolvable_returns_e006(
        self, grid_g3_unsolvable: list[list[int]]
    ) -> None:
        """Both combinations fail → E006 failure envelope."""
        boundary = UiBoundary()

        result = boundary.solve_puzzle(grid_g3_unsolvable)

        assert isinstance(result, FailureResult)
        assert result.code == "E006"
