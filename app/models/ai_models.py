from pydantic import BaseModel
from typing import Dict, List


class AgentStateModel(BaseModel):

    issue: str
    logs: List[str] = []
    jira_context: List[Dict] = []
    k8s_context: List[Dict] = []
    dependency_graph: Dict = {}
    memory: List[Dict] = []
    timeline: List[Dict] = []
    rca: str = ""


class EmbeddingDocument(BaseModel):

    content: str
    embedding: List[float]