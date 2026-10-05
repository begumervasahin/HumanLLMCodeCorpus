4. Repository: alex-rantos/Project-1-Search-in-Pacman
   File: ghostAgents.py
   URL: https:
   Code Content:
from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util
class GhostAgent( Agent ):
    def __init__( self, index ):
        self.index = index
    def getAction( self, state ):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist )
    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()
class RandomGhost( GhostAgent ):
    "A ghost that chooses a legal action uniformly at random."
    def getDistribution( self, state ):
        dist = util.Counter()
        for a in state.getLegalActions( self.index ): dist[a] = 1.0
        dist.normalize()
        return dist
class DirectionalGhost( GhostAgent ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
    def getDistribution( self, state ):
        ghostState = state.getGhostState( self.index )
        legalActions = state.getLegalActions( self.index )
        pos = state.getGhostPosition( self.index )
        isScared = ghostState.scaredTimer > 0
        speed = 1
        if isScared: speed = 0.5
        actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
        newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
        pacmanPosition = state.getPacmanPosition()
        distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
        if isScared:
            bestScore = max( distancesToPacman )
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min( distancesToPacman )
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]
        dist = util.Counter()
        for a in bestActions: dist[a] = bestProb / len(bestActions)
        for a in legalActions: dist[a] += ( 1-bestProb ) / len(legalActions)
        dist.normalize()
        return dist
   README Content:
Project : http:
------------------
Question q1: 3/3
Question q2: 3/3
Question q3: 3/3
Question q4: 3/3
Question q5: 3/3
Question q6: 3/3
Question q7: 2/4
Question q8: 3/3
------------------
Total: 23/25
The above algorithms are implemented so they pass the autograder.py.
So the idea is to check the node if has been visited before.Then you push it to
visited list and check if we reached goalState - if not expand children based on algorithm.
**Code is fully explained in comments.**
I changed my first-implementation of BFS to the one I used for ucs/a* so I can calculate the
number of corners I have visited.
In this problem the function of manhattanDistance() from util.py has been used.
First @cornersHeuristic we check which corners are left to visit and then we calculate
the currentpoint to each corner respectively - all written efficiently and cleanly in a
single line of code ::
*min([(util.manhattanDistance(curPoint, corner), corner) for corner in cornersLeftToVisit])*
There are 2 implementations.
First one is an oneliner that gets 2/4 on autograder and returns the length of the foodGrid.In that way
each food-node gets an additional cost of how many foods are left. *12517 nodes in ~9sec*
Second and faster implementation uses manhattanDistance to calculate the distance between each food
and pacman distance.(This one fails autograder.py) *6126 nodes in 3sec*
Worked as problem 6.There is no difference between bfs,ucs,astar as far as path cost is concerned.
