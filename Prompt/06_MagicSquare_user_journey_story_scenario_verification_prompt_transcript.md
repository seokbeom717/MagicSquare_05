# MagicSquare User Journey/Story/Scenario Verification Prompt Transcript

## Turn 01
### User
```text
Magic Square 프로젝트의 User Journey를 다음 구조로 만들고 싶습니다.

Epic → User Story → Task

지금은 Level 1: Epic, 즉 Business Goal만 작성합니다.

중요:
- 구현 코드를 작성하지 마십시오.
- 테스트 코드를 작성하지 마십시오.
- 파일을 생성하지 마십시오.
- 아직 User Story나 Task로 세분화하지 마십시오.
- 오직 Epic 수준의 비즈니스 목표와 학습 목표만 정의하십시오.

프로젝트:
Magic Square 4x4 TDD Practice

Epic:
“불변식 기반 사고 훈련 시스템 구축”

목적:
4x4 Magic Square 문제를 사용하여 다음을 훈련합니다.

- 불변식 중심 설계 사고
- Dual-Track UI + Logic TDD 적용
- 입력/출력 계약 명확화
- 설계 → 테스트 → 구현 → 리팩토링 흐름
- Concept → Invariant → Contract → Test 추적성

성공 기준:
- Domain Logic 테스트 커버리지 95% 이상
- Boundary 입력 검증 계약 테스트 100% 통과
- 설명 없는 매직 넘버 금지
- GRID_SIZE, MAX_VALUE, MAGIC_CONSTANT 같은 명명된 상수 사용
- 정답 하드코딩 금지
- 주요 Invariant는 최소 하나 이상의 테스트와 추적 가능해야 함
- 리팩토링 후에도 외부 입력/출력 계약은 변경되지 않아야 함

출력 형식:

# Level 1: Epic — Business Goal

## 1. Epic Title
## 2. Business Goal
## 3. Learning Goal
## 4. Problem Statement
## 5. Target Learners / Users
## 6. Scope
## 7. Non-Scope
## 8. Success Criteria
## 9. Key Invariants
## 10. Traceability Rule
## 11. Candidate User Stories for Level 2

주의:
- Epic 수준에서만 작성하십시오.
- 아직 세부 Task로 나누지 마십시오.
- 코드나 테스트 코드는 작성하지 마십시오.
- 다음 단계인 Level 2 User Story를 도출할 수 있도록 정리하십시오.
```

