from models.target import TargetList
from pydantic import BaseModel


class SelectedHardenModel(BaseModel):
    playbooks: list[str]
    targets: TargetList


class AutoHardenModel(BaseModel):
    targets: TargetList
