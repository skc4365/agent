"""02. Tools: 도구 연결

핵심 구문
@tool: 도구 정의 | 타입·docstring: 입력 형식·용도 | tool_calls: 호출 기록

실행: uv run doc_s/doc_s_agent_02.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

@tool
def search(query: str) -> str:
    """AI 에이전트 학습 자료 조회 — 로컬 모의 검색"""
    return (
        f"조회 질문: {query}\n"
        "에이전트는 모델이 도구를 선택하고 결과를 읽으며 작업을 수행한다. "
        "system_prompt는 행동 지침이고 response_format은 응답 구조다. "
        "checkpointer와 thread_id를 함께 사용하면 대화 이력을 유지한다."
    )

# 2. 에이전트 구성: 모델·도구·실습 옵션
# create_agent()에 등록된 검색 도구를 AI가 인식하고, 필요하다고 판단하면 자동으로 호출
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    system_prompt="학습 자료는 search로 확인하고 한국어로 답하세요.",
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": 'search 도구를 사용해서 AI 에이전트 학습 자료를 조회해줘.'}]}
)

# 4. 결과 확인
for message in result["messages"]:
    # 메시지 흐름: 사용자 입력 → 도구 호출 → 도구 결과 → 최종 답변
    message.pretty_print()

# 결과

# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\docs\doc_s_agent_02.py       
# ================================ Human Message =================================

# search 도구를 사용해서 AI 에이전트 학습 자료를 조회해줘.
# ================================== Ai Message ==================================
# Tool Calls:
#   search (call_xspE2cRTtyOhfHwiTERAL8zb)
#  Call ID: call_xspE2cRTtyOhfHwiTERAL8zb
#   Args:
#     query: AI 에이전트 학습 자료
# ================================= Tool Message =================================
# Name: search

# 조회 질문: AI 에이전트 학습 자료
# 에이전트는 모델이 도구를 선택하고 결과를 읽으며 작업을 수행한다. system_prompt는 행동 지침이고 response_format은 응답 구조다. checkpointer와 thread_id를 함께 사용하면 대화 이력을 유지한다.
# ================================== Ai Message ==================================

# 조회 결과입니다.

# - 에이전트는 모델이 도구를 선택하고 결과를 읽으며 작업을 수행합니다.
# - `system_prompt`는 에이전트의 행동 지침입니다.
# - `response_format`은 응답 구조를 정의합니다.
# - `checkpointer`와 `thread_id`를 함께 사용하면 대화 이력을 유지할 수 있습니다.
