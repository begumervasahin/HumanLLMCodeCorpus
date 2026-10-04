class DGraph:
    def __init__(self, matrix, goal_indices, start_state=0):
        self.matrix = matrix
        self.goal_indices = goal_indices
        self.start_state = start_state
    def get_start_state(self):
        return self.start_state
    def is_goal_state(self, state):
        return state in self.goal_indices
    def get_successors(self, state):
        row = self.matrix[state]
        successors = {}
        index = 0
        for cost in row:
            if cost is not None:
                successors[index] = cost
            index += 1
        return successors
def bfs(graph):
    from collections import deque
    start_state = graph.get_start_state()
    frontier = deque([start_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if graph.is_goal_state(state):
            return state
        explored.add(state)
        for successor in graph.get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
    return None
def dfs(graph):
    start_state = graph.get_start_state()
    frontier = [start_state]
    explored = set()
    while frontier:
        state = frontier.pop()
        if graph.is_goal_state(state):
            return state
        explored.add(state)
        for successor in graph.get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
    return None
def ids(graph):
    def dls(state, depth):
        if depth == 0 and graph.is_goal_state(state):
            return state
        if depth > 0:
            for successor in graph.get_successors(state):
                result = dls(successor, depth - 1)
                if result is not None:
                    return result
        return None
    depth = 0
    while True:
        result = dls(graph.get_start_state(), depth)
        if result is not None:
            return result
        depth += 1
def astar(graph, heuristic):
    from heapq import heappop, heappush
    start_state = graph.get_start_state()
    frontier = [(0, start_state)]
    explored = set()
    while frontier:
        cost, state = heappop(frontier)
        if graph.is_goal_state(state):
            return state
        explored.add(state)
        for successor, step_cost in graph.get_successors(state).items():
            if successor not in explored:
                total_cost = cost + step_cost + heuristic(successor)
                heappush(frontier, (total_cost, successor))
    return None
def heuristic(state):
    return 0
if __name__ == "__main__":
    matrix = [
        [None, 1, None, None, None],
        [None, None, 1, None, None],
        [None, None, None, 1, None],
        [None, None, None, None, 1],
        [None, None, None, None, None],
    ]
    goal_indices = {4}
    graph = DGraph(matrix, goal_indices)
    bfs_result = bfs(graph)
    print("BFS Result:", bfs_result)
    dfs_result = dfs(graph)
    print("DFS Result:", dfs_result)
    ids_result = ids(graph)
    print("IDS Result:", ids_result)
    astar_result = astar(graph, heuristic)
    print("A* Result:", astar_result)