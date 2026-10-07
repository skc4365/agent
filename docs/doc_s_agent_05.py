"""05. Agent state: 사용자 정의 상태

핵심 구문
AgentState: 사용자 정의 필드 | state_schema: 상태 형식
call_count: 직접 전달한 값, 자동 증가 없음 | 상태 필드의 프롬프트 자동 삽입 없음

실행: uv run doc_s/doc_s_agent_05.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents import AgentState

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# -------------------------------------
# AgentState: 
#   - 메시지와 도구 결과 전달
#   - 사용자 정보나 작업 진행 상태 추가: 사용자 정의 AgentState 필요.
#   - 장기기억X
# -------------------------------------
class LearningState(AgentState):
    user_id: str
    call_count: int  # 자동 증가 없음

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    state_schema=LearningState,
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": '에이전트 상태를 한 문장으로 설명해줘.'}],
        "user_id": "learner-001",
        "call_count": 0,
    }
)

# 4. 결과 확인
print(result["messages"][-1].content)
print("사용자 ID:", result["user_id"])
print("직접 전달한 호출 횟수:", result["call_count"])

# 결과
# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_05.py   
# 현재 에이전트는 요청을 처리할 준비가 된 활성 상태입니다.
# 사용자 ID: learner-001
# 직접 전달한 호출 횟수: 0