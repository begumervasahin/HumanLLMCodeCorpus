from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util
class class1(Agent):
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, state):
        b2 = self.fonk6(state)
        if len(b2) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution(b2)
    def fonk3(self, state):
        util.raiseNotDefined()
class class2(class1):
    def fonk4(self, state):
        b2 = util.Counter()
        for action in state.getLegalActions(self.b1):
            b2[action] = 1.0
        b2.normalize()
        return b2
class class3(class1):
    def fonk5(self, b1, b3 = 0.8, b4=0.8):
        super().fonk5(b1)
        self.b3 = b3
        self.b4 = b4
    def fonk6(self, state):
        b5 = state.getGhostState(self.b1)
        b6 = state.getLegalActions(self.b1)
        b7 = state.getGhostPosition(self.b1)
        b8 = state.getPacmanPosition()
        b9 = b5.scaredTimer > 0
        b10 = 0.5 if b9 else 1.0
        b11 = [Actions.directionToVector(action, b10) for action in b6]
        b12 = [(b7[0] + vector[0], b7[1] + vector[1]) for vector in b11]
        b13 = [manhattanDistance(pos, b8) for pos in b12]
        if b9:
            b14 = max(b13)
            b15 = self.b4
        else:
            b14 = min(b13)
            b15 = self.b3
        b16 = [action for action, distance in zip(b6, b13) if distance == b14]
        b2 = util.Counter()
        for action in b16:
            b2[action] = b15 / len(b16)
        for action in b6:
            b2[action] += (1 - b15) / len(b6)
        b2.normalize()
        return b2