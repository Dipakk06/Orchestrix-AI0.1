from typing import List

from pydantic import BaseModel

from app.schemas.common import APIMessage


class ChatRequest(BaseModel):
    user_id: str
    message: str
    stream: bool = True
    history: List[APIMessage] = []


class ChatResponse(BaseModel):
    response: str
    model: str
    used_memory: list[str] = []
