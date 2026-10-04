import itertools
from solver import Solver
class IDDFS(Solver):
    def __init__(self, initial_state):
        super(IDDFS, self).__init__(initial_state)
        self.frontier = []
    def dls(self, limit):
        self.frontier.append(self.initial_state)
        while self.frontier:
            current_board = self.frontier.pop()
            self.explored_nodes.add(tuple(current_board.state))
            if current_board.goal_test():
                self.set_solution(current_board)
                return self.solution
            if current_board.depth < limit:
                for neighbor in current_board.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.frontier.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
                        self.max_depth = max(self.max_depth, neighbor.depth)
        return None
    def solve(self):
        for depth_limit in itertools.count():
            self.frontier = []
            self.explored_nodes = set()
            self.max_depth = 0
            self.frontier.append(self.initial_state)
            solution = self.dls(depth_limit)
            if solution is not None:
                break
        return
if __name__ == "__main__":
    from board import Board
    initial_state = Board([1, 2, 5, 3, 4, 0, 6, 7, 8])
    solver = IDDFS(initial_state)
    solver.solve()
    if solver.solution:
        print("Solution found:")
        for step in solver.solution:
            print(step)
    else:
        print("No solution found.")