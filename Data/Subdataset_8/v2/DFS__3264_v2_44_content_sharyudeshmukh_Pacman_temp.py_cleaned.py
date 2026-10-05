from util import manhattanDistance
def evaluateGameState(currentGameState, successorGameState):
    pacmanPos = currentGameState.getPacmanPosition()
    foodLayout = currentGameState.getFood()
    ghostStates = currentGameState.getGhostStates()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    foodPositions = foodLayout.asList()
    nextGhostPositions = successorGameState.getGhostPositions()
    minFoodDistance = min(manhattanDistance(food, pacmanPos) for food in foodPositions)
    minGhostDistance = min(manhattanDistance(ghost, pacmanPos) for ghost in nextGhostPositions)
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000
    if len(foodPositions) == 0:
        return 1000000
    score = currentGameState.getScore() * 5
    score += len(currentGameState.getCapsules()) * 5
    score -= minFoodDistance * 2
    return score
