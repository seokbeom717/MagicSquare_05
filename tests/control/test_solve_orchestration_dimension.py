"""Control orchestration tests — Domain resolve() isolation (AC-FR-01-01 RED)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from src.control.magic_square_control import MagicSquareControl
from tests.conftest import (
    AC_FR_01_01_CODE,
    AC_FR_01_01_MESSAGE,
    assert_invalid_size_failure,
)


class TestResolveIsolation:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve() 0회 호출 격리 검증."""

    def test_grid_none_resolve_call_count_zero(
        self, grid_none: None
    ) -> None:
        """grid=None must not invoke resolve()."""
        # AC-FR-01-01
        # Given: grid None and spied resolve
        # When: solve orchestration runs
        # Then: resolve call count is 0
        control = MagicSquareControl()

        with patch.object(control, "resolve") as mock_resolve:
            result = control.solve(grid_none)

            mock_resolve.assert_not_called()

        assert_invalid_size_failure(result, label="grid_none_orchestration")

    def test_grid_empty_list_resolve_never_called(
        self, grid_empty: list[list[int]]
    ) -> None:
        """grid=[] must not invoke resolve()."""
        # AC-FR-01-01
        # Given: empty grid and spied resolve
        # When: solve runs
        # Then: resolve is never called
        control = MagicSquareControl()

        with patch.object(control, "resolve") as mock_resolve:
            control.solve(grid_empty)

            assert mock_resolve.call_count == 0

    def test_grid_four_empty_rows_resolve_assert_not_called(
        self, grid_four_empty_rows: list[list[int]]
    ) -> None:
        """grid=[[]]*4 must not invoke resolve()."""
        # AC-FR-01-01
        # Given: four empty rows and spied resolve
        # When: solve runs
        # Then: assert_not_called passes
        control = MagicSquareControl()

        with patch.object(control, "resolve") as mock_resolve:
            control.solve(grid_four_empty_rows)

            mock_resolve.assert_not_called()

    def test_grid_3x4_resolve_mock_call_count_is_zero(
        self, grid_3x4: list[list[int]]
    ) -> None:
        """grid 3×4 must leave resolve mock at zero calls."""
        # AC-FR-01-01
        # Given: 3×4 grid and MagicMock resolve
        # When: solve runs
        # Then: mock.call_count == 0
        control = MagicSquareControl()

        with patch.object(control, "resolve", new_callable=MagicMock) as mock_resolve:
            result = control.solve(grid_3x4)

            assert mock_resolve.call_count == 0
            assert result.code == AC_FR_01_01_CODE

    def test_grid_none_resolve_called_fails_via_mock_guard(
        self, grid_none: None
    ) -> None:
        """If resolve runs on None grid, the test must fail explicitly."""
        # AC-FR-01-01
        # Given: resolve mock that fails when touched
        # When: solve runs with grid None
        # Then: resolve is not called and failure contract still holds
        control = MagicSquareControl()

        def _fail_if_resolve_called(*_args: object, **_kwargs: object) -> None:
            pytest.fail("resolve() must not be called when grid is None")

        with patch.object(
            control,
            "resolve",
            side_effect=_fail_if_resolve_called,
        ):
            result = control.solve(grid_none)

        assert result.message == AC_FR_01_01_MESSAGE
