from searchproblem import SearchProblem
class DirectedGraph(SearchProblem):
    def __init__(self, adjacency_matrix, goal_indices, start_state=0):
        self.adjacency_matrix = adjacency_matrix
        self.goal_indices = goal_indices
        self.start_state = start_state
    def get_start_state(self):
        return self.start_state
    def is_goal_state(self, state):
        return state in self.goal_indices
    def get_successors(self, state):
        row = self.adjacency_matrix[state]
        successors = {}
        for index, cost in enumerate(row):
            if cost is not None:
                successors[index] = cost
        return successors