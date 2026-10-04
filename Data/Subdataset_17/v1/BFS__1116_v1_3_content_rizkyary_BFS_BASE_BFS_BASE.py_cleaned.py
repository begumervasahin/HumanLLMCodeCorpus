
base = {
    'A': set(['B', 'C']),
    'B': set(['A', 'H', 'J']),
    'C': set(['A', 'D', 'G']),
    'D': set(['C', 'E']),
    'E': set(['D', 'F']),
    'F': set(['E', 'G', 'K', 'L']),
    'G': set(['C', 'F']),
    'H': set(['B', 'I']),
    'I': set(['H', 'J', 'K']),
    'J': set(['B', 'I']),
    'K': set(['F', 'I', 'L']),
    'L': set(['F', 'K'])
}
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
    print("Tidak ditemukan")
    return None
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'L'
    path = bfs(base, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")