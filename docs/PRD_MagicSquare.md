# PRD — Magic Square 4x4 TDD Practice

## 1. Executive Summary
Magic Square 4x4 TDD Practice는 정답 계산 프로젝트가 아니라 **불변식 기반 사고, 입력/출력 계약 고정, Dual-Track(Track A: Boundary 계약, Track B: Domain 불변식) TDD, 설계→테스트→구현→리팩토링 흐름**을 훈련하는 기준 문서다. 본 PRD는 구현 전에 기능 요구사항, 비기능 요구사항, 실패 정책, 계층 경계, 추적성(Concept→Rule→Use Case→Contract→Test→Component)을 고정해 변경 가능성과 검증 가능성을 동시에 보장한다.

## 2. Background
학습자는 문제를 "마방진 완성"으로만 받아들이는 경우가 많아 구현을 먼저 시작하고 검증 기준을 나중에 붙인다. 이 접근은 다음 문제를 만든다: 불변식 누락, 입력/출력 계약 불명확, Boundary/Domain 책임 혼합, 리팩토링 후 회귀 발생.
본 프로젝트는 4x4 마방진을 재료로 사용해 **조건의 형식화, 계약 기반 검증, 계층 분리, TDD 루프 운영**을 명시적으로 훈련한다.

## 3. Problem Statement
이 프로젝트의 문제는 "마방진을 만든다"가 아니다.
이 프로젝트의 문제는 **검증 가능한 불변식 집합을 만족하는 입력/처리/출력 계약을 완성하고 유지하는 것**이다.

- 입력 계약이 없으면 Boundary에서 실패를 차단할 수 없다.
- 출력 계약이 없으면 결과 형식 검증이 불가능하다.
- 불변식이 없으면 Domain 로직의 정당성을 판별할 수 없다.
- 따라서 본 PRD는 기능보다 먼저 계약과 불변식을 요구사항으로 고정한다.

## 4. Why Now / Why Chain
- 학습자는 구현부터 시작해 RED 단계를 생략한다.
- 테스트 문장이 계약과 분리되어 실패 원인이 추적되지 않는다.
- Boundary와 Domain 책임이 섞여 수정 범위가 확대된다.
- 리팩토링 후 외부 계약이 깨져 회귀가 발생한다.

**Why Chain**
1. 왜 지금 하는가: 구현 습관을 교정하고 검증 우선 습관을 정착해야 하기 때문이다.
2. 왜 이 문제인가: 4x4는 불변식이 명확하고 검증 단위가 분해 가능하기 때문이다.
3. 왜 Dual-Track인가: Boundary 계약 실패와 Domain 불변식 실패를 분리해야 원인 분석이 가능하기 때문이다.
4. 왜 PRD 선행인가: 구현 이전에 계약/규칙/검증을 고정해야 추적성과 리팩토링 안정성을 확보할 수 있기 때문이다.

## 5. Target Users
- TDD 학습자
- 코드 리뷰어
- Clean Architecture + ECB 훈련 개발자

사용 환경:
- 콘솔 실행 및 테스트 실행 중심
- UI/DB/Web 의존성 없는 로컬 개발 환경

## 6. Vision & Epic Goal
- **Epic Goal**: 불변식 기반 사고 훈련 시스템 구축
- 비전: 정답 중심 구현에서 계약/검증 중심 개발로 학습 기준을 전환한다.
- 성공 상태:
  - 모든 핵심 규칙이 Business Rule로 식별된다.
  - 모든 핵심 규칙이 Feature/AC/Test/Component로 추적된다.
  - Boundary와 Domain 책임이 분리된 상태로 유지된다.

## 7. Persona
- TDD를 학습 중인 개발자
- 계층 분리(ECB)를 실습하려는 개발자
- 알고리즘 정답보다 설계/계약/테스트/리팩토링 흐름을 훈련하려는 사용자

## 8. User Journey Summary

| Stage | Pain Point | Learning Outcome |
|---|---|---|
| Problem Recognition | 정답 구현에 집중해 규칙 정의를 생략함 | 문제를 불변식 집합으로 재정의한다 |
| Contract Definition | 입력/출력/오류 정책이 문장으로 고정되지 않음 | 계약 기반 검증 문장을 작성한다 |
| Domain Separation | Blank/Missing/Validator/Solver 책임이 섞임 | 책임 분해와 계층 경계를 유지한다 |
| Dual-Track TDD | UI/Boundary 실패와 Domain 실패가 혼재됨 | Track A/B를 분리해 RED 원인을 식별한다 |
| Regression Protection | 정상 케이스만 검증해 회귀를 놓침 | 예외/경계/조합 실패를 회귀 케이스로 고정한다 |

