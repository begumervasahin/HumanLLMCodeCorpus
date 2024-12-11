from util import manhattanDistance
def fonk1(currentGameState, successorGameState):
    b1 = currentGameState.getPacmanPosition()
    b2 = currentGameState.getFood()
    b3 = currentGameState.getGhostStates()
    b4 = [ghostState.scaredTimer for ghostState in b3]
    b5 = b2.asList()
    b6 = successorGameState.getGhostPositions()
    a1 = 1000
    for food in b5:
        b7 = manhattanDistance(food, b1)
        a1 = min(a1, b7)
    a2 = 1000
    for ghost in b6:
        b8 = manhattanDistance(ghost, b1)
        a2 = min(a2, b8)
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000
    if len(b5) == 0:
        return 1000000
    else:
        b9 = min(b5)
    b10 = currentGameState.getScore() * 5
    b10 += len(currentGameState.getCapsules()) * 5
    b10 -= a1 * 2
    return b10
