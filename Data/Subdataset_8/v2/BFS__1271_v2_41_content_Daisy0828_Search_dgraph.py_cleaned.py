
class SearchProblem:
    def get_start_state(self):
        raise NotImplementedError
    def is_goal_state(self, state):
        raise NotImplementedError
    def get_successors(self, state):
        raise NotImplementedError
class DirectedGraph(SearchProblem):
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
        successors = {}
        index = 0
        for cost in row:
            if cost is not None:
                successors[index] = cost
            index += 1
        return successors
README_CONTENT =
if __name__ == "__main__":
    matrix = [
        [None, 2, 3, None],
        [None, None, None, 1],
        [4, None, None, None],
        [None, None, None, None]
    ]
    goal_indices = {3}
    dgraph = DirectedGraph(matrix, goal_indices)
    print("Start state:", dgraph.get_start_state())
    print("Is 3 a goal state?", dgraph.is_goal_state(3))
    print("Successors of state 2:", dgraph.get_successors(2))