# mcp-lab-demo

공개SW실무 강의자료 6의 MCP 연결 실습입니다.

## 기능
- add(a, b): 정수 두 개의 합
- grade_message(score): 점수에 따른 학점 메시지
- campus_notice(keyword): exam/project 예제 공지 검색 (실제 학교 공지가 아님)

## 실행
Python 3.11 이상과 uv를 설치하고 저장소 루트에서 `uv sync`를 실행합니다.
VS Code에서 이 폴더를 열고 MCP: List Servers에서 campus-tools를 시작합니다.
GitHub 서버는 별도로 OAuth 인증합니다. 설정은 Windows용입니다.

## 호출 예시
- campus-tools로 10과 32를 더해줘. → 42
- campus-tools에서 85점 메시지를 알려줘. → B: good
- campus-tools로 exam 공지를 찾아줘. → Midterm: Week 8

## 구조
- server.py: FastMCP stdio 서버와 도구 3개
- pyproject.toml: 교안과 호환되는 MCP SDK 1.x 의존성
- .vscode/mcp.json: GitHub HTTP 및 campus-tools stdio 연결

MCP는 모델을 재학습하는 대신 외부 도구와 데이터를 표준 방식으로 연결합니다.
