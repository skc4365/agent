"""12. Name your agent: 이름

핵심 구문
name: 그래프 식별자 | agent.name: 지정된 이름 확인

실행: uv run doc_s/doc_s_agent_12.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# 2. 에이전트 구성: 모델·도구·실습 옵션
# name="learning_assistant": 에이전트 식별 이름이면서,
#       내부 프레임워크(LangGraph 기반)에서 노드(Node) 및 서브그래프(Subgraph)의 구분 식별자로 사용됨.
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    name="learning_assistant",
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": '에이전트의 역할을 한 문장으로 설명해줘.'}]}
)

# 4. 결과 확인
print(result["messages"][-1].content)
print("그래프 이름:", agent.name)

# 결과
# 에이전트는 목표를 달성하기 위해 환경을 인식하고 스스로 판단하여 행동하는 시스템입니다.                                                   
# 그래프 이름: learning_assistant  