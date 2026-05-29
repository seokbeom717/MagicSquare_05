# MagicSquare GREEN To-Do Checklist 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 요청을 수행한다.
- 본 세션에서 수행한 **RED 커밋 묶음 ↔ GREEN 처리 순서 정리** 및 **README 체크리스트 추가** 작업을 기록한다.
- 후속 GREEN 단계 구현·커밋의 **SSOT 진행 추적 문서**로 사용한다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **TDD 단계** | RED 완료(부분) → GREEN 진입 준비 |
| **설계 SSOT** | `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` |
| **선행 작업** | Report/08 AC-FR-01-01 Full RED 25건; Report/10 RED Skeleton 22건 |
| **현재 구현** | `src/boundary/boundary_validator.py` — `grid=None` 분기만 GREEN |
| **요청 의도** | RED를 묶어 커밋한 뒤, 대응 GREEN을 오름차순으로 진행할 To-Do Checklist |

## 3. 세션 타임라인 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | RED 커밋 묶음(R1~R6) 설계 | 대화 산출 — 5~6개 RED 커밋 단위 |
| 2 | GREEN 마스터 리스트 오름차순 정렬 | Test ID 파이프라인 순서 28건 boundary + control 연동 |
| 3 | `README.md` **GREEN 단계 To-Do 리스트** 섹션 추가 | GREEN-0 ~ GREEN-6 + 메타 + 완료 기준 |
| 4 | `pytest tests/boundary/` 현황 확인 | 13 passed, 15 failed |
| 5 | 본 보고서·transcript | `Report/11_...`, `Prompt/11_...` |

## 4. RED 커밋 묶음 (권장)

| 묶음 | 범위 | 주요 파일 | 테스트 수 |
|------|------|-----------|-----------|
| **R1** | 인프라 + 스코프 가드 | `failure_result.py`, `schemas.py`, `conftest.py`, `test_ac_fr_01_01_scope.py` | 5 |
| **R2** | U-IN-01/02 Full RED (차원) | `test_boundary_validator_dimension.py`, `boundary_validator.py`(스텁) | 15 |
| **R3** | U-IN-03 blank count 스켈레톤 | `test_u_in_blank_count.py` | 2 |
| **R4** | U-IN-04 range + U-IN-05 duplicate | `test_u_in_range.py`, `test_u_in_duplicate.py` | 3 |
| **R5** | U-OUT 스켈레톤 | `test_u_out_contract.py` | 2 |
| **R6** | control orchestration (선택 분리) | `test_solve_orchestration_dimension.py`, `test_u_flow_execute_isolation.py` | 10 |

> R5/R6는 `src.control` 미구현 시 collect ERROR 가능 — boundary RED 먼저, control은 R6 별도 커밋 권장.

## 5. GREEN 처리 순서 (오름차순 마스터)

정렬 키: Report/09 검증 파이프라인 — **차원 → blank → range → duplicate → 출력 → 오케스트레이션**  
동일 ID 내: **테스트 함수명 오름차순**

| GREEN 묶음 | 대응 RED | Test ID | 테스트 수 | 상태 (세션 종료 시) |
|------------|----------|---------|-----------|---------------------|
| GREEN-0 | R2 (1/2) | U-IN-01 (`grid=None`) | 8 | ✅ 8/8 |
| GREEN-1 | R2 (2/2) | U-IN-02 (4×4 차원) | 8 + control 5 | 🔴 0/8 |
| GREEN-2 | R3 | U-IN-03a/b | 2 | ⏸ 스켈레톤 |
| GREEN-3 | R4 (1/2) | U-IN-04a/b | 2 | ⏸ 스켈레톤 |
| GREEN-4 | R4 (2/2) | U-IN-05 | 1 | ⏸ 스켈레톤 |
| GREEN-5 | R5 | U-OUT-01/02 | 2 | ⏸ 스켈레톤 |
| GREEN-6 | R5/R6 | U-FLOW-02 ×5 | 5 | ⏸ 스켈레톤 |
| GREEN 메타 | R1 | scope guard | 5 | ✅ 5/5 |

