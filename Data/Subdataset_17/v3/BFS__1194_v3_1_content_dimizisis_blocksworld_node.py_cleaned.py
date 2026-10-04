import configparser
import heapq
import sys
import time
class Node:
    def __init__(self, parent=None, world_state=None, priority=0):
        self.parent = parent
        self.world_state = world_state
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __eq__(self, other):
        return self.world_state == other.world_state
    def __hash__(self):
        return hash(str(self.world_state))
def read_input_file(input_file):
    config = configparser.ConfigParser()
    config.read(input_file)
    start_state = {}
    goal_state = {}
    for key, value in config['START'].items():
        if key == 'size':
            size = tuple(map(int, value.split(',')))
        else:
            start_state[key] = tuple(map(int, value.split(',')))
    for key, value in config['GOAL'].items():
        goal_state[key] = tuple(map(int, value.split(',')))
    return size, start_state, goal_state
def write_output_file(output_file, path, nodes_expanded, execution_time):
    with open(output_file, 'w') as f:
        for state in path:
            for block, position in state.items():
                f.write(f"{block} {position}\n")
            f.write("----------\n")
        f.write(f"Nodes expanded: {nodes_expanded}\n")
        f.write(f"--- Execution time (seconds): {execution_time:.4f} ---\n")
def heuristic(state, goal_state):
    return sum(abs(state[block][0] - goal_state[block][0]) + abs(state[block][1] - goal_state[block][1]) for block in state)
def generate_successors(current_node, size):
    successors = []
    return successors
def astar(start_state, goal_state, size):
    open_list = []
    closed_set = set()
    start_node = Node(None, start_state, 0)
    heapq.heappush(open_list, (0, start_node))
    nodes_expanded = 0
    while open_list:
        current_priority, current_node = heapq.heappop(open_list)
        nodes_expanded += 1
        if current_node.world_state == goal_state:
            path = []
            while current_node:
                path.append(current_node.world_state)
                current_node = current_node.parent
            return path[::-1], nodes_expanded
        closed_set.add(current_node)
        successors = generate_successors(current_node, size)
        for successor_state in successors:
            successor_node = Node(current_node, successor_state, heuristic(successor_state, goal_state))
            if successor_node in closed_set:
                continue
            heapq.heappush(open_list, (successor_node.priority, successor_node))
    return None, nodes_expanded
def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <search_method> <input_file> <output_file>")
        return
    search_method = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    size, start_state, goal_state = read_input_file(input_file)
    start_time = time.time()
    if search_method == 'astar':
        path, nodes_expanded = astar(start_state, goal_state, size)
    elif search_method == 'best':
        path, nodes_expanded = best_first_search(start_state, goal_state, size)
    else:
        print(f"Unknown search method: {search_method}")
        return
    end_time = time.time()
    execution_time = end_time - start_time
    if path:
        write_output_file(output_file, path, nodes_expanded, execution_time)
    else:
        print("No solution found")
if __name__ == "__main__":
    main()