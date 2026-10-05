class Puzzle:
    def __init__(self, arr):
        self.goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.state = State(arr)
        self.initial = State(arr)
        self.is_done = False
    def build_path_actions(self, end):
        path = []
        state = end
        while state.parent:
            path.append(state.action)
            state = state.parent
        path.pop()
        path = path[::-1]
        path.append("")
        return path
    def build_path(self, end):
        path = []
        state = end
        while state.parent:
            path.append(state.arr)
            state = state.parent
        return path[::-1]
    def solve(self):
        self.solve_dfs(self.state, [], 0)
    def solve_dfs(self, state, visited, count):
        if self.is_done:
            return
        if state.arr == self.goal:
            path_actions = self.build_path_actions(state)
            path_states = self.build_path(state)
            print("The exact path and its move is:")
            for i in range(len(path_states)):
                print(str(path_states[i]) + '   ' + str(path_actions[i]))
            print("Depth = " + str(len(path_states)))
            print ("It took " + str(count) + " states")
            self.is_done = True
            return visited
        if state.arr not in visited:
            visited.append(state.arr)
            index_of_0 = state.arr.index(0)
            up = state.move_up(index_of_0)
            if up is not None:
                self.solve_dfs(up, visited, count + 1)
            left = state.move_left(index_of_0)
            if left is not None:
                self.solve_dfs(left, visited, count + 1)
            right = state.move_right(index_of_0)
            if right is not None:
                self.solve_dfs(right, visited, count + 1)
            down = state.move_down(index_of_0)
            if down is not None:
                self.solve_dfs(down, visited, count + 1)
class State:
    def __init__(self, arr, parent=None, action=""):
        self.arr = arr
        self.parent = parent
        self.goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.weight = 0
        self.action = action
        self.depth = 0
    def swap(self, index_of_0, arr, i, action):
        if index_of_0 in arr:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + i] = new_state[index_of_0 + i], new_state[index_of_0]
            return State(new_state, self, action)
        return None
    def move_up(self, index_of_0):
        return self.swap(index_of_0, [3, 4, 5, 6, 7, 8], -3, "U")
    def move_down(self, index_of_0):
        return self.swap(index_of_0, [0, 1, 2, 3, 4, 5], 3, "D")
    def move_right(self, index_of_0):
        return self.swap(index_of_0, [0, 1, 3, 4, 6, 7], 1, "R")
    def move_left(self, index_of_0):
        return self.swap(index_of_0, [1, 2, 4, 5, 7, 8], -1, "L")
print("DFS Medium")
my_puzzle = Puzzle([2, 8, 1, 0, 4, 3, 7, 6, 5])
my_puzzle.solve()