class Node:
    def __init__(self, parent=None, world_state=None, priority=None):
        self.parent = parent
        self.world_state = world_state
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
class BlockSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    def solve(self):
        pass
if __name__ == "__main__":
    initial_state = {
        'size': (3, 3),
        'a': (0, 2),
        'b': (1, 2),
        'agent': (2, 2)
    }
    goal_state = {
        'a': (1, 1),
        'b': (1, 2)
    }
    solver = BlockSolver(initial_state, goal_state)
    solver.solve()