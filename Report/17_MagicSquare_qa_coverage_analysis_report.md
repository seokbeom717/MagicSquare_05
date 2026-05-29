# MagicSquare QA 커버리지 분석 보고서

## 1. 작업 목적

- REFACTOR 완료 후 **Dual-Track QA 커버리지 분석**(Step 0·Step 1)을 수행한다.
- 프롬프트·문서·저장소 간 불일치를 **`docs/qa_ssot_mapping.md`** 로 보정하고, SSOT 기준으로 재측정한다.
- TDD REFACTOR gate(테스트·GM·NFR) 충족 여부를 기록한다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **TDD 단계** | REFACTOR — QA 분석 only (production 코드 변경 없음) |
| **선행** | Report/16 REFACTOR 실행 완료, 72 pytest GREEN |
| **NFR 기준** | `docs/test_plan.md` §6·§7 — Domain ≥95%, Boundary ≥85%, 전역 ≥80% |
| **SSOT** | `docs/qa_ssot_mapping.md` (신규), `docs/test_plan.md` v1.1 |

## 3. SSOT 보정 작업 요약

프롬프트 템플릿과 저장소 불일치를 식별·문서화·반영했다.

| 구분 | 구식/프롬프트 | SSOT |
|------|---------------|------|
| GM 테스트 | `test_gm_01_magic_square_golden_master.py` | `tests/test_golden_master_magic_square.py` |
| GM baseline | — | `tests/golden_master_expected.txt` (GM-01) |
| Domain Control | `control/solve_partial_magic_square.py` | `control/magic_square_control.py` |
| Domain solver | — | `entity/two_cell_solver.py` → `solution()` |
| Entity 구조 | `entity/services/*` | `entity/*.py` (flat) |
| GUI | `boundary/screen/` | `boundary/gui/` |
| 오류 code | `ERR_INVALID_DIMENSION` (PRD 추적) | **`INVALID_SIZE`** (assert SSOT) |
| boundary pytest | 28건 | **38건** |
| RED gate | 19 RED 스켈레톤 | **0건** (GREEN 완료) |
| Report/02 DualTrack | `02.MagicSquare_DualTrack_TDD_Design_Report.md` | `02_MagicSquare_4x4_TDD_design_report.md` |
| I1~I11 | Report/02 | **Report/09** §5.2 |

### 3.1 갱신 파일

| 파일 | 변경 |
|------|------|
| `docs/qa_ssot_mapping.md` | **신규** — QA SSOT 보정 매핑표 |
| `docs/test_plan.md` | v1.1 — INVALID_SIZE, PuzzleGateway mock, Dual-Track cov §7.5 |
| `README.md` | 38건, Track B ✅, ECB 표 확장, GM 별칭, qa_ssot 링크 |
| `tests/test_golden_master_magic_square.py` | docstring — GM-04 SSOT, legacy alias |

## 4. Step 0 — 기준선 (측정 결과)

```text
python -m pytest -q                    → 72 passed, 0 failed
python -m pytest tests/test_golden_master_magic_square.py -q → 6 passed
```

| 항목 | 결과 |
|------|------|
| **PASS / FAIL** | 72 / 0 |
| **RED 스켈레톤** | 0건 (`pytest.fail("RED: ...")` 없음) |
| **Mock guard** | 1건 — `test_solve_orchestration_dimension.py` L96 (의도적) |
| **GM (SSOT)** | 6/6 PASS (GM-TC-00~05) |
| **19 RED gate** | 해당 없음 — REFACTOR gate (테스트) ✅ |

### 4.1 pytest 건수 (SSOT)

| 스코프 | 건수 |
|--------|------|
| `tests/boundary/` | 38 |
| `tests/control/` | 10 |
| `tests/entity/` | 18 |
| Golden Master | 6 |
| **합계** | **72** |

## 5. Step 1 — Dual-Track 커버리지

### 5.1 NFR 게이트

| Track | NFR | 목표 | 측정 | 판정 |
|-------|-----|------|------|------|
| Domain (`entity`+`control`) | NFR-01 | ≥ 95% | **90%** | ❌ −5pp |
| Boundary (패키지 전체) | NFR-02 | ≥ 85% | **35%** | ❌ |
| Boundary (비-GUI 핵심) | — | ≥ 85% | **~97%** | ✅ |
| 전역 `src/` | NFR-03 | ≥ 80% | **50%** | ❌ −30pp |

