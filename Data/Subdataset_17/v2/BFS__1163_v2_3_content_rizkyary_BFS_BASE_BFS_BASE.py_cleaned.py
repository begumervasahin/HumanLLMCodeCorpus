
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'H', 'J'},
    'C': {'A', 'D', 'G'},
    'D': {'C', 'E'},
    'E': {'D', 'F'},
    'F': {'E', 'G', 'K', 'L'},
    'G': {'C', 'F'},
    'H': {'B', 'I'},
    'I': {'H', 'J', 'K'},
    'J': {'B', 'I'},
    'K': {'F', 'I', 'L'},
    'L': {'F', 'K'}
}
def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    print("No path found")
    return None
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'L'
    path = bfs(graph, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")