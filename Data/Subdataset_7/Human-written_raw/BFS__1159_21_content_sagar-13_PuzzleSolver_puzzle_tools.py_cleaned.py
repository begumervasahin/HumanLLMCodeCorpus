21. Repository: sagar-13/PuzzleSolver
   File: puzzle_tools.py
   URL: https:
   Code Content:
from b6 import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def fonk1(b6):
    b1 = set()
    b2 = deque()
    b2.append(class1(b6))
    while b2:
        b3 = b2.pop()
        for config in b3.b6.extensions():
            if str(config) in b1:
                continue
            if config.is_solved():
                return class1(config)
            if config.fail_fast() or len(config.extensions())== 0:
                continue
            b4 = class1(config)
            b1.add(str(b4.b6))
            b2.append(b4)
    return None
def fonk2(b6):
    b1 = set()
    b5 = deque()
    b5.append(class1(b6))
    while b5:
        b3 = b5.popleft()
        for child in b3.b6.extensions():
            if str(child) in b1:
                continue
            if child.is_solved():
                return class1(child)
            if child.fail_fast() or len(child.extensions()) == 0:
                continue
            b4 = class1(child)
            b1.add(str(b4.b6))
            b5.append(b4)
    return None
class class1:
    def fonk3(self, b6 = None, b8=None, b7=None):
        self.b6, self.b7 = b6, b7
        if b8 is None:
            self.b8 = []
        else:
            self.b8 = b8[:]
        self.b1 = False
    def fonk4(self, other):
        """
        Return whether class1 self is equivalent to other
        @type self: class1
        @type other: class1 | Any
        @rtype: bool
        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> b9 = class1(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> b10 = class1(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> b11 = class1(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> b9.fonk4(b10)
        True
        >>> b9.fonk4(b11)
        False
        Return b4 human-readable string representing class1 self.
        """
        return "{}\n\n{}".format(self.b6,
                                 "\n".join([str(x) for x in self.b8]))
   README Content:
Puzzle solver which use BFS and DFS algorithms to search for solutions and solve various puzzles.
