from typing import Any

from PySide6.QtCore import QObject


class PackageModel(QObject):
    def __init__(self, name: str = "", version: str = ""):
        super().__init__()
        self.name = name
        self.version = version

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.name == other.name and self.version == other.version

    def __hash__(self) -> int:
        return hash((type(self), self.name, self.version))

    def to_packages_to_update_format(self) -> dict:
        return {"name": self.name, "version": self.version}
