# MagicSquare REFACTOR 계획 Prompt Transcript

## Turn 01
### User
```text
/code-reviewer 를 이용해서 @c:\DEV\MagicSquare_05\ 코드 리뷰 진행
```

### Assistant
```text
code-reviewer 서브에이전트 전체 리뷰 수행.

종합: needs changes
- control→boundary ECB 위반 (MagicSquareControl)
- 솔버 Step A only, is_magic_square/Step B/unsolvable 미구현
- entity 테스트 import 오류 (empty_cell_locator, find_not_exist_nums)
- GM-TC-05 no_valid_solution baseline이 잘못된 성공 int[6] 고정

잘된 점: Boundary short-circuit, execute 격리 테스트, Golden Master 인프라
우선순위: ECB 해소 → Track B GREEN → import 수정 → 타입 안전 → InputValidator 정리
```

---

## Turn 02
### User
```text
리팩토링 대상 파일 test 매핑, RED 스켈레톤 GREEN 선행, REFACTOR phase 기준 답변
(domain.py / ui_boundary.py / screen/main_window.py)
```

### Assistant
```text
제시 경로 3건 모두 저장소에 없음.

실제 매핑:
- solve_partial → entity/solve_partial + control/two_cell_solver + magic_square_control
- ui_boundary → boundary_validator (입력 검증만) + main_window/grid_panel (GUI 연결)
- main_window → boundary/gui/main_window.py

RED→GREEN 선행: test_d_loc, test_d_mis, test_d_val, test_d_sol, GM-TC-02/05
GUI: RED 스켈레톤 없음 → 신규 테스트 RED→GREEN 필요

REFACTOR 한 줄: GREEN 이후에만 REFACTOR, 테스트 없이 구조 변경 시 회귀 검증 불가
```

---

## Turn 03
### User
```text
boundary_validator.py가 ui_boundary.py를 대체하는지?
```

### Assistant
```text
부분만 대체.

BoundaryValidator = 입력 계약 검증 (FR-01, E001~E005)
ui_boundary 역할 나머지 = main_window + grid_panel (PyQt I/O, control 호출, 실패/성공 표시)

InputValidator는 설계명 잔재, 실구현은 BoundaryValidator.
```

---

## Turn 04
### User
```text
ECB 매핑·스멜 점검·SRP·REFACTOR 계획 (표 형식)
```

### Assistant
```text
ECB 역할: magic_square_control 부적합(control→boundary), main_window 부적합(Screen→Control),
solve_partial Entity 부분(Step B 미완).

스멜 High: Step A only, control→boundary, 이중 솔버 진입, TypeError on bad input,
main_window int[6] 미검증.

SRP: MagicSquareControl 검증+조율, main_window UI+Gateway, execute locate+assign+int[6.

P0: Track B GREEN → ECB 검증 이동 → ui_boundary → Screen 분리
```

---

## Turn 05
### User
```text
리팩토링 계획서 작성 (표: 대상 목록, 테스트 선행, 회귀 검증)
```

### Assistant
```text
REFACTOR 계획서 작성:
- P0: entity GREEN, control boundary 분리, solver SSOT, validator 타입 안전
- P1: ui_boundary, main_window/grid_panel, input_validator 정리
- P2: constants SSOT, rename

회귀: pytest boundary/control/entity/golden_master/full/cov
```

---

## Turn 06
### User
```text
README.md REFACTOR To-Do 업데이트, workflow-automation 보고서 작성, GitHub push
```

### Assistant
```text
Ask mode로 차단 → Agent mode 전환 요청
```

---

## Turn 07
### User
```text
진행해줘
```

### Assistant
```text
Agent mode에서 실행:
1. README.md — REFACTOR 단계 To-Do 리스트 추가
2. Report/15_MagicSquare_refactoring_plan_report.md
3. Prompt/15_MagicSquare_refactoring_plan_prompt_transcript.md
4. git commit & push (refactor/refactor)
```

---

## 산출물 요약

| 파일 | 내용 |
|------|------|
| `README.md` | REFACTOR P0~P2 체크리스트, ECB 매핑, 회귀 명령어 |
| `Report/15_MagicSquare_refactoring_plan_report.md` | 통합 REFACTOR 계획 보고서 |
| `Prompt/15_MagicSquare_refactoring_plan_prompt_transcript.md` | 본 transcript |

## REFACTOR 1순위 (SSOT)

Track B GREEN → `MagicSquareControl`에서 Boundary 검증 분리 → `ui_boundary`/Screen 분리
