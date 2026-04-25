from typing import TypedDict

from langgraph.graph import END, StateGraph

from app.memory.chroma_store import MemoryStore
from app.services.llm_service import generate_response
from app.tools.registry import ToolRegistry


class AgentState(TypedDict):
    objective: str
    plan: list[str]
    logs: list[str]
    result: str


tools = ToolRegistry()
memory = MemoryStore()


def planner_node(state: AgentState) -> AgentState:
    objective = state["objective"]
    plan = [
        f"Analyze objective: {objective}",
        "Gather context from memory",
        "Execute required tool actions",
        "Synthesize final response",
    ]
    state["plan"] = plan
    state["logs"].append("Planner created a 4-step plan.")
    return state


def researcher_node(state: AgentState) -> AgentState:
    memories = memory.search(state["objective"], limit=3)
    state["logs"].append(f"Research agent fetched {len(memories)} memory items.")
    return state


def executor_node(state: AgentState) -> AgentState:
    calc = tools.run("calculator", {"expression": "2 + 2"})
    state["logs"].append(f"Executor ran calculator tool: {calc}")
    return state


def memory_node(state: AgentState) -> AgentState:
    memory.save("system", f"Objective handled: {state['objective']}", {"type": "run_log"})
    state["logs"].append("Memory agent persisted execution note.")
    return state


def final_node(state: AgentState) -> AgentState:
    state["result"] = generate_response(
        f"Objective: {state['objective']}\nPlan: {state['plan']}\nLogs: {state['logs']}"
    )
    return state


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("planner", planner_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("executor", executor_node)
    graph.add_node("memory", memory_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "executor")
    graph.add_edge("executor", "memory")
    graph.add_edge("memory", "final")
    graph.add_edge("final", END)
    return graph.compile()


agent_graph = build_graph()
