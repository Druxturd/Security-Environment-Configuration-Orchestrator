from enum import Enum


class SECTION_1_HARDEN_CONTROL(Enum):
    FILESYSTEM_KERNEL_MODULES = {
        "name": "Filesystem kernel modules",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_1_1": "true",
                "deb12cis_rule_1_1_1_2": "true",
                "deb12cis_rule_1_1_1_3": "true",
                "deb12cis_rule_1_1_1_4": "true",
                "deb12cis_rule_1_1_1_5": "true",
                "deb12cis_rule_1_1_1_6": "true",
                "deb12cis_rule_1_1_1_7": "true",
                "deb12cis_rule_1_1_1_8": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_1_1": "true",
                "ubtu22cis_rule_1_1_1_2": "true",
                "ubtu22cis_rule_1_1_1_3": "true",
                "ubtu22cis_rule_1_1_1_4": "true",
                "ubtu22cis_rule_1_1_1_5": "true",
                "ubtu22cis_rule_1_1_1_6": "true",
                "ubtu22cis_rule_1_1_1_7": "true",
                "ubtu22cis_rule_1_1_1_8": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_1_1": "true",
                "ubtu24cis_rule_1_1_1_2": "true",
                "ubtu24cis_rule_1_1_1_3": "true",
                "ubtu24cis_rule_1_1_1_4": "true",
                "ubtu24cis_rule_1_1_1_5": "true",
                "ubtu24cis_rule_1_1_1_6": "true",
                "ubtu24cis_rule_1_1_1_7": "true",
                "ubtu24cis_rule_1_1_1_8": "true",
                "ubtu24cis_rule_1_1_1_9": "true",
                "ubtu24cis_rule_1_1_1_10": "true",
            },
        },
    }
    FILESYSTEM_TMP = {
        "name": "Filesystem /tmp",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_1_1": "true",
                "deb12cis_rule_1_1_2_1_2": "true",
                "deb12cis_rule_1_1_2_1_3": "true",
                "deb12cis_rule_1_1_2_1_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_1_1": "true",
                "ubtu22cis_rule_1_1_2_1_2": "true",
                "ubtu22cis_rule_1_1_2_1_3": "true",
                "ubtu22cis_rule_1_1_2_1_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_1_1": "true",
                "ubtu24cis_rule_1_1_2_1_2": "true",
                "ubtu24cis_rule_1_1_2_1_3": "true",
                "ubtu24cis_rule_1_1_2_1_4": "true",
            },
        },
    }
    FILESYSTEM_DEV_SHM = {
        "name": "Filesystem /dev/shm",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_2_1": "true",
                "deb12cis_rule_1_1_2_2_2": "true",
                "deb12cis_rule_1_1_2_2_3": "true",
                "deb12cis_rule_1_1_2_2_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_2_1": "true",
                "ubtu22cis_rule_1_1_2_2_2": "true",
                "ubtu22cis_rule_1_1_2_2_3": "true",
                "ubtu22cis_rule_1_1_2_2_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_2_1": "true",
                "ubtu24cis_rule_1_1_2_2_2": "true",
                "ubtu24cis_rule_1_1_2_2_3": "true",
                "ubtu24cis_rule_1_1_2_2_4": "true",
            },
        },
    }
    FILESYSTEM_HOME = {
        "name": "Filesystem /home",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_3_1": "true",
                "deb12cis_rule_1_1_2_3_2": "true",
                "deb12cis_rule_1_1_2_3_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_3_1": "true",
                "ubtu22cis_rule_1_1_2_3_2": "true",
                "ubtu22cis_rule_1_1_2_3_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_3_1": "true",
                "ubtu24cis_rule_1_1_2_3_2": "true",
                "ubtu24cis_rule_1_1_2_3_3": "true",
            },
        },
    }
    FILESYSTEM_VAR = {
        "name": "Filesystem /var",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_4_1": "true",
                "deb12cis_rule_1_1_2_4_2": "true",
                "deb12cis_rule_1_1_2_4_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_4_1": "true",
                "ubtu22cis_rule_1_1_2_4_2": "true",
                "ubtu22cis_rule_1_1_2_4_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_4_1": "true",
                "ubtu24cis_rule_1_1_2_4_2": "true",
                "ubtu24cis_rule_1_1_2_4_3": "true",
            },
        },
    }
    FILESYSTEM_VAR_TMP = {
        "name": "Filesystem /var/tmp",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_5_1": "true",
                "deb12cis_rule_1_1_2_5_2": "true",
                "deb12cis_rule_1_1_2_5_3": "true",
                "deb12cis_rule_1_1_2_5_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_5_1": "true",
                "ubtu22cis_rule_1_1_2_5_2": "true",
                "ubtu22cis_rule_1_1_2_5_3": "true",
                "ubtu22cis_rule_1_1_2_5_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_5_1": "true",
                "ubtu24cis_rule_1_1_2_5_2": "true",
                "ubtu24cis_rule_1_1_2_5_3": "true",
                "ubtu24cis_rule_1_1_2_5_4": "true",
            },
        },
    }
    FILESYSTEM_VAR_LOG = {
        "name": "Filesystem /var/log",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_6_1": "true",
                "deb12cis_rule_1_1_2_6_2": "true",
                "deb12cis_rule_1_1_2_6_3": "true",
                "deb12cis_rule_1_1_2_6_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_6_1": "true",
                "ubtu22cis_rule_1_1_2_6_2": "true",
                "ubtu22cis_rule_1_1_2_6_3": "true",
                "ubtu22cis_rule_1_1_2_6_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_6_1": "true",
                "ubtu24cis_rule_1_1_2_6_2": "true",
                "ubtu24cis_rule_1_1_2_6_3": "true",
                "ubtu24cis_rule_1_1_2_6_4": "true",
            },
        },
    }
    FILESYSTEM_VAR_LOG_AUDIT = {
        "name": "FIlesystem /var/log/audit",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_1_2_7_1": "true",
                "deb12cis_rule_1_1_2_7_2": "true",
                "deb12cis_rule_1_1_2_7_3": "true",
                "deb12cis_rule_1_1_2_7_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_1_2_7_1": "true",
                "ubtu22cis_rule_1_1_2_7_2": "true",
                "ubtu22cis_rule_1_1_2_7_3": "true",
                "ubtu22cis_rule_1_1_2_7_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_1_2_7_1": "true",
                "ubtu24cis_rule_1_1_2_7_2": "true",
                "ubtu24cis_rule_1_1_2_7_3": "true",
                "ubtu24cis_rule_1_1_2_7_4": "true",
            },
        },
    }
    PACKAGE_MANAGEMENT = {
        "name": "Package Management",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_2_1_1": "true",
                "deb12cis_rule_1_2_1_2": "true",
                "deb12cis_rule_1_2_2_1": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_2_1_1": "true",
                "ubtu22cis_rule_1_2_1_2": "true",
                "ubtu22cis_rule_1_2_2_1": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_2_1_1": "true",
                "ubtu24cis_rule_1_2_1_2": "true",
                "ubtu24cis_rule_1_2_2_1": "true",
            },
        },
    }
    MANDATORY_ACCESS_CONTROLL_APPARMOR = {
        "name": "Mandatory Access Control AppArmor",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_3_1_1": "true",
                "deb12cis_rule_1_3_1_2": "true",
                "deb12cis_rule_1_3_1_3": "true",
                "deb12cis_rule_1_3_1_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_3_1_1": "true",
                "ubtu22cis_rule_1_3_1_2": "true",
                "ubtu22cis_rule_1_3_1_3": "true",
                "ubtu22cis_rule_1_3_1_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_3_1_1": "true",
                "ubtu24cis_rule_1_3_1_2": "true",
                "ubtu24cis_rule_1_3_1_3": "true",
                "ubtu24cis_rule_1_3_1_4": "true",
            },
        },
    }
    CONFIGURE_BOOTLOADER = {
        "name": "Configure Bootloader",
        "os_version_name": {
            "debian_12": {"deb12cis_rule_1_4_1": "true", "deb12cis_rule_1_4_2": "true"},
            "ubuntu_22": {
                "ubtu22cis_rule_1_4_1": "true",
                "ubtu22cis_rule_1_4_2": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_4_1": "true",
                "ubtu24cis_rule_1_4_2": "true",
            },
        },
    }
    ADDITIONAL_HARDENING = {
        "name": "Additional Hardening (ASLR, ptrace_scope restriction, core dumps,  prelink, and autometic error reporting)",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_5_1": "true",
                "deb12cis_rule_1_5_2": "true",
                "deb12cis_rule_1_5_3": "true",
                "deb12cis_rule_1_5_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_5_1": "true",
                "ubtu22cis_rule_1_5_2": "true",
                "ubtu22cis_rule_1_5_3": "true",
                "ubtu22cis_rule_1_5_4": "true",
                "ubtu22cis_rule_1_5_5": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_5_1": "true",
                "ubtu24cis_rule_1_5_2": "true",
                "ubtu24cis_rule_1_5_3": "true",
                "ubtu24cis_rule_1_5_4": "true",
                "ubtu24cis_rule_1_5_5": "true",
            },
        },
    }
    CONFIGURE_COMMAND_LIEN_WARNING_BANNERS = {
        "name": "Configure Command Line Warning Banners",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_6_1": "true",
                "deb12cis_rule_1_6_2": "true",
                "deb12cis_rule_1_6_3": "true",
                "deb12cis_rule_1_6_4": "true",
                "deb12cis_rule_1_6_5": "true",
                "deb12cis_rule_1_6_6": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_6_1": "true",
                "ubtu22cis_rule_1_6_2": "true",
                "ubtu22cis_rule_1_6_3": "true",
                "ubtu22cis_rule_1_6_4": "true",
                "ubtu22cis_rule_1_6_5": "true",
                "ubtu22cis_rule_1_6_6": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_6_1": "true",
                "ubtu24cis_rule_1_6_2": "true",
                "ubtu24cis_rule_1_6_3": "true",
                "ubtu24cis_rule_1_6_4": "true",
                "ubtu24cis_rule_1_6_5": "true",
                "ubtu24cis_rule_1_6_6": "true",
            },
        },
    }
    GNOME_DISPLAY_MANAGER = {
        "name": "Gnome Display Manager",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_1_7_1": "true",
                "deb12cis_rule_1_7_2": "true",
                "deb12cis_rule_1_7_3": "true",
                "deb12cis_rule_1_7_4": "true",
                "deb12cis_rule_1_7_5": "true",
                "deb12cis_rule_1_7_6": "true",
                "deb12cis_rule_1_7_7": "true",
                "deb12cis_rule_1_7_8": "true",
                "deb12cis_rule_1_7_9": "true",
                "deb12cis_rule_1_7_10": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_1_7_1": "true",
                "ubtu22cis_rule_1_7_2": "true",
                "ubtu22cis_rule_1_7_3": "true",
                "ubtu22cis_rule_1_7_4": "true",
                "ubtu22cis_rule_1_7_5": "true",
                "ubtu22cis_rule_1_7_6": "true",
                "ubtu22cis_rule_1_7_7": "true",
                "ubtu22cis_rule_1_7_8": "true",
                "ubtu22cis_rule_1_7_9": "true",
                "ubtu22cis_rule_1_7_10": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_1_7_1": "true",
                "ubtu24cis_rule_1_7_2": "true",
                "ubtu24cis_rule_1_7_3": "true",
                "ubtu24cis_rule_1_7_4": "true",
                "ubtu24cis_rule_1_7_5": "true",
                "ubtu24cis_rule_1_7_6": "true",
                "ubtu24cis_rule_1_7_7": "true",
                "ubtu24cis_rule_1_7_8": "true",
                "ubtu24cis_rule_1_7_9": "true",
                "ubtu24cis_rule_1_7_10": "true",
            },
        },
    }


