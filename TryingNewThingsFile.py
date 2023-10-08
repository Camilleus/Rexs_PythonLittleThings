from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(data, value):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)
        return keys