### 5.2 Domain Track — 90% (28 passed)

| 모듈 | Cover | Missing | 비고 |
|------|-------|---------|------|
| `blank_locator`, `constants`, `missing_number_finder` | 100% | — | |
| `two_cell_solver` | 97% | L48 | Step A-only magic |
| `user` | 94% | 73–74, 98 | Magic Square 범위 외 |
| `magic_square_validator` | 82% | 17, 19, 22 | 열/역대각/범위 실패 |
| `magic_square_control` | 80% | L13 | `resolve()` 직접 경로 |
| `solve_partial_magic_square` | 0% | 3–13 | Control 미배선 |

도메인 핵심 (`user`, `solve_partial` 제외): ~**94%**.

### 5.3 Boundary Track — 35% (38 passed)

| 모듈 | Cover |
|------|-------|
| `puzzle_gateway`, `ui_boundary`, `failure_result` | 100% |
| `boundary_validator` | 96% (L60–62) |
| `input_validator` | 88% (L24) |
| `schemas`, `demo_data` | 0% |
| **`boundary/gui/*`** | **0%** (219 stmts) |

패키지 35%는 `gui/` drag-down. 핵심 계약 모듈은 NFR-02 충족.

### 5.4 전역 — 50%

- miss 243 stmts 중 ~90% = `boundary/gui/*`
- Report/16·README Refactoring CheckList와 동일

## 6. REFACTOR gate 종합

| Gate | 판정 |
|------|------|
| RED 0 + 72 PASS | ✅ |
| GM 6/6 | ✅ |
| NFR-01 Domain ≥95% | ❌ |
| NFR-02 Boundary (패키지) | ❌ / 핵심 ✅ |
| NFR-03 전역 ≥80% | ❌ |

**결론:** 회귀·Golden Master GREEN. 커버리지 NFR 패키지 기준 3종 미충족 — 후속 GREEN 과제.

## 7. ECB 실제 매핑 (QA 분석 기준)

| 레이어 | SSOT 파일 |
|--------|-----------|
| Screen | `boundary/gui/main_window.py`, `app.py`, `grid_panel.py` |
| Boundary | `boundary_validator`, `puzzle_gateway`, `ui_boundary`, `failure_result`, `input_validator` |
| Control | `magic_square_control.py`, `two_cell_solver.py` (re-export) |
| Entity | `two_cell_solver.solution`, `blank_locator`, `magic_square_validator`, `solve_partial_magic_square` |

**의존:** `Screen → UiBoundary → PuzzleGateway → MagicSquareControl → entity.solution`

## 8. 후속 권고 (우선순위)

| P | 조치 | 기대 |
|---|------|------|
| P0 | `magic_square_validator` 열/역대각/범위 실패 테스트 3건 | NFR-01 +3~4pp |
| P0 | Step A-only magic (`two_cell_solver` L48) | NFR-01 +1pp |
| P1 | `solve_partial` Control 배선 또는 dead code 정리 | NFR-01 +4pp |
| P2 | `tests/boundary/gui/test_grid_panel.py` | NFR-03 +~45pp |

## 9. 재현 명령

```powershell
python -m pytest -q
python -m pytest tests/test_golden_master_magic_square.py -q
python -m pytest tests/entity/ tests/control/ --cov=src/entity --cov=src/control --cov-report=term-missing
python -m pytest tests/boundary/ --cov=src/boundary --cov-report=term-missing
python -m pytest --cov=src --cov-report=term-missing
```

## 10. 산출물

| 파일 | 설명 |
|------|------|
| `docs/qa_ssot_mapping.md` | QA SSOT 보정 매핑표 |
| `docs/test_plan.md` v1.1 | test_plan SSOT 정합 |
| `README.md` | 건수·ECB·GM·커버리지 갱신 |
| `Report/17_MagicSquare_qa_coverage_analysis_report.md` | 본 보고서 |
| `Prompt/17_MagicSquare_qa_coverage_analysis_prompt_transcript.md` | 세션 transcript |

## 11. 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 1.0 | 2026-05-29 | QA 커버리지 분석·SSOT 보정·Dual-Track cov 측정 |

> **후속:** [Report/18 — QA NFR gate GREEN](18_MagicSquare_qa_coverage_gate_green_report.md) (커버리지 보완 테스트·`.coveragerc`, 98%/98%/98%)
