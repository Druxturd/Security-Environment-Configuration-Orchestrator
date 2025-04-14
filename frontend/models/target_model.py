from PyQt5.QtCore import QObject

class TargetModel(QObject):
    
    # Initialize
    def __init__(self, IPAddress: str = "", hostName: str = "", SSHKey: str = ""):
        super().__init__()
        self.IPAddress = IPAddress
        self.hostName = hostName
        self.SSHKey = SSHKey

    # To prevent duplicate data (__eq__ and __hash__)
    def __eq__(self, other):
        return (
            isinstance(other, TargetModel) and
            self.IPAddress == other.IPAddress and
            self.hostName == other.hostName and
            self.SSHKey == other.SSHKey
        )
    
    def __hash__(self):
        return hash((self.IPAddress, self.hostName, self.SSHKey))