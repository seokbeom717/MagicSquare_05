"""U-OUT-01/02 — success output contract RED skeleton (Report/09)."""

from __future__ import annotations

import pytest

# UIBoundary.solve (Report/09 When notation) — orchestration via Control at GREEN
# from src.control.magic_square_control import MagicSquareControl


class TestSuccessOutputContract:
    """AC-FR05-03, AC-FR05-04 — int[6] success envelope, 1-index coordinates."""

    def test_u_out_01_valid_g1_returns_int6_length(self) -> None:
        """U-OUT-01: success result length is 6."""
        # Given: G1_placeholder (valid input contract)
        # When: UIBoundary.solve(matrix)  # Control.solve alias
        # Then: success=true; len(result) == 6
        # Mock: none on Domain (valid path — GREEN)
        pytest.fail("RED: U-OUT-01 — success payload length 6")

    def test_u_out_02_valid_g1_coordinates_one_indexed(self) -> None:
        """U-OUT-02: r,c in [1,4]; expect [2,2,7,3,3,10] for G1 Step A."""
        # Given: G1_placeholder
        # When: UIBoundary.solve(matrix)
        # Then: result[0],result[1],result[3],result[4] in 1..4
        pytest.fail("RED: U-OUT-02 — 1-index coords; G1 → [2,2,7,3,3,10]")
