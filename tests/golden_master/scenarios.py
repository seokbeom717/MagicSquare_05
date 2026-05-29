"""Golden Master scenario definitions — input grids keyed by section name."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

Grid = list[list[int]]


@dataclass(frozen=True)
class GoldenMasterScenario:
    """One approval scenario: section name plus input grid."""

    name: str
    grid: Grid | Any


NORMAL_SUCCESS_GRID: Grid = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

REVERSE_SUCCESS_GRID: Grid = [
    [0, 0, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

INVALID_BLANK_COUNT_GRID: Grid = [
    [0, 1, 2, 3],
    [4, 0, 6, 7],
    [8, 9, 0, 11],
    [12, 13, 14, 15],
]

DUPLICATE_NUMBER_GRID: Grid = [
    [16, 2, 3, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 8, 15, 1],
]

NO_VALID_SOLUTION_GRID: Grid = [
    [0, 3, 2, 0],
    [5, 10, 15, 8],
    [9, 6, 7, 12],
    [4, 11, 14, 1],
]

GOLDEN_MASTER_SCENARIOS: tuple[GoldenMasterScenario, ...] = (
    GoldenMasterScenario("normal_success", NORMAL_SUCCESS_GRID),
    GoldenMasterScenario("reverse_success", REVERSE_SUCCESS_GRID),
    GoldenMasterScenario("invalid_blank_count", INVALID_BLANK_COUNT_GRID),
    GoldenMasterScenario("duplicate_number", DUPLICATE_NUMBER_GRID),
    GoldenMasterScenario("no_valid_solution", NO_VALID_SOLUTION_GRID),
)
