
from game import Agent, Actions, Directions
import util
from util import manhattanDistance
class class1(Agent):
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, state):
        b2 = self.fonk6(state)
        return util.chooseFromDistribution(b2) if b2 else Directions.STOP
    def fonk3(self, state):
        util.raiseNotDefined()
class class2(class1):
    def fonk4(self, state):
        b2 = util.Counter()
        b3 = state.getLegalActions(self.b1)
        for action in b3:
            b2[action] = 1.0
        b2.normalize()
        return b2
class class3(class1):
    def fonk5(self, b1, b4 = 0.8, b5=0.8):
        super().fonk5(b1)
        self.b4 = b4
        self.b5 = b5
    def fonk6(self, state):
        b6 = state.getGhostState(self.b1)
        b3 = state.getLegalActions(self.b1)
        b7 = state.getGhostPosition(self.b1)
        b8 = b6.scaredTimer > 0
        b9 = 0.5 if b8 else 1.0
        b10 = [Actions.directionToVector(action, b9) for action in b3]
        b11 = [(b7[0] + vec[0], b7[1] + vec[1]) for vec in b10]
        b12 = state.getPacmanPosition()
        b13 = [manhattanDistance(b7, b12) for b7 in b11]
        if b8:
            b14 = max(b13)
            b15 = self.b5
        else:
            b14 = min(b13)
            b15 = self.b4
        b16 = [action for action, distance in zip(b3, b13) if distance == b14]
        b2 = util.Counter()
        for action in b16:
            b2[action] = b15 / len(b16)
        for action in b3:
            b2[action] += (1 - b15) / len(b3)
        b2.normalize()
        return b2