"""01. Model: 기본 에이전트

핵심 구문
create_agent: 모델 연결 | invoke: 질문 실행 | messages[-1]: 최종 답변

실행: uv run doc_s/doc_s_agent_01.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": 'AI 에이전트란 무엇인지 한 문장으로 설명해줘.'}]}
)

# 4. 결과 확인
print(result["messages"][-1].content)

# 결과
# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_01.py 
# AI 에이전트는 목표를 달성하기 위해 환경을 인식하고 스스로 판단·행동하는 인공지능 시스템입니다.

# --------------------------------------------
# 각 요소의 역할은 :
# - messages: 에이전트 상태에서 정해진 필수 키
# - role: 메시지를 보낸 주체
# - content: 실제 질문 내용
# - system_prompt: 모델의 답변 방식을 결정
# - result["messages"][-1]: 실행 후 추가된 마지막 AI 응답