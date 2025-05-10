from pydantic import BaseModel

class Target(BaseModel):
    IPAddress: str
    hostName: str
    SSHUsername: str
    SSHPort: str
    SSHKey: str
    osVersionName: str

class TargetList(BaseModel):
    target_list: list[Target]