## 9. Scope

### 9.1 In-Scope
- 빈칸 좌표 탐색
- 누락 숫자 탐색
- 마방진 판정
- 두 조합 시도 후 결과 반환
- Boundary 입력 검증
- 출력 계약 검증
- RED-GREEN-REFACTOR 실행 가능 요구사항 정의

### 9.2 Out-of-Scope
- UI 화면 개발
- DB 저장/검색
- Web/API 서버 개발
- N×N 일반화
- 완전한 마방진 생성기 개발
- 사용자 인증/권한
- 네트워크 오류 처리
- QR 스캔
- 외부 서비스 연동

## 10. Functional Requirements

### FR-01 Input Verification
- Description: Boundary는 Domain 호출 전에 입력 계약 위반을 차단한다.
- Layer: Boundary (Track A)
- Input: `int[4][4]`
- Processing Rules:
  - 입력 크기는 4x4여야 한다.
  - 값은 `0` 또는 `1..16`이어야 한다.
  - `0` 개수는 정확히 2개여야 한다.
  - `0` 제외 중복은 허용되지 않는다.
- Output: 검증 성공 또는 표준 오류 응답
- Acceptance Criteria:
  - AC-FR01-01: 4x4가 아니면 오류 코드 `ERR_INVALID_DIMENSION` 반환
  - AC-FR01-02: 0 개수가 2가 아니면 `ERR_INVALID_BLANK_COUNT` 반환
  - AC-FR01-03: 범위 위반 값이 있으면 `ERR_OUT_OF_RANGE` 반환
  - AC-FR01-04: 0 제외 중복이 있으면 `ERR_DUPLICATE_VALUE` 반환
  - AC-FR01-05: 검증 실패 시 Domain resolver를 호출하지 않음
- Error / Exception Policy: 예외 throw 대신 표준 오류 응답 객체 반환
- Related Business Rules: BR-01, BR-02, BR-03, BR-04
- Related Test Direction: TC-BND-001~005
- Component Candidate: `BoundaryValidator`

### FR-02 Blank Coordinate Discovery
- Description: Domain은 빈칸 두 좌표를 row-major 기준으로 결정한다.
- Layer: Domain (Track B)
- Input: 검증 통과한 4x4 행렬
- Processing Rules:
  - 값 `0`인 셀만 빈칸으로 인정
  - row-major 스캔으로 첫 번째/두 번째 빈칸 결정
- Output: 빈칸 좌표 2개(내부 좌표 0-index)
- Acceptance Criteria:
  - AC-FR02-01: 빈칸 좌표를 정확히 2개 반환
  - AC-FR02-02: 반환 순서는 row-major 순서
  - AC-FR02-03: 첫 번째 빈칸은 스캔 시 첫 `0` 위치와 일치
- Error / Exception Policy: FR-01 선행 실패 시 실행되지 않음
- Related Business Rules: BR-05
- Related Test Direction: TC-DOM-BLK-001~003
- Component Candidate: `BlankFinder`

### FR-03 Missing Number Discovery
- Description: Domain은 1..16에서 누락된 두 숫자를 도출한다.
- Layer: Domain (Track B)
- Input: 검증 통과한 4x4 행렬
- Processing Rules:
  - `0`은 누락 숫자 계산에서 제외
  - 누락 숫자 2개를 오름차순으로 반환
- Output: `[small, large]`
- Acceptance Criteria:
  - AC-FR03-01: 누락 숫자 개수는 항상 2개
  - AC-FR03-02: 반환 순서는 오름차순
  - AC-FR03-03: 반환 숫자는 1..16 범위 내 값
- Error / Exception Policy: FR-01 선행 실패 시 실행되지 않음
- Related Business Rules: BR-06, BR-07
- Related Test Direction: TC-DOM-MISS-001~003
- Component Candidate: `MissingNumberFinder`

### FR-04 Magic Square Validation
- Description: Domain은 완성 행렬이 마방진 불변식을 만족하는지 판정한다.
- Layer: Domain (Track B)
- Input: 4x4 완성 행렬
- Processing Rules:
  - 마방진 상수는 34
  - 모든 행/열/양 대각선 합 검사
