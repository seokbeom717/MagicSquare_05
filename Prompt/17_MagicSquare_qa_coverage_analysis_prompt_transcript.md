# MagicSquare QA 커버리지 분석 Prompt Transcript

## 세션 개요

- **주제:** Dual-Track QA 커버리지 분석 (Ask mode) → SSOT 보정 (Agent mode) → 재측정 → 보고서·GitHub
- **브랜치:** `refactor/refactor`
- **TDD 단계:** REFACTOR — QA only (production 코드 미변경)

---

## Turn 1 — 사용자: QA 커버리지 분석 (Step 0·1)

### 요청

- Ask mode — QA 커버리지 분석 only
- ECB 경로 매핑 (가상명 → 실경로) 표 제공
- Step 0: `pytest -q`, GM-1, RED 스켈레톤, 19 RED gate
- Step 1: Dual-Track cov (Domain ≥95%, Boundary ≥85%, 전역 ≥80%)
- 참조: `.cursorrules`, `docs/test_plan.md` §6·§7, Report/02 DualTrack (I1~I11)

### 에이전트 실행

1. `python -m pytest -q` → **72 passed**
2. `tests/test_gm_01_magic_square_golden_master.py` → **파일 없음**
3. Dual-Track cov → Domain 90%, Boundary 35%, 전역 50%
4. `pytest.fail` → mock guard 1건만 (RED 스켈레톤 0건)

### 주요 발견

- GM SSOT: `tests/test_golden_master_magic_square.py` (6 passed)
- 19 RED: 해당 없음 (0 RED)
- 프롬프트 ECB 표·파일명·건수 다수 불일치

---

## Turn 2 — 사용자: GM 파일명 확인

### 요청

> `test_gm_01_magic_square_golden_master.py`를 대체하는 게 `test_golden_master_magic_square.py`일 것 같은데, 이 부분 추가해서 다시 진행

### 에이전트 실행

- GM 경로 SSOT로 재측정 — 동일 수치 (72/6 PASS, cov 90/35/50%)
- GM 매핑표 정리 (GM-01=txt, GM-04=test file)

---

## Turn 3 — 사용자: 다른 보정 항목?

### 요청

> 다른 실패들에 대해서 보정 반영할 게 없어?

### 에이전트 답변 (7~8건)

1. ECB 경로 (control/solve_partial 없음, entity flat, gui/screen)
2. Report/02 파일명, I1~I11 → Report/09
3. ERR_INVALID_DIMENSION vs INVALID_SIZE
4. DomainResolver → PuzzleGateway mock
5. boundary 28 → 38건
6. 19 RED → 0 RED
7. FailureResult vs schemas.FailureResponse
8. README 90% → 80% 전역 목표

---

## Turn 4 — 사용자: 보정 매핑표 작성 및 적용

### 요청

> 보정 매핑표를 만들고 보정을 진행해줘. 그 다음 다시 진행할거야

### 에이전트 실행 (Agent mode)

**신규**

- `docs/qa_ssot_mapping.md` — QA SSOT 보정 매핑표 v1.0

**갱신**

- `docs/test_plan.md` v1.1 — INVALID_SIZE, PuzzleGateway mock, §7.5 Dual-Track cov
- `README.md` — 38건, Track B ✅, ECB 표, GM 별칭, qa_ssot 링크
- `tests/test_golden_master_magic_square.py` — docstring GM-04 + legacy alias

**검증:** `pytest -q` → 72 passed

---

## Turn 5 — 사용자: SSOT로 QA 재수행

### 요청

> 보정 데이터를 활용해서 QA 스크립트 다시 수행

### 에이전트 실행

- `docs/qa_ssot_mapping.md` SSOT 적용하여 Step 0·1 재측정
- 결과 동일: 72/6 PASS, NFR Domain ❌ 90%, Boundary ❌ 35% (핵심 ~97%), 전역 ❌ 50%
- REFACTOR gate: 테스트·GM ✅, cov NFR ❌

---

## Turn 6 — 사용자: 보고서 작성 및 GitHub 업로드

### 요청

> `@.cursor/rules/workflow-automation.mdc` 보고서 작성 및 깃허브 업로드

### 에이전트 실행 (예정)

1. `Report/17_MagicSquare_qa_coverage_analysis_report.md`
2. `Prompt/17_MagicSquare_qa_coverage_analysis_prompt_transcript.md` (본 파일)
3. git commit + push `refactor/refactor`

---

## 기술 결정·SSOT 요약

| 항목 | SSOT |
|------|------|
| GM 테스트 | `tests/test_golden_master_magic_square.py` |
| GM baseline | `tests/golden_master_expected.txt` |
| 차원 오류 | `INVALID_SIZE` / `Grid must be 4x4.` |
| Orchestration SUT | `PuzzleGateway.solve` + `patch.object(gateway._control, "resolve")` |
| Solver SSOT | `entity/two_cell_solver.solution` |
| pytest 합계 | 72 (boundary 38 + control 10 + entity 18 + GM 6) |
| cov 게이트 | Domain 90% ❌, Boundary 패키지 35% ❌, 전역 50% ❌ |

## 커버리지 갭 (후속)

- `magic_square_validator` L17,19,22
- `two_cell_solver` L48 (Step A-only)
- `solve_partial_magic_square` 0%
- `boundary/gui/*` 0%
