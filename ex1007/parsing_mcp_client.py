"""
실행 순서
1. .env에서 OpenAI API 설정을 불러온다.
2. parsing_mcp_server.py를 stdio 방식으로 실행하여 MCP에 연결한다.
3. 서버가 제공하는 문서 파싱 도구 목록을 가져온다.
4. MCP 도구를 GPT-5.5 기반 LangChain 에이전트에 등록한다.
5. 에이전트가 대상 문서에 맞는 MCP 도구를 호출하고 결과를 요약한다.

주요 기능
- 로컬 MCP 서버의 도구를 LangChain 도구로 변환하여 에이전트에 연결한다.
- 지정한 PDF 등의 문서를 MCP 서버에서 파싱하고 최종 요약 결과를 출력한다.
"""

import asyncio
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter


PROJECT_DIR = Path(__file__).resolve().parents[1]
#  MCP서버 가져와서 실행함.
MCP_SERVER = PROJECT_DIR / "parsing_mcp_server.py"
SAMPLE_DOCUMENT = PROJECT_DIR / "sample/천안캠퍼스_캡스톤_프로젝트.pdf" #두번째샘플
# SAMPLE_DOCUMENT = PROJECT_DIR / "pre-requirments.txt"  #첫번째샘플
 

async def main():
    load_dotenv(PROJECT_DIR / ".env")

    # Path 객체를 넘기면 FastMCP가 로컬 서버를 stdio 방식으로 실행합니다.
    async with MCPAdapter(MCP_SERVER) as adapter:
        tools = await adapter.list_tools()

        print("MCP Tools:")
        for tool in tools:
            print("-", tool.name)

        # *** 에이전트 생성시 툴로 가져와서 등록  ***
        agent = create_agent(
            model="openai:gpt-5.5",
            tools=tools,
        )

        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            f"MCP 도구를 사용해서 {SAMPLE_DOCUMENT} 문서를 파싱하고 "
                            "결과를 간단히 요약해 줘."
                        ),
                    }
                ]
            }
        )

        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())


# 두번째 결과

# (ex1007) D:\han_skc1001\agent\ex1007>uv run docs\test1.py         
# D:\han_skc1001\agent\ex1007\docs\test1.py:6: LangChainBetaWarning: `langchain.mcp` is in beta. It is actively being worked on, so the API may change.
#   from langchain.mcp import MCPAdapter
# MCP Tools:
# - parse_and_normalize_document
# - batch_parse_directory
# 문서 파싱이 완료되었습니다. 간단 요약은 아래와 같습니다.

# ## 요약

# 해당 PDF는 **“천안캠퍼스 캡스톤 프로젝트”** 관련 문서로, A조부터 D조까지 총 4개 조의 프로젝트 주제, 핵심 결과물, 조원 명단을 정리한 표 형식의 자료입니다.

# ### 조별 프로젝트 주제

# - **A조**
#   - Ontology 기반 제조 Product 정보 생성 및 등록 자동화
#   - 핵심 결과물: 웹 데모

# - **B조**
#   - 고객 요구사항 기반 시스템 기능/데이터 모델 자동 설계 Agent 기술
#   - 핵심 결과물: 설계 자동화 웹 데모

# - **C조**
#   - 프로젝트 산출물 기반 제조 설비 지식 자산화 Agent
#   - 핵심 결과물: 지식 베이스 구축 및 검색·Q&A·웹 데모

# - **D조**
#   - 이상정보 기반 원인·대응정보 생성 Agent
#   - 핵심 결과물: 이상 대응 지원 웹 데모

# ### 조원 구성

# 문서에는 각 조별로 조원 명단이 포함되어 있으며, 예를 들어 A조는 김대영, 구보회, 박건화, 서유진, 장혁 등으로 구성되어 있습니다.

# 전체적으로 이 문서는 **제조/설비/고객 요구사항/프로젝트 산출물 등을 AI Agent와 웹 데모 형태로 구현하는 캡스톤 프로젝트 주제 및 팀 구성표**로 볼 수 있습니다.

# ----------------------------

# 첫번째 결과
# (ex1007) D:\han_skc1001\agent\ex1007>uv run docs\test1.py       
# D:\han_skc1001\agent\ex1007\docs\test1.py:6: LangChainBetaWarning: `langchain.mcp` is in beta. It is actively being worked on, so the API may change.
#   from langchain.mcp import MCPAdapter
# MCP Tools:
# - parse_and_normalize_document
# - batch_parse_directory
# 문서 `D:\han_skc1001\agent\ex1007\pre-requirments.txt` 파싱 결과, 내용은 **Python/LangChain 기반 개발 환경에 필요한 패키지 목록**으로 보입니다.

# 주요 항목은 다음과 같습니다.

# - Jupyter 실행 관련: `ipykernel`
# - 데이터 처리: `pandas`
# - 환경변수 관리: `python-dotenv`
# - LangChain/OpenAI 연동: `langchain`, `langchain-openai`
# - LangGraph 관련: `langgraph`, `langgraph-cli[inmem]`
# - 그래프 시각화/처리: `grandalf`
# - 검색/외부 도구 연동: `langchain-tavily`, `tools`
# - MCP 및 자동화 관련: `fastmcp`, `langchain[mcp]`
# - 문서 변환/파싱: `markitdown`
# - 데이터 검증/모델링: `pydantic`

# 간단히 말해, 이 문서는 **LangChain + LangGraph + MCP 기반 에이전트 개발을 위한 Python 의존성 목록(requirements)** 입니다.
