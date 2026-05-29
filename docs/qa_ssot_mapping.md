# MagicSquare — QA SSOT 보정 매핑표

| 항목 | 내용 |
|------|------|
| **문서 버전** | 1.0 |
| **용도** | Dual-Track QA·커버리지 분석 프롬프트 ↔ 저장소 SSOT 정합 |
| **갱신 기준** | REFACTOR 완료 후 (Report/16, README Refactoring CheckList) |

> QA 커버리지 분석(Step 0·Step 1) 실행 전 본 문서를 **단일 진실 공급원(SSOT)** 으로 사용한다.

---

## 1. ECB 경로 매핑 (프롬프트 가상명 → 실경로)

| 프롬프트 관례 | 잘못된/구식 경로 | **실제 SSOT 경로** | 레이어 |
|---------------|------------------|-------------------|--------|
| `domain.py` | `src/control/solve_partial_magic_square.py` | ❌ **Control에 없음** — 아래 Entity·Control 참조 | — |
| Domain orchestration | `Control.solve()` | `src/control/magic_square_control.py` → `resolve()` | Control |
| Domain solver SSOT | — | `src/entity/two_cell_solver.py` → `solution()` | Entity |
| Domain execute 래퍼 | — | `src/entity/solve_partial_magic_square.py` → `execute()` | Entity |
| Control re-export | — | `src/control/two_cell_solver.py` (entity re-export) | Control |
| `boundary.py` | `ui_boundary`, `input_validator`, `schemas` 만 | + `boundary_validator.py`, `puzzle_gateway.py`, `failure_result.py` | Boundary |
| Failure envelope | `schemas.FailureResponse` (pydantic) | `failure_result.FailureResult` | Boundary |
| `gui` / Screen | `boundary/screen/main_window.py` | `boundary/gui/main_window.py`, `grid_panel.py`, `app.py` | Screen (Boundary 하위) |
| Entity services | `entity/services/*.py`, `value_objects/`, `exceptions/` | ❌ **미존재** — `src/entity/*.py` (flat) | Entity |

**허용 의존:** `Screen → Boundary(UiBoundary) → Boundary(PuzzleGateway) → Control → Entity`

---

## 2. 문서·Report 파일명

| 프롬프트/구식 | **실제 SSOT** |
|---------------|---------------|
| `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md` | `Report/02_MagicSquare_4x4_TDD_design_report.md` |
| I1~I11 invariant 매핑 (Report/02) | `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` §5.2 |
| Dual-Track RED 설계 SSOT | `Report/09_...` (Track A/B Test ID) |
| REFACTOR 실행 보고 | `Report/16_MagicSquare_refactoring_execution_report.md` |

---

## 3. Golden Master 매핑

| ID / 구식명 | **실제 SSOT** | 비고 |
|-------------|---------------|------|
| GM-01 | `tests/golden_master_expected.txt` | baseline **파일** (approve 패턴) |
| GM-04 (테스트 코드) | `tests/test_golden_master_magic_square.py` | GM-TC-00~05 (6건) |
| ~~`test_gm_01_magic_square_golden_master.py`~~ | ❌ **존재하지 않음** | → 위 파일로 치환 |
| 실행 명령 | `python -m pytest -m golden_master -v` | 마커 = 파일 6건과 동일 |
| 파일 docstring "GM-2" | GM-04 테스트 SSOT와 동일 | 명칭만 다름 |

---

## 4. 오류 코드·메시지 (차원 검증 AC-FR01-01)

| 출처 | code | message |
|------|------|---------|
| PRD / test_plan v1.0 (추적용) | `ERR_INVALID_DIMENSION` | `Input matrix must be 4x4.` |
| **구현·pytest assert SSOT** | **`INVALID_SIZE`** | **`Grid must be 4x4.`** |

`tests/conftest.py` → `AC_FR_01_01_CODE`, `AC_FR_01_01_MESSAGE`  
`src/boundary/boundary_validator.py` → `_INVALID_SIZE_*`

---

## 5. SUT·mock 대상 (orchestration / AC-FR01-05)

| test_plan v1.0 (개념) | **실제 SSOT** |
|-----------------------|---------------|
| `control.solve(grid=None)` | `PuzzleGateway().solve(grid=None)` |
| `@patch("...DomainResolver")` | `patch.object(gateway._control, "resolve")` |
| `DomainResolver.solve` | `MagicSquareControl.resolve` → `entity.two_cell_solver.solution` |
| U-FLOW execute spy | `patch.object(..., "execute")` on `SolvePartialMagicSquare` (control tests) |

**대표 테스트:** `tests/control/test_solve_orchestration_dimension.py` (5건)

---

## 6. pytest 건수 (2026-05-29 REFACTOR 후)

| 스코프 | 구식 기재 | **현재 SSOT** |
|--------|-----------|---------------|
| `tests/boundary/` | 28건 | **38건** |
| `tests/control/` | 10건 (orchestration) | **10건** |
| `tests/entity/` (D-* + user) | — | **18건** |
| Golden Master | — | **6건** |
| **전체** | — | **72 passed** |

**boundary 38건 내역:** scope 5 + dimension 16 + type_safety 7 + u_in 5 + u_out 2 + ui_boundary 3

---

## 7. REFACTOR gate · RED

| 조건 | **현재 SSOT** |
|------|---------------|
| ~~19 RED 스켈레톤~~ (구 템플릿) | **0건** — Report/10·11 스켈레톤 → GREEN 완료 |
| RED 확인 | `pytest.fail("RED: ...")` 스켈레톤 0건; mock guard 1건(의도적) |
| REFACTOR gate (테스트) | 72/72 PASS + GM 6/6 PASS |
| REFACTOR gate (커버리지) | NFR-01·02·03 — §8 참조 |

---

## 8. Dual-Track 커버리지 측정 (Step 1 SSOT)

```powershell
# Domain Track (NFR-01: ≥ 95%)
python -m pytest tests/entity/ tests/control/ `
  --cov=src/entity --cov=src/control `
  --cov-report=term-missing

# Boundary Track (NFR-02: ≥ 85%)
python -m pytest tests/boundary/ `
  --cov=src/boundary `
  --cov-report=term-missing

# 전역 gate (NFR-03: ≥ 80%)
python -m pytest `
  --cov=src --cov-report=term-missing
```

### 8.1 해석 규칙

| Track | 목표 | 패키지 전체 (현재) | 비-GUI 핵심 모듈 |
|-------|------|-------------------|------------------|
| Domain | ≥ 95% | ~90% | `user.py`·`solve_partial` 제외 시 ~94% |
| Boundary | ≥ 85% | ~35% (gui 0%) | validator/gateway/ui ~97% |
| 전역 | ≥ 80% | ~50% (gui drag-down) | GUI pytest 후속 과제 |

**Boundary NFR-02:** `--cov=src/boundary`는 `gui/` 포함. 핵심 계약 모듈만 게이트할 때는 `boundary_validator`, `puzzle_gateway`, `ui_boundary`, `failure_result` term-missing을 별도 확인.

---

## 9. QA Step 0 명령 (보정 반영)

```powershell
# 기준선
python -m pytest -q
python -m pytest tests/test_golden_master_magic_square.py -q
python -m pytest -m golden_master -q

# Step 1 — §8 명령
```

---

## 10. 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 1.0 | 2026-05-29 | REFACTOR 후 QA 프롬프트·test_plan·README 불일치 보정 SSOT 초안 |
