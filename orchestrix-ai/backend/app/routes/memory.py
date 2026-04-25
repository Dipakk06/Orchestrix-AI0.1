from fastapi import APIRouter, Query

from app.memory.chroma_store import MemoryStore
from app.schemas.memory import MemorySaveRequest, MemorySearchResponse

router = APIRouter(prefix="/api", tags=["memory"])
store = MemoryStore()


@router.post("/memory/save")
def save_memory(request: MemorySaveRequest):
    memory_id = store.save(request.user_id, request.text, request.metadata)
    return {"memory_id": memory_id, "status": "saved"}


@router.get("/memory/search", response_model=MemorySearchResponse)
def search_memory(query: str = Query(...), limit: int = Query(5, ge=1, le=20)):
    return MemorySearchResponse(results=store.search(query, limit))
