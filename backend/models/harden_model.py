from pydantic import BaseModel

from backend.models.target import TargetList


class SupportedOSModel(BaseModel):
    debian_11: dict
    debian_12: dict
    ubuntu_22: dict
    ubuntu_24: dict


class ControlModel(BaseModel):
    name: str
    os_version_name: SupportedOSModel


class SelectedHardenModel(BaseModel):
    controls: list[ControlModel]
    targets: TargetList


class SemiAutoHardenModel(BaseModel):
    controls: ControlModel
    targets: TargetList


class AutoHardenModel(BaseModel):
    targets: TargetList