**short-circuit 구현 순서:** 차원(E001) → blank(E002) → range(E004) → duplicate(E005)

## 6. README.md 변경 사항

### 6.1 추가 섹션

`README.md` 하단 **「GREEN 단계 To-Do 리스트」** 섹션 신규 추가 (기존 RED 단계 To-Do 리스트 유지).

포함 내용:

- GREEN-0 ~ GREEN-6 개별 체크박스 (테스트 함수명 단위)
- 묶음별 `pytest` 검증 명령
- 구현 대상 파일 (`boundary_validator.py`, `control/` 등)
- GREEN 완료 기준 (boundary 28건, orchestration, 커버리지 85%+)
- RED ↔ GREEN 매핑 요약 표

### 6.2 미변경

- 기존 RED 단계 To-Do 리스트 (TC-A/B, 커버리지 목표) — 그대로 유지
- `src/` 구현 코드 — 본 세션에서 GREEN 구현 미수행

## 7. pytest 실행 결과

### 7.1 명령

```powershell
cd C:\DEV\MagicSquare_05
python -m pytest tests/boundary/ -q
```

### 7.2 관측 (세션 종료 시점)

| 구분 | 결과 |
|------|------|
| **scope guard** (`test_ac_fr_01_01_scope.py`) | 5 **passed** |
| **U-IN-01** (`TestNormalFailureReturn`) | 6 **passed** (GREEN-0) |
| **U-IN-02** (`TestBoundaryValueCases`, `TestMessageCharacterIdentity` 일부) | 8 **failed** — `NotImplementedError` |
| **스켈레톤** (`test_u_in_*`, `test_u_out_*`) | 7 **failed** — `pytest.fail` |
| **합계** | **13 passed, 15 failed** |

### 7.3 실패 원인

| 실패 그룹 | 원인 |
|-----------|------|
| GREEN-1 (8건) | `BoundaryValidator.validate`가 `grid is None` 이후 `NotImplementedError` |
| GREEN-2~5 (7건) | 스켈레톤 `pytest.fail("RED: ...")` — Full RED·구현 대기 |

## 8. 다음 GREEN 작업 (권장 순서)

1. **GREEN-1** — `src/boundary/boundary_validator.py`에 4×4 차원 검사 추가
   - `[]`, `[[]]*4`, `3×4` → `FailureResult(INVALID_SIZE, "Grid must be 4x4.")`
   - 검증: `pytest tests/boundary/test_boundary_validator_dimension.py -q`
2. **(선택)** control dimension orchestration 5건 — `src/control/` 최소 스텁
3. **GREEN-2** — 스켈레톤 → Full RED assert + blank count E002
4. **GREEN-3~4** — range E004, duplicate E005
5. **GREEN-5~6** — G1 fixture + solve 경로 + U-FLOW execute 격리

## 9. 관련 문서

| 문서 | 역할 |
|------|------|
| `README.md` § GREEN 단계 To-Do 리스트 | 진행 체크리스트 SSOT |
| `Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md` | Test ID·파이프라인 설계 |
| `Report/10_MagicSquare_red_skeleton_fr01_fr05_report.md` | RED Skeleton 22건 |
| `Report/08_MagicSquare_ac_fr_01_01_red_test_and_defect_report.md` | AC-FR-01-01 Full RED |
| `Prompt/11_MagicSquare_green_todo_checklist_prompt_transcript.md` | 본 세션 대화 원문 |

## 10. 결론

본 세션은 GREEN **구현**이 아니라 **진행 계획·추적 체계**를 확립했다.

- RED 커밋 묶음(R1~R6)과 GREEN 묶음(GREEN-0~6)의 1:1 대응 관계를 문서화했다.
- `README.md`에 체크박스 기반 To-Do List를 추가해, GREEN 단계마다 pytest 명령과 구현 대상을 한눈에 확인할 수 있게 했다.
- 현재 **GREEN-0·메타 완료**, **GREEN-1이 즉시 착수 가능한 다음 작업**이다.

---

*작성일: 2026-05-29 | TDD 단계: GREEN 준비 | workflow-automation 보고서 작성*
