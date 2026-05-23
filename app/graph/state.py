from typing import TypedDict

class AgentState(TypedDict):

    issue: str
    logs: list
    jira_context: list
    k8s_context: list
    dependency_graph: dict
    deployment_risk: dict
    memory: list
    timeline: list
    rca: str