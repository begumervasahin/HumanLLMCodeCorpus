from copy import deepcopy
from math import sqrt
from queue import Queue
from heapq import heappush, heappop
class ProblemClass:
    def __init__(self):
        self.state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_init_state(self):
        return self.state
    def get_moves(self, my_state):
        moves = []
        indexes = [(ix, iy) for ix, row in enumerate(my_state) for iy, i in enumerate(row) if i == 0]
        i_index, j_index = indexes[0]
        if i_index > 0:
            moves.append('U')
        if i_index < 2:
            moves.append('D')
        if j_index > 0:
            moves.append('L')
        if j_index < 2:
            moves.append('R')
        return moves
    def do_move(self, states, transaction):
        my_state = deepcopy(states)
        indexes = [(ix, iy) for ix, row in enumerate(my_state) for iy, i in enumerate(row) if i == 0]
        i_index, j_index = indexes[0]
        if transaction == 'R':
            my_state[i_index][j_index] = my_state[i_index][j_index + 1]
            my_state[i_index][j_index + 1] = 0
        elif transaction == 'L':
            my_state[i_index][j_index] = my_state[i_index][j_index - 1]
            my_state[i_index][j_index - 1] = 0
        elif transaction == 'U':
            my_state[i_index][j_index] = my_state[i_index - 1][j_index]
            my_state[i_index - 1][j_index] = 0
        elif transaction == 'D':
            my_state[i_index][j_index] = my_state[i_index + 1][j_index]
            my_state[i_index + 1][j_index] = 0
        return my_state
    def check_goal(self, my_state):
        return my_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, my_matrix):
        sum_h = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                indexes = [(ix, iy) for ix, row in enumerate(my_matrix) for iy, i in enumerate(row) if i == number]
                sum_h += sqrt((i - indexes[0][0]) ** 2 + (j - indexes[0][1]) ** 2)
        return round(sum_h, 2)
def bfs(problem):
    start_state = problem.get_init_state()
    if problem.check_goal(start_state):
        return start_state
    frontier = Queue()
    frontier.put(start_state)
    explored = set()
    while not frontier.empty():
        state = frontier.get()
        explored.add(tuple(map(tuple, state)))
        for move in problem.get_moves(state):
            new_state = problem.do_move(state, move)
            if tuple(map(tuple, new_state)) not in explored:
                if problem.check_goal(new_state):
                    return new_state
                frontier.put(new_state)
    return None
def dfs(problem, limit=10):
    start_state = problem.get_init_state()
    if problem.check_goal(start_state):
        return start_state
    return dfs_recursive(problem, start_state, set(), limit)
def dfs_recursive(problem, state, explored, limit):
    if problem.check_goal(state):
        return state
    if limit == 0:
        return None
    explored.add(tuple(map(tuple, state)))
    for move in problem.get_moves(state):
        new_state = problem.do_move(state, move)
        if tuple(map(tuple, new_state)) not in explored:
            result = dfs_recursive(problem, new_state, explored, limit - 1)
            if result is not None:
                return result
    return None
def ucs(problem):
    start_state = problem.get_init_state()
    if problem.check_goal(start_state):
        return start_state
    frontier = []
    heappush(frontier, (0, start_state))
    explored = set()
    while frontier:
        cost, state = heappop(frontier)
        if problem.check_goal(state):
            return state
        explored.add(tuple(map(tuple, state)))
        for move in problem.get_moves(state):
            new_state = problem.do_move(state, move)
            if tuple(map(tuple, new_state)) not in explored:
                new_cost = cost + 1
                heappush(frontier, (new_cost, new_state))
    return None
def a_star(problem):
    start_state = problem.get_init_state()
    if problem.check_goal(start_state):
        return start_state
    frontier = []
    heappush(frontier, (problem.find_h(start_state), start_state))
    explored = set()
    while frontier:
        _, state = heappop(frontier)
        if problem.check_goal(state):
            return state
        explored.add(tuple(map(tuple, state)))
        for move in problem.get_moves(state):
            new_state = problem.do_move(state, move)
            if tuple(map(tuple, new_state)) not in explored:
                new_cost = problem.find_h(new_state) + len(explored)
                heappush(frontier, (new_cost, new_state))
    return None
def main():
    problem = ProblemClass()
    print("BFS:", bfs(problem))
    print("DFS:", dfs(problem))
    print("UCS:", ucs(problem))
    print("A*:", a_star(problem))
if __name__ == "__main__":
    main()