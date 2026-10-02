from langgraph.graph import StateGraph, MessagesState, START, END
from dotenv import load_dotenv
load_dotenv()

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

# 실행
result = graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
print(result)
print(f"AIMessage: {result["messages"][-1].content}")
