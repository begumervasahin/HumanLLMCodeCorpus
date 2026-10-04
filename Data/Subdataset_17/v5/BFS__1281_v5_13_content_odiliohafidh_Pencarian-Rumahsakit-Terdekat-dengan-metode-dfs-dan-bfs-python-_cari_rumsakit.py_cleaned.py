
graph = {
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
    goals = {'RS1', 'RS2', 'RS3'}
    visited = set()
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        if current_node in goals:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                new_path = path + [neighbor]
                queue.append(new_path)
    print("No path found")
    return None
def dfs(graph, start):
    stack = [[start]]
    goals = {'RS1', 'RS2', 'RS3'}
    visited = set()
    while stack:
        path = stack.pop()
        current_node = path[-1]
        if current_node in goals:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                new_path = path + [neighbor]
                stack.append(new_path)
    print("No path found")
    return None
if __name__ == "__main__":
    start_node = 'A'
    print("BFS path to nearest hospital:", bfs(graph, start_node))
    print("DFS path to nearest hospital:", dfs(graph, start_node))