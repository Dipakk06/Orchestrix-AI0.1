# Orchestrix AI

Orchestrix AI is a production-minded full-stack assistant platform with agentic orchestration, tool usage, long-term memory, and voice capabilities.

## Stack
- **Frontend:** Next.js 15, React, Tailwind CSS, Framer Motion
- **Backend:** FastAPI, LangGraph, PostgreSQL, ChromaDB
- **LLM:** Ollama local models (default: `gemma3`)
- **Voice:** Whisper STT + pyttsx3 TTS
- **Auth:** JWT utilities included

## Project Structure
```
orchestrix-ai/
├── frontend/
├── backend/
├── docs/
├── README.md
├── .env.example
└── docker-compose.yml
```

## Quick Start
1. Copy env file:
   ```bash
   cp .env.example .env
   ```
2. Start infra:
   ```bash
   docker compose up -d
   ```
3. Run backend:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
4. Run frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Windows PowerShell Commands
```powershell
cd orchestrix-ai
Copy-Item .env.example .env

docker compose up -d

cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# New PowerShell tab
cd orchestrix-ai\frontend
npm install
npm run dev
```

## API Endpoints
- `POST /api/chat`
- `POST /api/agent/run`
- `GET /api/conversations`
- `POST /api/memory/save`
- `GET /api/memory/search`
- `POST /api/voice/stt`
- `POST /api/voice/tts`
- `GET /api/tools`

## Testing
```bash
cd backend
pytest
```

## Notes
- Streaming chat is implemented via SSE when `stream=true`.
- `web_search`, `email_automation`, and `calendar_automation` are placeholders ready for real integrations.
- For production, rotate secrets, enable TLS, and deploy Ollama close to the API server.
