from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.memory.chroma_store import MemoryStore
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_service import generate_response, stream_response

router = APIRouter(prefix="/api", tags=["chat"])
memory = MemoryStore()


@router.post("/chat")
def chat(request: ChatRequest):
    memories = memory.search(request.message, limit=3)
    context = "\n".join([m["text"] for m in memories])
    prompt = f"Relevant memory:\n{context}\n\nUser: {request.message}"

    history = [m.model_dump() for m in request.history]
    if request.stream:
        return StreamingResponse(stream_response(prompt, history), media_type="text/event-stream")

    response = generate_response(prompt, history)
    return ChatResponse(response=response, model="gemma3", used_memory=[m["text"] for m in memories])
