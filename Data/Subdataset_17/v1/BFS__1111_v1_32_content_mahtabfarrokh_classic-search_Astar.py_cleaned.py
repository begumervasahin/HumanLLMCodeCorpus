class AStar:
    def __init__(self, initial_state, actions, result, goal_test, get_cost, heuristic):
        self.f = []
        self.e = []
        self.visited = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.get_cost = get_cost
        self.heuristic = heuristic
        self.max_memory = 0
    def search(self):
        while self.f:
            self.max_memory = max(self.max_memory, len(self.f) + len(self.e))
            current_node = min(self.f, key=lambda x: x[1] + x[3])
            path, cost, udru, heur = current_node
            if self.goal_test(path[-1]):
                return [udru, path, cost, heur]
            self.f.remove(current_node)
            self.e.append(path[-1])
            for act in self.actions(path[-1]):
                v = self.result(path[-1], act)
                if v not in self.e:
                    new_cost = self.get_cost(path[0], v) + cost
                    heur = self.heuristic(v)
                    new_path = path + [v]
                    new_udru = udru + [act]
                    self.f.append([new_path, new_cost, new_udru, heur])
                    if v not in self.visited:
                        self.visited.append(v)
    def search_astar(self):
        start = self.initial_state()
        self.f = [[[start], 0, [], 0]]
        p = self.search()
        if not p:
            print("No path found.")
        else:
            print("Path found:")
            print("Actions:", p[0])
            print("Number of visited nodes:", len(self.visited))
            print("Number of nodes in closed list:", len(self.e))
            print("Max memory used:", self.max_memory)
            print("Total path cost:", p[2] + p[3])
def initial_state():
    return (1, 2, 3, 4, 5, 6, 7, 8, 0)
def actions(state):
    zero_index = state.index(0)
    possible_actions = []
    if zero_index % 3 > 0:
        possible_actions.append('Left')
    if zero_index % 3 < 2:
        possible_actions.append('Right')
    if zero_index > 2:
        possible_actions.append('Up')
    if zero_index < 6:
        possible_actions.append('Down')
    return possible_actions
def result(state, action):
    zero_index = state.index(0)
    new_state = list(state)
    if action == 'Left':
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
    elif action == 'Right':
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
    elif action == 'Up':
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
    elif action == 'Down':
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
    return tuple(new_state)
def goal_test(state):
    return state == (0, 1, 2, 3, 4, 5, 6, 7, 8)
def get_cost(state1, state2):
    return 1
def heuristic(state):
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    return sum(abs(s % 3 - g % 3) + abs(s
if __name__ == "__main__":
    astar_solver = AStar(initial_state, actions, result, goal_test, get_cost, heuristic)
    astar_solver.search_astar()