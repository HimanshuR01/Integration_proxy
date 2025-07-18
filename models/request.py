from pydantic import BaseModel
from typing import Dict, Any

class IntegrationRequest(BaseModel):
    action: str
    parameters: Dict[str, Any]