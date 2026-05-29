# MagicSquare FR-01~FR-05 Dual-Track RED 설계 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 요청을 수행한다.
- 본 대화 세션에서 수행한 **전체 FR-01~FR-05 Dual-Track RED 설계표** 작업을 정리한다.
- 후속 RED 테스트 코드 작성·GREEN 구현의 **SSOT 설계 기준**으로 사용한다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **TDD 단계** | RED — 설계표만 작성 (구현·테스트 코드·pytest 실행·파일 저장 금지) |
| **방법론** | Dual-Track UI + Logic TDD, ECB 계층 분리 |
| **SSOT** | `docs/PRD_MagicSquare.md` v0.2, `Report/02_MagicSquare_4x4_TDD_design_report.md`, `.cursor/rules/*.mdc` |
| **프로젝트 계약** | E003/E001/E002/E004/E005 Failure envelope, `int[6]` 1-index 출력, M=34, short-circuit 검증, invalid 시 `SolvePartialMagicSquare.execute` 0회 |

> **참고:** 요청 문서명 `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md`는 저장소 실제 파일 `Report/02_MagicSquare_4x4_TDD_design_report.md`에 대응한다. **부록 G0~G3 격자는 Report/02에 미등재**하여 설계표에 placeholder 격자를 명시했다.

## 3. 수행 내용 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | SSOT(PRD·Report/02·규칙) 참조·격차 확인 | G0~G3 부록 부재 → placeholder 정책 |
| 2 | Track A — Boundary/UI Contract RED 설계표 | U-IN-01~05, U-OUT-01~02, U-FLOW-02 (9행) |
| 3 | Track B — Domain/Logic RED 설계표 | D-LOC-01, D-MIS-01, D-VAL-01~06, D-SOL-01~04 (13행) |
| 4 | RED 설계 자체 검수 체크리스트 | 6항목 전부 충족 |
| 5 | 본 보고서·transcript | `Report/09_...`, `Prompt/09_...` |

**본 세션에서 생성하지 않은 것:** pytest 테스트 파일, `src/` 구현, 스켈레톤, GREEN/REFACTOR 진입.

## 4. Track A — Boundary / UI Contract RED (요약)

### 4.1 입력 검증 (U-IN-*) — Domain 0회 전제

| Test ID | 트리거 | 기대 code | AC-FR |
|---------|--------|-----------|-------|
| U-IN-01 | `matrix=null` | E003 | null 선행 거부 |
| U-IN-02 | size ≠ 4×4 (3×4, 4×3, 5×5, `[]`) | E001 | AC-FR01-01 |
| U-IN-03a/b | `0` 개수 0 / 3 | E002 | AC-FR01-02 |
| U-IN-04a/b | `-1`, `17` | E004 | AC-FR01-03 |
| U-IN-05 | non-zero 중복 | E005 | AC-FR01-04 |

- **When:** `InputValidator.validate(matrix)` (호출 대상만 명시, 코드 없음)
- **Then:** Failure envelope 반환, Python 예외 throw 금지
- **Expected RED:** `ModuleNotFoundError`, `AttributeError`, `AssertionError`

### 4.2 출력 계약 (U-OUT-*)

| Test ID | 검증 내용 | AC-FR |
|---------|-----------|-------|
| U-OUT-01 | 성공 시 배열 길이 6 | AC-FR05-03 |
| U-OUT-02 | r,c ∈ [1,4], G1 기대 `[2,2,7,3,3,10]` | AC-FR05-04 |

- **When:** `UIBoundary.solve(matrix)` (유효 G1_placeholder)

### 4.3 흐름 격리 (U-FLOW-*)

| Test ID | 검증 내용 | AC-FR |
|---------|-----------|-------|
| U-FLOW-02 | invalid 입력 시 `SolvePartialMagicSquare.execute` **call_count == 0** | AC-FR01-05 |

- **When:** `UIBoundary.solve` + execute mock/spy

## 5. Track B — Domain / Logic RED (요약)

### 5.1 별칭 ↔ 책임 (구현명 확정 금지)

| 설계 별칭 | 책임 후보 | Test ID |
|-----------|-----------|---------|
| `find_blank_coords()` | EmptyCellLocator | D-LOC-01 |
| `find_not_exist_nums()` | MissingNumberFinder | D-MIS-01 |
| `is_magic_square()` | MagicSquareValidator | D-VAL-01~06 |
| `solution()` | TwoCellSolver / Use Case | D-SOL-01~04 |

### 5.2 Logic Invariant (I1~I11) 매핑

