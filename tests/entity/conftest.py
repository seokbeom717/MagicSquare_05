"""Entity-track grid placeholders (Report/09 §6) — RED skeleton fixtures TBD at GREEN."""

from __future__ import annotations

# G0_placeholder — complete 4x4 magic square (D-VAL-01, U-IN-03a)
# G0 = [
#     [16, 3, 2, 13],
#     [5, 10, 11, 8],
#     [9, 6, 7, 12],
#     [4, 15, 14, 1],
# ]

# G1_placeholder — blanks 0-index (1,1), (2,2); missing {7, 10} (D-LOC-01, D-MIS-01)
# G1 = [
#     [16, 2, 3, 13],
#     [5, 0, 11, 8],
#     [9, 6, 0, 12],
#     [4, 14, 15, 1],
# ]

# G2_placeholder — Step A fail, Step B success (D-SOL-02): TBD before GREEN
# G3_placeholder — both steps fail → UnsolvableDomainError (D-SOL-03): TBD before GREEN
