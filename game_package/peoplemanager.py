from game_package.peoplelist import PeopleList
from game_package.person import Person
import random
from game_package.constant import SCALE, CHANCE_OF_CHANGING_DIRECTION, NUMBER_OF_PEOPLE, AREA
from game_package.contagion_manager import ConstagionManager
from game_package.persons import State,SickSymptoms,SickNo,Healthy,Protected

class PeopleManager:
    def __init__(self):
        self._number_of_people = len(PeopleList().list_of_people)
        #print(self._number_of_people)
        if self._number_of_people != NUMBER_OF_PEOPLE:  # liczba osobników w symulacji
            for i in range(NUMBER_OF_PEOPLE - self._number_of_people):
                self.appender()

    def update_position(self):
        for person in PeopleList().list_of_people:
            if random.uniform(0, 1) < CHANCE_OF_CHANGING_DIRECTION:
                person.vect_x *= -1
            if random.uniform(0, 1) < CHANCE_OF_CHANGING_DIRECTION:
                person.vect_y *= -1
            while True:
                a = random.uniform(0, 2.5 * SCALE) * float(person.vect_x) / 25
                b = random.uniform(0, 2.5 * SCALE) * float(person.vect_y) / 25
                if a ** 2 + b ** 2 <= (6.25 * SCALE / 25):
                    break
            person.x += a
            person.y += b
            if person.x < 0 or person.x > AREA * SCALE or person.y < 0 or person.y > AREA * SCALE:
                if random.uniform(0, 1) < 0.5:
                    PeopleList().list_of_people.remove(person)
                    '''
                    if person in ConstagionManager()._list_of_sick:
                        ConstagionManager()._list_of_sick.pop(person)
                    '''
                else:
                    person.vect_x *= -1
                    person.vect_y *= -1

    def appender(self):
        x = random.randint(1, 5)
        x2 =random.uniform(0, 1)
        if x2 < 0.05:  #zmienic na 0.1
            state = SickSymptoms()
        elif x2 < 0.1:
            state = SickNo()
        elif x2 < 0.2:
            state = Protected()
        else:
            state = Healthy()

        if x == 1:
            person_storage = Person(random.randint(0, AREA * SCALE), 0, state)
            PeopleList().list_of_people.append(person_storage)
            if isinstance(person_storage.state,SickSymptoms) or isinstance(person_storage.state,SickSymptoms):
                ConstagionManager().list_of_sick_updater(person_storage)
        elif x == 2:
            person_storage = Person(random.randint(0, AREA * SCALE), AREA * SCALE, state)
            PeopleList().list_of_people.append(person_storage)
            if isinstance(person_storage.state,SickSymptoms) or isinstance(person_storage.state,SickSymptoms):
                ConstagionManager().list_of_sick_updater(person_storage)
        elif x == 3:
            person_storage = Person(0, random.randint(0, AREA * SCALE), state)
            PeopleList().list_of_people.append(person_storage)
            if isinstance(person_storage.state,SickSymptoms) or isinstance(person_storage.state,SickSymptoms):
                ConstagionManager().list_of_sick_updater(person_storage)
        elif x == 4:
            person_storage = Person(AREA * SCALE, random.randint(0, AREA * SCALE), state)
            PeopleList().list_of_people.append(person_storage)
            if isinstance(person_storage.state,SickSymptoms) or isinstance(person_storage.state,SickSymptoms):
                ConstagionManager().list_of_sick_updater(person_storage)




