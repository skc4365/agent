"""08. Streaming: 진행 과정

핵심 구문
stream_mode="updates": 노드별 중간 결과 | model → tools → model: 실행 흐름

실행: uv run doc_s/doc_s_agent_08.py
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
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    system_prompt="학습 자료는 search로 확인하고 한국어로 답하세요.",
)

# 3. 질문 실행: content 수정 → 결과 비교
# stream_mode="updates": 
#               LangGraph에서 상태(State)가 갱신될 때마다, 
#               변경된 부분(노드의 실행 결과)만 이벤트 단위로 스트리밍하도록 지정하는 옵션
for update in agent.stream(
    {"messages": [{"role": "user", "content": 'search를 사용해서 에이전트를 조회하고 요약해줘.'}]}, stream_mode="updates"
):
    # model·tools 노드: 완료 순서별 결과 출력
    for node, data in update.items():
        print("진행 노드:", node)
        if isinstance(data, dict):
            for message in data.get("messages", []):
                message.pretty_print()

# 결과

# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_08.py      
# 진행 노드: model
# ================================== Ai Message ==================================
# Tool Calls:
#   search (call_gCPzxhj47BNYNg1Sa1t9ysyu)
#  Call ID: call_gCPzxhj47BNYNg1Sa1t9ysyu
#   Args:
#     query: 에이전트
# 진행 노드: tools
# ================================= Tool Message =================================
# Name: search

# 조회 질문: 에이전트
# 에이전트는 모델이 도구를 선택하고 결과를 읽으며 작업을 수행한다. system_prompt는 행동 지침이고 response_format은 응답 구조다. checkpointer와 thread_id를 함께 사용하면 대화 이력을 유지한다.
# 진행 노드: model
# ================================== Ai Message ==================================

# 조회 결과 요약:

# 에이전트는 **모델이 필요한 도구를 선택하고**, 그 **도구의 실행 결과를 읽어 작업을 수행하는 구조**입니다.

# 핵심 개념은 다음과 같습니다.

# - **system_prompt**: 에이전트의 행동 방식과 지침을 정의합니다.
# - **response_format**: 에이전트가 반환할 응답의 구조를 지정합니다.
# - **checkpointer + thread_id**: 함께 사용하면 대화 이력을 유지할 수 있습니다.

# 즉, 에이전트는 단순히 답변만 생성하는 것이 아니라, 상황에 따라 도구를 활용하고 이전 대화 맥락을 이어가며 작업을 처리할 수 있는 실행 주체입니다.
