from searchproblem import SearchProblem
class DGraph(SearchProblem):
    def __init__(self, matrix, goal_indices, start_state=0):
        self.matrix = matrix
        self.goal_indices = goal_indices
        self.start_state = start_state
    def get_start_state(self):
        return self.start_state
    def is_goal_state(self, state):
        return state in self.goal_indices
    def get_successors(self, state):
        row = self.matrix[state]
        successors = {index: cost for index, cost in enumerate(row) if cost is not None}
        return successors
if __name__ == "__main__":
    matrix = [
        [None, 1, None, None],
        [None, None, 2, None],
        [None, None, None, 3],
        [None, None, None, None]
    ]
    goal_indices = {3}
    graph = DGraph(matrix, goal_indices)
    print("Start state:", graph.get_start_state())
    print("Is goal state (2):", graph.is_goal_state(2))
    print("Is goal state (3):", graph.is_goal_state(3))
    print("Successors of state 1:", graph.get_successors(1))