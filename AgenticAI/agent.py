from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True,
    )

from dotenv import load_dotenv
load_dotenv()

agent=build_agent()
agent.print_response("Is it safe to travel to UAE now?")

