"""Docs Gap — run from a Vision-Agents accelerate checkout, or via getstream agents.

    uv run docs_gap.py
    uv run docs_gap.py "When will a message have text: \"\" ?"
"""

import asyncio
import logging
import os
import sys
import webbrowser

from dotenv import load_dotenv
from vision_agents.core import Agent
from vision_agents.plugins import stream

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

load_dotenv()

USER_ID = os.environ.get("DOCS_GAP_USER_ID", "seetha")

QUESTION = 'When will a Chat message have text: "" ? Check official docs, then the code.'


async def main(question: str) -> None:
    llm = stream.Accelerated(config="docs-gap", user_id=USER_ID)
    agent = Agent(config="docs-gap", llm=llm)

    async with agent.chat():
        dashboard = os.environ.get("DASHBOARD_BASE_URL")
        if dashboard:
            url = f"{dashboard.rstrip('/')}/sessions/{llm.router_session_id}"
            print(f"[dashboard: {url}]", flush=True)
            webbrowser.open(url, 2)

        await ask_here(agent, question)


async def ask_here(agent: Agent, question: str) -> None:
    asking = question
    while asking:
        connect = ""
        async for event in agent.ask(asking):
            if event.type == "agent_speech_delta":
                print(event.text, end="", flush=True)
            elif event.type == "authorization_required":
                connect = event.url
                print(f"\n[{event.text}: {event.url}]", flush=True)
            elif event.type == "delegated":
                print(f"\n[handed to {event.skill}]", flush=True)
            elif event.type == "task_settled":
                if event.error:
                    print(f"\n[{event.skill} failed: {event.error}]")
            elif event.type == "error":
                print(f"[{event.error}]", flush=True)
        print()
        asking = ""
        if connect:
            await asyncio.to_thread(input, "Press Enter once connected. ")
            asking = question


if __name__ == "__main__":
    asyncio.run(main(" ".join(sys.argv[1:]) or QUESTION))
