# MagicSquare AC-FR-01-01 RED 테스트·결함 분석 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 요청을 수행한다.
- 본 대화 세션에서 수행한 **AC-FR-01-01 RED 단계** 작업(테스트 설계·계획·테스트 코드·결함 문서화·실행 환경 안내)을 정리한다.
- 후속 **GREEN** 구현 및 결함 해소(DEF-001~006)의 기준 문서로 사용한다.

## 2. 배경

- 기준 PRD: `docs/PRD_MagicSquare.md` (FR-01 Input Verification, NFR-01 Coverage).
- Dual-Track TDD: Track A(Boundary) 선행 — Domain resolver 미호출(AC-FR01-05).
- 작업 표기: README·테스트는 `INVALID_SIZE` / `Grid must be 4x4.` 사용; PRD §12·§13 정식 코드는 `ERR_INVALID_DIMENSION` / `Input matrix must be 4x4.` (정합은 GREEN 이후 결정).

## 3. 수행 내용 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | PRD FR-01 샘플 예제 선정 (코드 없음) | 대화 산출 (AC-FR01-01, `grid=None`) |
| 2 | 테스트 계획서 작성 | `docs/test_plan.md` |
| 3 | README RED To-Do 체크리스트 삽입 | `README.md` §RED 단계 To-Do |
| 4 | AC-FR-01-01 RED pytest 25건 작성 | `tests/boundary/`, `tests/control/`, `tests/conftest.py`, `pytest.ini` |
| 5 | 가상환경·pytest·cov 실행 안내 | 대화 산출 |
| 6 | 커버리지 85% 출처 설명 (PRD NFR-01) | 대화 산출 |
| 7 | ImportError 결함 분석·GREEN 최소 수정안 | 대화 산출 |
| 8 | 결함 목록 문서화 | `defect_list.md` |
| 9 | 본 보고서·transcript | `Report/08_...`, `Prompt/08_...` |

## 4. 생성·수정 파일

### 4.1 신규

| 파일 | 설명 |
|------|------|
| `docs/test_plan.md` | AC-FR01-01/05, 경계값, mock/spy, pytest-cov 전략 |
| `pytest.ini` | `pythonpath`, `--continue-on-collection-errors` |
| `tests/conftest.py` | fixtures, `INVALID_SIZE` 계약 상수 |
| `tests/boundary/test_boundary_validator_dimension.py` | Boundary 15 tests (3 classes × 5) |
| `tests/boundary/test_ac_fr_01_01_scope.py` | 범위 가드 5 tests |
| `tests/control/test_solve_orchestration_dimension.py` | Control resolve 격리 5 tests |
| `tests/boundary/__init__.py`, `tests/control/__init__.py` | 패키지 |
| `defect_list.md` | DEF-001~006 |
| `Report/08_MagicSquare_ac_fr_01_01_red_test_and_defect_report.md` | 본 보고서 |
| `Prompt/08_MagicSquare_ac_fr_01_01_red_prompt_transcript.md` | 대화 transcript |

### 4.2 수정

| 파일 | 변경 |
|------|------|
| `README.md` | §RED 단계 To-Do 리스트 추가; 결함 목록 `defect_list.md` 체크 1건 완료 |

### 4.3 미구현 (GREEN 대상)

| 경로 | 관련 결함 |
|------|-----------|
| `src/boundary/` | DEF-001 |
| `src/control/` | DEF-002 |

## 5. 테스트 현황 (RED-1)

### 5.1 실행 명령 (권장)

```powershell
cd C:\DEV\MagicSquare_05
.\.venv\Scripts\Activate.ps1
python -m pip install pytest pydantic pytest-cov
python -m pytest tests/boundary tests/control -v
```

### 5.2 관측 결과 (2026-05-29 기준)

| 구분 | 결과 |
|------|------|
| `test_ac_fr_01_01_scope.py` | **5 passed** |
| `test_boundary_validator_dimension.py` | **ERROR collecting** — `No module named 'src.boundary'` |
| `test_solve_orchestration_dimension.py` | **ERROR collecting** — `No module named 'src.control'` |
| `tests/entity/test_user.py` | **6 passed** (기존) |
| 전체 + htmlcov | **11 passed, 2 errors**; Boundary cov **No data collected** |

### 5.3 해석

- RED-1(테스트 선행)으로 **의도된 수집 실패**에 해당.
- Assertion 실패가 아닌 **SUT 모듈 부재**이므로 `defect_list.md` DEF-001·002를 Critical로 등록.

## 6. 결함 목록 연동

| ID | Severity | 상태 | 요약 |
|----|----------|------|------|
| DEF-001 | Critical | Open | `src.boundary` 미구현 |
| DEF-002 | Critical | Open | `src.control` 미구현 |
| DEF-003 | Major | Open | DEF-001 종속, Boundary 15건 미실행 |
| DEF-004 | Major | Open | DEF-002 종속, Control 5건 미실행 |
| DEF-005 | Info | Open | Boundary cov 측정 불가 |
| DEF-006 | Info | Open | 전체 스위트 2 collection errors |

상세: `defect_list.md`

## 7. GREEN 최소 수정 방안 (요약)

1. `src/boundary/failure_result.py` — pydantic `FailureResult`
2. `src/boundary/boundary_validator.py` — `grid is None`, 4×4 차원만 (AC-FR01-01)
3. `src/control/magic_square_control.py` — 검증 실패 시 early return, `resolve()` 미호출 (AC-FR01-05)
4. **금지:** AC-FR01-02~04, FR-02~05 Domain 로직 선제 구현

GREEN 확인:

```powershell
python -m pytest tests/boundary/test_boundary_validator_dimension.py tests/control/test_solve_orchestration_dimension.py -v
python -m pytest tests/boundary --cov=src/boundary --cov-report=term-missing --cov-fail-under=85
```

## 8. 커버리지 목표 출처

| 레이어 | 목표 | 문서 |
|--------|------|------|
| Domain | 95%+ | `docs/PRD_MagicSquare.md` NFR-01 |
| Boundary | 85%+ | 동일, `docs/test_plan.md`, `README.md` RED To-Do |
| 프로젝트 최소 | 80%+ | `.cursor/rules/magicsquare-project.mdc` |

현재 Boundary cov 명령은 **DEF-001 해결 전까지 의미 없음**.

## 9. README 체크리스트 상태

- RED To-Do: Track A/B·커버리지 항목 — **미완료** (GREEN 후 체크)
- 결함 목록: `defect_list.md` 생성 — **완료 [x]**
- 결함 수정 후 회귀 — **미완료 [ ]**

## 10. 다음 단계

1. DEF-001·002 GREEN 구현 (최소 diff).
2. 20 SUT tests + scope 5 → boundary/control GREEN 확인.
3. `defect_list.md` DEF-001~006 Closed 처리.
4. README RED To-Do·결함 회귀 체크박스 갱신.
5. (선택) PRD `ERR_INVALID_DIMENSION` vs 테스트 `INVALID_SIZE` 정합 결정.

## 11. 결과

- **보고서·transcript** 작성 완료.
- **RED 테스트·test_plan·defect_list** 저장소 반영 완료.
- **프로덕션 코드(boundary/control)** 미구현 — GREEN 대기.
