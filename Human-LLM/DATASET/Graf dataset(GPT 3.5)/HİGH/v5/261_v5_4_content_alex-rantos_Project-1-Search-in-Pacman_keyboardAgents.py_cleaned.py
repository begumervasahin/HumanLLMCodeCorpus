
from game import Agent, Directions
from graphicsUtils import keys_waiting, keys_pressed
import random
class class1(Agent):
    b1 = 'a'
    b2 = 'd'
    b3 = 'w'
    b4 = 's'
    b5 = 'q'
    def fonk1(self, b6 = 0):
        self.b7 = Directions.STOP
        self.b6 = b6
        self.b8 = []
    def fonk2(self, state):
        b8 = keys_waiting() + keys_pressed()
        if b8:
            self.b8 = b8
        b9 = state.get_legal_actions(self.b6)
        b10 = self.fonk4(b9)
        if b10 = = Directions.STOP and self.b7 in b9:
            b10 = self.b7
        if self.b5 in self.b8 and Directions.STOP in b9:
            b10 = Directions.STOP
        if b10 not in b9:
            b10 = random.choice(b9)
        self.b7 = b10
        return b10
    def fonk3(self, b9):
        b10 = Directions.STOP
        b11 = {
            'Left': self.b1,
            'Right': self.b2,
            'Up': self.b3,
            'Down': self.b4
        }
        for key, direction in b11.items():
            if direction in self.b8 and getattr(Directions, key) in b9:
                b10 = getattr(Directions, key)
                break
        return b10
class class2(class1):
    b1 = 'j'
    b2 = 'l'
    b3 = 'i'
    b4 = 'k'
    b5 = 'u'
    def fonk4(self, b9):
        b10 = Directions.STOP
        b11 = {
            'Left': self.b1,
            'Right': self.b2,
            'Up': self.b3,
            'Down': self.b4
        }
        for key, direction in b11.items():
            if direction in self.b8 and getattr(Directions, key) in b9:
                b10 = getattr(Directions, key)
                break
        return b10