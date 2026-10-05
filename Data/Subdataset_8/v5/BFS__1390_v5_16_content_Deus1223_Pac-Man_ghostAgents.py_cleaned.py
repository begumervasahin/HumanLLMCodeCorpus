
from game import Agent, Actions, Directions
from util import manhattanDistance, Counter
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
        dist = Counter()
        for action in state.getLegalActions(self.index):
            dist[action] = 1.0
        dist.normalize()
        return dist
class DirectionalGhost(GhostAgent):
    def __init__(self, index, prob_attack=0.8, prob_scared_flee=0.8):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scared_flee = prob_scared_flee
    def getDistribution(self, state):
        ghost_state = state.getGhostState(self.index)
        legal_actions = state.getLegalActions(self.index)
        position = state.getGhostPosition(self.index)
        is_scared = ghost_state.scaredTimer > 0
        speed = 1 if not is_scared else 0.5
        action_vectors = [Actions.directionToVector(action, speed) for action in legal_actions]
        new_positions = [(position[0] + vector[0], position[1] + vector[1]) for vector in action_vectors]
        pacman_position = state.getPacmanPosition()
        distances_to_pacman = [manhattanDistance(pos, pacman_position) for pos in new_positions]
        if is_scared:
            best_score = max(distances_to_pacman)
            best_prob = self.prob_scared_flee
        else:
            best_score = min(distances_to_pacman)
            best_prob = self.prob_attack
        best_actions = [action for action, distance in zip(legal_actions, distances_to_pacman) if distance == best_score]
        dist = Counter()
        for action in best_actions:
            dist[action] = best_prob / len(best_actions)
        for action in legal_actions:
            dist[action] += (1 - best_prob) / len(legal_actions)
        dist.normalize()
        return dist