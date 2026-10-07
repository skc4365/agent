"""09. Execution environment: 가상 파일

핵심 구문
FilesystemMiddleware: 파일 도구 | StateBackend: 상태 기반 가상 파일
실제 디스크 저장 없음

실행: uv run doc_s/doc_s_agent_09.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
추가 패키지: uv add deepagents
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# 가상 파일: 에이전트 상태에 저장 / 실제 디스크 저장 없음
backend = StateBackend()

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    middleware=[
        FilesystemMiddleware(backend=backend),
    ],
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": "write_file 도구로 /notes.txt에 '에이전트 실습'을 저장하고 read_file로 읽어줘."}]}
)

# 4. 결과 확인
print(result["messages"][-1].content)
print("가상 파일 상태:", result.get("files", {}))

# 결과
# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_09.py     
# /notes.txt 내용:

# 에이전트 실습
# 가상 파일 상태: {'/notes.txt': 
#                       {'content': '에이전트 실습', 'encoding': 'utf-8', 
#                       'created_at': '2026-10-07T00:38:46.951434+00:00', 
#                       'modified_at': '2026-10-07T00:38:46.951434+00:00'}}