### AI
```text
# Level 1: Epic — Business Goal

## 1. Epic Title
**불변식 기반 사고 훈련 시스템 구축**  
(Magic Square 4x4 TDD Practice)

## 2. Business Goal
4x4 Magic Square 문제를 학습용 도메인으로 삼아, **정답 맞추기 중심 개발이 아닌 불변식 중심 설계·검증 방식**을 팀/학습자가 일관되게 적용할 수 있는 훈련 체계를 확립한다.  
핵심 목표는 “작동하는 코드”보다 “설명 가능한 설계 근거와 검증 가능성”을 우선하는 개발 습관을 정착시키는 것이다.

## 3. Learning Goal
학습자는 다음 역량을 실제 사이클로 습득한다.

- 불변식 중심 설계 사고(문제 제약을 설계의 출발점으로 정의)
- Dual-Track UI + Logic TDD 적용(도메인 규칙과 경계 계약을 분리 검증)
- 입력/출력 계약 명확화(허용/거부 조건을 테스트 가능 형태로 명세)
- 설계 → 테스트 → 구현 → 리팩토링 흐름의 반복 숙련
- Concept → Invariant → Contract → Test 추적성 유지 능력

## 4. Problem Statement
기존 학습/구현 방식은 다음 리스크를 가진다.

- 결과(정답) 중심 구현으로 인해 설계 근거가 약함
- 하드코딩/매직 넘버 사용으로 일반화와 유지보수성 저하
- 입력 검증, 오류 처리, 외부 계약의 명세 부족
- 리팩토링 시 동작 보존 기준이 불명확
- “왜 이 테스트가 필요한가”에 대한 추적성이 부족

이 Epic은 위 문제를 해결하기 위해, **불변식과 계약을 중심으로 설계-검증 체계**를 만든다.

## 5. Target Learners / Users
- TDD 입문~중급 개발자
- ECB/계층 분리 설계를 실습하려는 학습자
- 도메인 규칙을 테스트로 표현하는 역량을 강화하려는 팀
- 리팩토링 안정성을 높이고 싶은 실무 개발자

## 6. Scope
이 Epic에서 다루는 범위:

- 4x4 Magic Square 도메인 규칙을 불변식으로 정의
- 도메인 로직과 Boundary 계약을 구분한 검증 기준 수립
- 명명된 상수 기반 표현 원칙 수립 (`GRID_SIZE`, `MAX_VALUE`, `MAGIC_CONSTANT` 등)
- 정답 하드코딩 금지 원칙 수립
- 리팩토링 전/후 외부 I/O 계약 동일성 유지 원칙 수립
- 불변식 ↔ 테스트 간 추적 가능성 기준 수립

## 7. Non-Scope
이 Epic에서 **아직 하지 않는 것**:

- 구현 코드 작성
- 테스트 코드 작성
- 세부 Task 분해
- UI 상세 플로우/화면 설계 확정
- 인프라/배포/운영 자동화 설계
- 성능 최적화 세부 전략 수립

## 8. Success Criteria
Epic 성공 판단 기준:

- Domain Logic 테스트 커버리지 **95% 이상**
- Boundary 입력 검증 계약 테스트 **100% 통과**
- 설명 없는 매직 넘버 **0건**
- `GRID_SIZE`, `MAX_VALUE`, `MAGIC_CONSTANT` 등 **명명된 상수 사용 준수**
- 정답 하드코딩 **금지 준수**
- 주요 Invariant 각각이 **최소 1개 이상 테스트와 연결**
- 리팩토링 이후에도 외부 입력/출력 계약 **비변경 유지**

## 9. Key Invariants
Epic 레벨 핵심 불변식(도메인 + 품질 관점):

- **구조 불변식**: 격자는 항상 4x4 구조를 유지한다.
- **값 범위 불변식**: 사용 가능한 값은 정의된 범위를 벗어나지 않는다.
- **유일성 불변식**: 각 값은 규칙에 따라 중복 없이 사용된다.
- **합 불변식**: 각 행/열/대각선의 합은 `MAGIC_CONSTANT`와 일치해야 한다.
- **계약 불변식**: 유효하지 않은 입력은 명시된 방식으로 거부되어야 한다.
- **표현 불변식**: 핵심 숫자는 매직 넘버가 아닌 명명된 상수로 표현된다.
- **진화 불변식**: 내부 리팩토링은 허용하되 외부 I/O 계약은 변하지 않는다.

## 10. Traceability Rule
모든 학습/검증 산출물은 아래 체인을 반드시 따른다.

**Concept → Invariant → Contract → Test**

운영 규칙:

- 각 Concept는 1개 이상 Invariant에 매핑된다.
- 각 Invariant는 1개 이상 Contract 조항으로 구체화된다.
- 각 Contract 조항은 1개 이상 Test 케이스로 검증된다.
- 역추적(실패한 Test → 어떤 Contract/Invariant/Concept 위반인지) 가능해야 한다.
- “검증되지 않은 Invariant”와 “근거 없는 Test”는 허용하지 않는다.

## 11. Candidate User Stories for Level 2
다음 단계(Level 2)로 확장 가능한 후보 User Story(제목 수준):

- 학습자로서, 4x4 Magic Square의 핵심 Concept와 Invariant를 명시적으로 정의하고 싶다.
- 학습자로서, 각 Invariant를 입력/출력 계약 형태로 변환하고 싶다.
- 학습자로서, Domain Logic 규칙을 TDD로 검증 가능한 단위로 분해하고 싶다.
- 학습자로서, Boundary 입력 검증 규칙을 정상/오류 케이스로 구분해 명세하고 싶다.
- 학습자로서, 매직 넘버를 제거하고 명명된 상수 정책을 일관되게 적용하고 싶다.
- 학습자로서, 하드코딩 없이 규칙 기반으로 정답 성립 여부를 판정하고 싶다.
- 학습자로서, 리팩토링 전후 외부 계약 동일성을 검증하고 싶다.
- 학습자로서, Test 실패 시 어느 Invariant가 깨졌는지 추적 가능한 구조를 갖추고 싶다.
```

