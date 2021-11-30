import copy


class Caretaker():

    def __init__(self):
        self._mementos = []
        self.index = 0

    def add_to_memento(self,element):
        self.index += 1
        #self._mementos.append([population,self.index])
        self._mementos.append(element)

    def take_last_from_memento(self):
        element = self._mementos[self.index-1]
        #print(len(self._mementos))
        return element

    def printing(self):
        print(self._mementos)

class Mementos:
    def __init__(self,element):
        self._state = element

    @property
    def state(self):
        return self._state

