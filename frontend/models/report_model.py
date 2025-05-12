from os import name
from typing import Any
from pydantic import BaseModel


class PlaybookModel(BaseModel):
    name: str
    status: str
    rc: int
    playbook_start: list
    events: dict[str, list]
    recap: list
    stdout: str

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.name == other.name and self.status == other.status and self.rc == other.rc and self.playbook_start == other.playbook_start and self.events == other.events and self.recap == other.recap and self.stdout == other.stdout
    
    def __hash__(self) -> int:
        return hash((type(self), self.name, self.status, self.rc, self.playbook_start, self.events, self.recap, self.stdout))

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