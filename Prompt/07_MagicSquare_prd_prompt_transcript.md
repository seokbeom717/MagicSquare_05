# MagicSquare PRD 작성 Prompt Transcript

## Turn 01
### User
```text
PRD를 바로 작성하지 말고,
먼저 PRD 작성에 참고해야 할 문서들을 분석하고,
각 문서의 어떤 내용을 PRD의 어떤 섹션에 반영해야 하는지 매핑해 주세요.
```

### Assistant
```text
요청을 수락하고 Prompt/Report/.cursor/rules 문서들을 수집·분석하여 PRD 섹션 매핑을 준비함.
```

## Turn 02
### User
```text
당신은 PRD 작성 전문가이자 Dual-Track UI + Logic TDD 기반 제품 기획자입니다.
(중략)
출력 형식:
# PRD Reference Document Analysis
...
```

### Assistant
```text
요청 형식에 맞춰 문서 분석 결과를 제공함.
- Overall Judgment
- Document Summary
- PRD Section Mapping
- Source Priority Rules
- Directly Transfer / Appendix 분리
- Conflicts / Ambiguities
- Recommended PRD Outline
```

## Turn 03
### User
```text
당신은 Senior Product/Software Architect이며,
Dual-Track UI + Logic TDD, Clean Architecture, ECB, Concept-to-Code Traceability 전문가입니다.
(중략)
[PRD 작성 구조] 1~23 섹션을 반드시 따르십시오.
...
단 Report 폴더내 파일명은 실제와 다를 수 있으므로 현재 실제 저장된 파일명을 통해 참조할것
```

### Assistant
```text
요청한 구조(1~23)를 따르는 PRD 본문 Markdown을 작성함.
- 코드/테스트 코드는 작성하지 않음
- Dual-Track 전략 반영
- 계약/불변식/오류정책/추적성 표 포함
- 실제 파일명 기준 참고 문서 반영
```

## Turn 04
### User
```text
@.cursor/rules/workflow-automation.mdc
보고서 작성 및 PRD 저장,  그리고 깃의 spec 브랜치에 push 까지 해줘
```

### Assistant
```text
진행 계획:
1) workflow-automation 규칙 확인
2) PRD 파일 저장
3) Report 파일 작성
4) Prompt transcript 저장
5) git commit 후 spec 브랜치 push
```

## Turn 05
### Assistant (실행 내역 요약)
```text
- `.cursor/rules/workflow-automation.mdc` 확인 완료
- `docs/PRD_MagicSquare.md` 생성 완료
- `Report/07_MagicSquare_prd_and_push_report.md` 생성 완료
- 현재 파일: `Prompt/07_MagicSquare_prd_prompt_transcript.md` 작성 완료
- 다음 단계: git commit 및 `spec` 브랜치 push
```
