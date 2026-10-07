"""14. Guardrails: 이메일 가림

핵심 구문
PIIMiddleware: 이메일 탐지 | strategy="redact": 이메일 가림
apply_to_input=True: 입력 처리 | 메시지 출력: 처리 결과 확인

실행: uv run doc_s/doc_s_agent_14.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# ==================================
# PIIMiddleware는 개인식별정보(PII, Personally Identifiable Information)의 
#               유출을 방지하고 보안을 강화하기 위한 검증 및 보호 미들웨어.
# 예시
        # PIIMiddleware(
        #     "email",               # 1. 탐지 대상: 이메일 주소
        #     strategy="redact",     # 2. 처리 방식: 가리기/대체하기 (Redact: 안전한 대체 문구로 치환)
        #     apply_to_input=True    # 3. 적용 시점: 사용자 입력(Input) 단계에서 적용
        # )
# ==================================

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    middleware=[PIIMiddleware("email", strategy="redact", apply_to_input=True)],
)

# 3. 질문 실행: content 수정 → 결과 비교
result = agent.invoke(
    {"messages": [{"role": "user", "content": '내 테스트 이메일은 learner@example.com이야. 입력 내용을 짧게 설명해줘.'}]}
)

# 4. 결과 확인
for message in result["messages"]:
    # 메시지 흐름: 사용자 입력 → 도구 호출 → 도구 결과 → 최종 답변
    message.pretty_print()

# 결과

# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_14.py        
# ================================ Human Message =================================

# 내 테스트 이메일은 learner@example.com이야. 입력 내용을 짧게 설명해줘.
# ================================== Ai Message ==================================

# 입력 내용은 테스트용 이메일 주소 **learner@example.com**을 알려준 것입니다.