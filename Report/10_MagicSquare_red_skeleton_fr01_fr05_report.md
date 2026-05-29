# MagicSquare FR-01~FR-05 RED Skeleton 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 요청을 수행한다.
- 본 세션에서 수행한 **RED (Skeleton)** 단계 — Report/09 설계표 기반 pytest 스켈레톤 추가 — 를 정리한다.
- 후속 **RED (Full)** / **GREEN** 구현의 기준·범위 문서로 사용한다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **TDD 단계** | RED (Skeleton) — 구조·`pytest.fail()`만; 기대값 assert 금지 |
| **설계 SSOT** | `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` |
| **선행 작업** | Report/09 RED 설계표; Report/08 AC-FR-01-01 Full RED 25건 |
| **금지** | `src/` 구현, GREEN/REFACTOR, Report/08·`test_user.py` 수정 |

## 3. 세션 타임라인 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | FR-01~FR-05 Dual-Track **RED 설계표** (코드 없음) | 대화 산출 → `Report/09`, `Prompt/09` |
| 2 | Skeleton 프롬프트 **Report 경로 정합** (실행 없음) | 수정 프롬프트 텍스트 제공 |
| 3 | **RED Skeleton** pytest 22건 + fixture 주석 | `tests/boundary|entity|control/test_u_*`, `test_d_*` |
| 4 | `pytest` 실행 검증 | 2 failed, 11 passed, 10 errors |
| 5 | 본 보고서·transcript | `Report/10_...`, `Prompt/10_...` |

## 4. 프롬프트 정합 수정 (Report 경로)

요청 프롬프트의 가상 파일명을 저장소 실제명으로 교정한 뒤 Skeleton 작업에 사용했다.

| 요청(가상) | 저장소 실제 |
|------------|-------------|
| `Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md` | `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` |
| `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md` | `Report/02_MagicSquare_4x4_TDD_design_report.md` |
| `Report/08` + `test_ac_fr_01_01_*.py` 13건 | `Report/08_MagicSquare_ac_fr_01_01_red_test_and_defect_report.md` + dimension 15 + scope 5 + control 5 = **25건** |

설계표 Test ID 범위도 정정: `U-IN-04~08` / `U-OUT-01~03` → **`U-IN-03a/b~05`, `U-OUT-01~02`, `U-FLOW-02`**.

## 5. 생성·수정 파일

### 5.1 신규 (스켈레톤)

| 파일 | Test ID | 테스트 수 |
|------|---------|-----------|
| `tests/boundary/test_u_in_blank_count.py` | U-IN-03a, U-IN-03b | 2 |
| `tests/boundary/test_u_in_range.py` | U-IN-04a, U-IN-04b | 2 |
| `tests/boundary/test_u_in_duplicate.py` | U-IN-05 | 1 |
| `tests/boundary/test_u_out_contract.py` | U-OUT-01, U-OUT-02 | 2 |
| `tests/control/test_u_flow_execute_isolation.py` | U-FLOW-02 (5 spots) | 5 |
| `tests/entity/test_d_loc_blank_coords.py` | D-LOC-01 | 1 |
| `tests/entity/test_d_mis_missing_numbers.py` | D-MIS-01 | 1 |
| `tests/entity/test_d_val_magic_square.py` | D-VAL-01~06 | 6 |
| `tests/entity/test_d_sol_solution.py` | D-SOL-01~04 | 4 |
| `tests/entity/conftest.py` | G0~G3 placeholder 주석 | — |

**신규 스켈레톤 합계: 22 test functions**

### 5.2 수정 (주석만)

| 파일 | 변경 |
|------|------|
| `tests/conftest.py` | Report/09 §6 G0/G1 placeholder 주석 블록 추가 |

### 5.3 미수정 (금지 준수)

| 파일 | 비고 |
|------|------|
| `tests/boundary/test_boundary_validator_dimension.py` | 15건 Full RED assert 유지 |
| `tests/boundary/test_ac_fr_01_01_scope.py` | 5건 scope 가드 유지 |
| `tests/control/test_solve_orchestration_dimension.py` | 5건 Full RED 유지 |
| `tests/entity/test_user.py` | 6건 유지 |
| `src/` | **변경 없음** |

### 5.4 작성하지 않음 (중복 방지)

| Test ID | 사유 |
|---------|------|
| U-IN-01, U-IN-02 | Report/08 `test_boundary_validator_dimension.py` + `test_solve_orchestration_dimension.py`에 Full RED 존재 |

## 6. 스켈레톤 규칙 준수

