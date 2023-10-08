from collections import UserString
from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(data, value):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)
        return keys


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith("01"):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException
