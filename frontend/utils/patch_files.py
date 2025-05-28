from enum import Enum, StrEnum


class PATCH_TYPE(StrEnum):
    CLOSE_PORT = "close_port.yml"
    MANAGE_SERVICES = "manage_services.yml"
    OPEN_PORT = "open_port.yml"
    UPDATE_INSTALL = "update_install.yml"

class PATCH_TYPE_TEXT(Enum):
    GET = {
        "close_port.yml": "Close Port(s)",
        "manage_services.yml": "Manage Service(s)",
        "open_port.yml": "Open Port(s)",
        "update_install.yml": "Update or Install to the latest"
    }
