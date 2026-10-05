def bfs(graph, start):
    queue = [[start]]
    targets = {'RS1', 'RS2', 'RS3'}
    visited = set()
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if state in targets:
            return path
        if state not in visited:
            for neighbor in graph.get(state, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(state)
        if len(queue) == 0:
            print("Tidak ditemukan")
def dfs(graph, start):
    stack = [[start]]
    targets = {'RS1', 'RS2', 'RS3'}
    visited = set()
    while stack:
        path = stack.pop()
        state = path[-1]
        if state in targets:
            return path
        if state not in visited:
            for neighbor in graph.get(state, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(state)
        if len(stack) == 0:
            print("Tidak ditemukan")
map = {
    'A': {'RS1', 'C', 'E'},
    'B': {'E', 'D'},
    'C': {'A', 'B', 'RS2'},
    'D': {'B', 'F', 'K', 'RS3'},
    'E': {'A', 'B'},
    'F': {'D', 'G'},
    'G': {'H', 'F', 'I'},
    'H': {'G'},
    'I': {'G', 'J'},
    'J': {'I'},
    'K': {'D', 'L', 'M'},
    'L': {'RS2', 'K'},
    'M': {'K'},
    'RS1': {'A'},
    'RS2': {'C', 'L'},
    'RS3': {'D'}
}
if __name__ == "__main__":
    start_node = 'A'
    print("BFS Result:", bfs(map, start_node))
    print("DFS Result:", dfs(map, start_node))