- Output: `valid=true/false`
- Acceptance Criteria:
  - AC-FR04-01: 모든 행 합이 34면 행 조건 통과
  - AC-FR04-02: 모든 열 합이 34면 열 조건 통과
  - AC-FR04-03: 양 대각선 합이 34면 대각선 조건 통과
  - AC-FR04-04: 모든 조건 통과 시에만 `valid=true`
- Error / Exception Policy: 위 조건 중 하나라도 실패 시 `valid=false`
- Related Business Rules: BR-08, BR-09
- Related Test Direction: TC-DOM-VAL-001~004
- Component Candidate: `MagicSquareValidator`

### FR-05 Two-Combination Solver and Result Formatting
- Description: Domain은 두 조합을 순서대로 시도하고 Boundary 계약 형식으로 결과를 반환한다.
- Layer: Domain + Boundary
- Input: 빈칸 좌표 2개, 누락 숫자 2개
- Processing Rules:
  - Attempt 1: small→first blank, large→second blank
  - Attempt 1 실패 시 Attempt 2: large→first blank, small→second blank
  - 성공 조합을 출력 형식으로 변환
- Output: `int[6]` `[r1,c1,n1,r2,c2,n2]` (1-index)
- Acceptance Criteria:
  - AC-FR05-01: Attempt 1 성공 시 Attempt 1 순서로 반환
  - AC-FR05-02: Attempt 1 실패 + Attempt 2 성공 시 Attempt 2 순서로 반환
  - AC-FR05-03: 반환 배열 길이는 6
  - AC-FR05-04: 좌표는 1-index
  - AC-FR05-05: 두 조합 모두 실패 시 `ERR_NO_VALID_COMBINATION` 반환
- Error / Exception Policy: 실패 시 표준 오류 응답(`ERR_NO_VALID_COMBINATION`)
- Related Business Rules: BR-10, BR-11, BR-12, BR-13
- Related Test Direction: TC-DOM-SOL-001~003, TC-BND-OUT-001~002
- Component Candidate: `Solver`, `ResultFormatter`

## 11. Business Rules / Domain Rules
- BR-01: 입력 행렬은 정확히 4행 4열이어야 한다.
- BR-02: 입력에서 값 `0`은 정확히 2개여야 한다.
- BR-03: 각 셀 값은 `0` 또는 `1..16`이어야 한다.
- BR-04: `0`을 제외한 숫자는 중복될 수 없다.
- BR-05: 첫 번째 빈칸은 row-major 스캔에서 처음 발견된 `0`이다.
- BR-06: 누락 숫자는 정확히 2개여야 한다.
- BR-07: 누락 숫자 반환 순서는 오름차순이어야 한다.
- BR-08: 마방진 상수는 34여야 한다.
- BR-09: 모든 행/열/양 대각선 합은 34여야 한다.
- BR-10: Solver는 small-first를 첫 시도로 사용해야 한다.
- BR-11: small-first 실패 시 reverse 조합을 두 번째 시도로 사용해야 한다.
- BR-12: 결과 좌표는 1-index 규칙을 따라야 한다.
- BR-13: 최종 성공 결과는 길이 6의 `int[6]` 형식이어야 한다.

## 12. Input / Output Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code 또는 Failure Policy |
|---|---|---|---|---|---|
| Input Matrix | `int[4][4]` | 4x4 고정 | 4행 4열 정수 행렬 | 3x4, 4x5 | `ERR_INVALID_DIMENSION` |
| Blank Count | integer count | `0` 개수=2 | `0`이 2개 | `0`이 1개/3개 | `ERR_INVALID_BLANK_COUNT` |
| Value Range | int | 값은 `0` 또는 `1..16` | `0,1,16` | `-1,17` | `ERR_OUT_OF_RANGE` |
| Uniqueness | set rule | `0` 제외 중복 금지 | `1..16` 중복 없음 | `8`이 두 번 등장 | `ERR_DUPLICATE_VALUE` |
| Blank Order | coordinate rule | 첫 빈칸=row-major 첫 `0` | 스캔 첫 위치 사용 | 임의 순서 사용 | `ERR_INVALID_BLANK_ORDER` |
| Output Result | `int[6]` | `[r1,c1,n1,r2,c2,n2]` | 길이 6 정수 배열 | 길이 5/7, 타입 불일치 | `ERR_INVALID_OUTPUT_FORMAT` |
| Output Coordinate | int | 좌표는 1-index | `r1=1,c1=1` | `r1=0,c1=0` | `ERR_INVALID_OUTPUT_COORDINATE` |
| Solve Result | success/failure | 두 시도 모두 실패 시 명시적 실패 반환 | 성공 배열 반환 | 실패를 미정 상태로 반환 | `ERR_NO_VALID_COMBINATION` |

