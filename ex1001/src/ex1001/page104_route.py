from operator import add
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    messages: Annotated[list[str], add]
    # 출력메세지 확인하기
    # messages: list[str]


def chatbot(state: State) -> dict[str, list[str]]:
    """마지막 사용자 메시지에 간단히 답합니다."""
    question = state["messages"][-1]
    return {"messages": [f"'{question}'에 대한 답변입니다."]}


def routing_function(state: State) -> bool:
    """마지막 메시지가 길면 요약 노드로, 아니면 종료로 보냅니다."""
    return len(state["messages"][-1]) > 1000


def summary(state: State) -> dict[str, list[str]]:
    """긴 답변을 짧게 줄여 저장합니다."""
    message = state["messages"][-1]
    return {"messages": [f"요약: {message[:100]}..."]}


graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_node("summary", summary)

graph.add_edge(START, "chatbot")
graph.add_conditional_edges(
    "chatbot",
    routing_function,
    {True: "summary", False: END},
)
graph.add_edge("summary", END)

app = graph.compile()
print(app.get_graph().draw_mermaid())
print("^^^라우터 챗봇서비스를 시작합니다 ^^^")

if __name__ == "__main__":
    result = app.invoke({"messages": ["안녕하세요"]})
    print(result)

# ----- 실행방법1 -----
# 프로젝트 루트에서 실행: 파이썬 모듈, 단위파일 실행하기
# 프로젝트 초기화 이루에 단일파일 실행.
# uv run python -m ex1001.page104_route

# ----- 실행방법2 -----
# 파일 경로로 직접 실행: __main__단위파일 실행하기
# uv run src/ex1001/page104_route.py