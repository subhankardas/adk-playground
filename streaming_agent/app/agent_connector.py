import asyncio
from dotenv import load_dotenv

from google.genai.types import (
    Part,
    Content,
)

from google.adk.runners import Runner
from google.adk.agents import LiveRequestQueue
from google.adk.agents.run_config import RunConfig
from google.adk.sessions.in_memory_session_service import InMemorySessionService

from google_search_agent.agent import root_agent


# Load Gemini API Key
load_dotenv()

APP_NAME = "SEARCH_AGENT_APP"
session_service = InMemorySessionService()


def start_agent_session(session_id: str):
    """Starts an agent session."""

    # Create a Session
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=session_id,
        session_id=session_id,
    )

    # Create a Runner
    runner = Runner(
        app_name=APP_NAME,
        agent=root_agent,
        session_service=session_service,
    )

    # Set response modality = TEXT
    run_config = RunConfig(response_modalities=["TEXT"])

    # Create a LiveRequestQueue for this session
    live_request_queue = LiveRequestQueue()

    # Start agent session
    live_events = runner.run_live(
        session=session,
        live_request_queue=live_request_queue,
        run_config=run_config,
    )
    return live_events, live_request_queue


async def client_to_agent(message, live_request_queue):
    """Client to agent communication."""
    
    # Send message to agent
    content = Content(role="user", parts=[Part.from_text(text=message)])
    live_request_queue.send_content(content=content)
    
    print(f"[CLIENT TO AGENT]: {message}")
    await asyncio.sleep(0)

    
async def agent_to_client(queue: asyncio.Queue, live_events):
    """Agent to client communication."""
    
    try:
        async for event in live_events:
            if event.turn_complete:
                print("[TURN COMPLETE]")
                await queue.put(None)  # Close stream

            if event.interrupted:
                print("[INTERRUPTED]")

            part = event.content and event.content.parts and event.content.parts[0]
            if not part or not event.partial:
                continue

            text = part.text
            if not text:
                continue

            print(f"[AGENT TO CLIENT]: {text}")
            
            # Split into lines and push each line
            for line in text.splitlines():
                await queue.put(line)

            await asyncio.sleep(0)
    except Exception as e:
        print(f"[AGENT ERROR]: {e}")
        await queue.put(None)

