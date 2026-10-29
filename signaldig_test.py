import asyncio
import os
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

async def main():
    key = os.environ.get("SIGNALDIG_API_KEY")
    if not key:
        raise RuntimeError("Missing SIGNALDIG_API_KEY GitHub secret")
    async with streamable_http_client(
        "https://mcp.signaldig.com/mcp",
        headers={"Authorization": f"Bearer {key}"},
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("SignalDig MCP connected. Available tools:")
            for tool in tools.tools:
                print("-", tool.name)

if __name__ == "__main__":
    asyncio.run(main())
