# Streaming Agent - GigaChadGPT

A FastAPI-based experimental project integrating Google's AI Development Kit (ADK) with real-time streaming chat using Server-Sent Events (SSE). The frontend provides a simple chat interface to interact with a Gemini-based agent.

## Features

- 🔁 Bidirectional communication with Gemini agents via ADK.
- 📡 Real-time agent responses streamed to the UI using SSE.
- 💬 User-friendly chat UI styled with Bootstrap 5.
- 🧠 Uses Google's `genai` and `adk` libraries under the hood.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/adk-playground.git
cd adk-playground
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file and add your Google API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 5. Run the Application

```bash
uvicorn streaming_agent.app.main:app --reload
```

Then open your browser at [http://localhost:8000](http://localhost:8000)

## Project Structure

```
adk-playground/
├── streaming_agent/
│   ├── app/
│   │   ├── main.py               # FastAPI app with chat endpoint
│   │   ├── agent_connector.py    # ADK integration and streaming logic
│   │   └── static/
│   │       └── index.html        # Chat frontend
├── .env                          # API key and config
├── requirements.txt              # Python dependencies
└── README.md
```

## License

MIT
