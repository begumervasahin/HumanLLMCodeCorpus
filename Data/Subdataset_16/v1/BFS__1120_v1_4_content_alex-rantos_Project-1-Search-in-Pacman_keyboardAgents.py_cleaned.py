from game import Agent
from game import Directions
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
        from graphicsUtils import keys_waiting
        from graphicsUtils import keys_pressed
        b8 = keys_waiting() + keys_pressed()
        if b8:
            self.b8 = b8
        b9 = state.getLegalActions(self.b6)
        b10 = self.fonk4(b9)
        if b10 = = Directions.STOP:
            if self.b7 in b9:
                b10 = self.b7
        if (self.b5 in self.b8) and Directions.STOP in b9:
            b10 = Directions.STOP
        if b10 not in b9:
            b10 = random.choice(b9)
        self.b7 = b10
        return b10
    def fonk3(self, b9):
        b10 = Directions.STOP
        if   (self.b1 in self.b8 or 'Left' in self.b8) and Directions.WEST in b9:  b10 = Directions.WEST
        if   (self.b2 in self.b8 or 'Right' in self.b8) and Directions.EAST in b9: b10 = Directions.EAST
        if   (self.b3 in self.b8 or 'Up' in self.b8) and Directions.NORTH in b9:  b10 = Directions.NORTH
        if   (self.b4 in self.b8 or 'Down' in self.b8) and Directions.SOUTH in b9: b10 = Directions.SOUTH
        return b10
class class2(class1):
    b1 = 'j'
    b2 = 'l'
    b3 = 'i'
    b4 = 'k'
    b5 = 'u'
    def fonk4(self, b9):
        b10 = Directions.STOP
        if   (self.b1 in self.b8) and Directions.WEST in b9:  b10 = Directions.WEST
        if   (self.b2 in self.b8) and Directions.EAST in b9:  b10 = Directions.EAST
        if   (self.b3 in self.b8) and Directions.NORTH in b9: b10 = Directions.NORTH
        if   (self.b4 in self.b8) and Directions.SOUTH in b9: b10 = Directions.SOUTH
        return b10