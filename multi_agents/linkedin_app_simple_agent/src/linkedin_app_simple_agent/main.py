import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
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
        system_prompt="You are a helpful assistant that finds LinkedIn job listings.",
    )

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Find me software engineering jobs in Cambridge.",
                }
            ]
        }
    )

    print(result["messages"][-1].content_blocks)


if __name__ == "__main__":
    asyncio.run(main())
