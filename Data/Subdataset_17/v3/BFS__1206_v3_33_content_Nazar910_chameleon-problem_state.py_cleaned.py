from collections import deque, defaultdict
import heapq
class State:
    def __init__(self, red, green, blue, parent=None):
        self.red_count = red
        self.green_count = green
        self.blue_count = blue
        self.parent = parent
    def has_only_one_color(self):
        return (self.red_count == 0 and self.green_count == 0) or \
               (self.red_count == 0 and self.blue_count == 0) or \
               (self.green_count == 0 and self.blue_count == 0)
    def red_meets_green(self):
        if self.red_count < 1 or self.green_count < 1:
            return None
        return State(self.red_count - 1, self.green_count - 1, self.blue_count + 2, self)
    def green_meets_blue(self):
        if self.green_count < 1 or self.blue_count < 1:
            return None
        return State(self.red_count + 2, self.green_count - 1, self.blue_count - 1, self)
    def blue_meets_red(self):
        if self.blue_count < 1 or self.red_count < 1:
            return None
        return State(self.red_count - 1, self.green_count + 2, self.blue_count - 1, self)
    def get_neighbors(self):
        neighbors = []
        if (new_state := self.red_meets_green()) is not None:
            neighbors.append(new_state)
        if (new_state := self.green_meets_blue()) is not None:
            neighbors.append(new_state)
        if (new_state := self.blue_meets_red()) is not None:
            neighbors.append(new_state)
        return neighbors
    def get_path(self):
        path = deque([self])
        parent = self.parent
        while parent:
            path.appendleft(parent)
            parent = parent.parent
        return path
    def __str__(self):
        return f"(red={self.red_count}, green={self.green_count}, blue={self.blue_count})"
    def __eq__(self, other):
        return self.red_count == other.red_count and \
               self.green_count == other.green_count and \
               self.blue_count == other.blue_count
    def __hash__(self):
        return hash((self.red_count, self.green_count, self.blue_count))
def bfs(initial_state):
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if state in explored:
            continue
        explored.add(state)
        if state.has_only_one_color():
            return state.get_path()
        for neighbor in state.get_neighbors():
            if neighbor not in explored:
                frontier.append(neighbor)
    return None
def dfs(initial_state):
    frontier = [initial_state]
    explored = set()
    while frontier:
        state = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        if state.has_only_one_color():
            return state.get_path()
        for neighbor in state.get_neighbors():
            if neighbor not in explored:
                frontier.append(neighbor)
    return None
def a_star(initial_state):
    frontier = []
    heapq.heappush(frontier, (0, initial_state))
    explored = set()
    cost_so_far = defaultdict(lambda: float('inf'))
    cost_so_far[initial_state] = 0
    while frontier:
        _, state = heapq.heappop(frontier)
        if state in explored:
            continue
        explored.add(state)
        if state.has_only_one_color():
            return state.get_path()
        for neighbor in state.get_neighbors():
            new_cost = cost_so_far[state] + 1
            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(frontier, (priority, neighbor))
    return None
def heuristic(state):
    return min(state.red_count, state.green_count, state.blue_count)
def print_path(path):
    for state in path:
        print(state)
def main():
    initial_state = State(red=13, green=16, blue=17)
    print("Solving with BFS...")
    bfs_path = bfs(initial_state)
    if bfs_path:
        print_path(bfs_path)
    else:
        print("No solution found with BFS.")
    print("\nSolving with DFS...")
    dfs_path = dfs(initial_state)
    if dfs_path:
        print_path(dfs_path)
    else:
        print("No solution found with DFS.")
    print("\nSolving with A*...")
    a_star_path = a_star(initial_state)
    if a_star_path:
        print_path(a_star_path)
    else:
        print("No solution found with A*.")
if __name__ == "__main__":
    main()