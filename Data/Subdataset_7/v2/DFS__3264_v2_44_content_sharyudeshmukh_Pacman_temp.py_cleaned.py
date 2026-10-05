from util import manhattanDistance
def fonk1(currentGameState, successorGameState):
    b1 = currentGameState.getPacmanPosition()
    b2 = currentGameState.getFood()
    b3 = currentGameState.getGhostStates()
    b4 = [ghostState.scaredTimer for ghostState in b3]
    b5 = b2.asList()
    b6 = successorGameState.getGhostPositions()
    b7 = min(manhattanDistance(food, b1) for food in b5)
    b8 = min(manhattanDistance(ghost, b1) for ghost in b6)
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000
    if len(b5) == 0:
        return 1000000
    b9 = currentGameState.getScore() * 5
    b9 += len(currentGameState.getCapsules()) * 5
    b9 -= b7 * 2
    return b9
