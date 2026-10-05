from util import manhattanDistance
def fonk1(currentGameState, successorGameState):
    b1 = currentGameState.getPacmanPosition()
    b2 = currentGameState.getFood().asList()
    b3 = successorGameState.getGhostPositions()
    b4 = min(manhattanDistance(food, b1) for food in b2) if b2 else float('inf')
    b5 = min(manhattanDistance(ghost, b1) for ghost in b3) if b3 else float('inf')
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000
    if not b2:
        return 1000000
    b6 = currentGameState.getScore() * 5
    b6 += len(currentGameState.getCapsules()) * 5
    b6 -= b4 * 2
    return b6