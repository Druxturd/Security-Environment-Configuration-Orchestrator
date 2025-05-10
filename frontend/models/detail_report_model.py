from typing import Any


# class EventModel:
#     task: str
#     stdout: str

#     def __init__(self, task: str = "", stdout: str = ""):
#         self.task = task
#         self.stdout = stdout

#     def __getitem__(self, key):
#         return getattr(self, key)
    
#     def __setitem__(self, key, value):
#         setattr(self, key, value)
    
#     def __eq__(self, other: Any) -> bool:
#         if type(self) is not type(other):
#             return NotImplemented
#         return self.task == other.task and self.stdout == other.stdout
    
#     def __hash__(self) -> int:
#         return hash((type(self), self.task, self.stdout))

class PlaybookModel:
    name: str
    status: str
    rc: int
    stdout: str
    eventList: dict[str, list]

    def __init__(
        self,
        name: str = "",
        status: str = "",
        rc: int = 0,
        stdout: str = "",
        eventList: dict[str, list] = {}
    ):
        self.name = name
        self.status = status
        self.rc = rc
        self.stdout = stdout
        self.eventList = eventList
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.name == other.name and self.status == other.status and self.rc == other.rc and self.stdout == other.stdout and self.eventList == other.eventList
    
    def __hash__(self) -> int:
        return hash((type(self), self.name, self.status, self.rc, self.stdout, self.eventList))

class DetailReportModel:
    host: str
    ip: str
    playbooks: list

    def __init__(self, host: str = "", ip: str = "", playbooks: list = []):
        self.host = host
        self.ip = ip
        self.playbooks=playbooks
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.host == other.host and self.ip == other.ip and self.playbooks == other.playbooks
    
    def __hash__(self) -> int:
        return hash((type(self), self.host, self.ip, self.playbooks))