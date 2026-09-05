import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessageChunk
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

linkedin_mcp_client = MultiServerMCPClient(
    {
        "linkedin": {
            "command": "uvx",
            "args": ["mcp-server-linkedin@latest"],
            "transport": "stdio",
        }
    }
)


async def main() -> None:
    tools = await linkedin_mcp_client.get_tools()

    agent = create_agent(
        model="anthropic:claude-sonnet-4-5",
        tools=tools,
        system_prompt=(
            "You are a helpful assistant that finds LinkedIn job listings. "
            "If a location name is ambiguous (e.g. Cambridge exists in the UK, "
            "Massachusetts, and Ontario), ask the user to confirm which one "
            "before searching, rather than guessing. "
            "For every job you present, fetch its job details so you can include "
            "the LinkedIn URL, and list results as a markdown list with the job "
            "title, company, location, and a link to the job in the form "
            "[View job](<url>)."
        ),
    )

    async for token, _metadata in agent.astream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Find me AI engineering jobs in Cambridge, UK.",
                }
            ]
        },
        stream_mode="messages",
    ):
        if isinstance(token, AIMessageChunk) and token.text:
            print(token.text, end="", flush=True)

    print()


if __name__ == "__main__":
    asyncio.run(main())
