"""10. Context management: 요약·메모리·스킬

핵심 구문
Summarization: 대화 요약 | Memory: 지침 로드 | Skills: 스킬 연결
AGENTS.md·SKILL.md: 초기 가상 파일 | 짧은 대화: 요약 미발동 가능

실행: uv run doc_s/doc_s_agent_10.py
준비: 프로젝트 루트 .env: OPENAI_API_KEY
추가 패키지: uv add deepagents
모델 변경: create_agent의 model
"""

from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware import MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware
from deepagents.backends.utils import create_file_data

# 1. 환경 설정: 프로젝트 루트 .env → OPENAI_API_KEY
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# 가상 파일: 에이전트 상태에 저장 / 실제 디스크 저장 없음
backend = StateBackend()

# 2. 에이전트 구성: 모델·도구·실습 옵션
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    system_prompt="한국어로 간단하게 답하세요.",
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model="openai:gpt-5.5", backend=backend),
        MemoryMiddleware(backend=backend, sources=["/AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["/skills/"]),
    ],
)

# 3. 질문 실행: content 수정 → 결과 비교
# ================================
# 실제 문서 파일 경로에서 읽어와 런타임 dict 구성
# files = {
#     "/AGENTS.md": create_file_data(Path("./docs/AGENTS.md").read_text(encoding="utf-8")),
#     "/skills/agent-study/SKILL.md": create_file_data(Path("./skills/agent-study/SKILL.md").read_text(encoding="utf-8")),
# }
# ================================

# 초기 상태: 가상 지침·스킬 파일
files = {
    "/AGENTS.md": create_file_data("학습자는 초보자입니다. 구체적인 예시로 설명하세요."),
    "/skills/agent-study/SKILL.md": create_file_data(
        "---\nname: agent-study\ndescription: AI agent learning guidance\n---\n"
        "Teach in order: model, tools, prompt, structured output."
    ),
}
result = agent.invoke(
    {"messages": [{"role": "user", "content": '에이전트 학습을 어떤 순서로 하면 좋을지 알려줘.'}], "files": files}
)

# 4. 결과 확인
print(result["messages"][-1].content)

# 결과

# (docs) D:\han_skc1001\agent\docs>uv run doc_s_agent_10.py     
# 에이전트 학습은 아래 순서로 하면 좋습니다.

# 1. **모델 이해하기**
#    - 먼저 LLM이 무엇을 잘하고 못하는지 배웁니다.
#    - 예: GPT가 글쓰기, 요약은 잘하지만 계산이나 최신 정보 확인은 틀릴 수 있음.

# 2. **도구 사용 배우기**
#    - 에이전트가 검색, 파일 읽기, 계산기, API 같은 도구를 어떻게 쓰는지 배웁니다.
#    - 예: “오늘 날씨 알려줘” → 모델 혼자 답하지 않고 날씨 API를 호출.

# 3. **프롬프트 설계**
#    - 에이전트에게 역할, 목표, 제약을 어떻게 지시할지 배웁니다.
#    - 예: “초보자에게 설명하듯이, 예시를 들어 한국어로 답해줘.”

# 4. **구조화된 출력**
#    - 답변을 JSON, 표, 체크리스트처럼 일정한 형식으로 받는 법을 배웁니다.
#    - 예:
#    ```json
#    {
#      "task": "날씨 확인",
#      "result": "맑음",
#      "confidence": "높음"
#    }
#    ```

# 정리하면 **모델 → 도구 → 프롬프트 → 구조화된 출력** 순서가 좋습니다.  
# 처음에는 간단한 “질문 답변 에이전트”를 만들고, 그다음 도구를 하나씩 붙여보는 방식으로 연습하세요.