## 13. Error / Failure Policy

| Error Code | Message | Layer | Domain resolver 호출 여부 | Related Acceptance Criteria |
|---|---|---|---|---|
| `ERR_INVALID_DIMENSION` | Input matrix must be 4x4. | Boundary | 호출 금지 | AC-FR01-01 |
| `ERR_INVALID_BLANK_COUNT` | Blank count must be exactly 2. | Boundary | 호출 금지 | AC-FR01-02 |
| `ERR_OUT_OF_RANGE` | Values must be 0 or 1..16. | Boundary | 호출 금지 | AC-FR01-03 |
| `ERR_DUPLICATE_VALUE` | Non-zero values must be unique. | Boundary | 호출 금지 | AC-FR01-04 |
| `ERR_NO_VALID_COMBINATION` | Both solve attempts failed to satisfy magic square invariants. | Domain/Boundary response | 호출 완료 후 실패 반환 | AC-FR05-05 |
| `ERR_INVALID_OUTPUT_FORMAT` | Output must be int[6] format. | Boundary | 호출 금지(출력 검증 실패) | AC-FR05-03 |
| `ERR_INVALID_OUTPUT_COORDINATE` | Output coordinates must be 1-index. | Boundary | 호출 금지(출력 검증 실패) | AC-FR05-04 |

정책 고정:
- 입력 검증 실패는 **반드시 Boundary에서 종료**한다.
- 입력 검증 실패 시 Domain resolver는 **반드시 미호출**이어야 한다.
- 실패는 예외 throw 대신 **표준 오류 응답**으로 반환한다.

## 14. Non-Functional Requirements
- NFR-01 Coverage:
  - Domain Logic coverage는 95% 이상이어야 한다.
  - Boundary Validation coverage는 85% 이상이어야 한다.
- NFR-02 Deterministic Execution:
  - 같은 입력은 항상 같은 출력 또는 같은 오류 코드를 반환해야 한다.
- NFR-03 Side Effect Policy:
  - 입력 행렬은 처리 전후 동일해야 한다(입력 불변).
- NFR-04 Performance:
  - 4x4 단일 실행은 50ms 이내여야 한다(로컬 표준 개발환경 기준).
- NFR-05 Maintainability:
  - Boundary/Domain 책임은 분리되어야 한다.
  - 정답 하드코딩은 금지한다.
  - 설명 없는 매직 넘버는 금지한다.
  - 명명된 상수(`GRID_SIZE`, `MAX_VALUE`, `MAGIC_CONSTANT`)를 사용해야 한다.

## 15. Dual-Track TDD Strategy

### 15.1 Track A — Boundary / UI Contract TDD
- 입력 검증 테스트
- 출력 형식 테스트
- 실패 응답 테스트
- Domain resolver 미호출 테스트

### 15.2 Track B — Domain / Logic TDD
- 빈칸 탐색 테스트
- 누락 숫자 탐색 테스트
- 마방진 검증 테스트
- small-first 성공 테스트
- small-first 실패 후 reverse 성공 테스트
- 두 조합 모두 실패 테스트

### 15.3 Parallel Progression Rules
- UI RED와 Logic RED를 분리한다.
- UI GREEN과 Logic GREEN은 각각 최소 구현으로 통과시킨다.
- 구조 개선은 REFACTOR 단계에서만 수행한다.
- Domain 전체를 먼저 구현하고 Boundary를 나중에 붙이는 방식은 금지한다.
- 테스트 약화/삭제로 통과시키는 행위는 금지한다.

## 16. Test Plan / QA

### 16.1 Normal Scenarios
- small-first 성공
- small-first 실패 후 reverse 성공

### 16.2 Exception Scenarios
- 4x4가 아닌 입력
- 빈칸 개수 오류
- 값 범위 오류
- 중복 숫자 오류
- 두 조합 모두 실패