class SECTION_2_HARDEN_CONTROL(Enum):
    CONFIGURE_SERVER_SERVICES = {
        "name": "Configure Server Services",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_2_1_1": "true",
                "deb12cis_rule_2_1_2": "true",
                "deb12cis_rule_2_1_3": "true",
                "deb12cis_rule_2_1_4": "true",
                "deb12cis_rule_2_1_5": "true",
                "deb12cis_rule_2_1_6": "true",
                "deb12cis_rule_2_1_7": "true",
                "deb12cis_rule_2_1_8": "true",
                "deb12cis_rule_2_1_9": "true",
                "deb12cis_rule_2_1_10": "true",
                "deb12cis_rule_2_1_11": "true",
                "deb12cis_rule_2_1_12": "true",
                "deb12cis_rule_2_1_13": "true",
                "deb12cis_rule_2_1_14": "true",
                "deb12cis_rule_2_1_15": "true",
                "deb12cis_rule_2_1_16": "true",
                "deb12cis_rule_2_1_17": "true",
                "deb12cis_rule_2_1_18": "true",
                "deb12cis_rule_2_1_19": "true",
                "deb12cis_rule_2_1_20": "true",
                "deb12cis_rule_2_1_21": "true",
                "deb12cis_rule_2_1_22": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_2_1_1": "true",
                "ubtu22cis_rule_2_1_2": "true",
                "ubtu22cis_rule_2_1_3": "true",
                "ubtu22cis_rule_2_1_4": "true",
                "ubtu22cis_rule_2_1_5": "true",
                "ubtu22cis_rule_2_1_6": "true",
                "ubtu22cis_rule_2_1_7": "true",
                "ubtu22cis_rule_2_1_8": "true",
                "ubtu22cis_rule_2_1_9": "true",
                "ubtu22cis_rule_2_1_10": "true",
                "ubtu22cis_rule_2_1_11": "true",
                "ubtu22cis_rule_2_1_12": "true",
                "ubtu22cis_rule_2_1_13": "true",
                "ubtu22cis_rule_2_1_14": "true",
                "ubtu22cis_rule_2_1_15": "true",
                "ubtu22cis_rule_2_1_16": "true",
                "ubtu22cis_rule_2_1_17": "true",
                "ubtu22cis_rule_2_1_18": "true",
                "ubtu22cis_rule_2_1_19": "true",
                "ubtu22cis_rule_2_1_20": "true",
                "ubtu22cis_rule_2_1_21": "true",
                "ubtu22cis_rule_2_1_22": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_2_1_1": "true",
                "ubtu24cis_rule_2_1_2": "true",
                "ubtu24cis_rule_2_1_3": "true",
                "ubtu24cis_rule_2_1_4": "true",
                "ubtu24cis_rule_2_1_5": "true",
                "ubtu24cis_rule_2_1_6": "true",
                "ubtu24cis_rule_2_1_7": "true",
                "ubtu24cis_rule_2_1_8": "true",
                "ubtu24cis_rule_2_1_9": "true",
                "ubtu24cis_rule_2_1_10": "true",
                "ubtu24cis_rule_2_1_11": "true",
                "ubtu24cis_rule_2_1_12": "true",
                "ubtu24cis_rule_2_1_13": "true",
                "ubtu24cis_rule_2_1_14": "true",
                "ubtu24cis_rule_2_1_15": "true",
                "ubtu24cis_rule_2_1_16": "true",
                "ubtu24cis_rule_2_1_17": "true",
                "ubtu24cis_rule_2_1_18": "true",
                "ubtu24cis_rule_2_1_19": "true",
                "ubtu24cis_rule_2_1_20": "true",
                "ubtu24cis_rule_2_1_21": "true",
                "ubtu24cis_rule_2_1_22": "true",
            },
        },
    }
    CONFIGURE_CLIENT_SERVICES = {
        "name": "Configure client services",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_2_2_1": "true",
                "deb12cis_rule_2_2_2": "true",
                "deb12cis_rule_2_2_3": "true",
                "deb12cis_rule_2_2_4": "true",
                "deb12cis_rule_2_2_5": "true",
                "deb12cis_rule_2_2_6": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_2_2_1": "true",
                "ubtu22cis_rule_2_2_2": "true",
                "ubtu22cis_rule_2_2_3": "true",
                "ubtu22cis_rule_2_2_4": "true",
                "ubtu22cis_rule_2_2_5": "true",
                "ubtu22cis_rule_2_2_6": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_2_2_1": "true",
                "ubtu24cis_rule_2_2_2": "true",
                "ubtu24cis_rule_2_2_3": "true",
                "ubtu24cis_rule_2_2_4": "true",
                "ubtu24cis_rule_2_2_5": "true",
                "ubtu24cis_rule_2_2_6": "true",
            },
        },
    }
    ENSURE_TIME_SYNCHRONIZATION = {
        "name": "Ensure time synchronization is in use",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_2_3_1_1": "true",
                "deb12cis_rule_2_3_2_1": "true",
                "deb12cis_rule_2_3_2_2": "true",
                "deb12cis_rule_2_3_3_1": "true",
                "deb12cis_rule_2_3_3_2": "true",
                "deb12cis_rule_2_3_3_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_2_3_1_1": "true",
                "ubtu22cis_rule_2_3_2_1": "true",
                "ubtu22cis_rule_2_3_2_2": "true",
                "ubtu22cis_rule_2_3_3_1": "true",
                "ubtu22cis_rule_2_3_3_2": "true",
                "ubtu22cis_rule_2_3_3_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_2_3_1_1": "true",
                "ubtu24cis_rule_2_3_2_1": "true",
                "ubtu24cis_rule_2_3_2_2": "true",
                "ubtu24cis_rule_2_3_3_1": "true",
                "ubtu24cis_rule_2_3_3_2": "true",
                "ubtu24cis_rule_2_3_3_3": "true",
            },
        },
    }
    JOB_SCHEDULERS = {
        "name": "Job Schedulers",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_2_4_1_1": "true",
                "deb12cis_rule_2_4_1_2": "true",
                "deb12cis_rule_2_4_1_3": "true",
                "deb12cis_rule_2_4_1_4": "true",
                "deb12cis_rule_2_4_1_5": "true",
                "deb12cis_rule_2_4_1_6": "true",
                "deb12cis_rule_2_4_1_7": "true",
                "deb12cis_rule_2_4_1_8": "true",
                "deb12cis_rule_2_4_2_1": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_2_4_1_1": "true",
                "ubtu22cis_rule_2_4_1_2": "true",
                "ubtu22cis_rule_2_4_1_3": "true",
                "ubtu22cis_rule_2_4_1_4": "true",
                "ubtu22cis_rule_2_4_1_5": "true",
                "ubtu22cis_rule_2_4_1_6": "true",
                "ubtu22cis_rule_2_4_1_7": "true",
                "ubtu22cis_rule_2_4_1_8": "true",
                "ubtu22cis_rule_2_4_2_1": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_2_4_1_1": "true",
                "ubtu24cis_rule_2_4_1_2": "true",
                "ubtu24cis_rule_2_4_1_3": "true",
                "ubtu24cis_rule_2_4_1_4": "true",
                "ubtu24cis_rule_2_4_1_5": "true",
                "ubtu24cis_rule_2_4_1_6": "true",
                "ubtu24cis_rule_2_4_1_7": "true",
                "ubtu24cis_rule_2_4_1_8": "true",
                "ubtu24cis_rule_2_4_2_1": "true",
            },
        },
    }


