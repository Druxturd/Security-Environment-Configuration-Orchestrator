from typing import List, Set

from models.target_model import TargetModel
from PySide6.QtCore import QObject, Signal


class TargetDataManager(QObject):
    supported_os_version = {"debian": ["12"], "ubuntu": ["22", "24"]}

    target_list_updated = Signal()

    def __init__(self):
        super().__init__()
        self._target_list: List[TargetModel] = []
        self._unique_keys: Set[TargetModel] = set()

    def get_target_list(self) -> List[TargetModel]:
        return self._target_list

    def get_payload(self) -> dict:
        return {"target_list": [target.to_payload() for target in self._target_list]}

    def get_count_target_list(self) -> int:
        return len(self._target_list)

    def add_new_target(self, new_data: TargetModel) -> bool:
        if new_data in self._unique_keys:
            return False

        self._target_list.append(new_data)
        self._unique_keys.add(new_data)

        self.target_list_updated.emit()
        return True

    def remove_selected_target(self, target):
        self._target_list.remove(target)
        self._unique_keys.remove(target)

        self.target_list_updated.emit()

    def clear_target_list(self):
        self._target_list.clear()
        self._unique_keys.clear()

        self.target_list_updated.emit()
