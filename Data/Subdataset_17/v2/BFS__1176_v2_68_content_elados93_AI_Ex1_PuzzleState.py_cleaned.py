import heapq
import itertools
class State:
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            self._board = board
            self._move = move
            self.came_from = came_from
        else:
            self._board = state.board
            self._move = state.move
            self.came_from = state.came_from
    def __copy__(self):
        import copy
        copy_board = copy.copy(self._board)
        return State(board=copy_board, move=self._move, came_from=self.came_from)
    def __hash__(self):
        return hash(self._board)
    @property
    def board(self):
        return self._board
    @property
    def move(self):
        return self._move
    def __eq__(self, other):
        return self._board == other.board
class HeuristicState(State):
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            State.__init__(self, board, move, came_from)
        else:
            State.__init__(self, state=state)
        self.h_cost = 0
        self.g_cost = 0
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    @property
    def f_cost(self):
        return self.h_cost + self.g_cost
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    algorithm = int(lines[0].strip())
    size = int(lines[1].strip())
    initial_state = list(map(int, lines[2].strip().split('-')))
    return algorithm, size, initial_state
def goal_state(size):
    return list(range(1, size * size)) + [0]
def manhattan_distance(state, size):
    distance = 0
    for idx, value in enumerate(state):
        if value == 0:
            continue
        target_row, target_col = divmod(value - 1, size)
        current_row, current_col = divmod(idx, size)
        distance += abs(target_row - current_row) + abs(target_col - current_col)
    return distance
def get_neighbors(state, size):
    zero_index = state.index(0)
    row, col = divmod(zero_index, size)
    neighbors = []
    if row > 0:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index - size] = new_state[zero_index - size], new_state[zero_index]
        neighbors.append(('U', new_state))
    if row < size - 1:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index + size] = new_state[zero_index + size], new_state[zero_index]
        neighbors.append(('D', new_state))
    if col > 0:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        neighbors.append(('L', new_state))
    if col < size - 1:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
        neighbors.append(('R', new_state))
    return neighbors
def bfs(initial_state, size):
    root = State(initial_state, None, None)
    if root.board == goal_state(size):
        return root
    frontier = [root]
    explored = set()
    while frontier:
        state = frontier.pop(0)
        explored.add(tuple(state.board))
        for move, neighbor in get_neighbors(state.board, size):
            child = State(neighbor, move, state)
            if tuple(child.board) not in explored and child not in frontier:
                if child.board == goal_state(size):
                    return child
                frontier.append(child)
    return None
def astar(initial_state, size):
    root = HeuristicState(initial_state, None, None)
    root.h_cost = manhattan_distance(initial_state, size)
    frontier = []
    heapq.heappush(frontier, root)
    explored = set()
    while frontier:
        state = heapq.heappop(frontier)
        if state.board == goal_state(size):
            return state
        explored.add(tuple(state.board))
        for move, neighbor in get_neighbors(state.board, size):
            g = state.g_cost + 1
            h = manhattan_distance(neighbor, size)
            child = HeuristicState(neighbor, move, state)
            child.g_cost = g
            child.h_cost = h
            if tuple(child.board) not in explored:
                heapq.heappush(frontier, child)
    return None
def ids(initial_state, size):
    def dls(state, limit):
        if state.board == goal_state(size):
            return state
        elif limit == 0:
            return None
        else:
            for move, neighbor in get_neighbors(state.board, size):
                child = State(neighbor, move, state)
                result = dls(child, limit - 1)
                if result is not None:
                    return result
            return None
    depth = 0
    root = State(initial_state, None, None)
    while True:
        result = dls(root, depth)
        if result is not None:
            return result
        depth += 1
def print_solution(solution):
    moves = []
    while solution.came_from is not None:
        moves.append(solution.move)
        solution = solution.came_from
    moves.reverse()
    print("Solution:", ''.join(moves))
    print("Number of moves:", len(moves))
if __name__ == "__main__":
    algorithm, size, initial_state = read_input("input.txt")
    solution = None
    if algorithm == 1:
        solution = ids(initial_state, size)
    elif algorithm == 2:
        solution = bfs(initial_state, size)
    elif algorithm == 3:
        solution = astar(initial_state, size)
    if solution is not None:
        print_solution(solution)
    else:
        print("No solution found.")