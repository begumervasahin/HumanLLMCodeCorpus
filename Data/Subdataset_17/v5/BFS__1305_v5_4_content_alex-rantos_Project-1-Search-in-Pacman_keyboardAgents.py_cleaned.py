
from game import Agent, Directions
import random
class KeyboardAgent(Agent):
    WEST_KEY = 'a'
    EAST_KEY = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'
    def __init__(self, index=0):
        super().__init__()
        self.lastMove = Directions.STOP
        self.index = index
        self.keys = []
    def getAction(self, state):
        from graphicsUtils import keys_waiting, keys_pressed
        self.keys = keys_waiting() + keys_pressed()
        legal_actions = state.getLegalActions(self.index)
        move = self.getMove(legal_actions)
        if move == Directions.STOP and self.lastMove in legal_actions:
            move = self.lastMove
        if self.STOP_KEY in self.keys and Directions.STOP in legal_actions:
            move = Directions.STOP
        if move not in legal_actions:
            move = random.choice(legal_actions)
        self.lastMove = move
        return move
    def getMove(self, legal_actions):
        move = Directions.STOP
        if (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.WEST in legal_actions:
            move = Directions.WEST
        if (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.EAST in legal_actions:
            move = Directions.EAST
        if (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.NORTH in legal_actions:
            move = Directions.NORTH
        if (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.SOUTH in legal_actions:
            move = Directions.SOUTH
        return move
class KeyboardAgent2(KeyboardAgent):
    WEST_KEY = 'j'
    EAST_KEY = 'l'
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u'
    def getMove(self, legal_actions):
        move = Directions.STOP
        if self.WEST_KEY in self.keys and Directions.WEST in legal_actions:
            move = Directions.WEST
        if self.EAST_KEY in self.keys and Directions.EAST in legal_actions:
            move = Directions.EAST
        if self.NORTH_KEY in self.keys and Directions.NORTH in legal_actions:
            move = Directions.NORTH
        if self.SOUTH_KEY in self.keys and Directions.SOUTH in legal_actions:
            move = Directions.SOUTH
        return move