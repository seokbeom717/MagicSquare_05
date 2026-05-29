# MagicSquare PyQt GUI 구현 보고서

## 1. 작업 목적

- `workflow-automation` 규칙에 따라 **「보고서 작성」** 및 **GitHub 반영**을 수행한다.
- 본 세션에서 구현한 **PyQt6 데스크톱 GUI**(Boundary 레이어)와 후속 UX 개선을 기록한다.
- ECB 아키텍처 준수 여부·실행 방법·검증 결과를 후속 유지보수 기준 문서로 남긴다.

## 2. 배경

| 항목 | 내용 |
|------|------|
| **요청** | PyQt를 이용해 GUI로 MagicSquare 프로그램 실행 |
| **선행 상태** | Track A GREEN 완료 — `MagicSquareControl.solve()` + Boundary 검증 계약 |
| **브랜치** | `stabilize/green` |
| **PRD 범위** | UI는 Out-of-Scope이나, Boundary I/O 확장으로 ECB `boundary` 레이어에 배치 |
| **의존성** | `PyQt6` (신규), `pydantic`, `pytest` (`requirements.txt`) |

## 3. 세션 타임라인 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | PyQt6 GUI 초기 구현 | `src/boundary/gui/`, `main.py`, `requirements.txt` |
| 2 | 숫자 입력 불가 수정 | `QSpinBox` → `QLineEdit` + `QIntValidator` |
| 3 | 랜덤 퍼즐 버튼 추가 | `random_puzzle.py`, `main_window.py` |
| 4 | 정답 칸 파란색 하이라이트 | `grid_panel.py` `set_highlighted()` |
| 5 | 본 보고서·transcript 작성 | `Report/13_...`, `Prompt/13_...` |
| 6 | GitHub 커밋·푸시 | `stabilize/green` |

## 4. 구현 구조 (ECB)

```
boundary/gui/
├── app.py              # QApplication 부트스트랩, run_gui()
├── main_window.py      # 메인 창 — 해결/샘플/랜덤/초기화
├── grid_panel.py       # 4×4 QLineEdit 격자
└── random_puzzle.py    # 유효 퍼즐 무작위 생성
main.py                 # 진입점: python main.py
```

| 레이어 | 책임 | 의존 |
|--------|------|------|
| `boundary/gui` | 외부 I/O, 격자 표시·입력, 오류/성공 메시지 | `control` (`MagicSquareControl`) |
| `control` | 검증 후 Domain 호출 조율 | `entity` |
| `entity` | 마방진 로직 | (I/O 없음) |

**준수 사항:** `boundary/gui`는 `entity`를 직접 import하지 않음. 격자 상수(`_GRID_SIZE=4` 등)는 GUI 로컬 상수로 유지.

## 5. 기능 상세

### 5.1 초기 GUI

- 4×4 격자, **해결** / **샘플 불러오기** / **초기화** 버튼
- 성공 시 `int[6]` 결과로 빈칸 2개 채움 (G1: `[2,2,7,3,3,10]`)
- 실패 시 `FailureResult` 코드·메시지를 상태 라벨 + `QMessageBox`로 표시

### 5.2 입력 수정 (QSpinBox → QLineEdit)

| 문제 | 원인 | 해결 |
|------|------|------|
| 키보드로 숫자 입력 불가 | `QSpinBox` + `setSpecialValueText("·")` 조합이 편집 필드 입력 차단 | `QLineEdit` + `QIntValidator(0,16)` |
| 빈칸 표현 | 0 입력 필요 | 빈 문자열 = 빈칸 (`·` placeholder) |

### 5.3 랜덤 퍼즐

- 완성된 4×4 마방진 3종 + 회전(0~3) + 좌우 반전
- 16칸 중 무작위 2칸을 빈칸(`0`)으로 설정
- 항상 Boundary 계약 충족: 빈칸 2개, 1~16 중복 없음

### 5.4 정답 하이라이트

- **해결** 후 채워진 2칸만 `#1565c0` 파란색 + 굵게
- 초기화·샘플·랜덤 로드 시 하이라이트 해제
- 사용자가 정답 칸을 수정하면 하이라이트 자동 해제

## 6. 실행 방법

```powershell
cd c:\DEV\MagicSquare_05
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python.exe main.py
```

또는:

```powershell
.venv\Scripts\python.exe -m src.boundary.gui.app
```

## 7. 검증 결과

| 검증 | 명령/방법 | 결과 |
|------|-----------|------|
| Boundary + Control 회귀 | `pytest tests/boundary/ tests/control/ -q` | **38 passed** |
| G1 샘플 해결 (headless) | `MagicSquareMainWindow._on_load_sample()` → `_on_solve()` | `(2,2)=7`, `(3,3)=10` |
| 랜덤 퍼즐 20건 | `generate_random_puzzle` + `BoundaryValidator` + `solve` | 20/20 통과 |
| 정답 하이라이트 | headless styleSheet 검사 | `#1565c0` 적용 확인 |

## 8. 신규·수정 파일

| 파일 | 유형 |
|------|------|
| `main.py` | 신규 — GUI 진입점 |
| `requirements.txt` | 신규 — PyQt6, pydantic, pytest |
| `src/boundary/gui/__init__.py` | 신규 |
| `src/boundary/gui/app.py` | 신규 |
| `src/boundary/gui/main_window.py` | 신규 |
| `src/boundary/gui/grid_panel.py` | 신규 |
| `src/boundary/gui/random_puzzle.py` | 신규 |
| `Report/13_MagicSquare_pyqt_gui_report.md` | 신규 — 본 보고서 |
| `Prompt/13_MagicSquare_pyqt_gui_prompt_transcript.md` | 신규 — 대화 transcript |

## 9. 미포함·후속 권장

| 항목 | 비고 |
|------|------|
| GUI 단위 테스트 | PRD Track A 범위 외; headless smoke만 수동 검증 |
| Track B Entity GREEN | `tests/entity/test_d_*.py` 스켈레톤 잔존 |
| README GUI 섹션 | 본 세션에서 미갱신 (필요 시 실행 방법 추가) |
| `is_magic_square` Attempt 1/2 | GREEN-5는 Step A 형식만 반환; 완전 솔버는 Track B 후속 |

## 10. 관련 문서

- `Report/12_MagicSquare_track_a_green_implementation_report.md` — 선행 GREEN 구현
- `docs/PRD_MagicSquare.md` — 계약·레이어 정의
- `.cursor/rules/magicsquare-ecb-architecture.mdc` — ECB 의존 방향
