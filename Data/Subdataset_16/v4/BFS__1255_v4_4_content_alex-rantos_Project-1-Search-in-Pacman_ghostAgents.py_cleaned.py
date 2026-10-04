
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
        b8 = b5.scaredTimer > 0
        b9 = 1 if not b8 else 0.5
        b10 = [Actions.directionToVector(a, b9) for a in b6]
        b11 = [(b7[0] + a[0], b7[1] + a[1]) for a in b10]
        b12 = state.getPacmanPosition()
        b13 = [manhattanDistance(b7, b12) for b7 in b11]
        if b8:
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