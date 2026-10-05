def breadth_first_search(graph, start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        if current_node == goal:
            return path
        if current_node not in visited:
            for neighbor in graph.get(current_node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(current_node)
    print("Path not found")
    return None
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
start_node = 'A'
goal_node = 'L'
result = breadth_first_search(graph, start_node, goal_node)
if result:
    print("Path found:", result)
else:
    print("Path not found")