import os
import asyncio
import logging

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from pathlib import Path

from agent_connector import start_agent_session, client_to_agent, agent_to_client


# Create the FastAPI app
app = FastAPI()
log = logging.getLogger("uvicorn")

# Serve static files
STATIC_DIR = Path("static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Define the root endpoint
@app.get("/")
async def root():
    """Serves the index.html"""
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# Define the request body schema
class MessageRequest(BaseModel):
    message: str

@app.post("/chat/{session_id}")
async def chat(req: MessageRequest, session_id: int):
    """
    Endpoint to stream chat responses as SSE.
    """
    session_id = str(session_id)
    log.info(f"Client #{session_id} connected.")
    
    queue = asyncio.Queue()
    
    # Start agent session
    live_events, live_request_queue = start_agent_session(session_id)

    # Start background tasks
    asyncio.create_task(client_to_agent(req.message, live_request_queue))
    asyncio.create_task(agent_to_client(queue, live_events))

    async def event_generator():
        while True:
            line = await queue.get()
            if line is None:
                break
            yield f"data: {line}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

