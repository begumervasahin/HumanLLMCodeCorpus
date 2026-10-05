class PuzzleSolver:
    def __init__(self, initial_arrangement):
        self.goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.current_state = State(initial_arrangement)
        self.initial_state = State(initial_arrangement)
        self.is_solved = False
    def build_path_actions(self, end_state):
        path = []
        state = end_state
        while state.parent:
            path.append(state.action)
            state = state.parent
        path.pop()
        path.reverse()
        path.append("")
        return path
    def build_path(self, end_state):
        path = []
        state = end_state
        while state.parent:
            path.append(state.arr)
            state = state.parent
        path.reverse()
        return path
    def solve(self):
        self.solve_dfs(self.current_state, [], 0)
    def solve_dfs(self, state, visited, count):
        if self.is_solved:
            return
        if state.arr == self.goal_state:
            path_actions = self.build_path_actions(state)
            path_states = self.build_path(state)
            print("The exact path and its move is:")
            for i in range(len(path_states)):
                print(str(path_states[i]) + '   ' + str(path_actions[i]))
            print("Depth = " + str(len(path_states)))
            print("It took " + str(count) + " states")
            self.is_solved = True
            return visited
        if state.arr not in visited:
            visited.append(state.arr)
            index_of_zero = state.arr.index(0)
            for move in ["Up", "Down", "Right", "Left"]:
                new_state = state.make_move(index_of_zero, move)
                if new_state is not None:
                    self.solve_dfs(new_state, visited, count + 1)
class State:
    def __init__(self, arrangement, parent=None, action=""):
        self.arr = arrangement
        self.parent = parent
        self.goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.action = action
        self.depth = 0
    def swap(self, zero_index, move_index, action):
        new_arrangement = self.arr[:]
        new_arrangement[zero_index], new_arrangement[move_index] = new_arrangement[move_index], new_arrangement[zero_index]
        return State(new_arrangement, self, action)
    def make_move(self, zero_index, direction):
        moves = {"Up": -3, "Down": 3, "Right": 1, "Left": -1}
        move_index = zero_index + moves[direction]
        if 0 <= move_index < len(self.arr):
            return self.swap(zero_index, move_index, direction)
        return None
print("DFS Medium")
solver = PuzzleSolver([2, 8, 1, 0, 4, 3, 7, 6, 5])
solver.solve()