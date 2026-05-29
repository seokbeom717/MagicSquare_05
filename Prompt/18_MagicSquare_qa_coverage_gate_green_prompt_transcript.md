# MagicSquare QA Gate GREEN Prompt Transcript

## 세션 개요

- **주제:** Report/17 QA gate 미충족 → TDD 보완 → NFR-01·02·03 GREEN
- **브랜치:** `refactor/refactor`
- **선행:** Report/17 (분석 baseline), `docs/qa_ssot_mapping.md`

---

## Turn 1 — 사용자: QA 실패 시 무엇을 더 해야 하나

### 에이전트 답변 요약

- 테스트 72/72 PASS — **실패는 커버리지 NFR** 3종
- Domain 90% → `solve_partial`, `resolve`, Step A-only, validator 분기, user
- Boundary 35% → `gui/` drag-down; 핵심 ~97%
- 전역 50% → GUI pytest 또는 cov omit
- 권장 순서: P0 Domain → validator → GUI/omit

---

## Turn 2 — 사용자: 추천 순서대로 진행

### 에이전트 실행

**Step 1 — Domain P0**

- `tests/entity/test_solve_partial_magic_square.py`
- `tests/control/test_magic_square_control_resolve.py`
- `grid_g4_step_a_only`, `grid_column_sum_mismatch` fixtures
- `test_d_sol_05`, D-VAL-03 수정, `test_user` +2

**Step 2 — Boundary**

- `tests/boundary/test_input_validator_and_schemas.py`
- `tests/boundary/gui/test_random_puzzle.py`

**Step 3 — GUI·cov 정책**

- `.coveragerc` — `omit src/boundary/gui/*`
- `src/boundary/gui/__init__.py` lazy `run_gui()`
- `tests/boundary/gui/test_grid_panel.py` (PyQt6, importorskip)
- PyQt6 pip 설치 실패(Windows long path) → grid_panel skip

### 측정 결과

| Gate | 결과 |
|------|------|
| NFR-01 | 98% ✅ |
| NFR-02 | 98% ✅ |
| NFR-03 | 98% ✅ |
| pytest | 86 passed, 1 skipped |

---

## Turn 3 — 사용자: Report/18 vs Report/17 업데이트?

### 에이전트 권고

- **Report/18 신규** — 17=진단(baseline FAIL), 18=구현(GREEN)
- Report/17에 후속 링크 1줄만 추가

---

## Turn 4 — 사용자: 진행

### 에이전트 실행 (예정)

1. `Report/18_MagicSquare_qa_coverage_gate_green_report.md`
2. `Prompt/18_...` (본 파일)
3. Report/17 §11 후속 링크
4. git commit + push

---

## 기술 결정

| 항목 | 결정 |
|------|------|
| Step A-only grid | G0에서 (2,1)(2,2) blank → `[3,2,6,3,3,7]` |
| cov gate | `.coveragerc` gui omit + `--cov-fail-under` |
| PyQt6 | grid_panel skip; random_puzzle는 lazy gui `__init__`로 import 가능 |
| GM·계약 | 변경 없음 — 테스트만 추가 |