## Turn 02
### User
```text
Magic Square 프로젝트의 User Journey를 다음 구조로 작성해 주세요.

현재 단계:
Level 2: User Journey

상위 Epic:
“불변식 기반 사고 훈련 시스템 구축”

중요:
- 구현 코드를 작성하지 마십시오.
- 테스트 코드를 작성하지 마십시오.
- 파일을 생성하지 마십시오.
- 아직 Task 수준으로 세분화하지 마십시오.
- 오직 User Journey 수준에서 작성하십시오.
- 이 User Journey는 다음 단계인 User Story와 Task로 분해될 수 있어야 합니다.

프로젝트:
Magic Square 4x4 TDD Practice

Persona:
- TDD를 학습 중인 소프트웨어 개발 학습자
- Clean Architecture의 계층 분리를 이해하려는 학습자
- 알고리즘 정답보다 설계, 계약, 테스트, 리팩토링 흐름을 훈련하려는 학습자

Journey Goal:
- 4x4 Magic Square 문제를 통해 불변식 중심 사고를 훈련한다.
- 입력/출력 계약을 먼저 정의한다.
- Domain Logic과 UI/Boundary 책임을 분리한다.
- Dual-Track UI + Logic TDD 흐름을 경험한다.
- 설계 → 테스트 → 구현 → 리팩토링 → 회귀 보호 흐름을 학습한다.

MagicSquare 기본 규칙:
- 입력은 4x4 int 행렬이다.
- 0은 빈칸을 의미한다.
- 빈칸은 정확히 2개여야 한다.
- 값의 범위는 0 또는 1~16이다.
- 0을 제외한 숫자는 중복될 수 없다.
- 출력은 int[6]이다.
- 좌표는 1-index 기준이다.
- 출력 형식은 [r1, c1, n1, r2, c2, n2]이다.
- 4x4 마방진 상수는 34이다.
- 먼저 작은 누락 숫자를 첫 번째 빈칸에, 큰 누락 숫자를 두 번째 빈칸에 넣어 시도한다.
- 실패하면 반대 조합을 시도한다.

User Journey는 다음 5단계로 작성하십시오.

## Stage 1: Problem Recognition
목적:
학습자가 이 과제를 단순한 “마방진 구현 문제”가 아니라 “불변식 기반 설계 훈련 문제”로 인식한다.

포함할 내용:
- Action
- Thinking
- Emotion
- Pain Point
- Opportunity
- Related Invariant
- Expected Learning Outcome

## Stage 2: Contract Definition
목적:
입력 스키마, 출력 스키마, 오류 정책을 먼저 정의한다.

포함할 내용:
- Action
- Thinking
- Emotion
- Pain Point
- Opportunity
- Input Contract
- Output Contract
- Error Contract
- Expected Learning Outcome

## Stage 3: Domain Separation
목적:
마방진 문제를 작은 책임 단위로 분리한다.

포함할 도메인 후보:
- BlankFinder
- MissingNumberFinder
- MagicSquareValidator
- Solver

포함할 내용:
- Action
- Thinking
- Emotion
- Pain Point
- Opportunity
- Responsibility Separation
- Related Invariant
- Expected Learning Outcome

## Stage 4: Dual-Track TDD Progress
목적:
UI/Boundary RED와 Logic/Domain RED를 분리하여 진행한다.

포함할 내용:
- Action
- Thinking
- Emotion
- Pain Point
- Opportunity
- UI RED Focus
- Logic RED Focus
- GREEN Minimal Implementation Principle
- REFACTOR Principle
- Expected Learning Outcome

## Stage 5: Regression Protection
목적:
정상 케이스뿐 아니라 오류 케이스와 조합 실패 케이스를 추가하여 회귀를 방지한다.

포함할 회귀 보호 대상:
- Edge case
- Input error case
- Combination failure case
- Output format case

포함할 내용:
- Action
- Thinking
- Emotion
- Pain Point
- Opportunity
- Regression Test Target
- Protected Contract or Invariant
- Expected Learning Outcome

출력 형식:

# Level 2: User Journey — Magic Square 4x4

## 1. Persona

## 2. Journey Goal

## 3. Journey Overview

| Stage | User Action | Thinking | Pain Point | Opportunity | Learning Outcome |
|---|---|---|---|---|---|

## 4. Detailed Journey

### Stage 1: Problem Recognition
...

## 5. Journey to User Story Mapping

| Journey Stage | Candidate User Story | Acceptance Criteria Direction |
|---|---|---|

## 6. Traceability Link

| Epic Goal | Journey Stage | Invariant / Contract | Future Test Target |
|---|---|---|---|
```

