import copy

from game_package.peoplelist import PeopleList
from game_package.peoplemanager import PeopleManager
import pygame
import random
import time
from game_package.constant import RED, GREEN, BLUE, GREY, BLACK, SCALE, AREA, DARK_RED
from game_package.contagion_manager import ConstagionManager
from game_package.persons import State,SickSymptoms,SickNo,Healthy,Protected
from game_package.memento import Mementos, Caretaker

class Game:
    def __init__(self, win):
        self.board = None
        self.win = win
        self._init()

        PeopleManager()
        ConstagionManager()
        self.care_taker = Caretaker()

    def _init(self):
        self.win.fill(BLACK)
        # pygame.draw.rect(self.win, RED, pygame.Rect(0, 0, AREA * SCALE, AREA * SCALE), 4)

    def update_drawing(self):
        list_of_people = self.care_taker.take_last_from_memento()
        for person in list_of_people.state:
            # pygame.draw.rect(self.win, (127, 127, 127), pygame.Rect(person.x * 4 - 4, person.y * 4 - 4, 8, 8))
            if isinstance(person.state,SickNo):
                color = RED
            elif isinstance(person.state,Healthy):
                color = GREEN
            elif isinstance(person.state,Protected):
                color = BLUE
            elif isinstance(person.state,SickSymptoms):
                color = DARK_RED
            pygame.draw.circle(self.win, color, (person.x, person.y), SCALE / 2)
            if color == DARK_RED or color == RED:
                pygame.draw.circle(self.win, GREY, (person.x, person.y), SCALE *3, 1)

    def update(self):
        PeopleManager().update_position()
        ConstagionManager().update()
        self.memento_add()
        #self.memento.printing()
        self.update_drawing()

    def memento_add(self):
        element = Mementos(copy.deepcopy(PeopleList().list_of_people))
        #print(element, element.element)
        self.care_taker.add_to_memento(element)



