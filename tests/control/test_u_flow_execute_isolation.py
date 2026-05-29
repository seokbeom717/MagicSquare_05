"""U-FLOW-02 — invalid input must not call execute (Report/09)."""

from __future__ import annotations

from unittest.mock import patch

from src.boundary.puzzle_gateway import PuzzleGateway
class TestExecuteIsolationExtended:
    """AC-FR01-05 — Domain resolver execute() call_count == 0 on invalid input."""

    def test_u_flow_02_null_matrix_execute_call_count_zero(
        self, grid_none: None
    ) -> None:
        """U-FLOW-02 spot: matrix=null → execute not called."""
        # AC-FR-01-05
        # Given: matrix is None
        # When: MagicSquareControl.solve(matrix) with execute spy
        # Then: execute.call_count == 0
        gateway = PuzzleGateway()

        with patch.object(gateway._control._solver, "execute") as mock_execute:
            gateway.solve(grid_none)

            assert mock_execute.call_count == 0

    def test_u_flow_02_invalid_size_execute_call_count_zero(
        self, grid_3x4: list[list[int]]
    ) -> None:
        """U-FLOW-02 spot: 3x4 matrix → execute not called."""
        # AC-FR-01-05
        # Given: non-4x4 grid
        # When: solve + execute spy
        # Then: execute.call_count == 0
        gateway = PuzzleGateway()

        with patch.object(gateway._control._solver, "execute") as mock_execute:
            gateway.solve(grid_3x4)

            assert mock_execute.call_count == 0

    def test_u_flow_02_invalid_blank_count_execute_call_count_zero(
        self, grid_three_blanks: list[list[int]]
    ) -> None:
        """U-FLOW-02 spot: blank count ≠ 2 → execute not called."""
        # AC-FR-01-05
        # Given: three blank cells
        # When: solve + execute spy
        # Then: execute.call_count == 0
        gateway = PuzzleGateway()

        with patch.object(gateway._control._solver, "execute") as mock_execute:
            gateway.solve(grid_three_blanks)

            assert mock_execute.call_count == 0

    def test_u_flow_02_out_of_range_execute_call_count_zero(
        self, grid_above_range: list[list[int]]
    ) -> None:
        """U-FLOW-02 spot: value 17 → execute not called."""
        # AC-FR-01-05
        # Given: range violation with two blanks
        # When: solve + execute spy
        # Then: execute.call_count == 0
        gateway = PuzzleGateway()

        with patch.object(gateway._control._solver, "execute") as mock_execute:
            gateway.solve(grid_above_range)

            assert mock_execute.call_count == 0

    def test_u_flow_02_duplicate_value_execute_call_count_zero(
        self, grid_duplicate_eight: list[list[int]]
    ) -> None:
        """U-FLOW-02 spot: non-zero duplicate → execute not called."""
        # AC-FR-01-05
        # Given: duplicate non-zero values
        # When: solve + execute spy
        # Then: execute.call_count == 0
        gateway = PuzzleGateway()

        with patch.object(gateway._control._solver, "execute") as mock_execute:
            gateway.solve(grid_duplicate_eight)

            assert mock_execute.call_count == 0
