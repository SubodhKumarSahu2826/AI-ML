from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team


load_dotenv()


eng_agent=Agent(name="English Agent", role="You answer questions in English")
chi_agent=Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_agent=Agent(name="Hindi Agent", role="You answer questions in Hindi")

team_leader=Team(
    name="Translation Team",
    members=[eng_agent, chi_agent,hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must respond to answer the query intheir specific language. Do not route just one agent.
    
                    Output the response of all agent"""
)

team_leader.print_response("What is Capital of India?")





