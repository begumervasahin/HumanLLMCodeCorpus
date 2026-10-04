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
class class1( Agent ):
    def fonk1( self, b1 ):
        self.b1 = b1
    def fonk2( self, state ):
        b2 = self.fonk6(state)
        if len(b2) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( b2 )
    def fonk3(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()
class class2( class1 ):
    "A ghost that chooses a legal action uniformly at random."
    def fonk4( self, state ):
        b2 = util.Counter()
        for a in state.getLegalActions( self.b1 ): b2[a] = 1.0
        b2.normalize()
        return b2
class class3( class1 ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def fonk5( self, b1, b3 = 0.8, b4=0.8 ):
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk6( self, state ):
        b5 = state.getGhostState( self.b1 )
        b6 = state.getLegalActions( self.b1 )
        b7 = state.getGhostPosition( self.b1 )
        b8 = b5.scaredTimer > 0
        a1 = 1
        if b8: a1 = 0.5
        b9 = [Actions.directionToVector( a, a1 ) for a in b6]
        b10 = [( b7[0]+a[0], b7[1]+a[1] ) for a in b9]
        b11 = state.getPacmanPosition()
        b12 = [manhattanDistance( b7, b11 ) for b7 in b10]
        if b8:
            b13 = max( b12 )
            b14 = self.b4
        else:
            b13 = min( b12 )
            b14 = self.b3
        b15 = [action for action, distance in zip( b6, b12 ) if distance == b13]
        b2 = util.Counter()
        for a in b15: b2[a] = b14 / len(b15)
        for a in b6: b2[a] += ( 1-b14 ) / len(b6)
        b2.normalize()
        return b2
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
