"""U-OUT-01/02 — success output contract (Report/09)."""

from __future__ import annotations

from src.boundary.puzzle_gateway import PuzzleGateway


class TestSuccessOutputContract:
    """AC-FR05-03, AC-FR05-04 — int[6] success envelope, 1-index coordinates."""

    def test_u_out_01_valid_g1_returns_int6_length(
        self, grid_normal_success: list[list[int]]
    ) -> None:
        """U-OUT-01: success result length is 6."""
        # AC-FR05-03
        # Given: valid two-blank grid with magic Step A solution
        # When: PuzzleGateway.solve(matrix)
        # Then: success=true; len(result) == 6
        gateway = PuzzleGateway()

        result = gateway.solve(grid_normal_success)

        assert isinstance(result, list)
        assert len(result) == 6

    def test_u_out_02_valid_g1_coordinates_one_indexed(
        self, grid_normal_success: list[list[int]]
    ) -> None:
        """U-OUT-02: r,c in [1,4]; expect Step A int[6] for normal_success grid."""
        # AC-FR05-04
        # Given: normal_success grid
        # When: PuzzleGateway.solve(matrix)
        # Then: result[0],result[1],result[3],result[4] in 1..4
        gateway = PuzzleGateway()

        result = gateway.solve(grid_normal_success)

        assert result == [3, 3, 6, 4, 4, 1]