class SECTION_3_HARDEN_CONTROL(Enum):
    CONFIGURE_NETWORK_DEVICES = {
        "name": "Configure Network Devices",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_3_1_1": "true",
                "deb12cis_rule_3_1_2": "true",
                "deb12cis_rule_3_1_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_3_1_1": "true",
                "ubtu22cis_rule_3_1_2": "true",
                "ubtu22cis_rule_3_1_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_3_1_1": "true",
                "ubtu24cis_rule_3_1_2": "true",
                "ubtu24cis_rule_3_1_3": "true",
            },
        },
    }
    CONFIGURE_NETWORK_KERNEL_MODULES = {
        "name": "Configure Network Kernel Modules",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_3_2_1": "true",
                "deb12cis_rule_3_2_2": "true",
                "deb12cis_rule_3_2_3": "true",
                "deb12cis_rule_3_2_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_3_2_1": "true",
                "ubtu22cis_rule_3_2_2": "true",
                "ubtu22cis_rule_3_2_3": "true",
                "ubtu22cis_rule_3_2_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_3_2_1": "true",
                "ubtu24cis_rule_3_2_2": "true",
                "ubtu24cis_rule_3_2_3": "true",
                "ubtu24cis_rule_3_2_4": "true",
            },
        },
    }
    CONFIGURE_NETWORK_KERNEL_PARAMETERS = {
        "name": "Configure Network Kernel Parameters",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_3_3_1": "true",
                "deb12cis_rule_3_3_2": "true",
                "deb12cis_rule_3_3_3": "true",
                "deb12cis_rule_3_3_4": "true",
                "deb12cis_rule_3_3_5": "true",
                "deb12cis_rule_3_3_6": "true",
                "deb12cis_rule_3_3_7": "true",
                "deb12cis_rule_3_3_8": "true",
                "deb12cis_rule_3_3_9": "true",
                "deb12cis_rule_3_3_10": "true",
                "deb12cis_rule_3_3_11": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_3_3_1": "true",
                "ubtu22cis_rule_3_3_2": "true",
                "ubtu22cis_rule_3_3_3": "true",
                "ubtu22cis_rule_3_3_4": "true",
                "ubtu22cis_rule_3_3_5": "true",
                "ubtu22cis_rule_3_3_6": "true",
                "ubtu22cis_rule_3_3_7": "true",
                "ubtu22cis_rule_3_3_8": "true",
                "ubtu22cis_rule_3_3_9": "true",
                "ubtu22cis_rule_3_3_10": "true",
                "ubtu22cis_rule_3_3_11": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_3_3_1": "true",
                "ubtu24cis_rule_3_3_2": "true",
                "ubtu24cis_rule_3_3_3": "true",
                "ubtu24cis_rule_3_3_4": "true",
                "ubtu24cis_rule_3_3_5": "true",
                "ubtu24cis_rule_3_3_6": "true",
                "ubtu24cis_rule_3_3_7": "true",
                "ubtu24cis_rule_3_3_8": "true",
                "ubtu24cis_rule_3_3_9": "true",
                "ubtu24cis_rule_3_3_10": "true",
                "ubtu24cis_rule_3_3_11": "true",
            },
        },
    }