### AI
```text
# Level 2: User Journey — Magic Square 4x4

## 1. Persona
- TDD를 학습 중인 소프트웨어 개발 학습자
- Clean Architecture의 계층 분리를 이해하려는 학습자
- 알고리즘 정답 자체보다 설계·계약·테스트·리팩토링 흐름을 훈련하려는 학습자

## 2. Journey Goal
- 4x4 Magic Square 문제를 통해 불변식 중심 사고를 훈련한다.
- 입력/출력 계약을 구현 이전에 명확히 정의한다.
- Domain Logic과 UI/Boundary 책임을 분리한다.
- Dual-Track UI + Logic TDD 흐름을 단계적으로 경험한다.
- 설계 → 검증 기준 정의 → 최소 구현 → 리팩토링 → 회귀 보호의 학습 루프를 체득한다.

## 3. Journey Overview
| Stage | User Action | Thinking | Pain Point | Opportunity | Learning Outcome |
|---|---|---|---|---|---|
| Stage 1 Problem Recognition | 문제를 규칙/불변식 단위로 재해석 | “정답 찾기보다 규칙 보존이 핵심” | 구현 충동으로 설계 생략 | 불변식 중심 사고로 전환 | 문제를 제약 기반으로 구조화 |
| Stage 2 Contract Definition | 입력/출력/오류 계약을 먼저 명세 | “계약이 먼저면 테스트 기준이 선다” | 예외 정책 모호성 | 계약 기반 검증 축 형성 | 테스트 가능한 명세 작성 습득 |
| Stage 3 Domain Separation | 책임을 도메인 컴포넌트로 분리 | “어떤 규칙을 누가 보장하는가?” | 관심사 혼재 | 변경 영향 최소화 구조 확보 | 경계/도메인 분리 설계 이해 |
| Stage 4 Dual-Track TDD Progress | UI RED와 Logic RED를 분리 진행 | “외부 계약과 내부 규칙을 분리 검증” | RED 범위 혼동 | 실패 원인 분리 가능 | 최소 GREEN·안전한 REFACTOR 습관 |
| Stage 5 Regression Protection | 정상/오류/조합실패/출력형식 회귀 보호 설계 | “리팩토링 후도 계약은 유지돼야 함” | 정상 케이스 편중 | 회귀 방지망 강화 | 계약·불변식 기반 안정성 사고 |

## 4. Detailed Journey
### Stage 1: Problem Recognition
- Action: 문제 설명을 읽고 핵심 제약(4x4, 빈칸 2개, 값 범위, 중복 금지, 합 34, 출력 포맷)을 불변식 후보로 추출한다.
- Thinking: “이 문제의 본질은 계산 알고리즘보다 규칙을 깨지 않는 설계다.”
- Emotion: 초반에는 막연함이 있으나, 불변식으로 분해하면서 명확성이 증가한다.
- Pain Point: 바로 구현하려는 습관 때문에 규칙 간 우선순위와 경계가 흐려진다.
- Opportunity: 불변식을 먼저 선언하면 이후 계약/검증/리팩토링의 기준점이 생긴다.
- Related Invariant:
  - 입력은 4x4 정수 행렬이어야 한다.
  - 빈칸(0)은 정확히 2개여야 한다.
  - 0 또는 1~16 범위를 벗어나는 값은 허용되지 않는다.
  - 0 제외 숫자 중복은 허용되지 않는다.
  - 유효 해는 마방진 상수 34를 만족해야 한다.
- Expected Learning Outcome: 문제를 “정답 생성”이 아니라 “불변식 보존 시스템”으로 정의하는 관점을 습득한다.

### Stage 2: Contract Definition
- Action: 입력 스키마, 출력 스키마, 오류 정책을 구현 전에 문서화 가능한 계약으로 정리한다.
- Thinking: “계약이 선행되면 RED의 실패 조건이 명확해진다.”
- Emotion: 불확실성이 줄고, 검증 가능성에 대한 자신감이 생긴다.
- Pain Point: 오류 유형(형식 오류 vs 규칙 위반 vs 해 조합 실패)을 혼동하기 쉽다.
- Opportunity: 오류를 계약 단위로 분리하면 사용자 피드백과 경계 검증이 안정화된다.
- Input Contract:
  - 타입: int[4][4]
  - 값 규칙: 각 셀은 0 또는 1~16
  - 구조 규칙: 0의 개수는 정확히 2
  - 유일성 규칙: 0 제외 중복 금지
- Output Contract:
  - 타입/길이: int[6]
  - 좌표 기준: 1-index
  - 형식: [r1, c1, n1, r2, c2, n2]
  - 배치 규칙: 작은 누락 수를 첫 빈칸, 큰 누락 수를 두 번째 빈칸 우선 시도
- Error Contract:
  - 입력 형식 위반 시: 입력 오류로 처리
  - 규칙 위반 입력 시: 도메인 유효성 오류로 처리
  - 우선/대체 조합 모두 실패 시: 해 없음(조합 실패)으로 처리
- Expected Learning Outcome: 구현 전 단계에서 테스트 가능한 계약(입력/출력/오류)을 분리 정의하는 능력을 습득한다.

### Stage 3: Domain Separation
- Action: 도메인 책임을 BlankFinder, MissingNumberFinder, MagicSquareValidator, Solver로 분해한다.
- Thinking: “각 컴포넌트는 하나의 불변식 책임만 가져야 유지보수 가능하다.”
- Emotion: 복잡도가 통제 가능한 단위로 나뉘며 부담이 감소한다.
- Pain Point: Solver에 검증·탐색·판정 책임이 과도하게 집중되기 쉽다.
- Opportunity: 책임 분리로 변경 영향 범위를 국소화하고 추적성을 높인다.
- Responsibility Separation:
  - BlankFinder: 0의 위치 2개 식별 책임
  - MissingNumberFinder: 누락 숫자 2개 도출 책임
  - MagicSquareValidator: 행/열/대각선 합 34 만족 여부 판정 책임
  - Solver: 우선 조합/대체 조합 적용 및 최종 출력 형식 조립 책임
- Related Invariant:
  - 빈칸 개수 불변식은 BlankFinder가 보장
  - 누락 숫자·중복 불변식은 MissingNumberFinder가 보장
  - 합 불변식은 MagicSquareValidator가 보장
  - 출력 형식·좌표 불변식은 Solver가 최종 보장
- Expected Learning Outcome: 도메인 규칙을 책임 단위로 분해해 계약 위반 지점을 빠르게 식별하는 설계 역량을 익힌다.

### Stage 4: Dual-Track TDD Progress
- Action: UI/Boundary RED와 Logic/Domain RED를 분리하여 실패 원인을 독립적으로 관찰한다.
- Thinking: “외부 계약 실패와 내부 규칙 실패를 분리해야 학습 피드백이 선명해진다.”
- Emotion: 초기에는 두 트랙 동기화가 어렵지만, 분리 기준이 생기면 안정된다.
- Pain Point: 하나의 실패에 여러 원인이 섞여 디버깅 방향이 흔들린다.
- Opportunity: 트랙 분리로 수정 범위를 최소화하고 학습 루프를 짧게 만든다.
- UI RED Focus:
  - 입력 구조/범위/빈칸 수/중복 검증 실패를 계약 위반으로 명시
  - 출력 길이/좌표 인덱스/순서 형식 불일치 검출
- Logic RED Focus:
  - 누락 숫자 계산 및 조합 적용 규칙 실패 검출
  - 합 34 검증 실패 및 조합 대체 규칙 실패 검출
- GREEN Minimal Implementation Principle:
  - 현재 RED를 통과하는 최소 책임만 충족
  - 불변식/계약 외 동작 확장 금지
  - 하드코딩 정답/설명 없는 매직 넘버 금지
- REFACTOR Principle:
  - 외부 입력/출력 계약 불변
  - 내부 중복 제거 및 책임 재배치 우선
  - 리팩토링 후에도 불변식 추적 링크 유지
- Expected Learning Outcome: RED-GREEN-REFACTOR를 “기능 추가”가 아닌 “계약 보존” 중심으로 운영하는 습관을 체득한다.

### Stage 5: Regression Protection
- Action: 정상 케이스 외에 경계/오류/조합 실패/출력 형식 영역을 회귀 보호 대상으로 체계화한다.
- Thinking: “성공 케이스만으로는 계약 안정성을 보장할 수 없다.”
- Emotion: 초기에는 테스트 범위 증가 부담이 있으나, 이후 변경 안정성으로 신뢰가 증가한다.
- Pain Point: 자주 성공하는 경로만 검증하면 리팩토링 시 숨은 결함이 재발한다.
- Opportunity: 실패 시나리오 중심 회귀 보호로 계약 신뢰도를 높일 수 있다.
- Regression Test Target:
  - Edge case: 값 범위 경계(0, 1, 16), 빈칸 위치 다양성
  - Input error case: 타입/크기/빈칸 개수/중복 위반
  - Combination failure case: 우선 조합 실패 후 대체 조합 검증, 최종 실패 처리
  - Output format case: int[6], 1-index 좌표, [r1,c1,n1,r2,c2,n2] 순서 보장
- Protected Contract or Invariant:
  - 입력 계약(스키마/범위/유일성)
  - 출력 계약(타입/길이/좌표/순서)
  - 조합 정책 계약(우선→대체 시도)
  - 합 34 불변식 및 리팩토링 후 외부 계약 불변식
- Expected Learning Outcome: 회귀 보호를 통해 “변경 가능하지만 계약은 안정적인 시스템” 사고를 학습한다.

## 5. Journey to User Story Mapping
Stage별 Candidate User Story 및 Acceptance Criteria 방향 표 제시

## 6. Traceability Link
Epic Goal, Journey Stage, Invariant/Contract, Future Test Target 연결 표 제시
```

