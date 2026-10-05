41. Repository: Daisy0828/Search
   File: dgraph.py
   URL: https:
   Code Content:
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
        successors = {}
        index = 0
        for cost in row:
            if not (cost == None):
                successors[index] = cost
            index += 1
        return successors
   README Content:
Implement breadth-first (bfs), depth-first (dfs), iterative deepening (ids), bi-directional (bds), and A* (astar) search algorithms.gorithms in their general forms. Use those search algorithms to solve tile game puzzles.
