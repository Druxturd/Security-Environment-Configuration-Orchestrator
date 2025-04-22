from pydantic import BaseModel


class Target(BaseModel):
    IPAddress: str
    hostName: str
    SSHKey: str

class TargetList(BaseModel):
    target_list: list[Target]