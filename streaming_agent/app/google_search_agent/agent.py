from google.adk.agents import Agent
from google.adk.tools import google_search

def create_agent() -> Agent:
    return Agent(
        name="basic_search_agent",
        model="gemini-2.0-flash-live-001",
        description="Agent to answer questions using Google Search.",
        instruction="You are an expert researcher. You always stick to the facts.",
        tools=[google_search],
    )
    
root_agent = create_agent()