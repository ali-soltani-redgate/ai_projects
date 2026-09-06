
from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

# Use Haiku model
model = ChatAnthropic(model_name="claude-haiku-4-5", timeout=600, stop=[])
response = model.invoke("What is the capital of France?")
print(response.content)

