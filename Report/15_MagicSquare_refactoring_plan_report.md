# MagicSquare REFACTOR 계획 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 및 **GitHub 반영**을 수행한다.
- code-reviewer·ECB 매핑·코드 스멜·SRP 점검 결과를 **REFACTOR phase 실행 계획**으로 통합한다.
- `README.md` REFACTOR To-Do 섹션의 SSOT로 본 보고서를 둔다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **요청** | 리팩토링 계획 정리, README 반영, 보고서·GitHub |
| **선행 상태** | Track A GREEN, Golden Master GM-1~3, PyQt GUI (Report/12~14) |
| **브랜치** | `refactor/refactor` |
| **아키텍처** | ECB — `boundary → control → entity` |
| **TDD 규칙** | RED → GREEN → REFACTOR (`.cursor/rules/magicsquare-tdd-testing.mdc`) |

## 3. 세션 분석 요약

| 순서 | 분석 | 핵심 결과 |
|------|------|-----------|
| 1 | code-reviewer 전체 리뷰 | Track A 견고; control→boundary ECB 위반; Track B 미완; entity import 오류 |
| 2 | ECB 파일 매핑 | 프롬프트 3경로 미존재 → 실제 `src/` 대응표 작성 |
| 3 | 코드 스멜 (High/Medium) | Step A only, 이중 솔버 진입, GM-TC-05 baseline 불일치 |
| 4 | SRP 점검 | `MagicSquareControl` 검증+조율, `main_window` UI+Gateway 혼재 |
| 5 | REFACTOR 계획서 | P0/P1/P2 우선순위, 테스트 선행, 회귀 명령어 |

## 4. ECB 실제 매핑

| 프롬프트 (목표) | 현재 파일 | ECB 역할 | 적합 |
|-----------------|-----------|----------|------|
| domain.py | `entity/solve_partial_magic_square.py` | Entity (Domain Service) | 부분 |
| domain.py | `control/magic_square_control.py` | Control + Boundary 혼재 | 부적합 |
| domain.py | `control/two_cell_solver.py` | Control (스텁) | 부적합 |
| boundary.py | `boundary/boundary_validator.py` | Boundary (E001~E005) | 부분 |
| boundary.py | `boundary/ui_boundary.py` | — | 미구현 |
| gui/main_window | `boundary/gui/main_window.py` | Screen + Gateway | 부적합 |

### 의존성 위반 (must_not)

| 위치 | 위반 |
|------|------|
| `control/magic_square_control.py` | `control → boundary` (`BoundaryValidator`, `FailureResult`) |
| `boundary/gui/main_window.py` | Screen → `MagicSquareControl` 직접 호출 |

## 5. 리팩토링 대상 (우선순위)

| 순번 | 대상 | 문제 | 기법 | 우선순위 |
|------|------|------|------|----------|
| 0 | entity 테스트 + GM | Track B RED, import 오류 | RED→GREEN | P0 선행 |
| 1 | `magic_square_control.py` | 검증+resolve 이중 역할, ECB 위반 | Move Method | P0 High |
| 2 | `solve_partial` + `two_cell_solver` | Step A only, 3중 진입점 | Split Class / Extract Method | P0 High |
| 3 | `boundary_validator.py` | non-int → TypeError | Guard Clause | P0 High |
| 4 | `ui_boundary.py` (신규) | Screen↔Control·envelope 부재 | Facade | P1 High |
| 5 | `main_window.py` | Control 직접 호출, fixture | Move Method | P1 Medium |
| 6 | `grid_panel.py` | apply_solution 다중 역할 | Extract Method | P1 Medium |
| 7 | `input_validator.py` | BoundaryValidator 이중 | Remove Dead Code | P1 Medium |
| 8 | constants SSOT | 4/16/2 중복 | Replace Magic Number | P2 Medium |
| 9 | 경로 rename | gui→screen 등 | Move Module | P2 Low |

## 6. 테스트 선행 필요 항목

| 함수 / 진입점 | 테스트 | 상태 |
|---------------|--------|------|
| `find_blank_coords` | `test_d_loc_blank_coords.py` | RED, import 깨짐 |
| `find_missing_numbers` | `test_d_mis_missing_numbers.py` | RED, import 깨짐 |
| `is_magic_square` | `test_d_val_magic_square.py` | RED 6건 |
| `solution` / `execute` | `test_d_sol_solution.py` | RED 4건 |
| `MagicSquareControl` | isolation + GM | GREEN (Track B 후 GM 재승인) |
| `BoundaryValidator` (타입) | 신규 | 미작성 |
| `ui_boundary` | 신규 | 미작성 |
| `GridPanel` | 신규 | 미작성 |

## 7. 회귀 검증

```powershell
python -m pytest tests/boundary/ -q
python -m pytest tests/control/test_u_flow_execute_isolation.py tests/control/test_solve_orchestration_dimension.py -q
python -m pytest tests/entity/ -q
python -m pytest -m golden_master -v
python -m pytest tests/ -v
python -m pytest tests/ --cov=src --cov-report=term-missing
```

### 외부 동작 불변 확인

| 항목 | 방법 |
|------|------|
| E001~E005 | boundary 테스트 코드·메시지·short-circuit |
| invalid → Domain 0회 | `test_u_flow_execute_isolation.py` |
| int[6] | Golden Master GM-TC-01~02, contracts |
| unsolvable | GM-TC-05 (Track B GREEN 후 Error baseline) |
| GUI | `python main.py` 수동 smoke |

## 8. REFACTOR phase 결론

**1순위:** Track B(D-LOC→D-MIS→D-VAL→D-SOL + GM) GREEN으로 int[6]/unsolvable 계약 고정 → `MagicSquareControl`에서 Boundary 검증 분리(control→boundary 역전 해소) → 그 다음 `ui_boundary`/Screen 분리(P1).

## 9. 산출물

| 파일 | 설명 |
|------|------|
| `README.md` | REFACTOR 단계 To-Do 리스트 추가 |
| `Report/15_MagicSquare_refactoring_plan_report.md` | 본 보고서 |
| `Prompt/15_MagicSquare_refactoring_plan_prompt_transcript.md` | 대화 transcript |

## 10. GitHub

- 브랜치: `refactor/refactor`
- 커밋: docs — REFACTOR 계획 README·Report·Prompt