class SECTION_4_HARDEN_CONTROL(Enum):
    CONFIGURE_UFW = {
        "name": "Configure UncomplicatedFirewall (UFW)",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_4_1_1": "true",
                "deb12cis_rule_4_1_2": "true",
                "deb12cis_rule_4_1_3": "true",
                "deb12cis_rule_4_1_4": "true",
                "deb12cis_rule_4_1_5": "true",
                "deb12cis_rule_4_1_6": "true",
                "deb12cis_rule_4_1_7": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_4_1_1": "true",
                "ubtu22cis_rule_4_1_2": "true",
                "ubtu22cis_rule_4_1_3": "true",
                "ubtu22cis_rule_4_1_4": "true",
                "ubtu22cis_rule_4_1_5": "true",
                "ubtu22cis_rule_4_1_6": "true",
                "ubtu22cis_rule_4_1_7": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_4_2_1": "true",
                "ubtu24cis_rule_4_2_2": "true",
                "ubtu24cis_rule_4_2_3": "true",
                "ubtu24cis_rule_4_2_4": "true",
                "ubtu24cis_rule_4_2_5": "true",
                "ubtu24cis_rule_4_2_6": "true",
                "ubtu24cis_rule_4_2_7": "true",
            },
        },
    }
    CONFIGURE_NFTABLES = {
        "name": "Configure nftables",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_4_2_1": "true",
                "deb12cis_rule_4_2_2": "true",
                "deb12cis_rule_4_2_3": "true",
                "deb12cis_rule_4_2_4": "true",
                "deb12cis_rule_4_2_5": "true",
                "deb12cis_rule_4_2_6": "true",
                "deb12cis_rule_4_2_7": "true",
                "deb12cis_rule_4_2_8": "true",
                "deb12cis_rule_4_2_9": "true",
                "deb12cis_rule_4_2_10": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_4_2_1": "true",
                "ubtu22cis_rule_4_2_2": "true",
                "ubtu22cis_rule_4_2_3": "true",
                "ubtu22cis_rule_4_2_4": "true",
                "ubtu22cis_rule_4_2_5": "true",
                "ubtu22cis_rule_4_2_6": "true",
                "ubtu22cis_rule_4_2_7": "true",
                "ubtu22cis_rule_4_2_8": "true",
                "ubtu22cis_rule_4_2_9": "true",
                "ubtu22cis_rule_4_2_10": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_4_3_1": "true",
                "ubtu24cis_rule_4_3_2": "true",
                "ubtu24cis_rule_4_3_3": "true",
                "ubtu24cis_rule_4_3_4": "true",
                "ubtu24cis_rule_4_3_5": "true",
                "ubtu24cis_rule_4_3_6": "true",
                "ubtu24cis_rule_4_3_7": "true",
                "ubtu24cis_rule_4_3_8": "true",
                "ubtu24cis_rule_4_3_9": "true",
                "ubtu24cis_rule_4_3_10": "true",
            },
        },
    }
    CONFIGURE_IPTABLES_SOFTWARE = {
        "name": "Configure iptables software",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_4_3_1_1": "true",
                "deb12cis_rule_4_3_1_2": "true",
                "deb12cis_rule_4_3_1_3": "true",
                "deb12cis_rule_4_3_2_1": "true",
                "deb12cis_rule_4_3_2_2": "true",
                "deb12cis_rule_4_3_2_3": "true",
                "deb12cis_rule_4_3_2_4": "true",
                "deb12cis_rule_4_3_3_1": "true",
                "deb12cis_rule_4_3_3_2": "true",
                "deb12cis_rule_4_3_3_3": "true",
                "deb12cis_rule_4_3_3_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_4_3_1_1": "true",
                "ubtu22cis_rule_4_3_1_2": "true",
                "ubtu22cis_rule_4_3_1_3": "true",
                "ubtu22cis_rule_4_3_2_1": "true",
                "ubtu22cis_rule_4_3_2_2": "true",
                "ubtu22cis_rule_4_3_2_3": "true",
                "ubtu22cis_rule_4_3_2_4": "true",
                "ubtu22cis_rule_4_3_3_1": "true",
                "ubtu22cis_rule_4_3_3_2": "true",
                "ubtu22cis_rule_4_3_3_3": "true",
                "ubtu22cis_rule_4_3_3_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_4_4_1_1": "true",
                "ubtu24cis_rule_4_4_1_2": "true",
                "ubtu24cis_rule_4_4_1_3": "true",
                "ubtu24cis_rule_4_4_2_1": "true",
                "ubtu24cis_rule_4_4_2_2": "true",
                "ubtu24cis_rule_4_4_2_3": "true",
                "ubtu24cis_rule_4_4_2_4": "true",
                "ubtu24cis_rule_4_4_3_1": "true",
                "ubtu24cis_rule_4_4_3_2": "true",
                "ubtu24cis_rule_4_4_3_3": "true",
                "ubtu24cis_rule_4_4_3_4": "true",
            },
        },
    }


