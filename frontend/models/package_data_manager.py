from typing import List, Set

from models.package_model import PackageModel
from PySide6.QtCore import QObject, Signal


class PackageDataManager(QObject):
    package_list_updated = Signal()

    def __init__(self):
        super().__init__()
        self._package_list: List[PackageModel] = []
        self._unique_keys: Set[PackageModel] = set()

    def get_package_list(self) -> List[PackageModel]:
        return self._package_list

    def get_count_package_list(self) -> int:
        return len(self._package_list)

    def add_new_package(self, new_data: PackageModel) -> bool:
        if new_data in self._unique_keys:
            return False

        self._package_list.append(new_data)
        self._unique_keys.add(new_data)

        self.package_list_updated.emit()
        return True

    def clear_package_list(self):
        self._package_list.clear()
        self._unique_keys.clear()

        self.package_list_updated.emit()
