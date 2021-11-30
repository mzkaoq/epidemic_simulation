
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PeopleList(metaclass=SingletonMeta):
    def __init__(self):
        self._list_of_people = []

    def append(self, value):
        self._list_of_people.append(value)

    def remove(self, value):
        self._list_of_people.remove(value)

    @property
    def list_of_people(self):
        return self._list_of_people

