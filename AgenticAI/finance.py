from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools



def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(), DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Make use of the tools whenever necessary and possible. Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )

from dotenv import load_dotenv
load_dotenv()

agent=build_agent()
agent.print_response("MSFT stock price in INR and analyst recomendation")

