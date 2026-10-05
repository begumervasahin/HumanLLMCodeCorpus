def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        if current_node == goal:
            return path
        elif current_node not in visited:
            neighbors = graph.get(current_node, [])
            for neighbor in neighbors:
                new_path = path + [neighbor]
                queue.append(new_path)
            visited.add(current_node)
    return None
start_node = 'A'
goal_node = 'F'
result = bfs(base, start_node, goal_node)
if result:
    print("Path found:", result)
else:
    print("Path not found")