## Turn 03
### User
```text
Level 3: Magic Square 프로젝트의 User Stories를 작성해 주세요.

맥락:
이 작업은 다음 흐름의 일부입니다.

Epic → User Journey → User Story → Task

상위 Epic:
“불변식 기반 사고 훈련 시스템 구축”

상위 User Journey:
학습자는 문제를 인식하고, 입력/출력 계약을 정의하고, 도메인 책임을 분리하고,
Dual-Track UI + Logic TDD를 적용하며, 회귀 테스트로 품질을 보호합니다.

중요:
- 구현 코드를 작성하지 마십시오.
- 테스트 코드를 작성하지 마십시오.
- 파일을 생성하지 마십시오.
- 아직 Task 수준으로 세분화하지 마십시오.
- 오직 User Story와 Acceptance Criteria만 작성하십시오.
- 모든 Acceptance Criteria는 테스트 가능한 문장으로 작성하십시오.
- Boundary Story와 Domain Story를 분리하십시오.
- 각 Story마다 보호하는 Contract 또는 Invariant를 명시하십시오.

프로젝트:
Magic Square 4x4 TDD Practice

도메인 규칙:
- 입력은 4x4 int 행렬입니다.
- 0은 빈칸을 의미합니다.
- 빈칸은 정확히 2개여야 합니다.
- 유효한 값은 0 또는 1부터 16까지입니다.
- 0을 제외한 숫자는 중복될 수 없습니다.
- 4x4 마방진 상수는 34입니다.
- 출력은 int[6]입니다.
- 최종 출력 좌표는 1-index 기준입니다.
- 출력 형식은 [r1, c1, n1, r2, c2, n2]입니다.

다음 User Stories를 작성하십시오.

Story 1 — 입력 검증
As a learner,
I want the Boundary layer to validate the input matrix before calling Domain logic,
So that invalid data is never transmitted to the Domain layer.

Acceptance Criteria:
- 입력이 4x4가 아니면 정의된 검증 실패를 반환하거나 발생시킨다.
- 빈칸 개수가 정확히 2개가 아니면 정의된 검증 실패를 반환하거나 발생시킨다.
- 값이 0 또는 1부터 16 범위를 벗어나면 정의된 검증 실패를 반환하거나 발생시킨다.
- 0을 제외한 중복 숫자가 있으면 정의된 검증 실패를 반환하거나 발생시킨다.
- 검증에 실패하면 Domain resolver는 호출되지 않아야 한다.

Story 2 — 빈칸 좌표 탐색
As a learner,
I want to find the exact coordinates of the two blank cells,
So that candidate number combinations can be applied correctly.

Acceptance Criteria:
- 값이 0인 셀을 빈칸으로 탐지한다.
- 정확히 두 개의 빈칸 좌표를 반환한다.
- 좌표는 row-major 순서로 반환한다.
- 내부 좌표 기준이 0-index인지 1-index인지 명시한다.

Story 3 — 누락 숫자 탐색
As a learner,
I want to find the two numbers missing from 1 through 16,
So that they can be used as candidates for the blank cells.

Acceptance Criteria:
- 0은 빈칸을 의미하므로 누락 숫자 계산에서 제외한다.
- 1부터 16 사이에서 정확히 두 개의 누락 숫자를 찾는다.
- 누락 숫자는 오름차순으로 반환한다.

Story 4 — 마방진 검증
As a learner,
I want to verify whether a completed 4x4 grid satisfies the magic square invariant,
So that only valid magic square results are accepted.

Acceptance Criteria:
- 모든 행의 합은 34와 같아야 한다.
- 모든 열의 합은 34와 같아야 한다.
- 두 대각선의 합은 각각 34와 같아야 한다.
- 모든 행, 열, 대각선 조건을 만족할 때만 true를 반환한다.
- 하나의 조건이라도 실패하면 false를 반환한다.

Story 5 — 두 가지 조합 시도
As a learner,
I want the solver to try both possible missing-number combinations,
So that it can find the valid magic square result without hardcoding the answer.

Acceptance Criteria:
- 먼저 작은 누락 숫자를 첫 번째 빈칸에, 큰 누락 숫자를 두 번째 빈칸에 넣어 시도한다.
- 첫 번째 조합이 실패하면 반대 조합을 시도한다.
- 성공한 결과를 int[6]으로 반환한다.
- 최종 출력 좌표는 1-index 기준이어야 한다.
- 최종 출력 형식은 [r1, c1, n1, r2, c2, n2]이어야 한다.
- 반환 배열의 길이는 6이어야 한다.
- 두 조합 모두 마방진을 만들지 못하면 정의된 실패를 반환하거나 발생시킨다.

출력 형식:

# Level 3: User Stories — Magic Square 4x4

## Story Overview

| Story ID | Story Name | Layer | Protected Contract / Invariant |
|---|---|---|---|

## Story 1 — 입력 검증
- Layer:
- User Story:
- Acceptance Criteria:
- Protected Contract:
- Future RED Test Direction:

## Story 2 — 빈칸 좌표 탐색
- Layer:
- User Story:
- Acceptance Criteria:
- Protected Invariant:
- Future RED Test Direction:

## Story 3 — 누락 숫자 탐색
- Layer:
- User Story:
- Acceptance Criteria:
- Protected Invariant:
- Future RED Test Direction:

## Story 4 — 마방진 검증
- Layer:
- User Story:
- Acceptance Criteria:
- Protected Invariant:
- Future RED Test Direction:

## Story 5 — 두 가지 조합 시도
- Layer:
- User Story:
- Acceptance Criteria:
- Protected Contract / Invariant:
- Future RED Test Direction:

## Traceability Matrix

| Epic Goal | Journey Stage | User Story | Acceptance Criteria | Future Test Target |
|---|---|---|---|---|
```

