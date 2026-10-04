
from game import Agent, Actions, Directions
import util
from util import manhattanDistance
class GhostAgent(Agent):
    def __init__(self, index):
        self.index = index
    def getAction(self, state):
        dist = self.getDistribution(state)
        return util.chooseFromDistribution(dist) if dist else Directions.STOP
    def getDistribution(self, state):
        util.raiseNotDefined()
class RandomGhost(GhostAgent):
    def getDistribution(self, state):
        dist = util.Counter()
        legalActions = state.getLegalActions(self.index)
        for action in legalActions:
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
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0
        speed = 0.5 if isScared else 1.0
        actionVectors = [Actions.directionToVector(action, speed) for action in legalActions]
        newPositions = [(pos[0] + vec[0], pos[1] + vec[1]) for vec in actionVectors]
        pacmanPosition = state.getPacmanPosition()
        distancesToPacman = [manhattanDistance(pos, pacmanPosition) for pos in newPositions]
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