from PyQt5.QtCore import QObject

from typing import Any

# Base Model
class TargetModel(QObject):
    
    # Initialize
    def __init__(self, IPAddress: str = "", hostName: str = "", SSHKey: str = "", osVersionName: str = ""):
        super().__init__()
        self.IPAddress = IPAddress
        self.hostName = hostName
        self.SSHKey = SSHKey
        self.osVersionName = osVersionName

    # To prevent duplicate data (__eq__ and __hash__)
    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.IPAddress == other.IPAddress and self.hostName == other.hostName and self.SSHKey == other.SSHKey and self.osVersionName == other.osVersionName
    
    def __hash__(self) -> int:
        return hash((type(self), self.IPAddress, self.hostName, self.SSHKey, self.osVersionName))
    
    def toPayload(self) -> dict:
        return {
            "IPAddress": self.IPAddress,
            "hostName": self.hostName,
            "SSHKey": self.SSHKey,
            "osVersionName": self.osVersionName
        }