### AI
```text
# Level 3: User Stories — Magic Square 4x4

## Story Overview
| Story ID | Story Name | Layer | Protected Contract / Invariant |
|---|---|---|---|
| US-1 | 입력 검증 | Boundary | 입력 계약(Input Contract), 계층 경계 계약(Boundary는 Domain에 유효 입력만 전달) |
| US-2 | 빈칸 좌표 탐색 | Domain | 빈칸 불변식(0은 빈칸, 빈칸 2개), 좌표 순서 불변식(row-major) |
| US-3 | 누락 숫자 탐색 | Domain | 값 집합 불변식(1~16), 0 제외 규칙, 누락 숫자 2개 불변식 |
| US-4 | 마방진 검증 | Domain | 마방진 불변식(모든 행/열/대각선 합 = 34) |
| US-5 | 두 가지 조합 시도 | Domain + Boundary Output | 해 탐색 계약(우선/대체 조합), 출력 계약(Output Contract: int[6], 1-index, 형식 고정) |

각 Story별로 Layer, User Story, 테스트 가능한 Acceptance Criteria, Protected Contract/Invariant, Future RED Test Direction을 상세 작성했다.

Traceability Matrix에서는 Epic Goal, Journey Stage, User Story, Acceptance Criteria, Future Test Target을 표로 연결했다.
```

