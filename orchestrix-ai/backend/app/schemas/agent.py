from pydantic import BaseModel


class AgentRunRequest(BaseModel):
    user_id: str
    objective: str


class AgentRunResponse(BaseModel):
    plan: list[str]
    result: str
    logs: list[str]
