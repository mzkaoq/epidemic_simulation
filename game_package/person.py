import random
from game_package.persons import State,SickSymptoms,SickNo,Healthy,Protected

class Person:
    def __init__(self, x, y,state):
        self._x = float(x)
        self._y = float(y)
        self._vect_x = random.randrange(-1, 2, 2)
        self._vect_y = random.randrange(-1, 2, 2)
        self._state = state

    def containgon_manager(self,person):
        if isinstance(self._state,Healthy):
            if person.state.infection() == True:
                something_returned = random.uniform(0, 1)
                if something_returned <= 0.9:
                    self._state = SickNo()
                else:
                    self._state = SickSymptoms()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def vect_x(self):
        return self._vect_x

    @property
    def vect_y(self):
        return self._vect_y

    @vect_x.setter
    def vect_x(self, value):
        self._vect_x = value

    @vect_y.setter
    def vect_y(self, value):
        self._vect_y = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value
