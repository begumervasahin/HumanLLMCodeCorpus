def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if state == goal:
            return path
        elif state not in visited:
            for branch in graph.get(state, []):
                new_path = list(path)
                new_path.append(branch)
                queue.append(new_path)
            visited.add(state)
    return "Path not found"
if __name__ == "__main__":
    graph = {
        'A': set(['B']),
        'B': set(['A', 'C']),
        'C': set(['B', 'D', 'H', 'I']),
        'D': set(['C', 'E', 'F', 'H', 'M']),
        'E': set(['D']),
        'F': set(['D', 'G', 'M']),
        'G': set(['F', 'H']),
        'H': set(['C', 'D', 'G', 'L']),
        'I': set(['C', 'J', 'K']),
        'J': set(['I']),
        'K': set(['I', 'L']),
        'L': set(['H', 'K']),
        'M': set(['D', 'F'])
    }
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    path = bfs(graph, start, goal)
    print("Path from {} to {}: {}".format(start, goal, path))
    print("\nLink to GitHub repository: https: