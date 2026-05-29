# MagicSquare_05

4×4 마방진(Magic Square) 프로그램 프로젝트입니다.

이 저장소는 **구현 전 문제 인식 단계**를 거친 결과를 담고 있습니다.  
마방진을 “만드는 것” 자체가 목적이 아니라, **조건을 먼저 정의하고 구현을 나중에 결정하는 사고 방식**을 훈련하는 것이 이 프로젝트의 핵심 목적입니다.

---

## 프로젝트 개요

1부터 16까지의 서로 다른 정수를 4×4 격자에 배치할 때, **모든 행·열·대각선의 합이 34**가 되는 배치를 찾고 검증하는 문제입니다.

| 항목 | 내용 |
|------|------|
| 격자 크기 | 4×4 |
| 사용 숫자 | 1 ~ 16 (중복 없음) |
| 마법 상수 | 34 (= n(n²+1)/2, n=4) |
| 본질적으로 다른 해 | 880가지 |
| 탐색 공간 | 16! ≈ 2×10¹³ |

겉으로는 “숫자를 채운다”는 문제처럼 보이지만, 실제로는 **방대한 탐색 공간에서 다중 제약 조건을 동시에 만족하는 상태를 찾고 표현하는 문제**입니다.

---

## 현재 진행 단계

| 단계 | 상태 | 설명 |
|------|------|------|
| STEP 1 — Observation | ✅ 완료 | 상황 관찰 및 맥락 정리 |
| STEP 2 — Why (완성) | ✅ 완료 | “완성해야 하는가”에 대한 가정 분석 |
| STEP 3 — Why (프로그램) | ✅ 완료 | 프로그램 구현의 필요성 분석 |
| STEP 4 — Why (TDD) | ✅ 완료 | TDD 설계 접근의 필요성 분석 |
| STEP 5 — 문제 정의 | ✅ 완료 | 표면/개선 정의, Invariant, 훈련 목표 |
| 설계 (What) | ⏳ 대기 | 생성기 / 검증기 / 표현기 역할 정의 |
| 구현 (How) | ⏳ 대기 | TDD 기반 구현 |

---

## 문제 정의 요약

### 표면 정의 (피해야 할 정의)

> “1부터 16까지의 숫자를 4×4 격자에 배치하여, 모든 행·열·대각선의 합이 34가 되도록 마방진을 완성하는 프로그램을 만든다.”

- **Why**가 없고 **What**만 있다
- “완성”의 기준이 모호하다 (하나의 해? 모든 해?)
- 탐색·검증·선택·표현이 한 문장에 압축되어 있다

### 개선된 정의

**상황:** 1~16을 4×4 격자에 배치할 때, 수학적으로 균형 잡힌 배치가 존재하는가를 **판별하고 표현**하는 문제.

**목적:**

- 복수의 불변 조건을 동시에 만족하는 상태를 찾는다
- 찾은 상태를 명확한 형식으로 표현하고 검증한다
- 이 과정을 재현 가능하고 신뢰할 수 있게 설계한다

**완성의 정의 (독립적으로 검증 가능):**

| 구분 | 내용 |
|------|------|
| 최소 완성 | 유효한 배치 1개 이상을 확인하고 표현 |
| 확장 완성 | 조건을 만족하는 모든 배치를 열거하고 개수 확인 |
| 검증 완성 | 임의의 배치가 조건을 만족하는지 판별 |

**하위 문제 분해:**

```
마방진 프로그램
├── 탐색   — 유효한 배치를 찾는다
├── 검증   — 조건 충족 여부를 판별한다
├── 선택   — 여러 해 중 무엇을 다룰지 결정한다
└── 표현   — 결과를 명확한 형식으로 출력한다
```

---

## 핵심 Invariant (불변 조건)

어떤 상태에서도 반드시 참이어야 하며, **하나라도 위반되면 무효**입니다.

### 수학적 Invariant

| ID | 조건 |
|----|------|
| INV-M1 | 사용된 정수의 집합 = {1, 2, …, 16} |
| INV-M2 | 모든 정수는 정확히 한 번만 사용 |
| INV-M3 | 4개 행 각각의 합 = 34 |
| INV-M4 | 4개 열 각각의 합 = 34 |
| INV-M5 | 주대각선의 합 = 34 |
| INV-M6 | 반대각선의 합 = 34 |

### 구조적 Invariant

| ID | 조건 |
|----|------|
| INV-S1 | 격자는 정확히 4행 4열 |
| INV-S2 | 모든 칸이 채워져 있음 |
| INV-S3 | 기준 합 = n(n²+1)/2 = 34 (n=4) |

```
INV-M1 + INV-M2  →  배치의 유효성 (누가 들어왔는가)
INV-M3 ~ INV-M6  →  균형의 유효성 (어떻게 배치되었는가)
INV-S1 + INV-S2  →  형태의 유효성 (구조가 온전한가)
```

---

## 설계 원칙

### Why → What → How

```
Why  : 제약 조건을 만족하는 상태를 재현 가능하게 찾고 검증한다
What : 생성기, 검증기, 표현기의 세 역할
How  : (다음 단계)
```

### 프로그램으로 구현하는 이유

| 관점 | 핵심 |
|------|------|
| 반복 가능성 | 16! 탐색을 사람이 반복할 수 없음 — 해결 가능성의 조건 |
| 검증 자동화 | 탐색과 검증을 독립적 관심사로 분리 |
| 오류 방지 | 오류를 발견하는 것이 아니라 발생 불가능한 구조로 설계 |
| 규칙 기반 사고 | 직관을 형식으로 번역하는 훈련 |

### TDD 접근

- **통제 대상:** 범위, 중복, 합, 격자 완전성을 계층별로 통제
- **불변 조건 우선:** 구현 전에 INV-M1~M6, INV-S1~S3를 테스트로 명시
- **입출력 명확성:** 인터페이스가 구현보다 먼저 확정되도록 유도

---

## 훈련 목표 (사고 능력)

1. **조건의 형식화** — “균형 잡혀 있다”를 수치 조건으로 번역
2. **문제 분해** — 탐색 / 검증 / 선택 / 표현으로 분리
3. **불변 조건 우선 사고** — 구현 전에 “무엇이 항상 참인가”를 먼저 정의
4. **Why → What → How 순서** — How가 Why를 결정하지 않도록 유지
5. **경계 인식** — 입력·출력·책임·확장 경계를 명확히 구분

---

## 프로젝트 구조

```
MagicSquare_05/
├── README.md                                          # 이 파일
├── Prompt/
│   └── 01_MagicSquare_problem_definition_prompt.md    # 문제 인식 대화 프롬프트 기록
└── Report/
    └── 01_MagicSquare_problem_definition_report.md    # 문제 인식 전체 보고서
```

상세한 관찰·Why 분석·문제 정의는 [Report/01_MagicSquare_problem_definition_report.md](Report/01_MagicSquare_problem_definition_report.md)를 참고하세요.

---

## 경계 (이 프로젝트가 다루지 않는 것)

| 경계 | 내용 |
|------|------|
| 입력 | 1~16, 중복 없음, 4×4 |
| 출력 | 유효한 배치 표현 또는 유효/무효 판정 |
| 책임 | “어떤 배치가 유효한가” — “어떤 배치가 더 좋은가”는 범위 밖 |
| 확장 | n×n 일반화는 현재 범위 밖 |

---

## 다음 단계

1. **What 정의** — 생성기 / 검증기 / 표현기의 역할과 입출력 계약 확정
2. **테스트 설계** — Invariant(M1~M6, S1~S3)를 테스트 케이스로 변환
3. **How 구현** — TDD 사이클(Red → Green → Refactor)로 점진적 구현

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 test_plan.md 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트
- [x] TC-A-01: grid=None 입력 → 실패 결과 반환 (Happy Path of Failure)
- [x] TC-A-02: code가 정확히 "INVALID_SIZE" 문자열인지 검증
- [x] TC-A-03: message가 "Grid must be 4x4." 와 문자 단위 동일한지 검증
- [x] TC-A-04: grid=None 시 Domain 진입점 0회 호출 (mock/spy 검증)
- [x] TC-A-05: grid=[] 빈 리스트 → 실패 결과 반환
- [x] TC-A-06: grid=3×4 크기 불일치 → 실패 결과 반환
- [x] TC-A-07: 반환 객체 타입이 지정 실패 결과 구조체인지 검증

### Track B — Domain / Logic 테스트
- [ ] TC-B-01: resolve()가 None grid를 직접 받지 않음을 격리 검증
- [ ] TC-B-02: Boundary가 None 분기를 처리 후 resolve() 미호출 확인
- [ ] TC-B-03: resolve() mock이 호출됐을 경우 테스트 실패 처리
- [ ] TC-B-04: AC-FR-01-02~05 범위의 케이스는 이 커밋에 포함하지 않음 확인

### 커버리지 목표
- [ ] Domain Logic: 95%+ (pip install pytest-cov)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결
- [x] defect_list.md 생성 및 발견 결함 기록
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## Golden Master 회귀 안전장치

> Refactoring 시작 전 구축. GREEN 완료 후 즉시 적용.

### 기준 파일 생성

- [x] GM-01: `golden_master_expected.txt` 생성
- [x] GM-02: 정상/역순/오류 시나리오 추가
- [x] GM-03: `git add tests/golden_master_expected.txt`

### 테스트 코드

- [x] GM-04: `test_golden_master_magic_square` 작성
- [x] GM-05: approve 패턴 적용
- [x] GM-06: Golden Master 테스트 PASS 확인

**검증:** `python -m pytest -m golden_master -v`

### 회귀 보호

- [x] GM-07: row-major 규칙 보호
- [x] GM-08: 1-index 출력 보호
- [x] GM-09: reverse 조합 fallback 보호
- [x] GM-10: Error Contract 보호

**관련 파일:** `tests/golden_master_expected.txt`, `tests/test_golden_master_magic_square.py`, `tests/golden_master/`, `scripts/generate_golden_master.py`, `docs/golden_master_approval_design.md`

---

## GREEN 단계 To-Do 리스트

> RED 커밋 묶음(R1~R6)에 대응하는 GREEN(최소 구현) 체크리스트입니다.  
> 각 묶음을 GREEN 처리한 뒤 해당 범위 pytest를 실행하고, 통과 시 체크합니다.  
> 정렬 기준: Report/09 검증 파이프라인 순서 — 차원 → blank → range → duplicate → 출력 → 오케스트레이션.

### GREEN-0 — U-IN-01 (`grid=None`) · 대응 RED: **R2** (AC-FR-01-01 차원, 1/2)

`BoundaryValidator.validate` — `None` 입력 시 `FailureResult(INVALID_SIZE)` 반환.

- [x] `test_grid_none_returns_failure_not_exception`
- [x] `test_grid_none_returns_invalid_size_code`
- [x] `test_grid_none_returns_grid_must_be_4x4_message`
- [x] `test_grid_none_returns_pydantic_failure_result_type`
- [x] `test_grid_none_repeat_call_returns_same_failure_contract`
- [x] `test_grid_none_code_equals_invalid_size_literal`
- [x] `test_grid_none_message_equals_prd_section_8_1_literal`
- [x] `test_none_grid_returns_failure_with_invalid_size_code`

**검증:** `python -m pytest tests/boundary/test_boundary_validator_dimension.py::TestNormalFailureReturn -q`

---