## Turn 04
### User
```text
Level 4: Implementation Scenario — Technical
Feature: 4x4 마방진 완성
(중략)
Scenario ID: SC-DOM-SOL-001 ... RED-DOM-SOL-001 ... TASK-DOM-SOL-001
Scenario ID: SC-BND-VAL-001 ... RED-BND-VAL-001 ... TASK-BND-VAL-001
Scenario ID: SC-BND-VAL-002 ... RED-BND-VAL-002 ... TASK-BND-VAL-002
Scenario ID: SC-BND-VAL-003 ... RED-BND-VAL-003 ... TASK-BND-VAL-003
```

### AI
```text
# Level 4: Implementation Scenario — Technical

Background:
- 4x4 입력
- 0=빈칸
- 빈칸 2개
- 값 범위 0 또는 1~16
- 0 제외 중복 금지
- 마방진 상수 34
- 출력 [r1,c1,n1,r2,c2,n2]
- 좌표 1-index

SC-DOM-SOL-001:
- small-first 실패 후 reverse 성공
- 최종 반환 [3, 3, 6, 4, 4, 1]
- 행/열/대각선 34 검증
- RED-DOM-SOL-001 / TASK-DOM-SOL-001 연결

SC-BND-VAL-001:
- 빈칸 개수 오류
- Domain 미호출
- RED-BND-VAL-001 / TASK-BND-VAL-001

SC-BND-VAL-002:
- 0 제외 중복 오류
- Domain 미호출
- RED-BND-VAL-002 / TASK-BND-VAL-002

SC-BND-VAL-003:
- 값 범위 오류
- Domain 미호출
- RED-BND-VAL-003 / TASK-BND-VAL-003
```

