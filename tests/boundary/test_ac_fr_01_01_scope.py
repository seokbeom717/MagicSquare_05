"""AC-FR-01-01 scope guard tests — no production imports (RED companion)."""

from __future__ import annotations

import ast
from pathlib import Path

_BOUNDARY_TEST_DIR = Path(__file__).resolve().parent
_AC_FR_01_01_SUT_TEST_FILES = (
    _BOUNDARY_TEST_DIR / "test_boundary_validator_dimension.py",
)
_FORBIDDEN_SCOPE_TEST_NAMES = (
    "test_grid_4x4_valid",
    "test_blank_count",
    "test_duplicate",
    "test_out_of_range",
)


class TestScopeRestriction:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — AC-FR-01-02~05 / FR-02~05 범위 제한."""

    def test_scope_boundary_suite_excludes_blank_count_error_token(
        self,
    ) -> None:
        """This suite must not reference AC-FR-01-02 blank-count errors."""
        # AC-FR-01-01
        # Given: boundary test sources under tests/boundary/
        # When: sources are scanned for forbidden tokens
        # Then: ERR_INVALID_BLANK_COUNT is absent
        sources = _read_ac_fr_01_01_sut_sources()

        assert "ERR_INVALID_BLANK_COUNT" not in sources

    def test_scope_boundary_suite_excludes_duplicate_value_token(
        self,
    ) -> None:
        """This suite must not reference AC-FR-01-04 duplicate errors."""
        # AC-FR-01-01
        # Given: boundary test sources
        # When: scanned for duplicate-value AC tokens
        # Then: ERR_DUPLICATE_VALUE is absent
        sources = _read_ac_fr_01_01_sut_sources()

        assert "ERR_DUPLICATE_VALUE" not in sources

    def test_scope_boundary_suite_excludes_out_of_range_token(
        self,
    ) -> None:
        """This suite must not reference AC-FR-01-03 range errors."""
        # AC-FR-01-01
        # Given: boundary test sources
        # When: scanned for range-violation AC tokens
        # Then: ERR_OUT_OF_RANGE is absent
        sources = _read_ac_fr_01_01_sut_sources()

        assert "ERR_OUT_OF_RANGE" not in sources

    def test_scope_boundary_suite_excludes_fr02_to_fr05_domain_components(
        self,
    ) -> None:
        """This suite must not import FR-02~05 domain components."""
        # AC-FR-01-01
        # Given: boundary test sources
        # When: scanned for domain component names
        # Then: BlankFinder/MissingNumberFinder/Validator/Solver absent
        sources = _read_ac_fr_01_01_sut_sources()

        for token in (
            "BlankFinder",
            "MissingNumberFinder",
            "MagicSquareValidator",
            "Solver",
        ):
            assert token not in sources

    def test_scope_no_four_by_four_valid_success_test_in_boundary_suite(
        self,
    ) -> None:
        """No test in this suite may target a valid 4×4 success path."""
        # AC-FR-01-01
        # Given: test function names in tests/boundary/
        # When: names are collected
        # Then: forbidden valid-grid / FR-02~05 test name patterns are absent
        names = _collect_test_function_names(_AC_FR_01_01_SUT_TEST_FILES)

        for forbidden in _FORBIDDEN_SCOPE_TEST_NAMES:
            assert forbidden not in names, (
                f"forbidden test name present: {forbidden}"
            )


def _read_ac_fr_01_01_sut_sources() -> str:
    """Read only AC-FR-01-01 SUT test sources (excludes scope guard module)."""
    parts: list[str] = []
    for path in _AC_FR_01_01_SUT_TEST_FILES:
        parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def _collect_test_function_names(paths: tuple[Path, ...]) -> set[str]:
    """Collect test function names from given pytest modules."""
    names: set[str] = set()
    for path in paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name.startswith(
                "test_"
            ):
                names.add(node.name)
    return names
