from typing import Any

from models.target import TargetList
from pydantic import BaseModel


class PatchModel(BaseModel):
    playbook: str
    extra_vars: Any
    targets: TargetList
