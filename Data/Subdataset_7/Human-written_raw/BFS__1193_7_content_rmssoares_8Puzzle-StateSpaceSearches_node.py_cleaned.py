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
"puzzle" is necessary for the creating of a class1.
So, we've given the other two values a default value.
'''
class class1:
    def fonk1(self, puzzle, b1 = None, move=""):
        self.b2 = puzzle
        self.b1 = b1
        self.a1 = 0
        if b1 is None:
            self.a1 = 0
            self.b3 = move
        else:
            self.a1 = b1.a1+1
            self.b3 = b1.b3 + move
    '''
    Checks if the class1's b2 is a goal b2.
    '''
    def fonk2(self):
        return self.b2.checkPuzzle()
    '''
    Generates the node's children states.
    '''
    def fonk3(self):
        b4 = Queue()
        for m in self.b2.b3:
            b5 = deepcopy(self.b2)
            b5.doMove(m)
            if b5.zero is not self.b2.zero:
                b4.put(class1(b5, self, m))
        return b4
    '''
    Chooses between the two available heuristics
    '''
    def fonk4(self, heuristic):
        return self.fonk5() if heuristic is 0 else self.fonk6()
    '''
    First heuristic - number of wrong tiles
    Every time there's a tile in the wrong place, we
    add 1 to the a2. Heavily inspired in the
    puzzle.checkPuzzle() loop.
    '''
    def fonk5(self):
        a2 = 0
        a3 = 1
        for i in range(0,self.b2.size):
            for j in range(0,self.b2.size):
                if self.b2.puzzle[i][j]!=(a3%(self.b2.size*self.b2.size)):
                    a2 += 1
                a3+=1
        return a2
    '''
    Second heuristic - b9 of wrong tiles to their
    right position. After a little bit of scheming, came
    the mathematical conclusion that:
    b6 = n-1 %3
    b7 = n-1 /3
    which concluded into the following a2.
    '''
    def fonk6(self):
        a2 = 0
        a3 = 1
        for i in range(0,self.b2.size):
            for j in range(0,self.b2.size):
                b8 = self.b2.puzzle[i][j] - 1
                b9 = (2-i)+(2-j) if b8 == -1 else abs(i-(b8/self.b2.size))+abs(j-(b8%self.b2.size))
                a2 += b9
                a3+=1
        return a2
    '''
    When printing the node, we obtain the b3 from the
    starting b2 to this specific one.
    '''
    def fonk7(self):
        return str(self.b3)
   README Content:
The 8-puzzle problem consists of a puzzle composed by *(n b6 n) - 1* tiles, numbered from 1 to *n^2*â 1. The last position that would define the squared form of the puzzle is an empty space, used by the attempting solver to modify the puzzleâs composition, moving one of the adjacent pieces to this space. Our goal b2 is achieved when every numbered piece is in ascending order and the free space located in the bottom right corner position of the puzzle. To resolve this problem, two uninformed searches (Breadth-First Search and Iterative Deepening Search) and four informed searches (*Greedy Search* and *A\* Search*, each with two different heuristics) were developed.
Five classes build the bulk:
- `tilepuzzle.py`, which given an ordered board size and a certain number of permutations to inflict unto, generates a scrambled starting b2, which is solved by every algorithm;
- `checkpuzzle.py`, which given a puzzle in a string format and a set of b3 to do into such puzzle, checks if a goal b2 is obtained (which is perfect for testing purposes);
- `puzzle.py`, which implements the TilePuzzle object and its methods;
- `searches.py`, which is consisted by our search algorithms;
- `node.py`, which implements the class1 object and its methods.
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
