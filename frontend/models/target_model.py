from PyQt5.QtCore import QObject, pyqtSignal
from typing import List
import random


class TargetModel(QObject):
    # Signal to trigger function updateTotalTargetCounter in every menu when changes occur to the target list
    targetListUpdated = pyqtSignal()

    # Initialize
    def __init__(self, IPAddress: str = "", hostName: str = "", SSHKey: str = ""):
        super().__init__()
        self.IPAddress = IPAddress
        self.hostName = hostName
        self.SSHKey = SSHKey

    # Set empty target list will be used to store target list data from user input / CSV file
    targetList:List['TargetModel'] = []

    # Function to get target list data
    def getTargetList(self):
        return self.targetList
    
    # Function to get total target list
    def getCountTargetList(self):
        return len(self.getTargetList())
    
    # Function to set target list data
    def setTargetList(self, newData):
        self.targetList = newData

    # Function to clear target list data
    def clearTargetList(self):
        self.targetList.clear()

        # Send signal to trigger function updateTotalTargetCounter
        self.targetListUpdated.emit()

    # Temp function to add counter
    def addCounter(self):
        IPAdd = f"{random.randint(0,1000)}"
        hostNmae = f"{random.randint(2000,3000)}"
        SSHKey = f"{random.randint(4000,5000)}"
        newData = TargetModel(IPAdd, hostNmae, SSHKey)
        self.targetList.append(newData)
        
        self.targetListUpdated.emit()