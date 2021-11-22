from game_package.peoplelist import PeopleList
from game_package.peoplemanager import PeopleManager
import pygame
import random
import time
from game_package.constant import RED, GREEN, BLUE, GREY, BLACK, SCALE, AREA, DARK_RED
from game_package.contagion_manager import ConstagionManager


class Game:
    def __init__(self, win):
        self.board = None
        self.win = win
        self._init()
        PeopleManager()
        ConstagionManager()

    def _init(self):
        self.win.fill(BLACK)
        # pygame.draw.rect(self.win, RED, pygame.Rect(0, 0, AREA * SCALE, AREA * SCALE), 4)

    def update_drawing(self):
        for person in PeopleList().list_of_people:
            # pygame.draw.rect(self.win, (127, 127, 127), pygame.Rect(person.x * 4 - 4, person.y * 4 - 4, 8, 8))
            if person.health == False and person.illness == False:
                color = RED
            elif person.health == True and person.immunity == False:
                    color = GREEN
            elif person.immunity == True:
                color = BLUE
            elif person.health == False and person.illness == True:
                color = DARK_RED
            pygame.draw.circle(self.win, color, (person.x, person.y), SCALE / 2)

    def update(self):
        PeopleManager().update_position()
        ConstagionManager().update()
        self.update_drawing()

