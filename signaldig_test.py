import asyncio
import os
import httpx

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():
    key = os.environ.get("SIGNALDIG_API_KEY")
    if not key:
        raise RuntimeError("Missing SIGNALDIG_API_KEY")

    async with httpx.AsyncClient(
        headers={"Authorization": f"Bearer {key}"}
    ) as client:
        async with streamable_http_client(
            "https://mcp.signaldig.com/mcp",
            http_client=client
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.list_tools()

                print("SignalDig MCP connected!")
                for tool in result.tools:
                    print("-", tool.name)


if __name__ == "__main__":
    asyncio.run(main())
