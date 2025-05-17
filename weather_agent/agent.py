from google.adk.agents import Agent
from weather_agent.tools import get_weather

def create_agent() -> Agent:
    return Agent(
        name="weather_agent",
        model="gemini-2.0-flash",
        description=(
            "Agent to provide current weather information for a specified city."
        ),
        instruction=(
            "You are a helpful agent who can tell the weather of a specified city in a funny manner."
        ),
        tools=[get_weather],
    )
    
root_agent = create_agent()