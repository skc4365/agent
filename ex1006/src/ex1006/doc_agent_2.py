from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool
load_dotenv()

class Answer(BaseModel):
    summary: str
    confidence: float

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"


agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    response_format=Answer,
    system_prompt="너는 학습 도우미야, 핵심과 간단구조만 알려줘",
)

result = agent.invoke({"messages": [{"role": "user", "content": "싱글 에이전트를 설명해줘"}]})
print(result["structured_response"])
# (skc-agent) E:\agent26_agent\skc-agent>uv run skc-agent
# Hello from skc-agent!
# summary='싱글 에이전트는 하나의 에이전트가 혼자서 목표를 달성하도록 판단하고 행동하는 구조입니다.\n\n
# 핵심 구조:\n
# 1. 입력: 사용자의 요청이나 환경 정보 받기\n
# 2. 판단: 목표를 이해하고 필요한 행동 결정\n
# 3. 실행: 검색, 계산, 도구 사용, 답변 생성 등 수행\n
# 4. 결과: 최종 답변 또는 행동 결과 제공\n\n
# 예시:\n
# - 챗봇 하나가 질문을 이해하고 답변하는 경우\n
# - 로봇 하나가 장애물을 피해 목적지까지 이동하는 경우\n
# - AI 하나가 자료를 검색하고 요약하는 경우\n\n
# 특징:\n
# - 구조가 단순함\n
# - 관리와 구현이 쉬움\n
# - 여러 에이전트 간 협업 조율이 필요 없음\n
# - 하지만 복잡한 문제에서는 역할 분담이 어렵고 한계가 있을 수 있음\n\n
# 비교:\n
# - 싱글 에이전트: 하나의 AI가 전체 작업 처리\n
# - 멀티 에이전트: 여러 AI가 역할을 나누어 협력' 
# confidence=0.96