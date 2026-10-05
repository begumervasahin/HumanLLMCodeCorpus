from util import manhattanDistance
def evaluateGameState(currentGameState, successorGameState):
    pacmanPos = currentGameState.getPacmanPosition()
    foodLayout = currentGameState.getFood().asList()
    ghostPositions = successorGameState.getGhostPositions()
    minFoodDistance = min(manhattanDistance(food, pacmanPos) for food in foodLayout) if foodLayout else float('inf')
    minGhostDistance = min(manhattanDistance(ghost, pacmanPos) for ghost in ghostPositions) if ghostPositions else float('inf')
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000
    if not foodLayout:
        return 1000000
    score = currentGameState.getScore() * 5
    score += len(currentGameState.getCapsules()) * 5
    score -= minFoodDistance * 2
    return score