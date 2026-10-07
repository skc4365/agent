"""15. Steering: 승인 후 도구 실행

핵심 구문
HumanInTheLoopMiddleware: 실행 전 중단 | 사용자 입력: 승인·거절
Command: 중단 지점 재개 | preview_note: 파일 생성 없는 모의 저장

실행: uv run doc_s/doc_s_agent_15.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# ====================================
# HumanInTheLoopMiddleware(interrupt_on={"preview_note": True}): 
        # 에이전트가 지정된 특정 도구(preview_note)를 실행하기 직전에 작업을 일시 정지하고, 
        # 사람(사용자/관리자)의 승인이나 개입을 기다리도록 제어하는 인터럽트(Interrupt) 미들웨어.

# checkpointer=InMemorySaver() (필수 짝꿍): 
        # 에이전트의 현재 실행 그래프 상태(State)를 메모리에 저장해둠.    
        # - 인터럽트로 멈춘 시점의 모든 상태(대화 내역, 도구 파라미터 등)를 저장해 두어야, 
        # 이후 사람이 승인했을 때 중단된 지점부터 이어 실행(Resume)할 수 있음.  
# 순서:
        # 1. 사용자 요청: "메모 미리보기 해줘."
        # 2. 에이전트 판단: preview_note(note_id=123) 도구 호출 결정.
        # 3. 미들웨어 개입 (Interrupt): 실행중단 -> InMemorySaver에 저장
        # 4. 사람의 개입 (Human Decision): Approve(승인) 또는 Reject(거부).
        # 5. 재개 (Resume): 승인 시, 에이전트가 중단된 지점부터 preview_note 도구 수행.
# ====================================

@tool
def preview_note(text: str) -> str:
    """메모 저장 모의 실행 — 실제 파일 생성 없음"""
    return f"모의 저장 완료: {text}"

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[preview_note],
    system_prompt="한국어로 간단하게 답하세요.",
    checkpointer=InMemorySaver(),
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"preview_note": True})],
)

# 3. 질문 실행: content 수정 → 결과 비교
# 동일 thread_id: 대화·중단 상태 유지
config = {"configurable": {"thread_id": "lesson-15"}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "preview_note 도구로 '에이전트 학습 완료'라는 메모를 저장해줘."}]}, config=config
)

# 승인 흐름: 도구 실행 전 중단 → 사용자 결정 → 재개
while result.get("__interrupt__"):
    decisions = []
    for interrupt in result["__interrupt__"]:
        for request in interrupt.value["action_requests"]:
            print("승인 대기:", request)
            if input("모의 저장을 승인할까요? [y/N]: ").strip().lower() == "y":
                decisions.append({"type": "approve"})
            else:
                decisions.append({"type": "reject", "message": "사용자가 저장을 거절했습니다."})
    result = agent.invoke(Command(resume={"decisions": decisions}), config=config)

# 4. 결과 확인
for message in result["messages"]:
    # 메시지 흐름: 사용자 입력 → 도구 호출 → 도구 결과 → 최종 답변
    message.pretty_print()

# 결과

# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_15.py        
# 승인 대기: {'name': 'preview_note', 'args': {'text': '에이전트 학습 완료'}, 
#           'description': "Tool execution requires approval\n\nTool: preview_note\nArgs: {'text': '에이전트 학습 완료'}"}
# 모의 저장을 승인할까요? [y/N]: y
# ================================ Human Message =================================

# preview_note 도구로 '에이전트 학습 완료'라는 메모를 저장해줘.
# ================================== Ai Message ==================================
# Tool Calls:
#   preview_note (call_iN3quWInk8igfBkYsmlFFsU5)
#  Call ID: call_iN3quWInk8igfBkYsmlFFsU5
#   Args:
#     text: 에이전트 학습 완료
# ================================= Tool Message =================================
# Name: preview_note

# 모의 저장 완료: 에이전트 학습 완료
# ================================== Ai Message ==================================

# 메모를 저장했습니다: “에이전트 학습 완료”