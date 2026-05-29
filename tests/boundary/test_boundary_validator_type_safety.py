"""BoundaryValidator type-safety — FailureResult without TypeError."""

from __future__ import annotations

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.failure_result import FailureResult
from tests.conftest import (
    AC_FR_01_01_CODE,
    U_IN_04_CODE,
    assert_invalid_size_failure,
    assert_out_of_range_failure,
)


class TestBoundaryValidatorTypeSafety:
    """Non-list, jagged row, and non-int cells return FailureResult envelopes."""

    def test_string_grid_returns_invalid_size_failure(self) -> None:
        """Non-list grid must not raise TypeError."""
        validator = BoundaryValidator()

        result = validator.validate("not-a-grid")

        assert_invalid_size_failure(result, label="string_grid")

    def test_jagged_row_returns_invalid_size_failure(self) -> None:
        """Ragged rows must return INVALID_SIZE without TypeError."""
        grid = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        validator = BoundaryValidator()

        result = validator.validate(grid)

        assert_invalid_size_failure(result, label="jagged_row")

    def test_float_cell_returns_out_of_range_failure(self) -> None:
        """Non-int cell must return E004 without TypeError."""
        grid = [
            [1.0, 2, 3, 4],
            [5, 0, 7, 8],
            [9, 10, 0, 12],
            [13, 14, 15, 16],
        ]
        validator = BoundaryValidator()

        result = validator.validate(grid)

        assert_out_of_range_failure(result, label="float_cell")

    def test_bool_cell_returns_out_of_range_failure(self) -> None:
        """bool is not int — must return E004 without TypeError."""
        grid = [
            [True, 2, 3, 4],
            [5, 0, 7, 8],
            [9, 10, 0, 12],
            [13, 14, 15, 16],
        ]
        validator = BoundaryValidator()

        result = validator.validate(grid)

        assert_out_of_range_failure(result, label="bool_cell")

    def test_type_safety_never_raises(self) -> None:
        """Validator must always return FailureResult or None."""
        validator = BoundaryValidator()
        samples: list[object] = [None, 42, [[1, 2], [3]]]

        for sample in samples:
            result = validator.validate(sample)
            assert result is None or isinstance(result, FailureResult)

    def test_invalid_size_code_literal_for_non_list(self) -> None:
        """Non-list failure code remains INVALID_SIZE."""
        validator = BoundaryValidator()

        result = validator.validate(12345)

        assert result is not None
        assert result.code == AC_FR_01_01_CODE

    def test_out_of_range_code_literal_for_non_int(self) -> None:
        """Non-int cell failure code remains E004."""
        grid = [
            ["a", 2, 3, 4],
            [5, 0, 7, 8],
            [9, 10, 0, 12],
            [13, 14, 15, 16],
        ]
        validator = BoundaryValidator()

        result = validator.validate(grid)

        assert result is not None
        assert result.code == U_IN_04_CODE
