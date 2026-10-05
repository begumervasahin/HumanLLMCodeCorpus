21. Repository: sagar-13/PuzzleSolver
   File: puzzle_tools.py
   URL: https:
   Code Content:
from puzzle import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def depth_first_solve(puzzle):
    visited = set()
    stack = deque()
    stack.append(PuzzleNode(puzzle))
    while stack:
        element = stack.pop()
        for config in element.puzzle.extensions():
            if str(config) in visited:
                continue
            if config.is_solved():
                return PuzzleNode(config)
            if config.fail_fast() or len(config.extensions())== 0:
                continue
            a = PuzzleNode(config)
            visited.add(str(a.puzzle))
            stack.append(a)
    return None
def breadth_first_solve(puzzle):
    visited = set()
    queue = deque()
    queue.append(PuzzleNode(puzzle))
    while queue:
        element = queue.popleft()
        for child in element.puzzle.extensions():
            if str(child) in visited:
                continue
            if child.is_solved():
                return PuzzleNode(child)
            if child.fail_fast() or len(child.extensions()) == 0:
                continue
            a = PuzzleNode(child)
            visited.add(str(a.puzzle))
            queue.append(a)
    return None
class PuzzleNode:
    def __init__(self, puzzle=None, children=None, parent=None):
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]
        self.visited = False
    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other
        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool
        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        Return a human-readable string representing PuzzleNode self.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
   README Content:
Puzzle solver which use BFS and DFS algorithms to search for solutions and solve various puzzles.
