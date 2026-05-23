from pydantic import BaseModel
from typing import List, Optional


class IncidentEntity(BaseModel):

    issue: str
    root_cause: str
    remediation: str
    confidence: Optional[str] = None


class SourceCodeEntity(BaseModel):

    file_path: str
    chunk: str


class KubernetesPodEntity(BaseModel):

    pod_name: str
    namespace: str
    status: str
    restart_count: int


class JiraIncidentEntity(BaseModel):

    ticket_id: str
    summary: str
    resolution: Optional[str] = None


class DependencyEntity(BaseModel):

    service_name: str
    dependencies: List[str]