class SECTION_5_HARDEN_CONTROL(Enum):
    CONFIGURE_SSH_SERVER = {
        "name": "Configure SSH Server",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_1_1": "true",
                "deb12cis_rule_5_1_2": "true",
                "deb12cis_rule_5_1_3": "true",
                "deb12cis_rule_5_1_4": "true",
                "deb12cis_rule_5_1_5": "true",
                "deb12cis_rule_5_1_6": "true",
                "deb12cis_rule_5_1_7": "true",
                "deb12cis_rule_5_1_8": "true",
                "deb12cis_rule_5_1_9": "true",
                "deb12cis_rule_5_1_10": "true",
                "deb12cis_rule_5_1_11": "true",
                "deb12cis_rule_5_1_12": "true",
                "deb12cis_rule_5_1_13": "true",
                "deb12cis_rule_5_1_14": "true",
                "deb12cis_rule_5_1_15": "true",
                "deb12cis_rule_5_1_16": "true",
                "deb12cis_rule_5_1_17": "true",
                "deb12cis_rule_5_1_18": "true",
                "deb12cis_rule_5_1_19": "true",
                "deb12cis_rule_5_1_20": "true",
                "deb12cis_rule_5_1_21": "true",
                "deb12cis_rule_5_1_22": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_1_1": "true",
                "ubtu22cis_rule_5_1_2": "true",
                "ubtu22cis_rule_5_1_3": "true",
                "ubtu22cis_rule_5_1_4": "true",
                "ubtu22cis_rule_5_1_5": "true",
                "ubtu22cis_rule_5_1_6": "true",
                "ubtu22cis_rule_5_1_7": "true",
                "ubtu22cis_rule_5_1_8": "true",
                "ubtu22cis_rule_5_1_9": "true",
                "ubtu22cis_rule_5_1_10": "true",
                "ubtu22cis_rule_5_1_11": "true",
                "ubtu22cis_rule_5_1_12": "true",
                "ubtu22cis_rule_5_1_13": "true",
                "ubtu22cis_rule_5_1_14": "true",
                "ubtu22cis_rule_5_1_15": "true",
                "ubtu22cis_rule_5_1_16": "true",
                "ubtu22cis_rule_5_1_17": "true",
                "ubtu22cis_rule_5_1_18": "true",
                "ubtu22cis_rule_5_1_19": "true",
                "ubtu22cis_rule_5_1_20": "true",
                "ubtu22cis_rule_5_1_21": "true",
                "ubtu22cis_rule_5_1_22": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_1_1": "true",
                "ubtu24cis_rule_5_1_2": "true",
                "ubtu24cis_rule_5_1_3": "true",
                "ubtu24cis_rule_5_1_4": "true",
                "ubtu24cis_rule_5_1_5": "true",
                "ubtu24cis_rule_5_1_6": "true",
                "ubtu24cis_rule_5_1_7": "true",
                "ubtu24cis_rule_5_1_8": "true",
                "ubtu24cis_rule_5_1_9": "true",
                "ubtu24cis_rule_5_1_10": "true",
                "ubtu24cis_rule_5_1_11": "true",
                "ubtu24cis_rule_5_1_12": "true",
                "ubtu24cis_rule_5_1_13": "true",
                "ubtu24cis_rule_5_1_14": "true",
                "ubtu24cis_rule_5_1_15": "true",
                "ubtu24cis_rule_5_1_16": "true",
                "ubtu24cis_rule_5_1_17": "true",
                "ubtu24cis_rule_5_1_18": "true",
                "ubtu24cis_rule_5_1_19": "true",
                "ubtu24cis_rule_5_1_20": "true",
                "ubtu24cis_rule_5_1_21": "true",
                "ubtu24cis_rule_5_1_22": "true",
            },
        },
    }
    CONFIGURE_PRIVILEGE_ESCALATION = {
        "name": "Configure privilege escalation",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_2_1": "true",
                "deb12cis_rule_5_2_2": "true",
                "deb12cis_rule_5_2_3": "true",
                "deb12cis_rule_5_2_4": "true",
                "deb12cis_rule_5_2_5": "true",
                "deb12cis_rule_5_2_6": "true",
                "deb12cis_rule_5_2_7": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_2_1": "true",
                "ubtu22cis_rule_5_2_2": "true",
                "ubtu22cis_rule_5_2_3": "true",
                "ubtu22cis_rule_5_2_4": "true",
                "ubtu22cis_rule_5_2_5": "true",
                "ubtu22cis_rule_5_2_6": "true",
                "ubtu22cis_rule_5_2_7": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_2_1": "true",
                "ubtu24cis_rule_5_2_2": "true",
                "ubtu24cis_rule_5_2_3": "true",
                "ubtu24cis_rule_5_2_4": "true",
                "ubtu24cis_rule_5_2_5": "true",
                "ubtu24cis_rule_5_2_6": "true",
                "ubtu24cis_rule_5_2_7": "true",
            },
        },
    }
    CONFIGURE_PAM_SOFTWARE_PACKAGES = {
        "name": "Configure PAM software packages",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_3_1_1": "true",
                "deb12cis_rule_5_3_1_2": "true",
                "deb12cis_rule_5_3_1_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_3_1_1": "true",
                "ubtu22cis_rule_5_3_1_2": "true",
                "ubtu22cis_rule_5_3_1_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_3_1_1": "true",
                "ubtu24cis_rule_5_3_1_2": "true",
                "ubtu24cis_rule_5_3_1_3": "true",
            },
        },
    }
    CONFIGURE_PAM_PROFILES_AND_MODULES = {
        "name": "Configure pam profiles and modules",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_3_2_1": "true",
                "deb12cis_rule_5_3_2_2": "true",
                "deb12cis_rule_5_3_2_3": "true",
                "deb12cis_rule_5_3_2_4": "true",
                "deb12cis_rule_5_3_3_1_1": "true",
                "deb12cis_rule_5_3_3_1_2": "true",
                "deb12cis_rule_5_3_3_1_3": "true",
                "deb12cis_rule_5_3_3_2_1": "true",
                "deb12cis_rule_5_3_3_2_2": "true",
                "deb12cis_rule_5_3_3_2_3": "true",
                "deb12cis_rule_5_3_3_2_4": "true",
                "deb12cis_rule_5_3_3_2_5": "true",
                "deb12cis_rule_5_3_3_2_6": "true",
                "deb12cis_rule_5_3_3_2_7": "true",
                "deb12cis_rule_5_3_3_2_8": "true",
                "deb12cis_rule_5_3_3_3_1": "true",
                "deb12cis_rule_5_3_3_3_2": "true",
                "deb12cis_rule_5_3_3_3_3": "true",
                "deb12cis_rule_5_3_3_4_1": "true",
                "deb12cis_rule_5_3_3_4_2": "true",
                "deb12cis_rule_5_3_3_4_3": "true",
                "deb12cis_rule_5_3_3_4_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_3_2_1": "true",
                "ubtu22cis_rule_5_3_2_2": "true",
                "ubtu22cis_rule_5_3_2_3": "true",
                "ubtu22cis_rule_5_3_2_4": "true",
                "ubtu22cis_rule_5_3_3_1_1": "true",
                "ubtu22cis_rule_5_3_3_1_2": "true",
                "ubtu22cis_rule_5_3_3_1_3": "true",
                "ubtu22cis_rule_5_3_3_2_1": "true",
                "ubtu22cis_rule_5_3_3_2_2": "true",
                "ubtu22cis_rule_5_3_3_2_3": "true",
                "ubtu22cis_rule_5_3_3_2_4": "true",
                "ubtu22cis_rule_5_3_3_2_5": "true",
                "ubtu22cis_rule_5_3_3_2_6": "true",
                "ubtu22cis_rule_5_3_3_2_7": "true",
                "ubtu22cis_rule_5_3_3_2_8": "true",
                "ubtu22cis_rule_5_3_3_3_1": "true",
                "ubtu22cis_rule_5_3_3_3_2": "true",
                "ubtu22cis_rule_5_3_3_3_3": "true",
                "ubtu22cis_rule_5_3_3_4_1": "true",
                "ubtu22cis_rule_5_3_3_4_2": "true",
                "ubtu22cis_rule_5_3_3_4_3": "true",
                "ubtu22cis_rule_5_3_3_4_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_3_2_1": "true",
                "ubtu24cis_rule_5_3_2_2": "true",
                "ubtu24cis_rule_5_3_2_3": "true",
                "ubtu24cis_rule_5_3_2_4": "true",
                "ubtu24cis_rule_5_3_3_1_1": "true",
                "ubtu24cis_rule_5_3_3_1_2": "true",
                "ubtu24cis_rule_5_3_3_1_3": "true",
                "ubtu24cis_rule_5_3_3_2_1": "true",
                "ubtu24cis_rule_5_3_3_2_2": "true",
                "ubtu24cis_rule_5_3_3_2_3": "true",
                "ubtu24cis_rule_5_3_3_2_4": "true",
                "ubtu24cis_rule_5_3_3_2_5": "true",
                "ubtu24cis_rule_5_3_3_2_6": "true",
                "ubtu24cis_rule_5_3_3_2_7": "true",
                "ubtu24cis_rule_5_3_3_2_8": "true",
                "ubtu24cis_rule_5_3_3_3_1": "true",
                "ubtu24cis_rule_5_3_3_3_2": "true",
                "ubtu24cis_rule_5_3_3_3_3": "true",
                "ubtu24cis_rule_5_3_3_4_1": "true",
                "ubtu24cis_rule_5_3_3_4_2": "true",
                "ubtu24cis_rule_5_3_3_4_3": "true",
                "ubtu24cis_rule_5_3_3_4_4": "true",
            },
        },
    }
    CONFIGURE_SHADOW_PASSWORD_SUITE_PARAMETERS = {
        "name": "Configure shadow password suite parameters",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_4_1_1": "true",
                "deb12cis_rule_5_4_1_2": "true",
                "deb12cis_rule_5_4_1_3": "true",
                "deb12cis_rule_5_4_1_4": "true",
                "deb12cis_rule_5_4_1_5": "true",
                "deb12cis_rule_5_4_1_6": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_4_1_1": "true",
                "ubtu22cis_rule_5_4_1_2": "true",
                "ubtu22cis_rule_5_4_1_3": "true",
                "ubtu22cis_rule_5_4_1_4": "true",
                "ubtu22cis_rule_5_4_1_5": "true",
                "ubtu22cis_rule_5_4_1_6": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_4_1_1": "true",
                "ubtu24cis_rule_5_4_1_2": "true",
                "ubtu24cis_rule_5_4_1_3": "true",
                "ubtu24cis_rule_5_4_1_4": "true",
                "ubtu24cis_rule_5_4_1_5": "true",
                "ubtu24cis_rule_5_4_1_6": "true",
            },
        },
    }
    CONFIGURE_ROOT_AND_SYSTEM_ACCOUNTS_AND_ENVIRONMENT = {
        "name": "Configure root and system accounts and environment",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_4_2_1": "true",
                "deb12cis_rule_5_4_2_2": "true",
                "deb12cis_rule_5_4_2_3": "true",
                "deb12cis_rule_5_4_2_4": "true",
                "deb12cis_rule_5_4_2_5": "true",
                "deb12cis_rule_5_4_2_6": "true",
                "deb12cis_rule_5_4_2_7": "true",
                "deb12cis_rule_5_4_2_8": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_4_2_1": "true",
                "ubtu22cis_rule_5_4_2_2": "true",
                "ubtu22cis_rule_5_4_2_3": "true",
                "ubtu22cis_rule_5_4_2_4": "true",
                "ubtu22cis_rule_5_4_2_5": "true",
                "ubtu22cis_rule_5_4_2_6": "true",
                "ubtu22cis_rule_5_4_2_7": "true",
                "ubtu22cis_rule_5_4_2_8": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_4_2_1": "true",
                "ubtu24cis_rule_5_4_2_2": "true",
                "ubtu24cis_rule_5_4_2_3": "true",
                "ubtu24cis_rule_5_4_2_4": "true",
                "ubtu24cis_rule_5_4_2_5": "true",
                "ubtu24cis_rule_5_4_2_6": "true",
                "ubtu24cis_rule_5_4_2_7": "true",
                "ubtu24cis_rule_5_4_2_8": "true",
            },
        },
    }
    CONFIGURE_USER_DEFAULT_ENVIRONMENT = {
        "name": "Configure user default environment",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_5_4_3_1": "true",
                "deb12cis_rule_5_4_3_2": "true",
                "deb12cis_rule_5_4_3_3": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_5_4_3_1": "true",
                "ubtu22cis_rule_5_4_3_2": "true",
                "ubtu22cis_rule_5_4_3_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_5_4_3_1": "true",
                "ubtu24cis_rule_5_4_3_2": "true",
                "ubtu24cis_rule_5_4_3_3": "true",
            },
        },
    }


