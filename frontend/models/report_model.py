from typing import Any
from pydantic import BaseModel
from models.playbook_model import PlaybookModel

class ReportModel(BaseModel):
    host: str
    ip: str
    playbook_results: list[PlaybookModel]

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.host == other.host and self.ip == other.ip and self.playbook_results == other.playbook_results

    def __hash__(self) -> int:
        return hash((type(self), self.host, self.ip, self.playbook_results))