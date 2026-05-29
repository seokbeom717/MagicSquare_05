# Prompting BP 개인 회고 및 개선 계획

| 항목 | 내용 |
|------|------|
| **프로젝트** | Prompting_BP (실습 구현: MagicSquare_05) |
| **Repository (제출 명명)** | `Prompting_BP_05` |
| **Author** | 김석범 |
| **Reviewer** | _(수강 과제에 맞게 기입)_ |
| **작성일** | 2026-05-29 |
| **회고 대상 기간** | REFACTOR 준비(Report/15) → 실행(16) → QA 분석(17) → NFR GREEN(18) → Session Summary(19) |
| **기준 브랜치** | `refactor/refactor` |
| **기준선 (Step 0)** | pytest **86 passed**, 1 skipped · GM **6/6** · NFR gate Domain/Boundary/전역 **98%** (gui omit) |

> 본 문서는 **개인** Prompting BP 회고·최종 제출용입니다. 팀 회고·공동 액션은 제외했습니다.

---

## 목차

1. [Keep](#1-keep)
2. [Problem](#2-problem)
3. [Try](#3-try)
4. [개인별 학습 성과](#4-개인별-학습-성과)
5. [개인 개선 액션 아이템](#5-개인-개선-액션-아이템)
6. [현업 적용 계획](#6-현업-적용-계획)
- [부록 A: 회고 세션 진행 가이드 (개인)](#부록-a-회고-세션-진행-가이드-개인)
- [부록 B: 액션 아이템 추적 템플릿](#부록-b-액션-아이템-추적-템플릿)
- [부록 C: 학습 자료 정리](#부록-c-학습-자료-정리)
- [부록 D: 다음 프로젝트 개선 계획서](#부록-d-다음-프로젝트-개선-계획서)

---

## 1. Keep

**무엇이 잘 되었는가?**

- `/code-reviewer`로 ECB·SRP 이슈를 P0/P1/P2로 나눈 뒤, **Track B GREEN → ECB 역전 해소 → REFACTOR** 순으로 진행해 회귀 없이 구조를 정리했다.
- Report/17에서 NFR이 FAIL이었을 때, 추측 대신 **Step 0 실측**(pytest, GM, cov)으로 원인을 좁혔고, Report/18에서 gate를 GREEN으로 맞췄다.
- Golden Master **6/6**을 REFACTOR·QA 전후 앵커로 두어, Track B 출력·`PuzzleGateway`·`UiBoundary` 변경 후에도 계약이 유지됐다.

**어떤 관행을 계속 유지해야 하는가?**

- **RED → GREEN → REFACTOR** — 테스트 없이 구조만 바꾸지 않기.
- **ECB 의존 방향** — `Screen → Boundary → Control → Entity` (control→boundary 금지).
- **SSOT 우선순위** — `docs/qa_ssot_mapping.md` > `docs/test_plan.md` > README > 구 프롬프트 템플릿.
- **커밋 단위 실행** — README REFACTOR CheckList A→B→C를 wave별로 커밋·회귀.
- **Report / Prompt 체인** — Report/15~19 + Prompt transcript로 단계·수치·판단 근거 남기기.

**개인에게 도움이 된 것들**

- Cursor **서브에이전트**(code-reviewer)로 리팩터링 전 전체 리뷰·우선순위 확보.
- **Dual-Track TDD**로 Boundary 계약(입력·envelope)과 Domain 규칙(솔버·검증) 분리 학습.
- **`.coveragerc` + NFR gate 명령**으로 “측정 대상”과 “제외 대상(gui)”을 문서화한 점.

---

## 2. Problem

**어떤 장애물이 있었는가?**

- 구 프롬프트와 저장소 **불일치**: GM 경로(`test_gm_01_*` vs `test_golden_master_magic_square.py`), “19 RED”, boundary pytest 건수, `boundary/screen` vs `gui` 등 → Step 0 혼선·재작업.
- **GUI·환경**: PyQt6 미설치 → `test_grid_panel` skip, `python main.py` smoke 미착수, gui 포함 Boundary cov **46%** 잔존.
- **잔여 기술 부채**: `boundary_validator` dead code(L60-62), gui→screen rename 보류(Report/15 C-2).

**무엇이 느리게 했는가?**

- SSOT 보정 전 QA Turn에서 **FAIL 수치 해석**에 시간 소요 (Domain 90% → 98%, Boundary 35% vs gate 98%).
- 프롬프트 템플릿을 그대로 쓰면 **exit 4·잘못된 경로**로 한 번 더 돌려야 함.
- Screen Track은 자동 gate만으로는 닫히지 않아 **수동 smoke·PyQt**가 병목.

**비효율적이었던 프로세스 (개인 관점)**

- Export·QA 세션 **시작 시 SSOT 프리플라이트 없음** → Report/17 이후에야 `qa_ssot_mapping.md` 정리.
- 커버리지 보고 시 **“gui 포함 / gate omit”** 기준을 초반에 한 줄로 고정하지 않음.

---

## 3. Try

**다음에는 무엇을 다르게 할까?**

- QA·Export·회고 세션 **첫 10분**에 SSOT·GM 경로·cov gate 명령만 확인하고 시작한다.
- REFACTOR·QA는 **작은 커밋 1건** + pytest 전체 + GM 6/6을 매 wave 습관화한다.
- 발표·제출 전 **개인 회고 문서(본 문서 형식)** 를 먼저 쓰고, 그다음 Report Export한다.

**새로운 도구·방법**

- 세션 시작 **체크리스트 파일** (1페이지): GM 경로, pytest 스코프, `.coveragerc`, NFR 명령 3줄.
- Cursor **재개 프롬프트 템플릿**(Prompt/19 §재개)을 QA·Summary마다 상단에 붙이기.
- PyQt6 설치 후 **grid_panel + main.py smoke**로 Screen Track 마감 실험.

**문제 해결 실험**

| 실험 | 가설 | 성공 기준 |
|------|------|-----------|
| SSOT 프리플라이트 | drift 1회 방지 | Step 0 첫 실행에서 exit 0, 경로 0건 수정 |
| gui omit vs smoke 분리 문서화 | cov 혼선 감소 | Report에 “gate / gui 포함 / smoke” 3행 표 고정 |
| RF-DEAD 1커밋 | dead code 제거 안전 | pytest 86+, GM 6/6 유지 |

---

## 4. 개인별 학습 성과

### 4.1 새로 배운 기술·개념

| 영역 | 내용 |
|------|------|
| **아키텍처** | ECB 레이어, Dual-Track TDD, PuzzleGateway·UiBoundary 역할 분리 |
| **품질** | Golden Master 회귀, NFR gate, `.coveragerc` omit 정책 |
| **프롬프팅** | code-reviewer 선행, Export-only 턴(실측 허용·production 변경 금지) 명시 |
| **추적성** | `qa_ssot_mapping.md`, Report/Prompt ID 체인, TASK↔Test ID |

### 4.2 개인 역량 향상

- AI 제안을 **테스트·GM·cov 숫자**로 검증하는 습관 (추측 → 실측).
- REFACTOR 시 **의존 방향·계약**을 먼저 고정하고 구조 변경하는 판단력.
- 프롬프트·저장소 불일치를 **매핑표로 정리**하는 문서화 능력.

### 4.3 공유하고 싶은 인사이트 (발표·문서용)

1. **“GREEN 없이 REFACTOR”는 회귀 비용이 크다** — Track B·GM을 먼저 닫을 것.
2. **커버리지 %는 ‘무엇을 측정했는지’가 먼저다** — gui 포함 46%와 gate 98%는 같은 저장소라도 다른 질문에 답한다.
3. **AI 개발의 추적성 = TDD 사이클 + SSOT + Report** — 코드만 맞추면 발표·회고에서 설명이 안 된다.

### 4.4 추천 학습 자료

| 자료 | 용도 |
|------|------|
| MagicSquare_05 `docs/test_plan.md` §6·§7 | NFR·Dual-Track cov |
| MagicSquare_05 `docs/qa_ssot_mapping.md` | 프롬프트 drift 보정 |
| MagicSquare_05 Report/15~19 | REFACTOR·QA·Export 흐름 샘플 |
| [BP_A KPT README](https://github.com/mobumkhj/BP_A) | 개인 KPT bullet 참고 (본인 섹션) |
| Kent Beck, *Test-Driven Development* | RED→GREEN→REFACTOR 원칙 |
| Cursor Docs — Rules / Subagents | code-reviewer·ECB rule 운영 |

---

## 5. 개인 개선 액션 아이템

> 책임자: **김석범** (개인). 팀 할당·공동 일정 없음.

| ID | 액션 | 구체적 작업 | 일정 (목표) | 진행 추적 | 성공 기준 |
|----|------|-------------|-------------|-----------|-----------|
| A-01 | Screen Track 마감 | PyQt6 설치 → `test_grid_panel` → `python main.py` smoke | D+3 | README 체크리스트 ☐ | skip 0, smoke PASS 기록 |
| A-02 | SSOT 프리플라이트 | 1페이지 체크리스트 + Prompt 재개 템플릿 | D+1 | `docs/` 또는 `.cursor/` 커밋 | 다음 QA 세션 Step 0 1회 성공 |
| A-03 | RF-DEAD | `boundary_validator` L60-62 제거, boundary 회귀 | D+5 | 단일 커밋 + pytest | 86+ pass, GM 6/6 |
| A-04 | 제출 저장소 | `Prompting_BP_05` 생성, Description·본 문서 push | D+2 | GitHub repo | README = 본 문서 요약 또는 링크 |
| A-05 | 발표 자료 | Keep/Problem/Try + 학습 성과 5슬라이드 | D+4 | `slides/` 또는 README §발표 | 10분 내 설명 가능 |

**진행 상황 추적 방법 (개인)**

- 주 2회: 액션 표 **상태 열** 갱신 (⬜ / 🔄 / ✅).
- 각 액션 완료 시 **커밋 1건 + pytest·GM 로그 1줄**을 Report 또는 Prompt에 붙임.
- 미완 시 **Problem에 원인 1줄** 추가 (다음 회고 입력).

---

## 6. 현업 적용 계획

| 현업 상황 | 적용할 Keep | Problem에서 피할 점 | Try (90일 내) |
|-----------|-------------|---------------------|----------------|
| 레거시 모듈 리팩터 | GM·characterization test 먼저 | 대규모 구조 변경 후 테스트 | wave별 커밋 + 회귀 gate |
| AI 보조 코딩 | code-reviewer·ECB rule | AI 출력을 그대로 믿기 | SSOT 문서 + 실측 검증 |
| QA·커버리지 리포트 | gate 대상 명시(omit 포함) | %만 보고 해석 | “측정 범위” 3행 표 템플릿 |
| 인수인계·발표 | Report/Prompt 체인 | 코드만 전달 | 단계별 요약 1페이지 Export |

**90일 목표 (개인 KPI)**

- 신규/개선 기능 1건 이상: **RED→GREEN→REFACTOR** 전 주기 적용.
- PR 설명에 **테스트 ID·회귀 명령** 필수 포함.
- 분기 1회: 개인 KPT + 액션 표 리뷰 (본 문서 부록 B 재사용).

---

## 부록 A: 회고 세션 진행 가이드 (개인)

**목적:** 1인(또는 리뷰어 1명) 기준으로 60~90분, KPT + 학습 성과 + 액션 확정.

| 순서 | 시간 | 활동 | 산출 |
|------|------|------|------|
| 0 | 5분 | Step 0 실측: `pytest -q`, GM 6건, cov gate | 수치 메모 |
| 1 | 15분 | **Keep** — 잘된 점 3개 (증거: Report·커밋 hash) | §1 초안 |
| 2 | 15분 | **Problem** — 막힌 점 3개 (원인 1줄씩) | §2 초안 |
| 3 | 15분 | **Try** — 다음 실험 3개 (성공 기준 포함) | §3 초안 |
| 4 | 20분 | **학습 성과** — 새 개념·역량·인사이트·자료 | §4 |
| 5 | 15분 | **액션 5건** 확정 + 일정 | §5 표 |
| 6 | 10분 | **현업 적용** 1표 + 발표 슬라이드 outline | §6, 발표 메모 |

**진행 원칙**

- 발언은 **사실(실측) → 해석 → 액션** 순.
- 팀 비교·책임 추궁 없음 (개인 세션).
- 리뷰어가 있으면 **§1·§3만** 피드백, Problem은 본인이 주도.

**발표 연결 (10분 예시)**

1. 프로젝트·담당 구간 (1분) — Report/15~19 다이어그램  
2. Keep 3 bullet (2분)  
3. Problem + Try (3분)  
4. 학습 성과 1가지 인사이트 (2분)  
5. 액션 1건 + 현업 적용 (2분)

---

## 부록 B: 액션 아이템 추적 템플릿

```markdown
## 개인 액션 트래커 — 김석범

| 주차 | ID | 상태 | 증거 (커밋/테스트) | 메모 |
|------|-----|------|-------------------|------|
| W1 | A-02 | ⬜ | | |
| W1 | A-04 | ⬜ | | |
| W2 | A-01 | ⬜ | | |
| W2 | A-03 | ⬜ | | |
| W2 | A-05 | ⬜ | | |

상태: ⬜ 예정 | 🔄 진행 | ✅ 완료 | ⏸ 보류
```

**주간 리뷰 질문 (5분)**

1. 이번 주 성공 기준을 충족한 ID는?  
2. 보류한 ID의 Problem은 §2에 반영했는가?  
3. 다음 주 **단 1개**만 최우선으로 무엇인가?

---

## 부록 C: 학습 자료 정리

| # | 제목 | 유형 | 링크/경로 | 메모 |
|---|------|------|-----------|------|
| 1 | QA SSOT 매핑 | 프로젝트 문서 | `MagicSquare_05/docs/qa_ssot_mapping.md` | drift 보정 |
| 2 | Test Plan v1.1 | 프로젝트 문서 | `MagicSquare_05/docs/test_plan.md` | NFR·Dual-Track |
| 3 | Session Summary | Report | `MagicSquare_05/Report/19_*.md` | 통합 실측 |
| 4 | REFACTOR 실행 | Report | `MagicSquare_05/Report/16_*.md` | A~C wave |
| 5 | TDD (Beck) | 도서 | — | 사이클 원칙 |
| 6 | Cursor Rules | 도구 | `.cursor/rules/` | ECB·TDD |

---

## 부록 D: 다음 프로젝트 개선 계획서

**프로젝트 가정:** 동일 규모의 TDD+ECB 훈련 또는 소형 업무 모듈 1건.

| 단계 | 개선 내용 | 적용 시점 |
|------|-----------|-----------|
| **착수** | SSOT·GM·cov 프리플라이트 10분 | Day 0 |
| **RED** | Dual-Track 스켈레톤, Test ID ↔ TASK 매핑 | Week 1 |
| **GREEN** | Track B → Track A, GM 6건 고정 | Week 1~2 |
| **REFACTOR** | code-reviewer → P0/P1 로드맵 → wave 커밋 | Week 2~3 |
| **QA** | FAIL 시 테스트 보완 + `.coveragerc` 정책 문서화 | Week 3 |
| **Export** | Report + Prompt + 개인 회고(본 형식) 동시 산출 | Week 4 |
| **마감** | GUI·smoke·dead code 등 잔여 3액션 이하 | Week 4 |

**다음 프로젝트에서 하지 않을 것**

- 구 프롬프트 경로·건수를 검증 없이 Step 0에 사용.
- cov %만 보고 gate 통과 여부 판단.
- REFACTOR 전 GM·Track B 미고정.

---

## 발표·제출 체크리스트

- [ ] GitHub `Prompting_BP_05` 생성 (Description: Author 김석범, Reviewer _(성명)_)
- [ ] 본 문서를 repo 루트 `README.md` 또는 `docs/회고_김석범.md`로 push
- [ ] 발표: §1~3 + §4.3 인사이트 1개 + §5 액션 1건
- [ ] BP_A 개인 KPT와 수치·메시지 정합 확인

---

*문서 버전 1.0 | Prompting_BP 개인 회고 | Author: 김석범 | 2026-05-29*
