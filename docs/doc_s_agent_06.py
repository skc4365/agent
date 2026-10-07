"""06. Invocation: 대화 이어가기

핵심 구문
InMemorySaver: 프로세스 내 대화 저장 | thread_id: 대화 식별
동일 thread_id: 이력 유지 | 프로세스 종료: 이력 소멸

실행: uv run doc_s/doc_s_agent_06.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    checkpointer=InMemorySaver(),  # 프로세스 종료 시 기억 소멸
)

# 3. 질문 실행: content 수정 → 결과 비교
# 동일 thread_id: 대화·중단 상태 유지
config = {"configurable": {"thread_id": "lesson-6"}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": '내 이름은 민수야. 기억해줘.'}]}, config=config
)

# 4. 결과 확인
print(result["messages"][-1].content)

# 5. 후속 질문: 동일 에이전트·thread_id
result = agent.invoke(
    {"messages": [{"role": "user", "content": "내 이름이 뭐였지?"}]},
    config=config,
)
print(result["messages"][-1].content)

# 결과
# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_06.py  
# 알겠어, 민수야. 기억할게!
# 민수야.