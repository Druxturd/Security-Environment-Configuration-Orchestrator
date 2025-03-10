from PyQt5.QtCore import QObject, pyqtSignal
import random


class TargetModel(QObject):
    # This variable holds the single instance (singelton)
    _instance = None

    targetListUpdated = pyqtSignal()

    def __new__(cls, *args, **kwargs):
        # Check if the instance already exists
        if cls._instance is None:
            cls._instance = super(TargetModel, cls).__new__(cls)
        
        return cls._instance

    # Initialize
    def __init__(self, IPAddress: str = "", hostName: str = "", SSHKey: str = ""):
        super().__init__()
        self.IPAddress = IPAddress
        self.hostName = hostName
        self.SSHKey = SSHKey
        self.targetList = [] # Initialize an empty list

    # Function to get target list data
    def getTargetList(self):
        return self.targetList
    
    def getCountTargetList(self):
        return len(self.getTargetList())
    
    # Function to set target list data
    def setTargetList(self, newData):
        self.targetList = newData

    # Temp function to add counter
    def addCounter(self):
        IPAdd = f"{random.randint(0,1000)}"
        hostNmae = f"{random.randint(2000,3000)}"
        SSHKey = f"{random.randint(4000,5000)}"
        newData = TargetModel(IPAdd, hostNmae, SSHKey)
        self.targetList.append(newData)
        
        self.targetListUpdated.emit()