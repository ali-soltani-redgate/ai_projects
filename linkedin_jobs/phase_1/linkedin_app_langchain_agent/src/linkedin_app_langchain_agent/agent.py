
import os

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langfuse import Langfuse, get_client
from langfuse.langchain import CallbackHandler

from dotenv import load_dotenv
load_dotenv()


def setup_langfuse() -> tuple[Langfuse, CallbackHandler]:
    """
    Setup and return the Langfuse client and callback handler. It loads the API keys from the environment variables automatically.

    Returns:
        tuple[Langfuse, CallbackHandler]: The configured Langfuse client and callback handler.
    """

    # Get the configured client instance
    langfuse = get_client()

    # Check that the connection works
    if not langfuse.auth_check():
        raise RuntimeError("Langfuse authentication failed!")

    # Initialize the Langfuse handler
    langfuse_handler = CallbackHandler()

    return langfuse, langfuse_handler


def get_weather(city: str) -> str:
    """
    Get the weather for a given city.

    Args:
        city (str): The name of the city.

    Returns:
        str: The weather information for the city.
    """
    # Placeholder implementation, replace with actual weather API call
    return f"The weather in {city} is sunny."

def set_up_agent():
    """
    Set up and return a Langchain agent using the Haiku model.

    Returns:
        Agent: The initialized Langchain agent.
    """
    # Use Haiku model
    model = ChatAnthropic(model_name="claude-haiku-4-5", timeout=600, stop=[])
    agent = create_agent(model, tools=[get_weather])
    return agent


def call_agent(user_prompt: str, agent, langfuse_handler):
    """
    Call the Langchain agent with the given user prompt and Langfuse handler.

    Args:
        user_prompt (str): The user's input prompt.
        agent: The Langchain agent instance.
        langfuse_handler: The Langfuse callback handler.

    Returns:
        dict: The response from the agent.
    """
    return agent.invoke(
        {"messages": [HumanMessage(content=user_prompt)]},
        config={"callbacks": [langfuse_handler]})


def main():
    langfuse, langfuse_handler = setup_langfuse()
    agent = set_up_agent()

    user_prompt = "What is the weather in Cambridge?"
    response = call_agent(user_prompt, agent, langfuse_handler)
    # Langchain returns the state of the agent's conversation, so the last message is the most recent response.
    content = response["messages"][-1].content
    print(content)

    # Ensure all buffered events are sent to Langfuse before the script exits
    langfuse.flush()


if __name__ == "__main__":
    main()
