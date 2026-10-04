4. Repository: alex-rantos/Project-1-Search-in-Pacman
   File: keyboardAgents.py
   URL: https:
   Code Content:
from game import Agent
from game import Directions
import random
class KeyboardAgent(Agent):
    WEST_KEY  = 'a'
    EAST_KEY  = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'
    def __init__( self, index = 0 ):
        self.lastMove = Directions.STOP
        self.index = index
        self.keys = []
    def getAction( self, state):
        from graphicsUtils import keys_waiting
        from graphicsUtils import keys_pressed
        keys = keys_waiting() + keys_pressed()
        if keys != []:
            self.keys = keys
        legal = state.getLegalActions(self.index)
        move = self.getMove(legal)
        if move == Directions.STOP:
            if self.lastMove in legal:
                move = self.lastMove
        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP
        if move not in legal:
            move = random.choice(legal)
        self.lastMove = move
        return move
    def getMove(self, legal):
        move = Directions.STOP
        if   (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if   (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if   (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if   (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move
class KeyboardAgent2(KeyboardAgent):
    WEST_KEY  = 'j'
    EAST_KEY  = "l"
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u'
    def getMove(self, legal):
        move = Directions.STOP
        if   (self.WEST_KEY in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if   (self.EAST_KEY in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if   (self.NORTH_KEY in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if   (self.SOUTH_KEY in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move
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