### GREEN-1 — U-IN-02 (4×4 차원) · 대응 RED: **R2** (AC-FR-01-01 차원, 2/2)

`BoundaryValidator.validate` — 행·열 개수 4×4 검사 (`[]`, `[[]]*4`, `3×4` 등).

- [x] `test_grid_empty_list_returns_invalid_size_failure`
- [x] `test_grid_four_empty_rows_returns_invalid_size_failure`
- [x] `test_grid_3x4_returns_invalid_size_failure`
- [x] `test_grid_empty_list_code_is_invalid_size_literal`
- [x] `test_grid_3x4_message_is_grid_must_be_4x4_literal`
- [x] `test_grid_empty_list_message_character_identity`
- [x] `test_grid_four_empty_rows_code_character_identity`
- [x] `test_grid_3x4_code_and_message_character_identity`

**구현 대상:** `src/boundary/boundary_validator.py` ✅

**검증:** `python -m pytest tests/boundary/test_boundary_validator_dimension.py -q` — 16건 통과 (GREEN-0 + GREEN-1)

**대표 node id:** `tests/boundary/test_boundary_validator_dimension.py::TestBoundaryValueCases::test_grid_empty_list_returns_invalid_size_failure`

**연동 (선택, 동일 커밋):** `tests/control/test_solve_orchestration_dimension.py` 5건 — invalid 차원 시 `resolve`/`execute` 0회 ✅

- [x] `test_grid_none_resolve_call_count_zero`
- [x] `test_grid_empty_list_resolve_never_called`
- [x] `test_grid_four_empty_rows_resolve_assert_not_called`
- [x] `test_grid_3x4_resolve_mock_call_count_is_zero`
- [x] `test_grid_none_resolve_called_fails_via_mock_guard`

---

### GREEN-2 — U-IN-03 (blank count) · 대응 RED: **R3**

blank 개수 ≠ 2 → **E002** (`FailureResult`, 예외 throw 금지).

- [x] `test_u_in_03a_zero_blanks_returns_e002` — 0개 blank
- [x] `test_u_in_03b_three_blanks_returns_e002` — 3개 blank

**구현 대상:** `src/boundary/boundary_validator.py` (차원 통과 후 blank 검사) ✅

**fixture:** `grid_g0_complete`, `grid_three_blanks` (`tests/conftest.py`)

**검증:** `python -m pytest tests/boundary/test_u_in_blank_count.py -q` — 2건 통과

**대표 node id:** `tests/boundary/test_u_in_blank_count.py::TestBlankCountValidation::test_u_in_03a_zero_blanks_returns_e002`

---

### GREEN-3 — U-IN-04 (value range) · 대응 RED: **R4** (1/2)

범위 위반 → **E004** (`-1`, `17`).

- [x] `test_u_in_04a_below_range_returns_e004`
- [x] `test_u_in_04b_above_range_returns_e004`

**구현 대상:** `src/boundary/boundary_validator.py` (blank 통과 후 range 검사) ✅

**검증:** `python -m pytest tests/boundary/test_u_in_range.py -q` — 2건 통과

**대표 node id:** `tests/boundary/test_u_in_range.py::TestValueRangeValidation::test_u_in_04a_below_range_returns_e004`

---

### GREEN-4 — U-IN-05 (duplicate) · 대응 RED: **R4** (2/2)

non-zero 중복 → **E005**.

- [x] `test_u_in_05_nonzero_duplicate_returns_e005`

**구현 대상:** `src/boundary/boundary_validator.py` (range 통과 후 duplicate 검사) ✅

**검증:** `python -m pytest tests/boundary/test_u_in_duplicate.py -q` — 1건 통과

**대표 node id:** `tests/boundary/test_u_in_duplicate.py::TestDuplicateValueValidation::test_u_in_05_nonzero_duplicate_returns_e005`

**short-circuit 순서 확인:** 차원(INVALID_SIZE) → blank(E002) → range(E004) → duplicate(E005) ✅