class SECTION_6_HARDEN_CONTROL(Enum):
    CONFIGURE_INTEGRITY_CHECKING = {
        "name": "Configure Integrity Checking",
        "os_version_name": {
            "debian_12": {"deb12cis_rule_6_1_1": "true", "deb12cis_rule_6_1_2": "true"},
            "ubuntu_22": {
                "ubtu22cis_rule_6_1_1": "true",
                "ubtu22cis_rule_6_1_2": "true",
                "ubtu22cis_rule_6_1_3": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_3_1": "true",
                "ubtu24cis_rule_6_3_2": "true",
                "ubtu24cis_rule_6_3_3": "true",
            },
        },
    }
    CONFIGURE_JOURNALD = {
        "name": "Configure journald",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_6_2_1_1_1": "true",
                "deb12cis_rule_6_2_1_1_2": "true",
                "deb12cis_rule_6_2_1_1_3": "true",
                "deb12cis_rule_6_2_1_1_4": "true",
                "deb12cis_rule_6_2_1_1_5": "true",
                "deb12cis_rule_6_2_1_1_6": "true",
                "deb12cis_rule_6_2_1_2_1": "true",
                "deb12cis_rule_6_2_1_2_2": "true",
                "deb12cis_rule_6_2_1_2_3": "true",
                "deb12cis_rule_6_2_1_2_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_6_2_1_1_1": "true",
                "ubtu22cis_rule_6_2_1_1_2": "true",
                "ubtu22cis_rule_6_2_1_1_3": "true",
                "ubtu22cis_rule_6_2_1_1_4": "true",
                "ubtu22cis_rule_6_2_1_1_5": "true",
                "ubtu22cis_rule_6_2_1_1_6": "true",
                "ubtu22cis_rule_6_2_1_2_1": "true",
                "ubtu22cis_rule_6_2_1_2_2": "true",
                "ubtu22cis_rule_6_2_1_2_3": "true",
                "ubtu22cis_rule_6_2_1_2_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_1_1_1": "true",
                "ubtu24cis_rule_6_1_1_2": "true",
                "ubtu24cis_rule_6_1_1_3": "true",
                "ubtu24cis_rule_6_1_1_4": "true",
                "ubtu24cis_rule_6_1_2_1_1": "true",
                "ubtu24cis_rule_6_1_2_1_2": "true",
                "ubtu24cis_rule_6_1_2_1_3": "true",
                "ubtu24cis_rule_6_1_2_1_4": "true",
                "ubtu24cis_rule_6_1_2_2": "true",
                "ubtu24cis_rule_6_1_2_3": "true",
                "ubtu24cis_rule_6_1_2_4": "true",
            },
        },
    }
    CONFIGURE_LOGFILES = {
        "name": "Configure Logfiles",
        "os_version_name": {
            "debian_12": {"deb12cis_rule_6_2_2_1": "true"},
            "ubuntu_22": {"ubtu22cis_rule_6_2_2_1": "true"},
            "ubuntu_24": {"ubtu24cis_rule_6_1_4_1": "true"},
        },
    }
    CONFIGURE_AUDITD_SERVICE = {
        "name": "Configure auditd Service",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_6_3_1_1": "true",
                "deb12cis_rule_6_3_1_2": "true",
                "deb12cis_rule_6_3_1_3": "true",
                "deb12cis_rule_6_3_1_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_6_3_1_1": "true",
                "ubtu22cis_rule_6_3_1_2": "true",
                "ubtu22cis_rule_6_3_1_3": "true",
                "ubtu22cis_rule_6_3_1_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_2_1_1": "true",
                "ubtu24cis_rule_6_2_1_2": "true",
                "ubtu24cis_rule_6_2_1_3": "true",
                "ubtu24cis_rule_6_2_1_4": "true",
            },
        },
    }
    CONFIGURE_DATA_RETENTION = {
        "name": "Configure Data Retention",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_6_3_2_1": "true",
                "deb12cis_rule_6_3_2_2": "true",
                "deb12cis_rule_6_3_2_3": "true",
                "deb12cis_rule_6_3_2_4": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_6_3_2_1": "true",
                "ubtu22cis_rule_6_3_2_2": "true",
                "ubtu22cis_rule_6_3_2_3": "true",
                "ubtu22cis_rule_6_3_2_4": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_2_2_1": "true",
                "ubtu24cis_rule_6_2_2_2": "true",
                "ubtu24cis_rule_6_2_2_3": "true",
                "ubtu24cis_rule_6_2_2_4": "true",
            },
        },
    }
    CONFIGURE_AUDITD_ROLES = {
        "name": "Configure auditd Rules",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_6_3_3_1": "true",
                "deb12cis_rule_6_3_3_2": "true",
                "deb12cis_rule_6_3_3_3": "true",
                "deb12cis_rule_6_3_3_4": "true",
                "deb12cis_rule_6_3_3_5": "true",
                "deb12cis_rule_6_3_3_6": "true",
                "deb12cis_rule_6_3_3_7": "true",
                "deb12cis_rule_6_3_3_8": "true",
                "deb12cis_rule_6_3_3_9": "true",
                "deb12cis_rule_6_3_3_10": "true",
                "deb12cis_rule_6_3_3_11": "true",
                "deb12cis_rule_6_3_3_12": "true",
                "deb12cis_rule_6_3_3_13": "true",
                "deb12cis_rule_6_3_3_14": "true",
                "deb12cis_rule_6_3_3_15": "true",
                "deb12cis_rule_6_3_3_16": "true",
                "deb12cis_rule_6_3_3_17": "true",
                "deb12cis_rule_6_3_3_18": "true",
                "deb12cis_rule_6_3_3_19": "true",
                "deb12cis_rule_6_3_3_20": "true",
                "deb12cis_rule_6_3_3_21": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_6_3_3_1": "true",
                "ubtu22cis_rule_6_3_3_2": "true",
                "ubtu22cis_rule_6_3_3_3": "true",
                "ubtu22cis_rule_6_3_3_4": "true",
                "ubtu22cis_rule_6_3_3_5": "true",
                "ubtu22cis_rule_6_3_3_6": "true",
                "ubtu22cis_rule_6_3_3_7": "true",
                "ubtu22cis_rule_6_3_3_8": "true",
                "ubtu22cis_rule_6_3_3_9": "true",
                "ubtu22cis_rule_6_3_3_10": "true",
                "ubtu22cis_rule_6_3_3_11": "true",
                "ubtu22cis_rule_6_3_3_12": "true",
                "ubtu22cis_rule_6_3_3_13": "true",
                "ubtu22cis_rule_6_3_3_14": "true",
                "ubtu22cis_rule_6_3_3_15": "true",
                "ubtu22cis_rule_6_3_3_16": "true",
                "ubtu22cis_rule_6_3_3_17": "true",
                "ubtu22cis_rule_6_3_3_18": "true",
                "ubtu22cis_rule_6_3_3_19": "true",
                "ubtu22cis_rule_6_3_3_20": "true",
                "ubtu22cis_rule_6_3_3_21": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_2_3_1": "true",
                "ubtu24cis_rule_6_2_3_2": "true",
                "ubtu24cis_rule_6_2_3_3": "true",
                "ubtu24cis_rule_6_2_3_4": "true",
                "ubtu24cis_rule_6_2_3_5": "true",
                "ubtu24cis_rule_6_2_3_6": "true",
                "ubtu24cis_rule_6_2_3_7": "true",
                "ubtu24cis_rule_6_2_3_8": "true",
                "ubtu24cis_rule_6_2_3_9": "true",
                "ubtu24cis_rule_6_2_3_10": "true",
                "ubtu24cis_rule_6_2_3_11": "true",
                "ubtu24cis_rule_6_2_3_12": "true",
                "ubtu24cis_rule_6_2_3_13": "true",
                "ubtu24cis_rule_6_2_3_14": "true",
                "ubtu24cis_rule_6_2_3_15": "true",
                "ubtu24cis_rule_6_2_3_16": "true",
                "ubtu24cis_rule_6_2_3_17": "true",
                "ubtu24cis_rule_6_2_3_18": "true",
                "ubtu24cis_rule_6_2_3_19": "true",
                "ubtu24cis_rule_6_2_3_20": "true",
                "ubtu24cis_rule_6_2_3_21": "true",
            },
        },
    }
    CONFIGURE_AUDITD_FILE_ACCESS = {
        "name": "Configure auditd File Access",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_6_3_4_1": "true",
                "deb12cis_rule_6_3_4_2": "true",
                "deb12cis_rule_6_3_4_3": "true",
                "deb12cis_rule_6_3_4_4": "true",
                "deb12cis_rule_6_3_4_5": "true",
                "deb12cis_rule_6_3_4_6": "true",
                "deb12cis_rule_6_3_4_7": "true",
                "deb12cis_rule_6_3_4_8": "true",
                "deb12cis_rule_6_3_4_9": "true",
                "deb12cis_rule_6_3_4_10": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_6_3_4_1": "true",
                "ubtu22cis_rule_6_3_4_2": "true",
                "ubtu22cis_rule_6_3_4_3": "true",
                "ubtu22cis_rule_6_3_4_4": "true",
                "ubtu22cis_rule_6_3_4_5": "true",
                "ubtu22cis_rule_6_3_4_6": "true",
                "ubtu22cis_rule_6_3_4_7": "true",
                "ubtu22cis_rule_6_3_4_8": "true",
                "ubtu22cis_rule_6_3_4_9": "true",
                "ubtu22cis_rule_6_3_4_10": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_6_2_4_1": "true",
                "ubtu24cis_rule_6_2_4_2": "true",
                "ubtu24cis_rule_6_2_4_3": "true",
                "ubtu24cis_rule_6_2_4_4": "true",
                "ubtu24cis_rule_6_2_4_5": "true",
                "ubtu24cis_rule_6_2_4_6": "true",
                "ubtu24cis_rule_6_2_4_7": "true",
                "ubtu24cis_rule_6_2_4_8": "true",
                "ubtu24cis_rule_6_2_4_9": "true",
                "ubtu24cis_rule_6_2_4_10": "true",
            },
        },
    }


