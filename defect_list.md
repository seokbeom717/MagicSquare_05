# MagicSquare — 결함 목록 (Defect List)

| 항목 | 내용 |
|------|------|
| **문서 버전** | 1.0 |
| **최종 갱신** | 2026-05-29 |
| **기준** | `docs/PRD_MagicSquare.md`, `docs/test_plan.md`, AC-FR-01-01 RED 테스트 |
| **상태 요약** | Open 4 · Closed 0 · Info 1 |

---

## 결함 테이블

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|-------|-----------|--------|--------|-----------|-----------|
| DEF-001 | Critical | AC-FR-01-01 | 1. `.venv` 활성화<br>2. `python -m pytest tests/boundary/test_boundary_validator_dimension.py -v` | 테스트 모듈 수집·실행; `grid=None` 시 `FailureResult(code="INVALID_SIZE", message="Grid must be 4x4.")` | `ModuleNotFoundError: No module named 'src.boundary'` (수집 단계, `test_boundary_validator_dimension.py:5`) | `src/boundary/` 패키지 및 `BoundaryValidator` 미구현 | `src/boundary/` 생성: `failure_result.py`, `boundary_validator.py`; `grid is None` 및 4×4 차원 검증만 구현 |
| DEF-002 | Critical | AC-FR-01-01, AC-FR-01-05 | 1. `.venv` 활성화<br>2. `python -m pytest tests/control/test_solve_orchestration_dimension.py -v` | `solve(grid=None)` 실패 반환; `resolve()` 호출 0회 (mock/spy) | `ModuleNotFoundError: No module named 'src.control'` (수집 단계, `test_solve_orchestration_dimension.py:9`) | `src/control/` 패키지 및 `MagicSquareControl` 미구현 | `src/control/magic_square_control.py` 생성; 검증 실패 시 early return, `resolve()` 미호출 |
| DEF-003 | Major | AC-FR-01-01 | DEF-001·002 동일 환경에서 `test_grid_none_returns_invalid_size_code` 등 15건 실행 시도 | Boundary 단위 assertion 통과 (code/message/타입) | 테스트 본문 **미실행** (import 실패로 assert 단계 미도달) | DEF-001에 종속 | DEF-001 해결 후 자동 해소 예상; 별도 로직 수정 없음 |
| DEF-004 | Major | AC-FR-01-05 | DEF-002 동일; `test_grid_none_resolve_call_count_zero` 실행 시도 | `patch.object(control, "resolve")` 후 `assert_not_called()` | 테스트 본문 **미실행** (import 실패) | DEF-002에 종속 | DEF-002 해결 후 자동 해소 예상 |
| DEF-005 | Info | NFR-01 (Boundary ≥85%) | `python -m pytest tests/boundary --cov=src/boundary --cov-report=term-missing` | Boundary 커버리지 % 및 `term-missing` 라인 목록 | `Module src/boundary was never imported` / `No data was collected` / 리포트 생성 실패 | DEF-001: 측정 대상 모듈 없음 | DEF-001 GREEN 후 동일 명령 재실행; `--cov-fail-under=85` 게이트 적용 |
| DEF-006 | Info | — | `python -m pytest --cov=src --cov-report=html` | exit code 0, AC-FR-01-01 SUT 포함 전체 수집 | **11 passed, 2 errors**; `htmlcov`는 주로 `src/entity/user.py`만 반영 | DEF-001·002; `pytest.ini`의 `--continue-on-collection-errors`로 일부만 실행 | DEF-001·002 해결 후 전체 스위트 재실행; 목표 36 passed (entity 6 + boundary 25 + control 5) |

---

## 재현 명령 (공통)

```powershell
cd C:\DEV\MagicSquare_05
.\.venv\Scripts\Activate.ps1
python -m pip install pytest pydantic pytest-cov

# DEF-001
python -m pytest tests/boundary/test_boundary_validator_dimension.py -v

# DEF-002
python -m pytest tests/control/test_solve_orchestration_dimension.py -v

# DEF-005
python -m pytest tests/boundary --cov=src/boundary --cov-report=term-missing
```

---

## 현재 통과 항목 (결함 아님)

| 항목 | 결과 | 비고 |
|------|------|------|
| `tests/boundary/test_ac_fr_01_01_scope.py` | 5 passed | AC-FR-01-02~05 / FR-02~05 토큰·테스트명 범위 가드 |
| `tests/entity/test_user.py` | 6 passed | 기존 Entity 테스트 |
| RED 테스트 코드 작성 | 완료 | `tests/boundary/`, `tests/control/` |

---

## 수정 우선순위 (GREEN 경로)

1. **DEF-001** — `BoundaryValidator` + `FailureResult` (AC-FR-01-01 차원만)
2. **DEF-002** — `MagicSquareControl.solve` + 검증 실패 시 `resolve()` 차단 (AC-FR-01-05)
3. **DEF-003, DEF-004** — 회귀 확인 (동일 pytest 명령)
4. **DEF-005, DEF-006** — 커버리지·전체 스위트 재측정

**범위 외 (본 결함 수정 시 작성 금지):** AC-FR-01-02~04, FR-02~05 Domain 로직.

---

## PRD vs 테스트 계약 참고 (잠재 Info)

| 항목 | PRD §12·§13 | 현재 테스트·README |
|------|-------------|-------------------|
| 오류 코드 | `ERR_INVALID_DIMENSION` | `INVALID_SIZE` |
| 메시지 | `Input matrix must be 4x4.` | `Grid must be 4x4.` |

현재는 **실행 전(import 단계)** 이므로 별도 DEF로 등록하지 않음. GREEN 후 PRD 정합이 필요하면 추적 항목으로 추가.

---

## 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 1.0 | 2026-05-29 | 초기 등록: DEF-001~006 (RED-1 수집·cov 이슈) |
