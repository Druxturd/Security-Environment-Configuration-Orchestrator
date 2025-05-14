from PySide6.QtCore import QObject

from typing import Any

class TargetModel(QObject):
    def __init__(
            self,
            ip_address: str = "",
            host_name: str = "",
            ssh_username: str = "",
            ssh_private_key: str = "",
            ssh_port: str = "22",
            os_version_name: str = ""
    ):
        super().__init__()
        self.ip_address = ip_address
        self.host_name = host_name
        self.ssh_username = ssh_username
        self.ssh_private_key = ssh_private_key
        self.ssh_port = ssh_port
        self.os_version_name = os_version_name
        self.is_checked = False

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.ip_address == other.ip_address and self.host_name == other.host_name and self.ssh_username == other.ssh_username and self.ssh_private_key == other.ssh_private_key and self.ssh_port == other.ssh_port and self.os_version_name == other.os_version_name
    
    def __hash__(self) -> int:
        return hash((type(self), self.ip_address, self.host_name, self.ssh_username, self.ssh_private_key, self.ssh_port, self.os_version_name))
    
    def to_payload(self) -> dict:
        return {
            "ip_address": self.ip_address,
            "host_name": self.host_name,
            "ssh_username": self.ssh_username,
            "ssh_private_key": self.ssh_private_key,
            "ssh_port": self.ssh_port,
            "os_version_name": self.os_version_name
        }
    
    def to_selected_target_format(self) -> str:
        return f"{self.host_name} - {self.os_version_name} - {self.ip_address}"