class SECTION_7_HARDEN_CONTROL(Enum):
    SYSTEM_FILE_PERMISSIONS = {
        "name": "System File Permissions",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_7_1_1": "true",
                "deb12cis_rule_7_1_2": "true",
                "deb12cis_rule_7_1_3": "true",
                "deb12cis_rule_7_1_4": "true",
                "deb12cis_rule_7_1_5": "true",
                "deb12cis_rule_7_1_6": "true",
                "deb12cis_rule_7_1_7": "true",
                "deb12cis_rule_7_1_8": "true",
                "deb12cis_rule_7_1_9": "true",
                "deb12cis_rule_7_1_10": "true",
                "deb12cis_rule_7_1_11": "true",
                "deb12cis_rule_7_1_12": "true",
                "deb12cis_rule_7_1_13": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_7_1_1": "true",
                "ubtu22cis_rule_7_1_2": "true",
                "ubtu22cis_rule_7_1_3": "true",
                "ubtu22cis_rule_7_1_4": "true",
                "ubtu22cis_rule_7_1_5": "true",
                "ubtu22cis_rule_7_1_6": "true",
                "ubtu22cis_rule_7_1_7": "true",
                "ubtu22cis_rule_7_1_8": "true",
                "ubtu22cis_rule_7_1_9": "true",
                "ubtu22cis_rule_7_1_10": "true",
                "ubtu22cis_rule_7_1_11": "true",
                "ubtu22cis_rule_7_1_12": "true",
                "ubtu22cis_rule_7_1_13": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_7_1_1": "true",
                "ubtu24cis_rule_7_1_2": "true",
                "ubtu24cis_rule_7_1_3": "true",
                "ubtu24cis_rule_7_1_4": "true",
                "ubtu24cis_rule_7_1_5": "true",
                "ubtu24cis_rule_7_1_6": "true",
                "ubtu24cis_rule_7_1_7": "true",
                "ubtu24cis_rule_7_1_8": "true",
                "ubtu24cis_rule_7_1_9": "true",
                "ubtu24cis_rule_7_1_10": "true",
                "ubtu24cis_rule_7_1_11": "true",
                "ubtu24cis_rule_7_1_12": "true",
                "ubtu24cis_rule_7_1_13": "true",
            },
        },
    }
    LOCAL_USER_AND_GROUP_SETTINGS = {
        "name": "Local User and Group Settings",
        "os_version_name": {
            "debian_12": {
                "deb12cis_rule_7_2_1": "true",
                "deb12cis_rule_7_2_2": "true",
                "deb12cis_rule_7_2_3": "true",
                "deb12cis_rule_7_2_4": "true",
                "deb12cis_rule_7_2_5": "true",
                "deb12cis_rule_7_2_6": "true",
                "deb12cis_rule_7_2_7": "true",
                "deb12cis_rule_7_2_8": "true",
                "deb12cis_rule_7_2_9": "true",
                "deb12cis_rule_7_2_10": "true",
            },
            "ubuntu_22": {
                "ubtu22cis_rule_7_2_1": "true",
                "ubtu22cis_rule_7_2_2": "true",
                "ubtu22cis_rule_7_2_3": "true",
                "ubtu22cis_rule_7_2_4": "true",
                "ubtu22cis_rule_7_2_5": "true",
                "ubtu22cis_rule_7_2_6": "true",
                "ubtu22cis_rule_7_2_7": "true",
                "ubtu22cis_rule_7_2_8": "true",
                "ubtu22cis_rule_7_2_9": "true",
                "ubtu22cis_rule_7_2_10": "true",
            },
            "ubuntu_24": {
                "ubtu24cis_rule_7_2_1": "true",
                "ubtu24cis_rule_7_2_2": "true",
                "ubtu24cis_rule_7_2_3": "true",
                "ubtu24cis_rule_7_2_4": "true",
                "ubtu24cis_rule_7_2_5": "true",
                "ubtu24cis_rule_7_2_6": "true",
                "ubtu24cis_rule_7_2_7": "true",
                "ubtu24cis_rule_7_2_8": "true",
                "ubtu24cis_rule_7_2_9": "true",
                "ubtu24cis_rule_7_2_10": "true",
            },
        },
    }