---

### GREEN-5 — U-OUT (성공 출력) · 대응 RED: **R5** (1/2)

유효 G1 입력 → `int[6]`, 1-index 좌표.

- [x] `test_u_out_01_valid_g1_returns_int6_length`
- [x] `test_u_out_02_valid_g1_coordinates_one_indexed` — 기대 `[2,2,7,3,3,10]`

**fixture:** `grid_g1_two_blanks` (`tests/conftest.py`)  
**구현 대상:** `src/control/magic_square_control.py`, `src/control/two_cell_solver.py`, `src/entity/*` ✅

**검증:** `python -m pytest tests/boundary/test_u_out_contract.py -q` — 2건 통과

**대표 node id:** `tests/boundary/test_u_out_contract.py::TestSuccessOutputContract::test_u_out_02_valid_g1_coordinates_one_indexed`

---

### GREEN-6 — U-FLOW-02 (execute 격리) · 대응 RED: **R5** / **R6**

invalid 입력 시 `SolvePartialMagicSquare.execute` **call_count == 0**.

- [x] `test_u_flow_02_duplicate_value_execute_call_count_zero`
- [x] `test_u_flow_02_invalid_blank_count_execute_call_count_zero`
- [x] `test_u_flow_02_invalid_size_execute_call_count_zero`
- [x] `test_u_flow_02_null_matrix_execute_call_count_zero`
- [x] `test_u_flow_02_out_of_range_execute_call_count_zero`

**구현 대상:** `src/control/magic_square_control.py` + `src/entity/solve_partial_magic_square.py` ✅

**검증:** `python -m pytest tests/control/test_u_flow_execute_isolation.py -q` — 5건 통과

**대표 node id:** `tests/control/test_u_flow_execute_isolation.py::TestExecuteIsolationExtended::test_u_flow_02_null_matrix_execute_call_count_zero`

---

### GREEN 메타 — 대응 RED: **R1** (스코프 가드, 구현 불필요)

AC-FR-01-01 SUT 범위 제한 테스트 — RED 커밋 시 이미 GREEN 유지.

- [x] `test_scope_boundary_suite_excludes_blank_count_error_token`
- [x] `test_scope_boundary_suite_excludes_duplicate_value_token`
- [x] `test_scope_boundary_suite_excludes_out_of_range_token`
- [x] `test_scope_boundary_suite_excludes_fr02_to_fr05_domain_components`
- [x] `test_scope_no_four_by_four_valid_success_test_in_boundary_suite`

**검증:** `python -m pytest tests/boundary/test_ac_fr_01_01_scope.py -q`

---

### GREEN 완료 기준 (Boundary Track)

- [x] `python -m pytest tests/boundary/ -q` — 28건 전부 통과
- [x] `python -m pytest tests/control/test_solve_orchestration_dimension.py tests/control/test_u_flow_execute_isolation.py -q` — orchestration 10건 통과
- [ ] Boundary Layer 커버리지 85%+ (`python -m pytest tests/boundary/ --cov=src/boundary --cov-report=term-missing`)

### RED ↔ GREEN 매핑 요약

| RED 묶음 | GREEN 묶음 | Test ID | 상태 |
|----------|------------|---------|------|
| R1 | GREEN 메타 | scope guard 5건 | ✅ |
| R2 | GREEN-0, GREEN-1 | U-IN-01, U-IN-02 | ✅ 16/16 (orchestration 5건 선택) |
| R3 | GREEN-2 | U-IN-03a/b | ✅ 2/2 |
| R4 | GREEN-3, GREEN-4 | U-IN-04, U-IN-05 | ✅ 3/3 |
| R5 | GREEN-5, GREEN-6 | U-OUT, U-FLOW | ✅ 7/7 |
| R6 | (Domain Track) | D-LOC~D-SOL | ⏳ 별 트랙 |

---

