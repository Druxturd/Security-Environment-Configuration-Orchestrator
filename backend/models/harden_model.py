from pydantic import BaseModel
from models.target import TargetList

class SelectedHardenModel(BaseModel):
    playbooks: list[str]
    targets: TargetList

class AutoHardenModel(BaseModel):
    targets: TargetList