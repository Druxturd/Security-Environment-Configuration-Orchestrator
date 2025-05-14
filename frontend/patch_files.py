from enum import StrEnum


class PATCH_ALL_HOST(StrEnum):
    MANAGE_SERVICES = "manage_services.yml"
    UPDATE_PORT = "update_port.yml"

class PATCH_SPECIFIC_HOST(StrEnum):
    UPDATER_LATEST = "updater_latest.yml"
    UPDATER_VERSION = "updater_version.yml"