
from puzzle import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def depth_first_solve(puzzle):
    visited = set()
    stack = deque([PuzzleNode(puzzle)])
    while stack:
        node = stack.pop()
        for config in node.puzzle.extensions():
            if str(config) in visited:
                continue
            if config.is_solved():
                return PuzzleNode(config)
            if config.fail_fast() or not config.extensions():
                continue
            child_node = PuzzleNode(config)
            visited.add(str(child_node.puzzle))
            stack.append(child_node)
    return None
def breadth_first_solve(puzzle):
    visited = set()
    queue = deque([PuzzleNode(puzzle)])
    while queue:
        node = queue.popleft()
        for config in node.puzzle.extensions():
            if str(config) in visited:
                continue
            if config.is_solved():
                return PuzzleNode(config)
            if config.fail_fast() or not config.extensions():
                continue
            child_node = PuzzleNode(config)
            visited.add(str(child_node.puzzle))
            queue.append(child_node)
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