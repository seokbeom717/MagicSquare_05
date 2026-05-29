"""U-OUT-01/02 — success output contract (Report/09)."""

from __future__ import annotations

from src.control.magic_square_control import MagicSquareControl


class TestSuccessOutputContract:
    """AC-FR05-03, AC-FR05-04 — int[6] success envelope, 1-index coordinates."""

    def test_u_out_01_valid_g1_returns_int6_length(
        self, grid_g1_two_blanks: list[list[int]]
    ) -> None:
        """U-OUT-01: success result length is 6."""
        # AC-FR05-03
        # Given: G1_placeholder (valid input contract)
        # When: MagicSquareControl.solve(matrix)
        # Then: success=true; len(result) == 6
        control = MagicSquareControl()

        result = control.solve(grid_g1_two_blanks)

        assert isinstance(result, list)
        assert len(result) == 6

    def test_u_out_02_valid_g1_coordinates_one_indexed(
        self, grid_g1_two_blanks: list[list[int]]
    ) -> None:
        """U-OUT-02: r,c in [1,4]; expect [2,2,7,3,3,10] for G1 Step A."""
        # AC-FR05-04
        # Given: G1_placeholder
        # When: MagicSquareControl.solve(matrix)
        # Then: result[0],result[1],result[3],result[4] in 1..4
        control = MagicSquareControl()

        result = control.solve(grid_g1_two_blanks)

        assert result == [2, 2, 7, 3, 3, 10]
