7. Repository: rmssoares/8Puzzle-StateSpaceSearches
   File: node.py
   URL: https:
   Code Content:
'''
Code developed by Ricardo Soares
------------------------------
University of Aberdeen
MSc Artificial Intelligence
Written in Python 2.7.14
'''
from Queue import Queue
from copy import deepcopy
'''
Instantiates the node. Only the passing argument
"puzzle" is necessary for the creating of a Node.
So, we've given the other two values a default value.
'''
class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth+1
            self.moves = parent.moves + move
    '''
    Checks if the Node's state is a goal state.
    '''
    def goalState(self):
        return self.state.checkPuzzle()
    '''
    Generates the node's children states.
    '''
    def succ(self):
        succs = Queue()
        for m in self.state.moves:
            p = deepcopy(self.state)
            p.doMove(m)
            if p.zero is not self.state.zero:
                succs.put(Node(p, self, m))
        return succs
    '''
    Chooses between the two available heuristics
    '''
    def costHeur(self, heuristic):
        return self.nWrongTiles() if heuristic is 0 else self.manhattanDistance()
    '''
    First heuristic - number of wrong tiles
    Every time there's a tile in the wrong place, we
    add 1 to the result. Heavily inspired in the
    puzzle.checkPuzzle() loop.
    '''
    def nWrongTiles(self):
        result = 0
        count = 1
        for i in range(0,self.state.size):
            for j in range(0,self.state.size):
                if self.state.puzzle[i][j]!=(count%(self.state.size*self.state.size)):
                    result += 1
                count+=1
        return result
    '''
    Second heuristic - distance of wrong tiles to their
    right position. After a little bit of scheming, came
    the mathematical conclusion that:
    x = n-1 %3
    y = n-1 /3
    which concluded into the following result.
    '''
    def manhattanDistance(self):
        result = 0
        count = 1
        for i in range(0,self.state.size):
            for j in range(0,self.state.size):
                index = self.state.puzzle[i][j] - 1
                distance = (2-i)+(2-j) if index == -1 else abs(i-(index/self.state.size))+abs(j-(index%self.state.size))
                result += distance
                count+=1
        return result
    '''
    When printing the node, we obtain the moves from the
    starting state to this specific one.
    '''
    def __str__(self):
        return str(self.moves)
   README Content:
The 8-puzzle problem consists of a puzzle composed by *(n x n) - 1* tiles, numbered from 1 to *n^2*â 1. The last position that would define the squared form of the puzzle is an empty space, used by the attempting solver to modify the puzzleâs composition, moving one of the adjacent pieces to this space. Our goal state is achieved when every numbered piece is in ascending order and the free space located in the bottom right corner position of the puzzle. To resolve this problem, two uninformed searches (Breadth-First Search and Iterative Deepening Search) and four informed searches (*Greedy Search* and *A\* Search*, each with two different heuristics) were developed.
Five classes build the bulk:
- `tilepuzzle.py`, which given an ordered board size and a certain number of permutations to inflict unto, generates a scrambled starting state, which is solved by every algorithm;
- `checkpuzzle.py`, which given a puzzle in a string format and a set of moves to do into such puzzle, checks if a goal state is obtained (which is perfect for testing purposes);
- `puzzle.py`, which implements the TilePuzzle object and its methods;
- `searches.py`, which is consisted by our search algorithms;
- `node.py`, which implements the Node object and its methods.
From these, `tilepuzzle.py`, `puzzle.py` and `checkpuzzle.py` **were given by the courseâs tutor** (*Dr. Nir Oren*, for the course of *Foundations of AI* in the *University of Aberdeen*) and have gone through slight modifications to accommodate the studentâs resolution. The approach the student has taken goes through running every algorithm orderly, one after the other, by generating a random puzzle.
The software provided was entirely done in *Python 2.7*. To start, clone the present repository into your local machine. If you're unaware of how to achieve this, please become familiar with the mechanisms of [GitHub](https:
```
git clone git@github.com:thyriki/8Puzzle-StateSpaceSearches.git
```
Ensure that you have [Python 2.7](https:
Navigate to the project's folder, and run the following command:
```
python tilepuzzle.py 3 10
```
According to the provided arguments, this would generate a 3 by 3 puzzle, with ten random permutations caused unto it.
* **Ricardo Soares** - [rmssoares](https:
For any inquiries, feel free to open up an issue.
