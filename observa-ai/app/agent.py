from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict

from app.services.query_generator import generate_query
from app.services.log_service import get_logs


# ✅ Define State
class AgentState(TypedDict):
    issue: str
    keyword: str
    logs: List[Dict]
    analysis: str
    decision: str
    result: str


# ✅ Node 1 — Context + Query
def context_node(state: AgentState):
    issue = state["issue"]

    # ✅ TEMP SAFE (replace with LLM later)
    keyword = generate_query(issue)

    return {**state, "keyword": keyword}


# ✅ Node 2 — Fetch Logs
def log_node(state: AgentState):
    logs = get_logs(state["keyword"])

    return {**state, "logs": logs}


# ✅ Node 3 — Analyze Logs
def analyze_node(state: AgentState):
    logs = state["logs"]

    if not logs:
        return {**state, "analysis": "No logs found"}

    messages = [log.get("message", "") for log in logs if "message" in log]

    analysis = " | ".join(messages[:5])

    return {**state, "analysis": analysis}


# ✅ Node 4 — Decision Engine
def decision_node(state: AgentState):
    text = state.get("analysis", "").lower()

    if "timeout" in text:
        decision = "db"
    elif "null" in text:
        decision = "code"
    else:
        decision = "general"

    return {**state, "decision": decision}


# ✅ Node 5 — RCA Generator
def rca_node(state: AgentState):
    decision = state["decision"]

    if decision == "db":
        result = "Possible DB latency issue. Check slow queries or missing indexes."

    elif decision == "code":
        result = "Null pointer detected. Check validations."

    else:
        result = "General issue. More investigation needed."

    return {**state, "result": result}


# ✅ Build Graph
builder = StateGraph(AgentState)

builder.add_node("extract_context", context_node)
builder.add_node("fetch_logs", log_node)           # ✅ fixed
builder.add_node("analyze_logs", analyze_node)     # ✅ fixed
builder.add_node("decide_action", decision_node)   # ✅ fixed
builder.add_node("generate_rca", rca_node)         # ✅ fixed

builder.set_entry_point("extract_context")

builder.add_edge("extract_context", "fetch_logs")
builder.add_edge("fetch_logs", "analyze_logs")
builder.add_edge("analyze_logs", "decide_action")
builder.add_edge("decide_action", "generate_rca")
builder.add_edge("generate_rca", END)

graph = builder.compile()

