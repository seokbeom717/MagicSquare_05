"""U-FLOW-02 — invalid input must not call execute (Report/09) RED skeleton."""

from __future__ import annotations

import pytest

from src.control.magic_square_control import MagicSquareControl

# GREEN: patch/spy SolvePartialMagicSquare.execute (Report/09)
# Report/08 uses resolve() on MagicSquareControl — do not modify that file.


class TestExecuteIsolationExtended:
    """AC-FR01-05 — Domain resolver execute() call_count == 0 on invalid input."""

    def test_u_flow_02_null_matrix_execute_call_count_zero(self) -> None:
        """U-FLOW-02 spot: matrix=null → execute not called."""
        # Given: matrix is None
        # When: MagicSquareControl.solve(matrix) with execute spy
        # Then: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — null → execute 0회")

    def test_u_flow_02_invalid_size_execute_call_count_zero(self) -> None:
        """U-FLOW-02 spot: 3x4 matrix → execute not called."""
        # Given: non-4x4 grid
        # When: solve + execute spy
        # Then: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — invalid size → execute 0회")

    def test_u_flow_02_invalid_blank_count_execute_call_count_zero(self) -> None:
        """U-FLOW-02 spot: blank count ≠ 2 → execute not called."""
        # Given: three blank cells
        # When: solve + execute spy
        # Then: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — invalid blank count → execute 0회")

    def test_u_flow_02_out_of_range_execute_call_count_zero(self) -> None:
        """U-FLOW-02 spot: value 17 → execute not called."""
        # Given: range violation with two blanks
        # When: solve + execute spy
        # Then: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — out of range → execute 0회")

    def test_u_flow_02_duplicate_value_execute_call_count_zero(self) -> None:
        """U-FLOW-02 spot: non-zero duplicate → execute not called."""
        # Given: duplicate non-zero values
        # When: solve + execute spy
        # Then: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — duplicate → execute 0회")
