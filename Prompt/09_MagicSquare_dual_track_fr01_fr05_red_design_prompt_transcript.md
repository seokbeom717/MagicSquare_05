# MagicSquare FR-01~FR-05 Dual-Track RED 설계 Prompt Transcript

## Turn 01
### User
```text
당신은 Dual-Track UI + Logic TDD 전문가입니다.

**TDD phase: RED** — 오직 RED 테스트 설계표만 작성하십시오.

## 금지 (엄격)
- 구현 코드, 테스트 코드, 스켈레톤 코드 작성 금지
- 클래스/파일 구조 확정 금지
- GREEN / REFACTOR 단계 진입 금지
- pytest 실행·코드 생성·파일 저장 금지 (설계표 텍스트 출력만)

## SSOT (반드시 참조)
- docs/PRD_MagicSquare.md v0.2
- Report/02.MagicSquare_DualTrack_TDD_Design_Report.md
- .cursorrules (ECB, Dual-Track, Test ID 규칙)

## 프로젝트 계약
입력: 4×4 int[][], 0=빈칸(정확히 2개), 값 0 또는 1~16, 0 제외 중복 금지
출력: int[6] = [r1,c1,n1,r2,c2,n2], 좌표 1-index
마방진 상수: M=34
검증 순서 (short-circuit): null → size → empty count → value range → duplicate
Boundary invalid: E003, E001, E002, E004, E005 — Failure envelope, execute 0회 (U-FLOW-02)
Domain Logic: Domain Mock 금지

## 범위
전체 FR-01~FR-05 Dual-Track RED 설계표

### TRACK A
U-IN-01~05 (입력), U-OUT-01~02 (출력), U-FLOW-02 (execute 0회)
항목별: Test ID, Layer, 테스트 이름, Given, When, Then, Expected RED Failure,
실패 이유, Boundary 계약, Invariant

### TRACK B
find_blank_coords, find_not_exist_nums, is_magic_square, solution
Given: Report/02 부록 G0~G3
D-LOC-01, D-MIS-01, D-VAL-01~06, D-SOL-01~03 (+ 길이/1-index)
Domain Mock 금지 명시

## 출력 형식
**TDD phase: RED**
# UI RED Tests (표)
# Logic RED Tests (표)
RED 설계 자체 검수 체크리스트
```

### Assistant
```text
**TDD phase: RED**

SSOT 확인: Report/02 실제 파일명 02_MagicSquare_4x4_TDD_design_report.md;
부록 G0~G3 미등재 → placeholder 격자 정책 명시.

# UI RED Tests — 9행
U-IN-01 null → E003
U-IN-02 size ≠ 4×4 → E001 (3×4, 4×3, 5×5, [])
U-IN-03a/b blank count 0/3 → E002
U-IN-04a/b -1, 17 → E004
U-IN-05 duplicate → E005
U-OUT-01 len 6
U-OUT-02 1-index [2,2,7,3,3,10] on G1
U-FLOW-02 execute call_count == 0

G1_placeholder 격자 literal 포함 (0-index blanks (1,1),(2,2), missing {7,10}).

# Logic RED Tests — 13행
D-LOC-01, D-MIS-01, D-VAL-01~06, D-SOL-01~04
I1~I11 매핑, Domain Mock 금지 (U-FLOW spy 예외)

체크리스트 6/6 충족.
PRD ERR_* vs E00x GREEN 시 매핑 필요 안내.
```

## Turn 02
### User
```text
@.cursor/rules/workflow-automation.mdc 보고서 작성
```

### Assistant
```text
workflow-automation 규칙 실행:
1. Report/09_MagicSquare_dual_track_fr01_fr05_red_design_report.md 작성
2. Prompt/09_MagicSquare_dual_track_fr01_fr05_red_design_prompt_transcript.md 작성
```
