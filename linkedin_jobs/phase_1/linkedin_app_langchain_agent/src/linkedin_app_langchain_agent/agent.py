
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
load_dotenv()

# Use Haiku model
model = init_chat_model("claude-haiku-4-5")
response = model.invoke("What is the capital of France?")
print(response.content)

