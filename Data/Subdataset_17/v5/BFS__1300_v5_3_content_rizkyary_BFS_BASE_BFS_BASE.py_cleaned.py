def bfs(graph, start, goal):
    queue = collections.deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state == goal:
            return path
        if state not in visited:
            for neighbor in graph.get(state, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(state)
    return None
def main():
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
    path = bfs(graph, start_node, goal_node)
    if path:
        print("Path found:", path)
    else:
        print("No path found")
if __name__ == "__main__":
    main()