class SEMI_HARDEN_CONTROL(Enum):
    CONTROLS = {
        "name": "Disruption High is set to False",
        "os_version_name": {
            "debian_12": {"deb12cis_disruption_high": "false"},
            "ubuntu_22": {"ubtu22cis_disruption_high": "false"},
            "ubuntu_24": {"ubtu24cis_disruption_high": "false"},
        },
    }


def fetch_all_harden_controls() -> list[
    SECTION_1_HARDEN_CONTROL
    | SECTION_2_HARDEN_CONTROL
    | SECTION_3_HARDEN_CONTROL
    | SECTION_4_HARDEN_CONTROL
    | SECTION_5_HARDEN_CONTROL
    | SECTION_6_HARDEN_CONTROL
    | SECTION_7_HARDEN_CONTROL
]:
    data = [
        y
        for x in (
            list(SECTION_1_HARDEN_CONTROL),
            list(SECTION_2_HARDEN_CONTROL),
            list(SECTION_3_HARDEN_CONTROL),
            list(SECTION_4_HARDEN_CONTROL),
            list(SECTION_5_HARDEN_CONTROL),
            list(SECTION_6_HARDEN_CONTROL),
            list(SECTION_7_HARDEN_CONTROL),
        )
        for y in x
    ]
    return data
