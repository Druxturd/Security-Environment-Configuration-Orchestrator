from typing import Any

from pydantic import BaseModel

from backend.models.target import TargetList


class PatchModel(BaseModel):
    playbook: str
    extra_vars: Any
    targets: TargetList
