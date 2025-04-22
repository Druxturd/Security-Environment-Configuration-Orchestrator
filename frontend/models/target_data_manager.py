import json
from PyQt5.QtCore import QObject, pyqtSignal
from typing import List, Set
from models.target_model import TargetModel

class TargetDataManager(QObject):

    # Signal to trigger function updateTotalTargetCounter in every menu when changes occur to the target list
    targetListUpdated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._targetList: List[TargetModel] = []
        self._uniqueKeys: Set[TargetModel] = set()
    
    # Function to get target list data
    def getTargetList(self) -> List[TargetModel]:
        return self._targetList
    
    def getPayload(self) -> dict:
        return {
            "target_list": [target.toPayload() for target in self._targetList]
        }
    
    # Function to get total target list
    def getCountTargetList(self) -> int:
        return len(self._targetList)
    
    # Function to add a new target into target list data
    def addNewTarget(self, newData:TargetModel) -> bool:
        if newData not in self._uniqueKeys:
            self._targetList.append(newData)
            self._uniqueKeys.add(newData)

            # Send signal to trigger function updateTotalTargetCounter
            self.targetListUpdated.emit()
            return True # Success add new data
        return False # Duplicated data


    # Function to clear target list data
    def clearTargetList(self):
        self._targetList.clear()
        self._uniqueKeys.clear()

        # Send signal to trigger function updateTotalTargetCounter
        self.targetListUpdated.emit()