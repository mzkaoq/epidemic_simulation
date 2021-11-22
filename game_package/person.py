import random


class Person:
    def __init__(self, x, y,health,illness):
        self._x = float(x)
        self._y = float(y)
        self._vect_x = random.randrange(-1, 2, 2)
        self._vect_y = random.randrange(-1, 2, 2)
        self._immunity = False
        self._health = health
        self._illness = illness

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
    def health(self):
        return self._health

    @health.setter
    def health(self,value):
        self._health = value

    @property
    def immunity(self):
        return self._immunity

    @immunity.setter
    def immunity(self, value):
        self._immunity = value

    @property
    def illness(self):
        return self._illness

    @illness.setter
    def illness(self, value):
        self._illness = value

