"""Approve-pattern utilities for Golden Master regression tests."""

from __future__ import annotations

import difflib
import os
from pathlib import Path

from src.boundary.puzzle_gateway import PuzzleGateway

from tests.golden_master.scenarios import GOLDEN_MASTER_SCENARIOS
from tests.golden_master.serializer import render_golden_master_document

DEFAULT_GOLDEN_MASTER_PATH = (
    Path(__file__).resolve().parent.parent / "golden_master_expected.txt"
)
_APPROVE_ENV_VAR = "GOLDEN_MASTER_APPROVE"


def collect_actual_output() -> str:
    """Run all scenarios through MagicSquareControl and render the document."""
    gateway = PuzzleGateway()
    sections = [
        (scenario, gateway.solve(scenario.grid))
        for scenario in GOLDEN_MASTER_SCENARIOS
    ]
    return render_golden_master_document(sections)


def approve(
    actual: str,
    expected_path: Path | None = None,
    *,
    force_approve: bool | None = None,
) -> str:
    """Compare actual output to golden master; approve when missing or forced.

    Returns the expected text (existing or newly written).
  """
    path = expected_path or DEFAULT_GOLDEN_MASTER_PATH
    should_approve = (
        force_approve
        if force_approve is not None
        else os.environ.get(_APPROVE_ENV_VAR, "").lower() in {"1", "true", "yes"}
    )

    if not path.exists() or should_approve:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(actual, encoding="utf-8")
        return actual

    expected = path.read_text(encoding="utf-8")
    if actual == expected:
        return expected

    raise AssertionError(format_golden_diff(expected, actual, hint=path))


def format_golden_diff(
    expected: str,
    actual: str,
    *,
    hint: Path | str | None = None,
) -> str:
    """Format a Golden Master mismatch as unified diff (--- expected / +++ actual)."""
    diff = "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm="",
        )
    )
    suffix = (
        f"\nRe-run with GOLDEN_MASTER_APPROVE=1 to update ({hint})."
        if hint is not None
        else "\nRe-run with GOLDEN_MASTER_APPROVE=1 to update."
    )
    return f"Golden Master mismatch.{suffix}\n{diff}"


def collect_scenario_section(scenario_name: str) -> str:
    """Serialize one scenario block from live solver output."""
    gateway = PuzzleGateway()
    for scenario in GOLDEN_MASTER_SCENARIOS:
        if scenario.name == scenario_name:
            from tests.golden_master.serializer import serialize_scenario_section

            result = gateway.solve(scenario.grid)
            return serialize_scenario_section(scenario, result)
    raise KeyError(f"Unknown golden master scenario: {scenario_name}")


def approve_section(
    scenario_name: str,
    actual_section: str,
    expected_path: Path | None = None,
    *,
    force_approve: bool | None = None,
) -> str:
    """Compare one scenario section against the golden master baseline."""
    path = expected_path or DEFAULT_GOLDEN_MASTER_PATH
    should_approve = (
        force_approve
        if force_approve is not None
        else os.environ.get(_APPROVE_ENV_VAR, "").lower() in {"1", "true", "yes"}
    )

    if not path.exists() or should_approve:
        full_actual = collect_actual_output()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(full_actual, encoding="utf-8")
        from tests.golden_master.serializer import parse_golden_master_document

        return parse_golden_master_document(full_actual)[scenario_name]

    from tests.golden_master.serializer import parse_golden_master_document

    expected_document = path.read_text(encoding="utf-8")
    expected_sections = parse_golden_master_document(expected_document)
    if scenario_name not in expected_sections:
        raise AssertionError(
            f"Golden Master missing section [{scenario_name}] in {path}"
        )

    expected_section = expected_sections[scenario_name]
    if actual_section == expected_section:
        return expected_section

    raise AssertionError(
        format_golden_diff(expected_section, actual_section, hint=path)
    )


def run_golden_master_approval(
    expected_path: Path | None = None,
    *,
    force_approve: bool | None = None,
) -> str:
    """Collect actual solver output and run the approve pattern."""
    actual = collect_actual_output()
    return approve(actual, expected_path, force_approve=force_approve)