### 16.3 Boundary Scenarios
- 값 1 처리
- 값 16 처리
- `0`은 빈칸으로만 처리
- 출력 좌표 1-index 검증
- 반환 배열 길이 6 검증

### 16.4 Representative Test Data
- small-first 성공 입력 행렬
- reverse 성공 입력 행렬
- invalid size 행렬
- invalid blank count 행렬
- duplicate value 행렬
- invalid range 행렬

## 17. Architecture Overview, High-Level
- Boundary Layer:
  - 입력 검증 수행
  - 오류 응답 반환
  - 출력 포맷 검증/변환 수행
- Domain Layer:
  - 빈칸 탐색, 누락 숫자 탐색, 마방진 판정, 조합 시도
  - 불변식 검증의 단일 책임 유지
- Control/Application Layer:
  - Boundary→Domain 호출 순서 조정
  - Track A/B 실행 흐름 연결

의존 방향:
- Boundary → Control → Domain
- Domain은 Boundary를 참조하지 않는다.
- Domain은 UI/DB/Web/파일 시스템에 의존하지 않는다.

## 18. Component Candidates

| Component | Responsibility | Layer | Input | Output | Related FR | Related Test |
|---|---|---|---|---|---|---|
| `BoundaryValidator` | 입력 계약 검증, Domain 미호출 보장 | Boundary | `int[4][4]` | valid/error | FR-01 | TC-BND-001~005 |
| `BlankFinder` | row-major 기준 빈칸 2개 좌표 추출 | Domain | validated matrix | 2 coordinates | FR-02 | TC-DOM-BLK-001~003 |
| `MissingNumberFinder` | 누락 숫자 2개 오름차순 추출 | Domain | validated matrix | `[small,large]` | FR-03 | TC-DOM-MISS-001~003 |
| `MagicSquareValidator` | 행/열/대각선 합 34 판정 | Domain | completed matrix | `valid=true/false` | FR-04 | TC-DOM-VAL-001~004 |
| `Solver` | small-first/reverse 조합 시도 | Domain | blanks + missing nums | success/failure | FR-05 | TC-DOM-SOL-001~003 |
| `ResultFormatter` | 1-index `int[6]` 형식 변환 | Boundary/Control | solved assignment | `[r1,c1,n1,r2,c2,n2]` | FR-05 | TC-BND-OUT-001~002 |

## 19. Risks & Ambiguities

| Risk | Impact | Decision / Mitigation |
|---|---|---|
| 0-index/1-index 혼동 | 출력 좌표 오류 | BR-12 고정, 출력 계약 테스트 필수 |
| row-major 첫 빈칸 정의 누락 | 조합 순서 불일치 | BR-05 고정, BlankFinder AC로 검증 |
| small-first/reverse 데이터 혼동 | 잘못된 시도 순서 통과 | FR-05 AC-FR05-01/02 분리 검증 |
| 입력 행렬 변경 여부 불명확 | 사이드이펙트 회귀 발생 | NFR-03 입력 불변 정책 고정 |
| 두 조합 실패 정책 누락 | 호출자 처리 분기 불가 | `ERR_NO_VALID_COMBINATION` 고정 |
| 상수 34 하드코딩 난립 | 유지보수성 저하 | `MAGIC_CONSTANT` 상수 사용 강제 |
| Boundary/Domain 책임 혼합 | 테스트 원인 분리 실패 | Track A/B 분리 규칙 강제 |

## 20. Engineering Principles
- PEP8 준수
- 모든 함수 파라미터/반환값에 type hints 적용
- `pytest` 사용
- AAA 패턴 준수
- Coverage 목표 준수(Domain 95%+, Boundary 85%+)
- ECB 계층 분리 준수
- RED-GREEN-REFACTOR 순서 준수
- `print()` 디버깅 금지
- bare `except` 금지
- 테스트 약화/삭제 금지
- 설명 없는 매직 넘버 금지

## 21. Traceability Matrix