| ID | 내용 | 대표 Test ID |
|----|------|--------------|
| I1 | 행 합 = M(34) | D-VAL-02 |
| I2 | 열 합 = M | D-VAL-03 |
| I3 | 대각 합 = M | D-VAL-04 |
| I4 | 완성 격자 {1..16}, 0·중복·범위 위반 시 false | D-VAL-05, D-VAL-06 |
| I5 | MagicConstant SSOT = 34 | D-VAL-01 |
| I6 | 빈칸 2개, row-major | D-LOC-01 |
| I7 | 누락 숫자 2개 | D-MIS-01 |
| I8 | Step A (small→first, large→second) | D-SOL-01, D-SOL-04 |
| I9 | Step B (reverse) | D-SOL-02 |
| I10 | 양쪽 실패 → `UnsolvableDomainError` | D-SOL-03 |
| I11 | 누락 숫자 오름차순 | D-MIS-01 |

### 5.3 Domain Mock 금지

- Logic Track 단위 테스트에서 Domain 동료 함수 mock/patch **금지**
- U-FLOW-02의 `execute` spy는 Boundary 격리 전용 **예외**

## 6. 대표 테스트 데이터 (placeholder)

### 6.1 G0_placeholder (완전 마방진, D-VAL-01)

```
[[16, 3, 2, 13],
 [ 5, 10, 11, 8],
 [ 9, 6, 7, 12],
 [ 4, 15, 14, 1]]
```

### 6.2 G1_placeholder (D-LOC-01, D-MIS-01, D-SOL-01, U-OUT)

- 빈칸 **0-index** `(1,1)`, `(2,2)` → **1-index** `(2,2)`, `(3,3)`
- 누락 `{7, 10}`
- Step A 성공: `[2, 2, 7, 3, 3, 10]`

```
[[16, 2, 3, 13],
 [ 5, 0, 11, 8],
 [ 9, 6, 0, 12],
 [ 4, 14, 15, 1]]
```

### 6.3 G2_placeholder / G3_placeholder

| 격자 | 용도 | 상태 |
|------|------|------|
| G2 | Step A 실패 · Step B 성공 (D-SOL-02) | Report/02 부록 없음 — GREEN 전 산술 확정 필요 |
| G3 | Step A·B 모두 실패 → `UnsolvableDomainError` (D-SOL-03) | 동일 |

## 7. 명명·계약 정합 이슈 (GREEN 전 결정)

| 구분 | RED 설계 (요청 계약) | PRD §12·§13 |
|------|----------------------|-------------|
| 오류 코드 | E003, E001~E005 | `ERR_INVALID_DIMENSION`, `ERR_INVALID_BLANK_COUNT`, … |
| null | E003 전용 | 차원 오류와 통합 여부 미정 |
| 메시지 | 설계표에 exact 문자열 고정 | PRD Message 열과 대부분 일치 |

**권장:** GREEN 시 `FailureResult`에 E00x ↔ `ERR_*` 매핑 테이블 단일 SSOT화.

## 8. RED 설계 자체 검수 결과

| # | 항목 | 결과 |
|---|------|------|
| 1 | Boundary E00x Failure schema (generic Exception 아님) | ✅ |
| 2 | invalid → execute 0회 (U-FLOW-02) | ✅ |
| 3 | U-IN vs U-OUT 분리 | ✅ |
| 4 | Logic Track Domain Mock 없음 | ✅ |
| 5 | I1~I11·AC-FR* 추적 가능 | ✅ |
| 6 | 코드/스켈레톤/구현 미작성 | ✅ |

## 9. 후속 작업 권장 순서

1. **G2/G3 격자 확정** — Report/02 부록 보강 또는 `tests/conftest.py` fixture로 SSOT 고정
2. **E00x ↔ ERR_* 매핑** 결정 후 Track A RED pytest 작성 (`tests/boundary/`, `tests/control/`)
3. **Track B RED pytest** — `tests/entity/`, `tests/control/` (ECB 의존 방향 준수)
4. **AC-FR-01-01 기존 스위트**와 범위 통합·중복 제거 (`test_ac_fr_01_01_scope.py` 가드 유지 여부 검토)
5. **GREEN** — DEF-001/002(`src/boundary`, `src/control`) 해소 후 설계표 Then 기준 통과

## 10. 관련 문서

| 문서 | 역할 |
|------|------|
| `docs/PRD_MagicSquare.md` | FR-01~05, AC, NFR, 오류 정책 |
| `docs/test_plan.md` | AC-FR01-01 앵커 테스트 계획 (Track A 부분 범위) |
| `Report/08_MagicSquare_ac_fr_01_01_red_test_and_defect_report.md` | 선행 AC-FR-01-01 RED pytest·결함 |
| `defect_list.md` | DEF-001~006 (boundary/control 미구현) |
| `Prompt/09_MagicSquare_dual_track_fr01_fr05_red_design_prompt_transcript.md` | 본 세션 대화 transcript |

## 11. 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | Dual-Track FR-01~FR-05 RED 설계표 세션 보고서 최초 작성 |
