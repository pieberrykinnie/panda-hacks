import os

from langchain_openai import ChatOpenAI


def get_openai_client() -> ChatOpenAI:
    """Return a LangChain OpenAI chat client using the OPENAI_API_KEY env variable."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set.")
    return ChatOpenAI(api_key=api_key)


def minimal_planner_flow(prompt: str) -> str:
    """Stub planner: sends prompt to OpenAI and returns response text."""
    client = get_openai_client()
    response = client.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)

if __name__ == "__main__":
    print(minimal_planner_flow("What is a good study plan for 1 week?"))