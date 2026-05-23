from pydantic import BaseModel
from typing import List, Dict, Optional


class TimelineEvent(BaseModel):

    timestamp: str
    event: str


class DeploymentRisk(BaseModel):

    risk: str
    reason: str


class RCAResponse(BaseModel):

    issue: str
    root_cause: str
    blast_radius: List[str]
    impacted_services: List[str]
    remediation: str
    confidence: str
    timeline: List[TimelineEvent]


class DashboardSummary(BaseModel):

    active_incidents: int
    healthy_services: int
    critical_services: int
    cluster_health: str


class IncidentModel(BaseModel):

    id: str
    service: str
    severity: str
    status: str