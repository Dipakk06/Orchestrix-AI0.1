from fastapi import APIRouter

from app.tools.registry import ToolRegistry

router = APIRouter(prefix="/api", tags=["tools"])
registry = ToolRegistry()


@router.get("/tools")
def list_tools():
    return {"tools": registry.list_tools()}
