
from puzzle import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def depth_first_solve(puzzle):
    visited = set()
    stack = deque([PuzzleNode(puzzle)])
    while stack:
        node = stack.pop()
        if node.puzzle.is_solved():
            return node
        visited.add(str(node.puzzle))
        for config in node.puzzle.extensions():
            if str(config) not in visited and not config.fail_fast():
                stack.append(PuzzleNode(config, parent=node))
    return None
def breadth_first_solve(puzzle):
    visited = set()
    queue = deque([PuzzleNode(puzzle)])
    while queue:
        node = queue.popleft()
        if node.puzzle.is_solved():
            return node
        visited.add(str(node.puzzle))
        for config in node.puzzle.extensions():
            if str(config) not in visited and not config.fail_fast():
                queue.append(PuzzleNode(config, parent=node))
    return None
class PuzzleNode:
    def __init__(self, puzzle=None, children=None, parent=None):
        self.puzzle = puzzle
        self.parent = parent
        self.children = children[:] if children else []
    def __eq__(self, other):
        return (
            isinstance(other, PuzzleNode) and
            self.puzzle == other.puzzle and
            set(self.children) == set(other.children)
        )
    def __str__(self):
        children_str = "\n".join(str(child) for child in self.children)
        return f"{self.puzzle}\n\n{children_str}"