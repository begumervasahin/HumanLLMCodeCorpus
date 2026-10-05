from collections import deque
class PuzzleSolver:
    def __init__(self):
        pass
    def depth_first_solve(self, puzzle):
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
                if config.fail_fast() or len(config.extensions()) == 0:
                    continue
                a = PuzzleNode(config)
                visited.add(str(a.puzzle))
                stack.append(a)
        return None
    def breadth_first_solve(self, puzzle):
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
        self.puzzle = puzzle
        self.parent = parent
        self.children = children[:] if children is not None else []
        self.visited = False
    def __eq__(self, other):
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all(x in self.children for x in other.children) and
                all(x in other.children for x in self.children))
    def __str__(self):
        return "{}\n\n{}".format(self.puzzle, "\n".join(str(x) for x in self.children))
if __name__ == '__main__':
    pass