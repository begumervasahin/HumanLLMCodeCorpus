4. Repository: alex-rantos/Project-1-Search-in-Pacman
   File: keyboardAgents.py
   URL: https:
   Code Content:
from game import Agent
from game import Directions
import random
class class1(Agent):
    b1 = 'a'
    b2 = 'd'
    b3 = 'w'
    b4 = 's'
    b5 = 'q'
    def fonk1( self, b6 = 0 ):
        self.b7 = Directions.STOP
        self.b6 = b6
        self.b8 = []
    def fonk2( self, state):
        from graphicsUtils import keys_waiting
        from graphicsUtils import keys_pressed
        b8 = keys_waiting() + keys_pressed()
        if b8 != []:
            self.b8 = b8
        b9 = state.getLegalActions(self.b6)
        b10 = self.fonk4(b9)
        if b10 = = Directions.STOP:
            if self.b7 in b9:
                b10 = self.b7
        if (self.b5 in self.b8) and Directions.STOP in b9: b10 = Directions.STOP
        if b10 not in b9:
            b10 = random.choice(b9)
        self.b7 = b10
        return b10
    def fonk3(self, b9):
        b10 = Directions.STOP
        if   (self.b1 in self.b8 or 'Left' in self.b8) and Directions.WEST in b9:  b10 = Directions.WEST
        if   (self.b2 in self.b8 or 'Right' in self.b8) and Directions.EAST in b9: b10 = Directions.EAST
        if   (self.b3 in self.b8 or 'Up' in self.b8) and Directions.NORTH in b9:   b10 = Directions.NORTH
        if   (self.b4 in self.b8 or 'Down' in self.b8) and Directions.SOUTH in b9: b10 = Directions.SOUTH
        return b10
class class2(class1):
    b1 = 'j'
    b2 = "l"
    b3 = 'i'
    b4 = 'k'
    b5 = 'u'
    def fonk4(self, b9):
        b10 = Directions.STOP
        if   (self.b1 in self.b8) and Directions.WEST in b9:  b10 = Directions.WEST
        if   (self.b2 in self.b8) and Directions.EAST in b9: b10 = Directions.EAST
        if   (self.b3 in self.b8) and Directions.NORTH in b9:   b10 = Directions.NORTH
        if   (self.b4 in self.b8) and Directions.SOUTH in b9: b10 = Directions.SOUTH
        return b10
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
