"""03. System prompt: 행동 지침

핵심 구문
system_prompt: 언어·형식·도구 사용 지침 | 02단계와 답변 비교

실행: uv run doc_s/doc_s_agent_03.py
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
    system_prompt="search로 자료를 확인하고 한국어로 정확히 세 개의 번호 항목으로 답하세요.",
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": 'search로 에이전트를 조회하고 설명해줘.'}]}
)

# 4. 결과 확인
for message in result["messages"]:
    # 메시지 흐름: 사용자 입력 → 도구 호출 → 도구 결과 → 최종 답변
    message.pretty_print()

# 결과

# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\docs\doc_s_agent_03.py       
# ================================ Human Message =================================

# search로 에이전트를 조회하고 설명해줘.
# ================================== Ai Message ==================================
# Tool Calls:
#   search (call_pgK3YH6aO5JfAXzENdXwYFZy)
#  Call ID: call_pgK3YH6aO5JfAXzENdXwYFZy
#   Args:
#     query: 에이전트 AI agent 정의 특징
# ================================= Tool Message =================================
# Name: search

# 조회 질문: 에이전트 AI agent 정의 특징
# 에이전트는 모델이 도구를 선택하고 결과를 읽으며 작업을 수행한다. system_prompt는 행동 지침이고 response_format은 응답 구조다. checkpointer와 thread_id를 함께 사용하면 대화 이력을 유지한다.
# ================================== Ai Message ==================================

# 1. 에이전트는 AI 모델이 단순히 답변만 생성하는 것이 아니라, 필요한 도구를 선택하고 그 결과를 읽어 작업을 수행하는 구조입니다.

# 2. 에이전트의 동작은 보통 `system_prompt` 같은 행동 지침에 의해 정해집니다. 이 지침은 에이전트가 어떤 역할을 해야 하는지, 어떤 방식으로 응답해야 하는지를 안내합니다.

# 3. 대화형 에이전트에서는 `checkpointer`와 `thread_id`를 함께 사용해 대화 이력을 유지할 수 있습니다. 이를 통해 이전 대화 내용을 기억하며 이어서 작업을 처리할 수 있습니다.

