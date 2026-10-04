
city_map = {
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
                new_path = path + [neighbor]
                queue.append(new_path)
            visited.add(state)
    print("Hospital not found")
    return None
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
                new_path = path + [neighbor]
                stack.append(new_path)
            visited.add(state)
    print("Hospital not found")
    return None
if __name__ == "__main__":
    start = input("Enter the starting position: ").strip()
    print("BFS searching for the nearest hospital from:", start)
    bfs_result = bfs(city_map, start)
    if bfs_result:
        print("BFS Path:", " -> ".join(bfs_result))
    print("\nDFS searching for the nearest hospital from:", start)
    dfs_result = dfs(city_map, start)
    if dfs_result:
        print("DFS Path:", " -> ".join(dfs_result))