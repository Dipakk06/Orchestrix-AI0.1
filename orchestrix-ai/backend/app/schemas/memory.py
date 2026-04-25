from pydantic import BaseModel


class MemorySaveRequest(BaseModel):
    user_id: str
    text: str
    metadata: dict = {}


class MemorySearchResponse(BaseModel):
    results: list[dict]