| Concept / Invariant | Business Rule | Feature ID | Acceptance Criteria | Test Case Candidate | Component |
|---|---|---|---|---|---|
| 4x4 입력 | BR-01 | FR-01 | AC-FR01-01 | TC-BND-001 | BoundaryValidator |
| 빈칸 2개 | BR-02 | FR-01 | AC-FR01-02 | TC-BND-002 | BoundaryValidator |
| 값 범위 0 또는 1~16 | BR-03 | FR-01 | AC-FR01-03 | TC-BND-003 | BoundaryValidator |
| 중복 금지 | BR-04 | FR-01 | AC-FR01-04 | TC-BND-004 | BoundaryValidator |
| row-major 첫 번째 빈칸 | BR-05 | FR-02 | AC-FR02-02,03 | TC-DOM-BLK-001 | BlankFinder |
| 누락 숫자 2개 | BR-06 | FR-03 | AC-FR03-01 | TC-DOM-MISS-001 | MissingNumberFinder |
| 누락 숫자 오름차순 | BR-07 | FR-03 | AC-FR03-02 | TC-DOM-MISS-002 | MissingNumberFinder |
| 마방진 상수 34 | BR-08 | FR-04 | AC-FR04-01~03 | TC-DOM-VAL-001~003 | MagicSquareValidator |
| 행/열/대각선 합 | BR-09 | FR-04 | AC-FR04-04 | TC-DOM-VAL-004 | MagicSquareValidator |
| small-first 시도 | BR-10 | FR-05 | AC-FR05-01 | TC-DOM-SOL-001 | Solver |
| reverse 시도 | BR-11 | FR-05 | AC-FR05-02 | TC-DOM-SOL-002 | Solver |
| int[6] 반환 | BR-13 | FR-05 | AC-FR05-03 | TC-BND-OUT-001 | ResultFormatter |
| 1-index 좌표 | BR-12 | FR-05 | AC-FR05-04 | TC-BND-OUT-002 | ResultFormatter |

## 22. Open Questions / Decision Needed
1. **Decision Needed**: 성능 기준 `50ms`의 측정 환경 정의
   - CPU/OS/파이썬 버전 기준을 PRD 부록에 고정해야 한다.
2. **Decision Needed**: 보고서 참조명과 실제 파일명 정합
   - 요청의 `Report/4.UserJourney...`는 실제 저장소에서 `Report/06_MagicSquare_user_journey_story_scenario_verification_report.md`를 우선 출처로 사용한다.
3. **Decision Needed**: 커버리지 기준 이중 정책 정리
   - 규칙 파일 최소 기준(80%+)과 본 PRD 목표(95%/85%)를 "최소 기준 vs 프로젝트 목표"로 확정 문구화해야 한다.

## 23. Appendix

### A. 참고 문서 목록 (실제 파일명 기준)
- `Report/01_MagicSquare_problem_definition_report.md`
- `Report/02_MagicSquare_4x4_TDD_design_report.md`
- `Report/03_MagicSquare_cursor_rules_and_user_entity_report.md`
- `Report/04_MagicSquare_cursor_rules_restructure_report.md`
- `Report/06_MagicSquare_user_journey_story_scenario_verification_report.md`
- `.cursorrules`
- `.cursor/rules/magicsquare-project.mdc`
- `.cursor/rules/magicsquare-ecb-architecture.mdc`
- `.cursor/rules/magicsquare-tdd-testing.mdc`
- `.cursor/rules/magicsquare-python-code-style.mdc`
- `.cursor/rules/magicsquare-forbidden.mdc`
- `.cursor/rules/workflow-automation.mdc`

### B. Cursor Rules 요약
- 계층 분리(ECB)와 의존 방향 준수
- RED→GREEN→REFACTOR 단계 강제
- pytest AAA 및 커버리지 기준 유지
- 금지 패턴(`print`, bare except, 테스트 약화) 차단
- 규칙 원문 소스는 `.cursor/rules/*.mdc`

### C. 대표 Gherkin Scenario 요약
- Scenario-N1: small-first 조합 성공
- Scenario-N2: small-first 실패 후 reverse 성공
- Scenario-E1: 입력 크기 오류 시 Boundary 차단
- Scenario-E2: 빈칸 개수 오류 시 Boundary 차단
- Scenario-E3: 범위/중복 오류 시 Boundary 차단
- Scenario-E4: 두 조합 실패 시 `ERR_NO_VALID_COMBINATION` 반환

### D. 향후 RED Test ID 후보
- Track A: `RED-BND-VAL-001..005`, `RED-BND-OUT-001..002`
- Track B: `RED-DOM-BLK-001..003`, `RED-DOM-MISS-001..003`, `RED-DOM-VAL-001..004`, `RED-DOM-SOL-001..003`
