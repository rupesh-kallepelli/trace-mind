from langgraph.graph import StateGraph, END
from app.graph.state import AgentState

from app.observability.log_service import LogService
from app.jira.jira_service import JiraService
from app.k8s.k8s_service import KubernetesService
from app.memory.vector_memory import VectorMemory
from app.services.dependency_service import DependencyService
from app.services.deployment_service import DeploymentRiskService
from app.services.timeline_service import TimelineService
from app.services.rca_service import RCAService

workflow = StateGraph(AgentState)

def logs_node(state):

    return {
        "logs": LogService.fetch_logs(
            state["issue"]
        )
    }

def jira_node(state):

    return {
        "jira_context": JiraService.fetch_incidents()
    }

def k8s_node(state):

    return {
        "k8s_context": KubernetesService.cluster_analysis()
    }

def memory_node(state):

    return {
        "memory": VectorMemory.search_similar(
            state["issue"]
        )
    }

def dependency_node(state):

    return {
        "dependency_graph": DependencyService.build_graph()
    }

def deployment_node(state):

    return {
        "deployment_risk": DeploymentRiskService.analyze()
    }

def timeline_node(state):

    return {
        "timeline": TimelineService.reconstruct(
            state["logs"]
        )
    }

def rca_node(state):

    context = {
        "issue": state["issue"],
        "logs": state["logs"],
        "jira": state["jira_context"],
        "k8s": state["k8s_context"],
        "memory": state["memory"],
        "dependencies": state["dependency_graph"],
        "deployment": state["deployment_risk"],
        "timeline": state["timeline"]
    }

    rca = RCAService.generate(context)

    return {
        "rca": rca
    }

workflow.add_node("logs_node", logs_node)
workflow.add_node("jira_node", jira_node)
workflow.add_node("k8s_node", k8s_node)
workflow.add_node("memory_node", memory_node)
workflow.add_node("dependency_node", dependency_node)
workflow.add_node("deployment_node", deployment_node)
workflow.add_node("timeline_node", timeline_node)
workflow.add_node("rca_node", rca_node)

workflow.set_entry_point("logs_node")

workflow.add_edge("logs_node", "jira_node")
workflow.add_edge("jira_node", "k8s_node")
workflow.add_edge("k8s_node", "memory_node")
workflow.add_edge("memory_node", "dependency_node")
workflow.add_edge("dependency_node", "deployment_node")
workflow.add_edge("deployment_node", "timeline_node")
workflow.add_edge("timeline_node", "rca_node")
workflow.add_edge("rca_node", END)

graph = workflow.compile()