from langgraph.graph import END, START, MessagesState, StateGraph

def mock_llm2222222(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}


builder = StateGraph(MessagesState)
builder.add_node("mock_llm", mock_llm2222222)
builder.add_edge(START, "mock_llm")
builder.add_edge("mock_llm", END)

# langgraph.json에서 가져가는 그래프 export 변수입니다.
graph = builder.compile()


if __name__ == "__main__":
    result = graph.invoke(
        {"messages": [{"role": "user", "content": "hi! 그래프 테스트"}]}
    )
    print(result)
    print(f"AIMessage: {result['messages'][-1].content}")
    print(graph.get_graph().draw_mermaid())


# 실행명령어-1
# (ex1002) D:\han_skc1001\agent\ex1002>uv run langgraph dev

# 실행명령어-2
# (ex1002) D:\han_skc1001\agent\ex1002>uv run langgraph dev --port 8000

# ========================================
# 랭스미스 랭그래프 뛰우기 유의사항


# langgraph.json
    # {
    #   "dependencies": ["."],
    #   "graphs": {
    #     "test_graph22222": "./test_graph22222.py:graph"
    #   },
    #   "env": ".env"
    # }

# json파일 기준으로 같은경로에 .env파일이 있어야함.

# ========================================

# # LangSmith 
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# LANGCHAIN_API_KEY=${LANGCHAIN_API_KEY}
# LANGCHAIN_PROJECT="proj0929"
# PYTHONUTF8=1         
# ========================================

# PYTHONUTF8=1  
# 윈도우 한글문제는 UnicodeDecodeError: 'cp949' 오류해결 방법.

# ========================================