## Refactoring CheckList

> Track A GREEN·Golden Master 구축 완료 후 진행.  
> **원칙:** `.cursor/rules/magicsquare-tdd-testing.mdc` — GREEN 통과 → 구조 변경 → 전체 회귀 PASS → 커버리지 유지.  
> **ECB 허용 의존:** `boundary → control`, `control → entity` / **금지:** `control → boundary`, `entity → boundary|control`, Screen→Control 직접 호출.  
> **실행 순서:** **A → B → C** (이전 P0/P1/P2를 3개 유형 그룹으로 통합)

### 유형 그룹 요약

| 그룹 | 유형 | 목적 | 실행 시점 |
|------|------|------|-----------|
| **A** | 기반·계약 고정 | Domain·테스트·에러 envelope 고정 — 리팩터 안전망 | 구조 변경 **전** (구 P0 선행) |
| **B** | ECB·책임 분리 | `boundary → control → entity` 정렬, SRP·솔버 SSOT | A GREEN 후 (구 P0~P1 핵심) |
| **C** | 일관성·정리 | 상수 SSOT, 명명, dead code·fixture 정리 | 전체 PASS 후 (구 P1~P2) |

상세 분석: [Report/15_MagicSquare_refactoring_plan_report.md](Report/15_MagicSquare_refactoring_plan_report.md)

### ECB 실제 파일 매핑 (프롬프트 ↔ 저장소)

| 프롬프트 (목표) | 현재 `src/` 파일 | 비고 |
|-----------------|------------------|------|
| `control/solve_partial_magic_square.py` | `entity/two_cell_solver.py`, `entity/solve_partial_magic_square.py`, `control/magic_square_control.py` | `solution()` SSOT in entity |
| `boundary/ui_boundary.py` | `boundary/ui_boundary.py`, `boundary/puzzle_gateway.py` | E006 unsolvable envelope |
| `boundary/screen/main_window.py` | `boundary/gui/main_window.py`, `boundary/gui/grid_panel.py` | `gui/` rename deferred (change budget) |

---

### 그룹 A — 기반·계약 고정

> 구조 변경 **전** 반드시 GREEN. `pytest.ini`의 `--continue-on-collection-errors`로 entity import 오류가 조용히 스킵될 수 있음 — 전체 스위트 실행 권장.

#### A-1 — Entity Track B 테스트 GREEN

- [x] `test_d_loc_blank_coords.py` — import `blank_locator.find_blank_coords` 수정 + GREEN
- [x] `test_d_mis_missing_numbers.py` — import `find_missing_numbers` 수정 + GREEN
- [x] `test_d_val_magic_square.py` — `is_magic_square` 6건 GREEN (구현은 존재)
- [x] `test_d_sol_solution.py` — D-SOL-01~04 GREEN (Step A/B, unsolvable, int[6])
- [x] Golden Master GM-TC-02/05 baseline 재승인 (Track B GREEN 후)

**검증:**

```powershell
python -m pytest tests/entity/test_d_loc_blank_coords.py tests/entity/test_d_mis_missing_numbers.py tests/entity/test_d_val_magic_square.py tests/entity/test_d_sol_solution.py -q
python -m pytest -m golden_master -v
```

#### A-2 — Domain·Boundary 계약 (FR-05, envelope)

- [x] Entity: `blank_locator`, `missing_number_finder`, `is_magic_square`, 순수 assignment
- [x] unsolvable → `UnsolvableDomainError` / `E006` (`PuzzleGateway`)
- [x] `boundary_validator.py` — non-int·non-list·jagged row → `FailureResult` (TypeError 금지)
- [x] 신규 테스트: `tests/boundary/test_boundary_validator_type_safety.py`
- [x] `FailureResult` vs `FailureResponse` envelope 단일화 (`InputValidator` delegate)

**대상:** `entity/solve_partial_magic_square.py`, `src/boundary/boundary_validator.py`

