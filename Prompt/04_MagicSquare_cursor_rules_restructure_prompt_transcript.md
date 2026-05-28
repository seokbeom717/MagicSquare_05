# MagicSquare Cursor Rules 재구성 대화형 프롬프트 Transcript

## 메타
- 목적: `.cursorrules` 확장 및 `.cursor/rules/*.mdc` 단계별 분리 작업 이력 기록
- 범위: 본 세션의 주요 사용자 요청과 어시스턴트 처리 내역
- 형식: role 기반 transcript

---

## Turn 1
### User
```text
@.cursorrules 에 대한 내용을 확장하고 싶어
/cursor/rules에 단계별 *.mdc 파일로 나누려면 너에게 어떻게 프롬프트를 주면 좋을지 알려줘
```

### Assistant
```text
복붙 가능한 프롬프트 템플릿 2종(일반형/프로젝트 구체형)을 제시하고,
프롬프트에 반드시 포함할 핵심 항목(alwaysApply vs globs, 파일명 규칙 등)을 안내함.
```

---

## Turn 2
### User
```text
니가 제시한 프롬프트 기준으로 작업 진행
```

### Assistant
```text
`.cursor/rules`에 00~05 규칙 파일을 생성하여
코어 스타일, ECB, TDD, 테스트, 금지 패턴, AI 워크플로를 분리 반영함.
```

---

## Turn 3
### User
```text
다음의 형태로 바꾸기 위에서 너에게 어떤 프롬프트를 줄까
```

### Assistant
```text
목표 파일명(`magicsquare-*.mdc`) 기준으로 실제 생성/정리까지 수행하도록
요구사항이 포함된 고정 프롬프트를 제시함.
```

---

## Turn 4
### User
```text
현재 규칙 구성을 아래 목표 형태로 재구성해줘.
...
workflow-automation.mdc는 그 상태를 그대로 유지해줘. 통합 하지 말고 건드리지 말것
```

### Assistant
```text
요청대로 실제 파일 작업 수행:
1) 목표 5개 파일 생성
2) 기존 00~05 파일 삭제
3) workflow-automation.mdc 무수정 유지
4) `.cursorrules`를 엔트리 안내 파일로 정리
5) 최종 목록/매핑/근거 보고
```

---

## Turn 5
### User
```text
보고서 작성
```

### Assistant
```text
자동화 규칙에 따라 Report/Prompt 폴더에 이번 세션의 보고서와 transcript를 생성함.
```

---

## Export 산출물 경로
- Report: `Report/04_MagicSquare_cursor_rules_restructure_report.md`
- Prompt: `Prompt/04_MagicSquare_cursor_rules_restructure_prompt_transcript.md`
