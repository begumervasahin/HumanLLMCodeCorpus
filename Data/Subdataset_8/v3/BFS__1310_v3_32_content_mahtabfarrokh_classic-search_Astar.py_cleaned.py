class AStar:
    def __init__(self, initial_state, actions, result, goal_test, get_cost, heuristic):
        self.open_list = []
        self.closed_list = []
        self.result_list = []
        self.visited_nodes = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.get_cost = get_cost
        self.heuristic = heuristic
        self.max_memory = 0
    def search(self):
        while self.open_list:
            self.max_memory = max(self.max_memory, len(self.open_list) + len(self.closed_list))
            current_node = self.open_list[0]
            min_f_value = current_node[1]
            path = current_node[0]
            actions_taken = current_node[2]
            heuristic_value = current_node[3]
            for node in self.open_list:
                if node[1] + node[3] < min_f_value + heuristic_value:
                    min_f_value = node[1]
                    path = node[0]
                    actions_taken = node[2]
                    heuristic_value = node[3]
            last_node = path[-1]
            for node in self.open_list:
                node_path = node[0]
                if node_path[-1] == last_node and node[1] + node[3] > min_f_value + heuristic_value:
                    self.open_list.remove(node)
            if self.goal_test(last_node):
                return [actions_taken, path, min_f_value, heuristic_value]
            self.open_list.remove([path, min_f_value, actions_taken, heuristic_value])
            if last_node not in self.closed_list:
                self.closed_list.append(last_node)
            for action in self.actions(last_node):
                new_node = self.result(last_node, action)
                if new_node not in self.closed_list:
                    cost = self.get_cost(path[0], new_node) + min_f_value
                    heuristic_value = self.heuristic(new_node)
                    new_path = path + [new_node]
                    new_actions_taken = actions_taken + [action]
                    self.open_list.append([new_path, cost, new_actions_taken, heuristic_value])
                    if new_node not in self.visited_nodes:
                        self.visited_nodes.append(new_node)
    def search_astar(self):
        start_state = self.initial_state()
        self.open_list = [[[start_state], 0, [], 0]]
        self.closed_list = []
        self.result_list = []
        result = self.search()
        if not result:
            print("There is no path")
        else:
            print("Path found:")
            print(result[0])
            print("Number of visited nodes:", len(self.visited_nodes))
            print("Number of nodes in closed list:", len(self.closed_list))
            print("Max memory usage:", self.max_memory)
            print("Path cost:", result[2] + result[3])
