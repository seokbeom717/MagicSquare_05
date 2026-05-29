"""Serialize solver results and grids into Golden Master text format."""

from __future__ import annotations

import re
from src.boundary.failure_result import FailureResult

from tests.golden_master.scenarios import GOLDEN_MASTER_SCENARIOS, GoldenMasterScenario

_SECTION_SEP = "________________________________________"
_SECTION_HEADER = re.compile(r"^\[([a-z_]+)\]$")


def format_grid(grid: list[list[int]]) -> str:
    """Format a 4x4 grid as space-separated rows."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def serialize_result(result: FailureResult | list[int]) -> str:
    """Serialize a solver result DTO into Golden Master output text."""
    if isinstance(result, FailureResult):
        return f"Error:\n{result.code}"
    compact = ",".join(str(value) for value in result)
    return f"Output:\n[{compact}]"


def serialize_scenario_section(
    scenario: GoldenMasterScenario,
    result: FailureResult | list[int],
) -> str:
    """Serialize one scenario block including input and result."""
    lines = [
        f"[{scenario.name}]",
        "Input:",
        format_grid(scenario.grid),
        serialize_result(result),
    ]
    return "\n".join(lines)


def render_golden_master_document(
    sections: list[tuple[GoldenMasterScenario, FailureResult | list[int]]],
) -> str:
    """Render the full Golden Master document from scenario results."""
    blocks = [
        serialize_scenario_section(scenario, result)
        for scenario, result in sections
    ]
    return f"\n{_SECTION_SEP}\n\n".join(blocks) + "\n"


def parse_golden_master_document(text: str) -> dict[str, str]:
    """Parse a Golden Master document into section-name → block text."""
    sections: dict[str, str] = {}
    current_name: str | None = None
    current_lines: list[str] = []

    for line in text.splitlines():
        header = _SECTION_HEADER.match(line)
        if header is not None:
            if current_name is not None:
                sections[current_name] = _normalize_section_text(
                    "\n".join(current_lines).rstrip()
                )
            current_name = header.group(1)
            current_lines = [line]
            continue
        if current_name is not None:
            current_lines.append(line)

    if current_name is not None:
        sections[current_name] = _normalize_section_text(
            "\n".join(current_lines).rstrip()
        )

    return sections


def _normalize_section_text(text: str) -> str:
    """Strip document separator lines from a parsed section block."""
    lines = text.splitlines()
    while lines and lines[-1] == _SECTION_SEP:
        lines.pop()
    return "\n".join(lines)


def expected_section_names() -> list[str]:
    """Return ordered scenario section names."""
    return [scenario.name for scenario in GOLDEN_MASTER_SCENARIOS]
