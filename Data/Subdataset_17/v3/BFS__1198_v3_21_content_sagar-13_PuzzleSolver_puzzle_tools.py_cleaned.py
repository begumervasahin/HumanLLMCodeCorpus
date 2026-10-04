import sys
from collections import deque
sys.setrecursionlimit(10**6)
class Puzzle:
    def extensions(self):
        pass
    def is_solved(self):
        pass
    def fail_fast(self):
        pass
class PuzzleNode:
    def __init__(self, puzzle=None, children=None, parent=None):
        self.puzzle = puzzle
        self.parent = parent
        self.children = children[:] if children else []
        self.visited = False
    def __eq__(self, other):
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all(x in self.children for x in other.children) and
                all(x in other.children for x in self.children))
    def __str__(self):
        return "{}\n\n{}".format(self.puzzle, "\n".join(str(x) for x in self.children))
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
            new_node = PuzzleNode(config)
            visited.add(str(new_node.puzzle))
            stack.append(new_node)
    return None
def breadth_first_solve(puzzle):
    visited = set()
    queue = deque([PuzzleNode(puzzle)])
    while queue:
        node = queue.popleft()
        for child in node.puzzle.extensions():
            if str(child) in visited:
                continue
            if child.is_solved():
                return PuzzleNode(child)
            if child.fail_fast() or not child.extensions():
                continue
            new_node = PuzzleNode(child)
            visited.add(str(new_node.puzzle))
            queue.append(new_node)
    return None
if __name__ == "__main__":
    class ExamplePuzzle(Puzzle):
        def __init__(self, state):
            self.state = state
        def extensions(self):
            pass
        def is_solved(self):
            pass
        def fail_fast(self):
            pass
        def __str__(self):
            return str(self.state)
    initial_state = ExamplePuzzle(state="initial state")
    solution_node = depth_first_solve(initial_state)
    if solution_node:
        print("Solution found using DFS:")
        print(solution_node)
    else:
        print("No solution found using DFS.")
    solution_node = breadth_first_solve(initial_state)
    if solution_node:
        print("Solution found using BFS:")
        print(solution_node)
    else:
        print("No solution found using BFS.")