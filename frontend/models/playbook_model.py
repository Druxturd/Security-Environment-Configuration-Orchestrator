from typing import Any

from pydantic import BaseModel


class PlaybookModel(BaseModel):
    name: str
    status: str
    rc: int
    playbook_start: list
    events: dict[str, list]
    recap: list
    stdout: str

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.name == other.name
            and self.status == other.status
            and self.rc == other.rc
            and self.playbook_start == other.playbook_start
            and self.events == other.events
            and self.recap == other.recap
            and self.stdout == other.stdout
        )

    def __hash__(self) -> int:
        return hash(
            (
                type(self),
                self.name,
                self.status,
                self.rc,
                self.playbook_start,
                self.events,
                self.recap,
                self.stdout,
            )
        )


class SelectedHardenPlaybookModel(PlaybookModel):
    harden_control: str

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return super().__eq__(other) and self.harden_control == other.harden_control

    def __hash__(self) -> int:
        return hash((super().__hash__(), self.harden_control))


class SemiHardenPlaybookModel(PlaybookModel):
    harden_control: dict

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return super().__eq__(other) and self.harden_control == other.harden_control

    def __hash__(self) -> int:
        return hash((super().__hash__(), self.harden_control))
