from pydantic import BaseModel


class Target(BaseModel):
    ip_address: str
    host_name: str
    ssh_username: str
    ssh_private_key: str
    ssh_port: str
    os_version_name: str
    password: str


class TargetList(BaseModel):
    target_list: list[Target]
