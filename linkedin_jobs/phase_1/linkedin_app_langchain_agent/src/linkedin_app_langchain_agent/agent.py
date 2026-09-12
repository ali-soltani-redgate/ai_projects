
import os

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langfuse import Langfuse, get_client
from langfuse.langchain import CallbackHandler

from dotenv import load_dotenv
load_dotenv()


def setup_langfuse() -> CallbackHandler:

    # Initialize Langfuse with host from environment
    Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST", "http://localhost:3000"),
        debug=True
    )
    """
    Setup and return a Langfuse callback handler. It loads the API keys from the environment variables automatically.

    Returns:
        CallbackHandler: The initialized Langfuse callback handler.
    """

    # Get the configured client instance
    langfuse = get_client()

    # Check that the connection works
    if langfuse.auth_check():
        print("Langfuse connected successfully!")
    else:
        print("Langfuse authentication failed!")

    # Initialize the Langfuse handler
    langfuse_handler = CallbackHandler()

    return langfuse_handler


langfuse_handler = setup_langfuse()
# Use Haiku model
model = ChatAnthropic(model_name="claude-sonnet-4-5", timeout=600, stop=[])
agent = create_agent(model)
user_prompt = "What is the capital of France?"

# Run your chain with Langfuse tracing
response = agent.invoke(
    {"messages": [HumanMessage(content=user_prompt)]},
    config={"callbacks": [langfuse_handler]})
# Langchain returns the state of the agent's conversation, so the last message is the most recent response.
content = response["messages"][-1].content
print(content)

# Ensure all buffered events are sent to Langfuse before the script exits
get_client().flush()
