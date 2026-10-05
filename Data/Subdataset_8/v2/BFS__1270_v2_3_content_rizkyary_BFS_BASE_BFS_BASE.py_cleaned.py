def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if state == goal:
            return path
        elif state not in visited:
            for neighbor in graph.get(state, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(state)
    print("Path not found")
start_node = 'A'
goal_node = 'F'
result = bfs(base, start_node, goal_node)
print(result)