---

### 그룹 B — ECB·책임 분리

> 그룹 A GREEN 후 진행. invalid 입력 시 Domain `resolve`/`execute` 0회 유지.

#### B-1 — Control ↔ Boundary 역전 해소

- [x] `MagicSquareControl` — `BoundaryValidator` 제거 (`resolve` only)
- [x] `PuzzleGateway` — E001~E005 검증 후 valid grid만 Control에 전달

**대상:** `src/control/magic_square_control.py`  
**검증:** `python -m pytest tests/control/test_u_flow_execute_isolation.py tests/control/test_solve_orchestration_dimension.py tests/boundary/ -q`

#### B-2 — 솔버 단일 SSOT (진입점·오케스트레이션)

- [x] Control/Entity: `entity/two_cell_solver.solution` 단일 진입점
- [x] `SolvePartialMagicSquare.execute` → `solution()` 위임

**대상:** `entity/solve_partial_magic_square.py`, `control/two_cell_solver.py`

#### B-3 — `ui_boundary` 신규 + Screen 책임 축소

- [x] `ui_boundary` — Screen↔`PuzzleGateway` 중재, E006 envelope
- [x] 신규 테스트: `tests/boundary/test_ui_boundary.py`
- [x] `main_window` — `UiBoundary.solve_puzzle`만 호출
- [x] `grid_panel.apply_solution` — `_placements_from_solution` / `_apply_placements` 분리
- [ ] 신규 테스트: `tests/boundary/gui/test_grid_panel.py` (후속 — PyQt 단위 테스트)

**대상:** `boundary/gui/main_window.py`, `boundary/gui/grid_panel.py` (신규 `boundary/ui_boundary.py`)

---

### 그룹 C — 일관성·정리

> 그룹 B 완료·전체 회귀 PASS 후. 관찰 계약(테스트·GM·E001~E005) 불변 유지.

#### C-1 — Boundary·테스트 데이터 정리

- [x] `input_validator.py` — `BoundaryValidator` thin delegate
- [x] `SAMPLE_G1_GRID` → `boundary/demo_data.py`

#### C-2 — SSOT·명명

- [x] `entity/constants.py` SSOT — `boundary_validator`, `grid_panel`, `random_puzzle`
- [ ] `gui/` → `screen/`, `entity/solve_partial` → `control/solve_partial` rename — **보류** (폴더 rename change budget)

---

### REFACTOR 완료 기준

- [x] `python -m pytest tests/ -v` — 전체 PASS (72건, 수집 오류 0건)
- [x] `python -m pytest -m golden_master -v` — GM-TC-00~05 PASS (baseline Track B 재승인)
- [ ] `python -m pytest tests/ --cov=src` — 전체 80%+ (현재 ~50%, GUI 미테스트) / boundary 핵심 모듈 85%+ ✅
- [x] import 검사 — `control`→`boundary` 없음; `main_window`→`control`/`entity` 직접 import 없음
- [x] 그룹 A·B·C 핵심 항목 완료 (rename·grid_panel pytest 후속)
- [ ] GUI smoke — `python main.py` 수동 확인 (로컬)

### REFACTOR 회귀 검증 명령어 (요약)

```powershell
cd c:\DEV\MagicSquare_05
python -m pytest tests/boundary/ -q
python -m pytest tests/control/test_u_flow_execute_isolation.py tests/control/test_solve_orchestration_dimension.py -q
python -m pytest tests/entity/ -q
python -m pytest -m golden_master -v
python -m pytest tests/ -v
python -m pytest tests/ --cov=src --cov-report=term-missing
```

---

## 참고

- 4×4 마방진의 본질적으로 다른 해: **880가지**
- 마법 상수 공식: `n(n²+1)/2` (n=4일 때 **34**)
- 역사적 맥락: 뒤러 《멜랑콜리아》(1514)에 등장한 4×4 마방진
