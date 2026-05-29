# MagicSquare Golden Master 회귀 테스트 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 및 **GitHub 반영**을 수행한다.
- 본 세션에서 구현한 **Golden Master(GM-1~GM-3) 회귀 안전장치**와 검증 결과를 기록한다.
- Refactoring·Track B 진입 전 **실제 솔버 출력**을 기준 파일로 고정하는 절차를 SSOT로 남긴다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **요청** | GM-1 기준 파일, GM-2 테스트 코드, GM-3 README, GM 검증 |
| **선행 상태** | Track A GREEN — `MagicSquareControl.solve()` + Boundary 검증 |
| **브랜치** | `stabilize/green` |
| **캡처 방식** | CLI stdout 없음 → **Result DTO 직렬화** (`FailureResult` / `list[int]`) |
| **테스트 프레임워크** | pytest + `@pytest.mark.golden_master` |

## 3. 세션 타임라인 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | GM-1 기준 파일·approve 패턴 | `tests/golden_master_expected.txt`, `tests/golden_master/` |
| 2 | GM-2 테스트 코드 | `tests/test_golden_master_magic_square.py`, `contracts.py` |
| 3 | GM-3 README | Golden Master 회귀 안전장치 섹션 (GM-01~10) |
| 4 | GM 검증 | 실제 vs 기준 일치 확인, pytest 6 passed |
| 5 | 본 보고서·transcript | `Report/14_...`, `Prompt/14_...` |
| 6 | GitHub 커밋·푸시 | `stabilize/green` |

## 4. 구현 구조

```
tests/
├── golden_master_expected.txt          # GM-1 기준 출력 (버전 관리)
├── test_golden_master_magic_square.py  # GM-2 pytest (GM-TC-00~05)
└── golden_master/
    ├── scenarios.py      # 5개 시나리오 입력 SSOT
    ├── serializer.py     # DTO → 텍스트, 파싱
    ├── approval.py       # approve 패턴, unified diff
    └── contracts.py      # int[6], row-major, 1-index, Error Contract

scripts/generate_golden_master.py       # 기준 파일 재생성 CLI
docs/golden_master_approval_design.md   # approve 패턴 설계 문서
```

### Approve 패턴

| 조건 | 동작 |
|------|------|
| 기준 파일 없음 | 현재 출력으로 자동 생성 후 PASS |
| 기준 파일 있음 | `actual` vs `open(expected).read()` 비교 |
| 불일치 | `--- expected` / `+++ actual` unified diff 후 FAIL |
| 강제 승인 | `GOLDEN_MASTER_APPROVE=1` |

## 5. 시나리오 및 기준 출력 (Track A 현재 구현)

| 섹션 | GM-TC | 실제 `solve()` | 기준 파일 |
|------|-------|----------------|-----------|
| `normal_success` | GM-TC-01 | `[3,3,1,4,4,6]` | 일치 |
| `reverse_success` | GM-TC-02 | `[1,1,3,1,2,16]` | 일치 (Step A) |
| `invalid_blank_count` | GM-TC-03 | `E002` | 일치 |
| `duplicate_number` | GM-TC-04 | `E005` | 일치 |
| `no_valid_solution` | GM-TC-05 | `[1,1,13,1,4,16]` | 일치 (Step A) |

> **Track B 후속:** `reverse_success`·`no_valid_solution`은 Domain GREEN(Step B, `ERR_NO_VALID_COMBINATION`) 후 baseline 재승인 필요.

## 6. 회귀 보호 (GM-07~10)

| ID | 검증 내용 | 구현 |
|----|-----------|------|
| GM-07 | row-major 빈칸 순서 | `assert_row_major_blank_order` |
| GM-08 | 1-index 좌표 (1..4) | `assert_one_index_coordinate_rule` |
| GM-09 | reverse fallback | baseline 비교 + Track B 후 `assert_reverse_fallback_assignment` |
| GM-10 | Error Contract | `assert_invalid_blank_count_contract`, `assert_duplicate_number_contract` |

## 7. 실행 방법

```powershell
cd c:\DEV\MagicSquare_05

# Golden Master 회귀 테스트
.venv\Scripts\python.exe -m pytest -m golden_master -v

# 기준 파일 재생성
.venv\Scripts\python.exe scripts\generate_golden_master.py

# 강제 승인 (의도된 출력 변경 시)
$env:GOLDEN_MASTER_APPROVE = "1"
.venv\Scripts\python.exe -m pytest -m golden_master -v
```

## 8. 검증 결과

| 검증 | 명령/방법 | 결과 |
|------|-----------|------|
| Golden Master pytest | `pytest tests/test_golden_master_magic_square.py -m golden_master -v` | **6 passed** |
| 전체 문서 일치 | `collect_actual_output()` vs `golden_master_expected.txt` | **PASS** |
| 시나리오 블록 | 5/5 섹션 | **PASS** |
| 계약 (GM-07~10) | row-major, 1-index, small-first, E002/E005 | **PASS** |
| Boundary + Control 회귀 | `pytest tests/boundary/ tests/control/ -q` | **46 passed** (선행) |

## 9. 신규·수정 파일

| 파일 | 유형 |
|------|------|
| `tests/golden_master_expected.txt` | 신규 — GM-1 기준 출력 |
| `tests/golden_master/*.py` | 신규 — 시나리오·직렬화·approve·계약 |
| `tests/test_golden_master_magic_square.py` | 신규 — GM-2 테스트 |
| `scripts/generate_golden_master.py` | 신규 — 생성 스크립트 |
| `docs/golden_master_approval_design.md` | 신규 — 설계 문서 |
| `pytest.ini` | 수정 — `golden_master` 마커 |
| `README.md` | 수정 — Golden Master 회귀 안전장치 섹션 |
| `Report/14_MagicSquare_golden_master_report.md` | 신규 — 본 보고서 |
| `Prompt/14_MagicSquare_golden_master_prompt_transcript.md` | 신규 — 대화 transcript |

## 10. README 체크리스트 (GM-01~10)

| 항목 | 상태 |
|------|------|
| GM-01~03 기준 파일 생성·git add | ✅ |
| GM-04~06 테스트·approve·PASS | ✅ |
| GM-07~10 회귀 보호 | ✅ (Track B 후 GM-09 재검토) |

## 11. 미포함·후속 권장

| 항목 | 비고 |
|------|------|
| Track B Entity GREEN | `is_magic_square`, reverse, `ERR_NO_VALID_COMBINATION` |
| GM baseline 재승인 | Track B GREEN 후 `GOLDEN_MASTER_APPROVE=1` |
| stdout 캡처 | 미사용 — DTO 직렬화만 |

## 12. 관련 문서

- `docs/golden_master_approval_design.md` — approve 패턴 SSOT
- `Report/12_MagicSquare_track_a_green_implementation_report.md` — 선행 GREEN
- `Report/13_MagicSquare_pyqt_gui_report.md` — GUI 구현
