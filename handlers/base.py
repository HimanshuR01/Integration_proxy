from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseHandler(ABC):
    @abstractmethod
    async def __call__(self, action: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        pass