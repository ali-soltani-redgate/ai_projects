
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv()

# Use Haiku model
model = ChatAnthropic(model_name="claude-haiku-3-5", timeout=600, stop=[])
agent = create_agent(model)
user_prompt = "What is the capital of France?"
result = agent.invoke({"messages": [HumanMessage(content=user_prompt)]})
print(result)

