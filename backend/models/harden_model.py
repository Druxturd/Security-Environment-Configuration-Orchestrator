from models.target import TargetList
from pydantic import BaseModel


class SelectedHardenModel(BaseModel):
    controls: list[dict]
    targets: TargetList


class AutoHardenModel(BaseModel):
    targets: TargetList
