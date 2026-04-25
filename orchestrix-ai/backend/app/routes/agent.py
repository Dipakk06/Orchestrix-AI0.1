from fastapi import APIRouter

from app.agents.graph import agent_graph
from app.schemas.agent import AgentRunRequest, AgentRunResponse

router = APIRouter(prefix="/api", tags=["agent"])


@router.post("/agent/run", response_model=AgentRunResponse)
def run_agent(request: AgentRunRequest):
    initial = {"objective": request.objective, "plan": [], "logs": [], "result": ""}
    result = agent_graph.invoke(initial)
    return AgentRunResponse(plan=result["plan"], result=result["result"], logs=result["logs"])
