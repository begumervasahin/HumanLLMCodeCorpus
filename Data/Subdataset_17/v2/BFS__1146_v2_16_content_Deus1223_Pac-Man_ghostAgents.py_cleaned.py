from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util
class GhostAgent(Agent):
    def __init__(self, index):
        self.index = index
    def getAction(self, state):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution(dist)
    def getDistribution(self, state):
        util.raiseNotDefined()
class RandomGhost(GhostAgent):
    def getDistribution(self, state):
        dist = util.Counter()
        for action in state.getLegalActions(self.index):
            dist[action] = 1.0
        dist.normalize()
        return dist
class DirectionalGhost(GhostAgent):
    def __init__(self, index, prob_attack=0.8, prob_scaredFlee=0.8):
        super().__init__(index)
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    def getDistribution(self, state):
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        ghostPos = state.getGhostPosition(self.index)
        pacmanPos = state.getPacmanPosition()
        isScared = ghostState.scaredTimer > 0
        speed = 0.5 if isScared else 1.0
        actionVectors = [Actions.directionToVector(action, speed) for action in legalActions]
        newPositions = [(ghostPos[0] + vector[0], ghostPos[1] + vector[1]) for vector in actionVectors]
        distancesToPacman = [manhattanDistance(pos, pacmanPos) for pos in newPositions]
        if isScared:
            bestScore = max(distancesToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distancesToPacman)
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip(legalActions, distancesToPacman) if distance == bestScore]
        dist = util.Counter()
        for action in bestActions:
            dist[action] = bestProb / len(bestActions)
        for action in legalActions:
            dist[action] += (1 - bestProb) / len(legalActions)
        dist.normalize()
        return dist