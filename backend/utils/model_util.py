from models.target import TargetList, Target

def split_OS(osVersionName: str):
        _os = osVersionName.lower().strip().split()
        _name = _os[0]
        _version = _os[1]
        return {
            "name": _name,
            "version": _version
        }
        
def is_Debian_11(osVersionName: str) -> bool:
    if not split_OS(osVersionName)['name'].startswith("debian"):
        return False
    if not split_OS(osVersionName)['version'].startswith('11'):
        return False
    return True

def is_Debian_12(osVersionName: str) -> bool:
    if not split_OS(osVersionName)['name'].startswith("debian"):
        return False
    if not split_OS(osVersionName)['version'].startswith('12'):
        return False
    return True

def is_Ubuntu_20(osVersionName: str) -> bool:
    if not split_OS(osVersionName)['name'].startswith("ubuntu"):
        return False
    if not split_OS(osVersionName)['version'].startswith('20'):
        return False
    return True

def is_Ubuntu_22(osVersionName: str) -> bool:
    if not split_OS(osVersionName)['name'].startswith("ubuntu"):
        return False
    if not split_OS(osVersionName)['version'].startswith('22'):
        return False
    return True

def is_Ubuntu_24(osVersionName: str) -> bool:
    if not split_OS(osVersionName)['name'].startswith("ubuntu"):
        return False
    if not split_OS(osVersionName)['version'].startswith('24'):
        return False
    return True

def grouping_os(payload: TargetList):
        debian_11_list: list[Target] = []
        debian_12_list: list[Target] = []
        ubuntu_20_list: list[Target] = []
        ubuntu_22_list: list[Target] = []
        ubuntu_24_list: list[Target] = []

        for target in payload.target_list:
            if is_Debian_11(target.os_version_name):
                debian_11_list.append(target)
            elif is_Debian_12(target.os_version_name):
                debian_12_list.append(target)
            elif is_Ubuntu_20(target.os_version_name):
                ubuntu_20_list.append(target)
            elif is_Ubuntu_22(target.os_version_name):
                ubuntu_22_list.append(target)
            elif is_Ubuntu_24(target.os_version_name):
                ubuntu_24_list.append(target)
            else:
                continue
        
        return {
            "debian_11": debian_11_list,
            "debian_12": debian_12_list,
            "ubuntu_20": ubuntu_20_list,
            "ubuntu_22": ubuntu_22_list,
            "ubuntu_24": ubuntu_24_list
        }