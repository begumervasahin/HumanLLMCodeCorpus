class AStar:
    def __init__(self, initial_state, actions, result, goal_test, get_cost, heuristic):
        self.frontier = []
        self.explored = []
        self.visited = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.get_cost = get_cost
        self.heuristic = heuristic
        self.max_memory = 0
    def search(self):
        while self.frontier:
            self.max_memory = max(self.max_memory, len(self.frontier) + len(self.explored))
            current_node = min(self.frontier, key=lambda x: x[1] + x[3])
            self.frontier.remove(current_node)
            path, g_cost, actions, h_cost = current_node
            node = path[-1]
            if self.goal_test(node):
                return actions, path, g_cost, h_cost
            if node not in self.explored:
                self.explored.append(node)
                for action in self.actions(node):
                    child = self.result(node, action)
                    if child not in self.explored:
                        new_g_cost = g_cost + self.get_cost(node, child)
                        new_h_cost = self.heuristic(child)
                        new_path = path + [child]
                        new_actions = actions + [action]
                        self.frontier.append([new_path, new_g_cost, new_actions, new_h_cost])
                        if child not in self.visited:
                            self.visited.append(child)
        return None
    def search_astar(self):
        start_node = self.initial_state()
        self.frontier = [[[start_node], 0, [], 0]]
        self.explored = []
        self.visited = []
        result = self.search()
        if not result:
            print("There is no path.")
        else:
            actions, path, g_cost, h_cost = result
            print("Path found:")
            print("Actions:", actions)
            print("Number of visited nodes:", len(self.visited))
            print("Number of nodes in the closed list:", len(self.explored))
            print("Maximum memory used:", self.max_memory)
            print("Path cost:", g_cost + h_cost)
if __name__ == "__main__":
    def initial_state():
        pass
    def actions(state):
        pass
    def result(state, action):
        pass
    def goal_test(state):
        pass
    def get_cost(state1, state2):
        pass
    def heuristic(state):
        pass
    astar_solver = AStar(initial_state, actions, result, goal_test, get_cost, heuristic)
    astar_solver.search_astar()