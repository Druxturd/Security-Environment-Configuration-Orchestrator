from enum import StrEnum


class PATCH_TYPE(StrEnum):
    CLOSE_PORT = "close_port.yml"
    MANAGE_SERVICES = "manage_services.yml"
    OPEN_PORT = "open_port.yml"
    UPDATE_INSTALL = "update_install.yml"
