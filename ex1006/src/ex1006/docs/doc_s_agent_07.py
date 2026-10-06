"""07. Invocation: 실행 컨텍스트

핵심 구문
context_schema: 실행 데이터 형식 | context: 사용자 정보
ToolRuntime: 도구 내부 접근 | runtime.context: 실행 컨텍스트

실행: uv run doc_s/doc_s_agent_07.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# ----------------------------------
# @dataclass :
#              - 데이터 보관용 클래스를 자동 생성
#  
# class Context:
#     def __init__(self, user_id: str):
#         self.user_id = user_id

#     def __repr__(self):
#         ...
    
#     def __eq__(self, other):
#         ...
# ----------------------------------
@dataclass
class Context:
    user_id: str

@tool
def current_user(runtime: ToolRuntime[Context]) -> str:
    """실행 컨텍스트의 현재 사용자 ID 조회"""
    # runtime: 실행 환경의 자동 주입 / 모델 입력 인자에서 제외
    return runtime.context.user_id

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[current_user],
    system_prompt="한국어로 간단하게 답하세요.",
    context_schema=Context,
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": 'current_user 도구로 내 사용자 ID를 확인해줘.'}]}, context=Context(user_id="learner-001")
)

# 4. 결과 확인
for message in result["messages"]:
    # 메시지 흐름: 사용자 입력 → 도구 호출 → 도구 결과 → 최종 답변
    message.pretty_print()

# 결과

# (ex1006) D:\han_skc1001\agent\ex1006>uv run src\ex1006\docs\doc_s_agent_07.py       
# ================================ Human Message =================================

# current_user 도구로 내 사용자 ID를 확인해줘.
# ================================== Ai Message ==================================
# Tool Calls:
#   current_user (call_0eMJmEDZQOVijqZ5nt7hgJoq)
#  Call ID: call_0eMJmEDZQOVijqZ5nt7hgJoq
#   Args:
# ================================= Tool Message =================================
# Name: current_user

# learner-001
# ================================== Ai Message ==================================

# 사용자 ID는 `learner-001`입니다.