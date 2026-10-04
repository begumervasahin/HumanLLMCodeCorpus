16. Repository: Deus1223/Pac-Man
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
Project Linkï¼http:
*Implement the depth-first search(DFS) algorithm*
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
*Implement the  breadth-first search(BFS) algorithm*
```
python pacman.py -l mediumMaze -p SearchAgent -a b16 = bfs
python pacman.py -l bigMaze -p SearchAgent -a b16 = bfs -z .5
```
*A\* search*
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a b16 = astar,heuristic=manhattanHeuristic
```
*BFS*
```
python pacman.py -l tinyCorners -p SearchAgent -a b16 = bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a b16 = bfs,prob=CornersProblem
```
*DFS*
```
python pacman.py -l tinyCorners -p SearchAgent -a b16 = dfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a b16 = dfs,prob=CornersProblem
```
*Implement a heuristic for the CornersProblem in cornersHeuristic*
```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