## Turn 05
### User
```text
Level 5: Scenario Verification and Summary를 작성해 주세요.
(중략)
출력 형식:
# Level 5: Scenario Verification and Summary
## 1. Overall Judgment
## 2. Epic → Journey Consistency Check
## 3. Journey → User Story Consistency Check
## 4. Story → Technical Scenario Consistency Check
## 5. MagicSquare Edge Case Coverage
## 6. Invariant Coverage Check
## 7. Dual-Track TDD Readiness Check
## 8. Implementation Possibility Check
## 9. Traceability Matrix
## 10. Missing Items / Correction Needed
## 11. Final Summary
```

### AI
```text
# Level 5: Scenario Verification and Summary

## 1. Overall Judgment
- 적합성 점수: 6.8/10
- 현재 상태: 일부 수정 필요
- 요약 판단: 구조 정합성은 양호하나 시나리오 커버리지 보강 필요

## 2. Epic → Journey Consistency Check
- 전반적 정합성 양호
- KPI 수치 연결 보강 권장

## 3. Journey → User Story Consistency Check
- 기능 분해 가능
- Boundary/Domain 분리 양호
- Stage 1 직접 대응 Story 추가 권장

## 4. Story → Technical Scenario Consistency Check
- SC-DOM-SOL-001, SC-BND-VAL-001~003 존재
- US-2/US-3/US-4 전용 시나리오 누락

## 5. Edge Case Coverage
- reverse 성공 있음
- small-first 성공 없음
- shape 오류(4x4 아님) 없음

## 6. Invariant Coverage Check
- 일부 불변식은 Story까지 연결, Scenario/RED 미연결 항목 존재

## 7. Dual-Track TDD Readiness Check
- 분리 가능하나 누락 시나리오 보강 필요

## 8. Implementation Possibility Check
- BlankFinder/MissingNumberFinder/Validator/Solver/Boundary Validator로 분리 가능

## 9. Traceability Matrix
- Story 1/5는 강한 연결
- Story 2/3/4는 연결 보강 필요

## 10. Missing Items / Correction Needed
- SC-BND-VAL-004 (shape)
- SC-DOM-BLK-001
- SC-DOM-MISS-001/002
- SC-DOM-VAL-001~004
- SC-DOM-SOL-002/003

## 11. Final Summary
- 조건부 진행 가능
- 누락 시나리오 보강 후 Level 6 권장
```

## Turn 06
### User
```text
보고서 작성
```

### AI
```text
# Magic Square 4x4 TDD 설계 검증 보고서

## 1) 보고서 개요
- 프로젝트: Magic Square 4x4 TDD Practice
- 검증 범위: Level 1(Epic) ~ Level 5(Scenario Verification)
- 목적: 불변식 기반 학습 목표가 Journey, Story, Scenario로 일관되게 연결되는지 확인

## 2) 핵심 결론
- 종합 상태: 일부 수정 필요
- 적합성 판단: 구조는 잘 잡혔으나 시나리오 커버리지 보강 필요
- 최종 평가: Level 6 진행은 가능하나 누락 시나리오 보완 후 진행 권장

## 3) 수준별 정합성 요약
- Level 1→2 정렬 양호
- Level 2→3 분해 가능
- Level 3→4에서 Story 2/3/4 시나리오 부족

## 4) 강점
- Boundary 입력 검증 시나리오 명확
- Solver reverse 조합 분기 명확
- 출력 계약 관점 반영

## 5) 보완 항목
- shape 오류 시나리오
- Story 2/3/4 전용 시나리오
- small-first 성공 / 양쪽 실패 시나리오

## 6) 불변식 추적성 요약
- 입력/도메인/출력 불변식 축 정리
- 일부는 Scenario/RED까지 미하강

## 7) 다음 단계 권고
- 누락 시나리오 보강 후 Level 6 진입 권장
```

## Turn 07
### User
```text
@.cursor/rules/workflow-automation.mdc  보고서 작성
```

