import queue
class Node:
    def __init__(self, state, parent=None, actions='Move to', path_cost=0):
        self.state = state
        self.path_cost = path_cost
        self.actions = actions
        self.parent = parent
city_list = []
adj_list = {}
problem = None
current_search_option = 1
class Problem:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def goal_test(self, node_state):
        return self.destination == node_state
    def expand_nodes(self, action, state):
        return adj_list[state]
def get_graph_node(state):
    for node in city_list:
        if node.state == state:
            return node
    return None
def read_graph():
    try:
        with open('input_data.txt', 'r') as file_obj:
            input_data = file_obj.read().split('\n')
            for data in input_data:
                data = data.split(',')
                if len(data) < 2:
                    break
                node1 = get_graph_node(data[0]) or Node(data[0])
                city_list.append(node1)
                node2 = get_graph_node(data[1]) or Node(data[1], data[0], data[2])
                city_list.append(node2)
                adj_list.setdefault(node1.state, []).append(node2)
                adj_list.setdefault(node2.state, []).append(node1)
    except Exception as e:
        print(e)
def pop(frontier):
    return frontier.get()
def get_solution(s_list):
    solution = []
    key = problem.destination
    solution.append(key)
    while key in s_list:
        key = s_list[key]
        solution.append(key)
    solution.reverse()
    return solution
def check_queue(frontier, node_state):
    result = False
    new_frontier = queue.Queue() if current_search_option == 1 else queue.LifoQueue()
    while not frontier.empty():
        n1 = frontier.get()
        if n1 == node_state:
            result = True
        new_frontier.put(n1)
    return new_frontier, result
def print_solution(solution):
    for node_state in solution:
        node = get_graph_node(node_state)
        if node:
            print(f"{node.state} {node.path_cost} {node.actions}")
def graph_search():
    solution = {}
    node = get_graph_node(problem.source)
    if problem.goal_test(node.state):
        return node.state
    frontier = initialize_frontier(node.state)
    explored = []
    while not frontier.empty():
        node = pop(frontier)
        explored.append(node.state)
        child_nodes = problem.expand_nodes(node.actions, node.state)
        for child in child_nodes:
            frontier, result = check_queue(frontier, child.state)
            if child.state not in explored and not result:
                if problem.goal_test(child.state):
                    solution[child.state] = node.state
                    return get_solution(solution)
                frontier = update_frontier(frontier, child.state)
                solution[child.state] = node.state
def initialize_frontier(node_name):
    return queue.Queue() if current_search_option == 1 else queue.LifoQueue()
def update_frontier(frontier, node_state):
    frontier.put(node_state)
    return frontier
if __name__ == "__main__":
    read_graph()
    source = input("Enter the Source Node: ")
    destination = input("Enter the Destination Node: ")
    current_search_option = int(input("Enter 1 for BFS or 2 for DFS: "))
    problem = Problem(source, destination)
    solution = graph_search()
    print_solution(solution)