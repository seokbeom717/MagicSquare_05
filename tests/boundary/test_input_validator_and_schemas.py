"""InputValidator delegate and FailureResponse schema tests."""

from __future__ import annotations

from src.boundary.demo_data import SAMPLE_G1_GRID
from src.boundary.input_validator import InputValidator
from src.boundary.schemas import FailureResponse


class TestInputValidator:
    """Thin delegate to BoundaryValidator SSOT."""

    def test_validate_none_returns_invalid_size(self, grid_none: None) -> None:
        """None grid returns INVALID_SIZE via delegate."""
        result = InputValidator.validate(grid_none)

        assert result is not None
        assert result.code == "INVALID_SIZE"


class TestDemoData:
    """Sample grid fixture for UI."""

    def test_sample_g1_grid_has_two_blanks(self) -> None:
        """SAMPLE_G1_GRID is 4x4 with exactly two zero cells."""
        blank_count = sum(cell == 0 for row in SAMPLE_G1_GRID for cell in row)

        assert len(SAMPLE_G1_GRID) == 4
        assert all(len(row) == 4 for row in SAMPLE_G1_GRID)
        assert blank_count == 2


class TestFailureResponseSchema:
    """Pydantic envelope for boundary failures."""

    def test_failure_response_fields(self) -> None:
        """FailureResponse stores type, code, and message."""
        model = FailureResponse(
            type="ERROR",
            code="E002",
            message="Blank count must be exactly 2.",
        )

        assert model.type == "ERROR"
        assert model.code == "E002"
