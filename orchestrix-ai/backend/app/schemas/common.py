from pydantic import BaseModel


class APIMessage(BaseModel):
    role: str
    content: str
