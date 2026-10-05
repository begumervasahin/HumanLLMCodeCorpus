from collections import deque
import heapq
import time
import resource
import sys
class Stack:
    def __init__(self):
        self.list = []
        self.state = set()
    def push(self, item):
        self.list.append(item)
        self.state.add(tuple(item.list))
    def pop(self):
        if not self.isEmpty():
            tos = self.list[-1]
            del self.list[-1]
            self.state.remove(tuple(tos.list))
            return tos
        else:
            return 0
    def isEmpty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0
    def clear_stack(self):
        self.list.clear()
        self.state.clear()
def write_output(path_to_goal, cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth, running_time, max_ram_usage):
    with open('output.txt', 'w') as f:
        f.write("path_to_goal: {}\n".format(path_to_goal))
        f.write("cost_of_path: {}\n".format(cost_of_path))
        f.write("nodes_expanded: {}\n".format(nodes_expanded))
        f.write("fringe_size: {}\n".format(fringe_size))
        f.write("max_fringe_size: {}\n".format(max_fringe_size))
        f.write("search_depth: {}\n".format(search_depth))
        f.write("max_search_depth: {}\n".format(max_search_depth))
        f.write("running_time: {}\n".format(running_time))
        f.write("max_ram_usage: {}\n".format(max_ram_usage))
def bfs(start_state):
    start_time = time.time()
    explored = set()
    fringe = deque([start_state])
    max_fringe_size = 0
    max_search_depth = 0
    while fringe:
        current_state = fringe.popleft()
        explored.add(tuple(current_state.list))
        if current_state.list == goal_state:
            running_time = time.time() - start_time
            path_to_goal, cost_of_path, nodes_expanded, fringe_size = [], 0, len(explored), len(fringe)
            search_depth = current_state.depth
            while current_state.parent:
                path_to_goal.insert(0, current_state.move)
                cost_of_path += 1
                current_state = current_state.parent
            write_output(path_to_goal, cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth, running_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.list) not in explored:
                fringe.append(neighbor)
                explored.add(tuple(neighbor.list))
                max_search_depth = max(max_search_depth, neighbor.depth)
        max_fringe_size = max(max_fringe_size, len(fringe))
def dfs(start_state):
    start_time = time.time()
    explored = set()
    fringe = Stack()
    fringe.push(start_state)
    max_fringe_size = 0
    max_search_depth = 0
    while not fringe.isEmpty():
        current_state = fringe.pop()
        explored.add(tuple(current_state.list))
        if current_state.list == goal_state:
            running_time = time.time() - start_time
            path_to_goal, cost_of_path, nodes_expanded, fringe_size = [], 0, len(explored), len(fringe.list)
            search_depth = current_state.depth
            while current_state.parent:
                path_to_goal.insert(0, current_state.move)
                cost_of_path += 1
                current_state = current_state.parent
            write_output(path_to_goal, cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth, running_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.list) not in explored:
                fringe.push(neighbor)
                explored.add(tuple(neighbor.list))
                max_search_depth = max(max_search_depth, neighbor.depth)
        max_fringe_size = max(max_fringe_size, len(fringe.list))
def dls(start_state, limit):
    start_time = time.time()
    explored = set()
    fringe = Stack()
    fringe.push(start_state)
    max_fringe_size = 0
    max_search_depth = 0
    while not fringe.isEmpty():
        current_state = fringe.pop()
        explored.add(tuple(current_state.list))
        if current_state.list == goal_state:
            running_time = time.time() - start_time
            path_to_goal, cost_of_path, nodes_expanded, fringe_size = [], 0, len(explored), len(fringe.list)
            search_depth = current_state.depth
            while current_state.parent:
                path_to_goal.insert(0, current_state.move)
                cost_of_path += 1
                current_state = current_state.parent
            write_output(path_to_goal, cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth, running_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        if current_state.depth < limit:
            for neighbor in current_state.get_neighbors():
                if tuple(neighbor.list) not in explored:
                    fringe.push(neighbor)
                    explored.add(tuple(neighbor.list))
                    max_search_depth = max(max_search_depth, neighbor.depth)
            max_fringe_size = max(max_fringe_size, len(fringe.list))
def ast(start_state):
    start_time = time.time()
    explored = set()
    fringe = []
    heapq.heappush(fringe, (0, start_state))
    max_fringe_size = 0
    max_search_depth = 0
    while fringe:
        current_priority, current_state = heapq.heappop(fringe)
        explored.add(tuple(current_state.list))
        if current_state.list == goal_state:
            running_time = time.time() - start_time
            path_to_goal, cost_of_path, nodes_expanded, fringe_size = [], 0, len(explored), len(fringe)
            search_depth = current_state.depth
            while current_state.parent:
                path_to_goal.insert(0, current_state.move)
                cost_of_path += 1
                current_state = current_state.parent
            write_output(path_to_goal, cost_of_path, nodes_expanded, fringe_size, max_fringe_size, search_depth, max_search_depth, running_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.list) not in explored:
                priority = neighbor.depth + neighbor.heuristic()
                heapq.heappush(fringe, (priority, neighbor))
                explored.add(tuple(neighbor.list))
                max_search_depth = max(max_search_depth, neighbor.depth)
        max_fringe_size = max(max_fringe_size, len(fringe))
class State:
    def __init__(self, state, parent, move, depth):
        self.list = state
        self.parent = parent
        self.move = move
        self.depth = depth
    def heuristic(self):
        return sum([1 if self.list[i] != goal_state[i] else 0 for i in range(len(self.list))])
    def get_neighbors(self):
        neighbors = []
        blank_index = self.list.index(0)
        row, col = divmod(blank_index, 3)
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                neighbor_list = self.list[:]
                new_blank_index = new_row * 3 + new_col
                neighbor_list[blank_index], neighbor_list[new_blank_index] = neighbor_list[new_blank_index], neighbor_list[blank_index]
                neighbors.append(State(neighbor_list, self, move, self.depth + 1))
        return neighbors
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def main():
    algorithm = sys.argv[1]
    start_state = State([int(i) for i in sys.argv[2].split(",")], None, None, 0)
    if algorithm == "bfs":
        bfs(start_state)
    elif algorithm == "dfs":
        dfs(start_state)
    elif algorithm == "dls":
        limit = int(sys.argv[3])
        dls(start_state, limit)
    elif algorithm == "ast":
        ast(start_state)
if __name__ == "__main__":
    main()