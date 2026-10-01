from operator import add
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph


load_dotenv()


class InputState(TypedDict):
    """그래프에 전달하는 입력 상태입니다."""

    question: str


class OutputState(TypedDict):
    """그래프가 반환하는 출력 상태입니다."""

    answer: str


class OverallState(TypedDict):
    """그래프 내부에서 사용하는 전체 상태입니다."""

    messages: Annotated[list[str], add]
    question: str
    answer: str


def chatbot(state: InputState) -> OverallState:
    """사용자의 질문을 LLM에 전달하고 답변을 상태에 저장합니다."""

    question = state["question"]
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke(question)

    return {
        "question": question,
        "answer": str(response.content),
        "messages": [question, str(response.content)],
    }


graph_builder = StateGraph(
    OverallState,
    input_schema=InputState,
    output_schema=OutputState,
)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

app = graph_builder.compile()


if __name__ == "__main__":
    result = app.invoke({"question": "대한민국의 수도는 어디인가요?"})
    print(result)

# uv run python -m ex1001.page105_109