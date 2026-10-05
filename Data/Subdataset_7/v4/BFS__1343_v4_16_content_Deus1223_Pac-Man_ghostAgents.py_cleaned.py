
from game import Agent, Actions, Directions
from util import manhattanDistance, Counter
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
        b2 = Counter()
        for action in state.getLegalActions(self.b1):
            b2[action] = 1.0
        b2.normalize()
        return b2
class class3(class1):
    def fonk5(self, b1, b3 = 0.8, b4=0.8):
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk6(self, state):
        b5 = state.getGhostState(self.b1)
        b6 = state.getLegalActions(self.b1)
        b7 = state.getGhostPosition(self.b1)
        b8 = b5.scaredTimer > 0
        a1 = 1
        if b8:
            a1 = 0.5
        b9 = [Actions.directionToVector(action, a1) for action in b6]
        b10 = [(b7[0] + vector[0], b7[1] + vector[1]) for vector in b9]
        b11 = state.getPacmanPosition()
        b12 = [manhattanDistance(pos, b11) for pos in b10]
        if b8:
            b13 = max(b12)
            b14 = self.b4
        else:
            b13 = min(b12)
            b14 = self.b3
        b15 = [action for action, distance in zip(b6, b12) if distance == b13]
        b2 = Counter()
        for action in b15:
            b2[action] = b14 / len(b15)
        for action in b6:
            b2[action] += (1 - b14) / len(b6)
        b2.normalize()
        return b2