import random


class State:
    def __init__(self):
        pass

    def infection(self):
        pass

    def infecting(self):
        pass


class Healthy(State):
    def infection(self):
        return False

    def infecting(self):
        return False


class SickNo(State):
    def infection(self):
        return True

    def infecting(self):
        something_returned = random.uniform(0, 1)
        if something_returned <= 0.5:
            return True
        else:
            return False


class SickSymptoms(State):
    def infection(self):
        return True

    def infecting(self):
        return True


class Protected(State):
    def infection(self):
        return False

    def infecting(self):
        return False


"""
class A:
    def __init__(self):
        self.state = SickSymptoms()


if __name__ == '__main__':
    a = A()
    print(isinstance(a.state, SickSymptoms))
"""
