from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from ollama import chat


class State(TypedDict):
    question: str
    answer: str


def call_model(state: State) -> dict:
    response = chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": state["question"]}
        ]
    )
    return {"answer": response.message.content}


def main():
    graph = StateGraph(State)
    graph.add_node("call_model", call_model)
    graph.add_edge(START, "call_model")
    graph.add_edge("call_model", END)
    compiled = graph.compile()

    question = input("Ask a question: ")
    result = compiled.invoke({"question": question, "answer": ""})
    print(f"\nAnswer: {result['answer']}")


if __name__ == "__main__":
    main()
