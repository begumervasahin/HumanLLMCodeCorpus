def bfs(graph, start):
    queue = [[start]]
    visited = set()
    targets = {'RS1', 'RS2', 'RS3'}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in targets:
            return path
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None
def dfs(graph, start):
    stack = [[start]]
    visited = set()
    targets = {'RS1', 'RS2', 'RS3'}
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in targets:
            return path
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(node)
    return None
if __name__ == "__main__":
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
    start_node = input("Enter the starting node: ")
    bfs_path = bfs(map, start_node)
    dfs_path = dfs(map, start_node)
    print("BFS Path:", bfs_path)
    print("DFS Path:", dfs_path)