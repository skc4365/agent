"""04. Structured output: 응답 스키마

핵심 구문
BaseModel: 필드 정의 | response_format: 응답 구조 | structured_response: 검증 결과
confidence: 모델 자기평가, 통계적 정확도 아님

실행: uv run doc_s/doc_s_agent_04.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from pydantic import BaseModel, Field

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

class Answer(BaseModel):
    summary: str = Field(description="핵심 내용을 한국어로 요약")
    # confidence: 직접 정의한 필드 / 모델 자기평가 / 통계적 확률 아님
    confidence: float = Field(ge=0, le=1, description="모델이 자기평가한 확신 정도")

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    system_prompt="학습 자료는 search로 확인하고 한국어로 답하세요.",
    response_format=Answer,  # 최종 응답 구조: Answer 필드
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": 'search로 확인하고 AI 에이전트를 요약해줘.'}]}
)

# 4. 결과 확인
answer = result["structured_response"]
# indent=2 : 결과포맷에 2칸 들여쓰기
print(answer.model_dump_json(indent=2))
print("신뢰도 (모델의 자기평가):", answer.confidence)

# 결과

# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_04.py       
# {
#   "summary": "AI 에이전트는 단순히 질문에 답하는 모델을 넘어, 주어진 목표를 달성하기 위해 스스로 필요한 도구를 선택하고 실행 결과를 해석하며 다음 행동을 결정하는 시스템입니다. 핵심 구성요소로는 에이전트의 행동 규칙을 정하는 system_prompt, 외부 검색·계산·API 호출 같은 도구 사용 기능, 도구 결과를 읽고 판단하는 모델의 추론 과정, 그리고 응답 형태를 고정하는 response_format이 있습니다. 또한 checkpointer와 thread_id를 함께 사용하면 이전 대화나 작업 맥락을 저장해 연속적인 대화 이력을 유지할 수 있습니다. 즉, AI 에이전트는 ‘목표 이해 → 필요한 도구 선택 → 실행 결과 확인 → 다음 단계 판단 → 구조화된 응답 생성’의 흐름으로 작동하며, 검색 보조, 업무 자동화, 고객 응대, 데이터 분석, 개인 비서 등 다양한 작업에 활용될 수 있습니다.",
#   "confidence": 0.86
# }
# 신뢰도 (모델의 자기평가): 0.86