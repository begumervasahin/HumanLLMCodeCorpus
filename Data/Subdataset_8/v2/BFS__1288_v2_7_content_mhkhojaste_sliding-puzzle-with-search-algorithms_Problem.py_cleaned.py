from copy import deepcopy
from math import sqrt
from queue import Queue
from heapq import heappush, heappop
class ProblemClass:
    def __init__(self):
        self.initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def get_init_state(self):
        return self.initial_state
    def get_moves(self, state):
        moves = []
        zero_index = self.find_zero(state)
        i, j = zero_index
        if i > 0:
            moves.append('U')
        if i < 2:
            moves.append('D')
        if j > 0:
            moves.append('L')
        if j < 2:
            moves.append('R')
        return moves
    def do_move(self, state, direction):
        new_state = deepcopy(state)
        zero_index = self.find_zero(new_state)
        i, j = zero_index
        if direction == 'R':
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], 0
        elif direction == 'L':
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], 0
        elif direction == 'U':
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], 0
        elif direction == 'D':
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], 0
        return new_state
    def check_goal(self, state):
        return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def find_h(self, state):
        h = 0
        for i in range(3):
            for j in range(3):
                number = (i * 3 + j + 1) % 9
                number_index = self.find_number(state, number)
                h += sqrt((i - number_index[0]) ** 2 + (j - number_index[1]) ** 2)
        return round(h, 2)
    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    def find_number(self, state, number):
        for i in range(3):
            for j in range(3):
                if state[i][j] == number:
                    return i, j
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