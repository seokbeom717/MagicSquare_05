"""GM-2 — Golden Master approval tests for Magic Square Solver.

[TAG][GoldenMaster] GM-TC-01 .. GM-TC-05

Run:
    pytest -m golden_master -v
"""

from __future__ import annotations

import pytest

from src.boundary.puzzle_gateway import PuzzleGateway
from tests.golden_master.approval import (
    collect_scenario_section,
    run_golden_master_approval,
    approve_section,
)
from tests.golden_master.contracts import (
    assert_duplicate_number_contract,
    assert_int6_success_format,
    assert_invalid_blank_count_contract,
    assert_one_index_coordinate_rule,
    assert_row_major_blank_order,
    assert_small_first_combination_rule,
)
from tests.golden_master.scenarios import (
    DUPLICATE_NUMBER_GRID,
    INVALID_BLANK_COUNT_GRID,
    NORMAL_SUCCESS_GRID,
    NO_VALID_SOLUTION_GRID,
    REVERSE_SUCCESS_GRID,
)

pytestmark = pytest.mark.golden_master


class TestGoldenMasterMagicSquare:
    """[TAG][GoldenMaster] approval regression and contract verification."""

    def test_gm_tc_00_full_baseline_approval(self) -> None:
        """Full document: open(expected).read() vs actual with approve pattern."""
        run_golden_master_approval()

    def test_gm_tc_01_normal_success(self) -> None:
        """GM-TC-01: 정상 조합 성공 — int[6], row-major, 1-index, small-first."""
        gateway = PuzzleGateway()
        grid = NORMAL_SUCCESS_GRID

        result = gateway.solve(grid)
        solution = assert_int6_success_format(result, label="GM-TC-01")
        assert_one_index_coordinate_rule(solution, label="GM-TC-01")
        assert_row_major_blank_order(grid, solution, label="GM-TC-01")
        assert_small_first_combination_rule(grid, solution, label="GM-TC-01")

        actual_section = collect_scenario_section("normal_success")
        approve_section("normal_success", actual_section)

    def test_gm_tc_02_reverse_success(self) -> None:
        """GM-TC-02: reverse 조합 성공 — baseline + coordinate contract."""
        gateway = PuzzleGateway()
        grid = REVERSE_SUCCESS_GRID

        result = gateway.solve(grid)
        solution = assert_int6_success_format(result, label="GM-TC-02")
        assert_one_index_coordinate_rule(solution, label="GM-TC-02")
        assert_row_major_blank_order(grid, solution, label="GM-TC-02")
        # Track B GREEN 전: Step A(small-first) 출력이 baseline에 고정됨.
        # reverse fallback 검증은 golden master baseline 비교로 수행.
        assert_small_first_combination_rule(grid, solution, label="GM-TC-02")

        actual_section = collect_scenario_section("reverse_success")
        approve_section("reverse_success", actual_section)

    def test_gm_tc_03_invalid_blank_count(self) -> None:
        """GM-TC-03: INVALID_BLANK_COUNT — Error Contract (E002)."""
        gateway = PuzzleGateway()
        grid = INVALID_BLANK_COUNT_GRID

        result = gateway.solve(grid)
        assert_invalid_blank_count_contract(result, label="GM-TC-03")

        actual_section = collect_scenario_section("invalid_blank_count")
        approve_section("invalid_blank_count", actual_section)

    def test_gm_tc_04_duplicate_number(self) -> None:
        """GM-TC-04: DUPLICATE_NUMBER — Error Contract (E005)."""
        gateway = PuzzleGateway()
        grid = DUPLICATE_NUMBER_GRID

        result = gateway.solve(grid)
        assert_duplicate_number_contract(result, label="GM-TC-04")

        actual_section = collect_scenario_section("duplicate_number")
        approve_section("duplicate_number", actual_section)

    def test_gm_tc_05_no_valid_magic_square(self) -> None:
        """GM-TC-05: NO_VALID_MAGIC_SQUARE — baseline + int[6] contract."""
        gateway = PuzzleGateway()
        grid = NO_VALID_SOLUTION_GRID

        result = gateway.solve(grid)
        solution = assert_int6_success_format(result, label="GM-TC-05")
        assert_one_index_coordinate_rule(solution, label="GM-TC-05")
        assert_row_major_blank_order(grid, solution, label="GM-TC-05")
        assert_small_first_combination_rule(grid, solution, label="GM-TC-05")
        # Track B GREEN 후 ERR_NO_VALID_COMBINATION 기대 — baseline 재승인 필요.

        actual_section = collect_scenario_section("no_valid_solution")
        approve_section("no_valid_solution", actual_section)
