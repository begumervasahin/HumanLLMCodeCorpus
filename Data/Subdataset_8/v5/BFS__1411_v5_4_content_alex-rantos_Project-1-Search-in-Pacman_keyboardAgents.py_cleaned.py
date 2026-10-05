
from game import Agent, Directions
from graphicsUtils import keys_waiting, keys_pressed
import random
class KeyboardAgent(Agent):
    WEST_KEY  = 'a'
    EAST_KEY  = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'
    def __init__(self, index=0):
        self.last_move = Directions.STOP
        self.index = index
        self.keys = []
    def get_action(self, state):
        keys = keys_waiting() + keys_pressed()
        if keys:
            self.keys = keys
        legal_actions = state.get_legal_actions(self.index)
        move = self.get_move(legal_actions)
        if move == Directions.STOP and self.last_move in legal_actions:
            move = self.last_move
        if self.STOP_KEY in self.keys and Directions.STOP in legal_actions:
            move = Directions.STOP
        if move not in legal_actions:
            move = random.choice(legal_actions)
        self.last_move = move
        return move
    def get_move(self, legal_actions):
        move = Directions.STOP
        key_mapping = {
            'Left': self.WEST_KEY,
            'Right': self.EAST_KEY,
            'Up': self.NORTH_KEY,
            'Down': self.SOUTH_KEY
        }
        for key, direction in key_mapping.items():
            if direction in self.keys and getattr(Directions, key) in legal_actions:
                move = getattr(Directions, key)
                break
        return move
class KeyboardAgent2(KeyboardAgent):
    WEST_KEY  = 'j'
    EAST_KEY  = 'l'
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u'
    def get_move(self, legal_actions):
        move = Directions.STOP
        key_mapping = {
            'Left': self.WEST_KEY,
            'Right': self.EAST_KEY,
            'Up': self.NORTH_KEY,
            'Down': self.SOUTH_KEY
        }
        for key, direction in key_mapping.items():
            if direction in self.keys and getattr(Directions, key) in legal_actions:
                move = getattr(Directions, key)
                break
        return move