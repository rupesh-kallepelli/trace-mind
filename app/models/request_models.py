from pydantic import BaseModel
from typing import Optional


class AnalyzeRequest(BaseModel):

    issue: str
    service_name: Optional[str] = None
    severity: Optional[str] = None
    namespace: Optional[str] = "default"