| 규칙 | 준수 |
|------|------|
| 본문 `pytest.fail("RED: <Test ID> — ...")` 한 줄 | ✅ 22건 |
| Given/When/Then 주석만 | ✅ |
| 기대값 `assert` 없음 | ✅ |
| Domain Mock 금지 (Logic Track) | ✅ |
| U-FLOW-02 신규 `test_u_flow_*.py` (Report/08 control 파일 미수정) | ✅ |
| production import 허용 (Report/08 패턴 `src.*`) | ✅ |

## 7. pytest 실행 결과

### 7.1 명령

```powershell
cd C:\DEV\MagicSquare_05
.\.venv\Scripts\Activate.ps1
python -m pytest tests/boundary/ tests/entity/ tests/control/ -v
```

### 7.2 관측 (세션 종료 시점)

| 구분 | 결과 |
|------|------|
| **신규** `test_u_out_contract.py` | 2 **FAILED** (`pytest.fail`) |
| **신규** `test_u_in_*.py`, `test_u_flow_*.py` | **ERROR** collect — `No module named 'src.boundary'` / `src.control` |
| **신규** `test_d_*.py` | **ERROR** collect — `src.entity.*` / `src.control.two_cell_solver` 부재 |
| **Report/08** scope | 5 **passed** |
| **Report/08** dimension / orchestration | **ERROR** collect (기존과 동일, DEF-001/002) |
| `test_user.py` | 6 **passed** |
| **합계** | **2 failed, 11 passed, 10 errors** |

### 7.3 해석

- Skeleton 목표(**전부 RED**) 달성: 신규 22건은 `pytest.fail` FAIL 또는 collection ERROR.
- `src/boundary`, `src/control`, `src/entity` 도메인 모듈 부재로 import 기반 파일은 수집 단계 ERROR — Report/08과 동일 RED-1 패턴.
- `test_u_out_contract.py`만 import 없이 수집되어 **의도적 FAIL** 2건 확인.

## 8. Test ID ↔ Report/09 매핑

| Test ID | 모듈 | RED 유형 (현재) |
|---------|------|-----------------|
| U-IN-03a, U-IN-03b | `test_u_in_blank_count.py` | ERROR (import) |
| U-IN-04a, U-IN-04b | `test_u_in_range.py` | ERROR |
| U-IN-05 | `test_u_in_duplicate.py` | ERROR |
| U-OUT-01, U-OUT-02 | `test_u_out_contract.py` | FAIL (`pytest.fail`) |
| U-FLOW-02 ×5 | `test_u_flow_execute_isolation.py` | ERROR |
| D-LOC-01 | `test_d_loc_blank_coords.py` | ERROR |
| D-MIS-01 | `test_d_mis_missing_numbers.py` | ERROR |
| D-VAL-01~06 | `test_d_val_magic_square.py` | ERROR |
| D-SOL-01, 03, 04 | `test_d_sol_solution.py` | ERROR |
| D-SOL-02 | `test_d_sol_solution.py` | ERROR + fail 메시지 `G2 TBD` |

## 9. 결함·블로커 (기존 연동)

| ID | 상태 | Skeleton 관련 |
|----|------|----------------|
| DEF-001 | Open | `src.boundary` 없음 → U-IN/U-OUT(import) 수집 ERROR |
| DEF-002 | Open | `src.control` 없음 → U-FLOW, D-SOL 수집 ERROR |
| — | 신규 | `src.entity` magic-square 모듈 없음 → D-* 수집 ERROR |

## 10. 후속 작업 권장

1. **G2/G3 격자 확정** — `tests/entity/conftest.py` 주석 → fixture 활성화 (D-SOL-02/03).
2. **RED (Full)** — 스켈레톤의 `pytest.fail`을 Report/09 Then 기준 assert로 교체 (Report/08 25건은 유지).
3. **GREEN 최소 구현** — DEF-001/002 해소 후 E00x ↔ `ERR_*` 매핑; `BoundaryValidator`에 blank/range/duplicate 순서 구현.
4. **커버리지** — Boundary 85%+ (PRD NFR-01); `src/` 생성 후 `pytest --cov=src` 재실행.

## 11. 관련 문서

| 문서 | 역할 |
|------|------|
| `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` | RED 설계표 SSOT |
| `Report/08_MagicSquare_ac_fr_01_01_red_test_and_defect_report.md` | AC-FR-01-01 Full RED·수정 금지 |
| `defect_list.md` | DEF-001~006 |
| `Prompt/10_MagicSquare_red_skeleton_fr01_fr05_prompt_transcript.md` | 본 세션 transcript |

## 12. 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | RED Skeleton 22건 추가 및 pytest 결과 보고 |
