"""Boundary dimension validation tests for AC-FR-01-01 (RED)."""

from __future__ import annotations

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.failure_result import FailureResult
from tests.conftest import (
    AC_FR_01_01_CODE,
    AC_FR_01_01_MESSAGE,
    assert_invalid_size_failure,
)


class TestNormalFailureReturn:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 정상 실패 반환 (Happy Path of Failure)."""

    def test_grid_none_returns_failure_not_exception(
        self, grid_none: None
    ) -> None:
        """grid=None must return a failure object without raising."""
        # AC-FR-01-01
        # Given: grid is explicitly None
        # When: BoundaryValidator validates the grid
        # Then: a failure result is returned (no exception)
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert isinstance(result, FailureResult)

    def test_grid_none_returns_invalid_size_code(
        self, grid_none: None
    ) -> None:
        """grid=None must yield code INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid is None
        # When: validation runs
        # Then: code equals INVALID_SIZE
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert result.code == AC_FR_01_01_CODE

    def test_grid_none_returns_grid_must_be_4x4_message(
        self, grid_none: None
    ) -> None:
        """grid=None must yield the §8.1 message literal."""
        # AC-FR-01-01
        # Given: grid is None
        # When: validation runs
        # Then: message matches Grid must be 4x4.
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert result.message == AC_FR_01_01_MESSAGE

    def test_grid_none_returns_pydantic_failure_result_type(
        self, grid_none: None
    ) -> None:
        """grid=None must return the designated failure structure."""
        # AC-FR-01-01
        # Given: grid is None
        # When: validation runs
        # Then: result is FailureResult with both fields set
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert_invalid_size_failure(result, label="grid_none")

    def test_grid_none_repeat_call_returns_same_failure_contract(
        self, grid_none: None
    ) -> None:
        """grid=None must be deterministic across repeated calls."""
        # AC-FR-01-01
        # Given: grid is None and validator instance
        # When: validate is invoked twice
        # Then: both results share the same code and message
        validator = BoundaryValidator()

        first = validator.validate(grid_none)
        second = validator.validate(grid_none)

        assert first.code == second.code == AC_FR_01_01_CODE
        assert first.message == second.message == AC_FR_01_01_MESSAGE


class TestBoundaryValueCases:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 경계값 차원 오류."""

    def test_grid_empty_list_returns_invalid_size_failure(
        self, grid_empty: list[list[int]]
    ) -> None:
        """Empty list must fail with INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid is []
        # When: validation runs
        # Then: INVALID_SIZE failure is returned
        validator = BoundaryValidator()

        result = validator.validate(grid_empty)

        assert_invalid_size_failure(result, label="grid_empty")

    def test_grid_four_empty_rows_returns_invalid_size_failure(
        self, grid_four_empty_rows: list[list[int]]
    ) -> None:
        """Four rows with no columns must fail dimension check."""
        # AC-FR-01-01
        # Given: grid is [[]] * 4
        # When: validation runs
        # Then: INVALID_SIZE failure is returned
        validator = BoundaryValidator()

        result = validator.validate(grid_four_empty_rows)

        assert_invalid_size_failure(result, label="grid_four_empty_rows")

    def test_grid_3x4_returns_invalid_size_failure(
        self, grid_3x4: list[list[int]]
    ) -> None:
        """3×4 grid must fail row-count dimension check."""
        # AC-FR-01-01
        # Given: grid has 3 rows and 4 columns
        # When: validation runs
        # Then: INVALID_SIZE failure is returned
        validator = BoundaryValidator()

        result = validator.validate(grid_3x4)

        assert_invalid_size_failure(result, label="grid_3x4")

    def test_grid_empty_list_code_is_invalid_size_literal(
        self, grid_empty: list[list[int]]
    ) -> None:
        """Empty list failure code must be exactly INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid is []
        # When: validation runs
        # Then: code string equals INVALID_SIZE
        validator = BoundaryValidator()

        result = validator.validate(grid_empty)

        assert result.code == "INVALID_SIZE"

    def test_grid_3x4_message_is_grid_must_be_4x4_literal(
        self, grid_3x4: list[list[int]]
    ) -> None:
        """3×4 failure message must match §8.1 literally."""
        # AC-FR-01-01
        # Given: grid is 3×4
        # When: validation runs
        # Then: message equals Grid must be 4x4.
        validator = BoundaryValidator()

        result = validator.validate(grid_3x4)

        assert result.message == "Grid must be 4x4."


class TestMessageCharacterIdentity:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 메시지·코드 문자 단위 동일성."""

    def test_grid_none_message_equals_prd_section_8_1_literal(
        self, grid_none: None
    ) -> None:
        """None grid message must byte-match PRD §8.1 text."""
        # AC-FR-01-01
        # Given: PRD §8.1 message literal and grid None
        # When: validation runs
        # Then: message is character-identical to Grid must be 4x4.
        expected = "Grid must be 4x4."
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert result.message == expected
        assert len(result.message) == len(expected)

    def test_grid_none_code_equals_invalid_size_literal(
        self, grid_none: None
    ) -> None:
        """None grid code must byte-match INVALID_SIZE."""
        # AC-FR-01-01
        # Given: PRD §8.1 code literal and grid None
        # When: validation runs
        # Then: code is character-identical to INVALID_SIZE
        expected = "INVALID_SIZE"
        validator = BoundaryValidator()

        result = validator.validate(grid_none)

        assert result.code == expected

    def test_grid_empty_list_message_character_identity(
        self, grid_empty: list[list[int]]
    ) -> None:
        """[] failure message must not differ by whitespace or casing."""
        # AC-FR-01-01
        # Given: grid [] and §8.1 message literal
        # When: validation runs
        # Then: message equals Grid must be 4x4. exactly
        validator = BoundaryValidator()

        result = validator.validate(grid_empty)

        assert repr(result.message) == repr(AC_FR_01_01_MESSAGE)

    def test_grid_four_empty_rows_code_character_identity(
        self, grid_four_empty_rows: list[list[int]]
    ) -> None:
        """[[]]*4 failure code must be exactly INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid [[]] * 4
        # When: validation runs
        # Then: code equals INVALID_SIZE with no suffix/prefix
        validator = BoundaryValidator()

        result = validator.validate(grid_four_empty_rows)

        assert result.code == AC_FR_01_01_CODE
        assert result.code.startswith("INVALID")
        assert "BLANK" not in result.code

    def test_grid_3x4_code_and_message_character_identity(
        self, grid_3x4: list[list[int]]
    ) -> None:
        """3×4 must return both §8.1 fields with character identity."""
        # AC-FR-01-01
        # Given: grid 3×4
        # When: validation runs
        # Then: code and message match §8.1 literals together
        validator = BoundaryValidator()

        result = validator.validate(grid_3x4)

        assert (result.code, result.message) == (
            AC_FR_01_01_CODE,
            AC_FR_01_01_MESSAGE,
        )
