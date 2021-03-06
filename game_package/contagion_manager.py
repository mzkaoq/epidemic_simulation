import random

from game_package.peoplelist import PeopleList
from game_package.person import Person
from game_package.constant import SCALE, INFECT_START, INFECT_STOP
from game_package.persons import State, SickSymptoms, SickNo, Healthy, Protected


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConstagionManager(metaclass=SingletonMeta):
    def __init__(self):
        self._list_of_potential_sick = {}
        self._list_of_sick = {}
        self._temporary_list = []

    def update(self):
        self.time_checking()
        self.infection()
        self.sick_manager()
        self.remove_sick_outside()
        self.print_stats()

    def print_stats(self):
        healthy = 0
        sick = 0
        protected = 0
        counter = 0
        for people in PeopleList().list_of_people:
            counter += 1
            if people.state.infection() == False:
                healthy += 1
            elif isinstance(people, Protected):
                protected += 1
            else:
                sick += 1
            # print(f"zdrowych {healthy / counter:.3f}% chorych {sick / counter:.3f}%")

    def infection(self):
        for key, value in self._list_of_potential_sick.items():
            if value == 25 * 3:
                time = random.randint(INFECT_START, INFECT_STOP)
                symptoms_in_new = random.uniform(0, 1)
                # print(isinstance(key[1].state,SickNo),isinstance(key[1].state,SickNo))
                if key[0].state.infecting() == True and isinstance(key[1].state, Healthy):
                    key[1].state = SickNo()
                    if symptoms_in_new < 0.1:
                        key[1].state = SickSymptoms()
                    self._list_of_sick.update({key[1]: (0, time * 25)})
                elif key[1].state.infecting() == True and isinstance(key[0].state, Healthy):
                    key[0].state = SickNo()
                    if symptoms_in_new < 0.1:
                        key[0].state = SickSymptoms()
                    self._list_of_sick.update({key[0]: (0, time * 25)})

    def remove_sick_outside(self):
        self._temporary_list = []
        for person2 in self._list_of_sick:
            if person2 not in PeopleList().list_of_people:
                self._temporary_list.append(person2)
            if person2.state.infection() == False:
                self._temporary_list.append(person2)
            """
            elif person2.immunity == True:
                self._temporary_list.append(person2)
            """
        for person2 in self._temporary_list:
            if person2 in self._temporary_list:
                self._list_of_sick.pop(person2)

    def distance_checking(self, person1, person2):
        x1, y1 = person1.x, person1.y
        x2, y2 = person2.x, person2.y
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if dist <= (2 * SCALE + 2 * SCALE) and dist != 0:
            return True
        else:
            return False

    def possibility_beeing_ill(self, person, person2):
        if person.state.infection() == True:
            if isinstance(person2.state, Healthy):
                return True
        elif person2.state.infection() == True:
            if isinstance(person.state, Healthy):
                return True
        else:
            return False

    def time_checking(self):
        for people in PeopleList().list_of_people:
            for people2 in PeopleList().list_of_people:
                if self.distance_checking(people, people2) == True:
                    if (people, people2) in self._list_of_potential_sick:
                        # print("update",self._list_of_potential_sick[(people,people2)])
                        self._list_of_potential_sick[(people, people2)] += 1
                        if (people2, people) in self._list_of_potential_sick:
                            self._list_of_potential_sick.pop((people2, people))
                    elif self.possibility_beeing_ill(people, people2) == True:
                        self._list_of_potential_sick.update({(people, people2): 0})
                        # print("add",(people,people2))
                else:
                    if (people, people2) in self._list_of_potential_sick:
                        self._list_of_potential_sick.pop((people, people2))
                    if (people2, people) in self._list_of_potential_sick:
                        self._list_of_potential_sick.pop((people2, people))

    def sick_manager(self):
        for key, values in self._list_of_sick.items():
            values = (values[0] + 1, values[1])
            self._list_of_sick[key] = values
            if values[0] == values[1]:
                key.state = Protected()

    def append_sick(self, value):
        self._list_of_potential_sick.append(value)

    def remove_sick(self, value):
        self._list_of_potantial_sick.remove(value)

    @property
    def list_of_potential_sick(self):
        return self._list_of_potential_sick

    def list_of_sick_updater(self, value):

        time = random.randint(INFECT_START, INFECT_STOP)
        self._list_of_sick.update({value: (0, time * 25)})

    """
        def infection(self):
            for key, value in self._list_of_potential_sick.items():
                if value == 25 * 3:
                    time = random.randint(INFECT_START, INFECT_STOP)
                    symptoms = random.uniform(0, 1)
                    symptoms_in_new = random.uniform(0, 1)
                    #print(isinstance(key[1].state,SickNo),isinstance(key[1].state,SickNo))
                    if isinstance(key[0].state, SickSymptoms) and isinstance(key[1].state, Healthy):
                        key[1].state = SickNo()
                        if symptoms_in_new < 0.1:
                            key[1].state = SickSymptoms()
                        self._list_of_sick.update({key[1]: (0, time * 25)})
                    elif isinstance(key[1].state, SickSymptoms) and isinstance(key[0].state, Healthy):
                        key[0].state = SickNo()
                        if symptoms_in_new < 0.1:
                            key[0].state = SickSymptoms()
                        self._list_of_sick.update({key[0]: (0, time * 25)})
                    elif isinstance(key[0].state, SickNo) and isinstance(key[1].state, Healthy) and symptoms < 0.5:
                        key[1].state = SickNo()
                        if symptoms_in_new < 0.1:
                            key[1].state = SickSymptoms()
                        self._list_of_sick.update({key[1]: (0, time * 25)})
                    elif isinstance(key[1].state, SickNo) and isinstance(key[0].state, Healthy) and symptoms < 0.5:
                        key[0].state = SickNo()
                        if symptoms_in_new < 0.1:
                            key[0].state = SickSymptoms()
                        self._list_of_sick.update({key[0]: (0, time * 25)})
    """
