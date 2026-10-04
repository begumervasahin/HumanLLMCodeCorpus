
graph = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'H', 'I'},
    'D': {'C', 'E', 'F', 'H', 'M'},
    'E': {'D'},
    'F': {'D', 'G', 'M'},
    'G': {'F', 'H'},
    'H': {'C', 'D', 'G', 'L'},
    'I': {'C', 'J', 'K'},
    'J': {'I'},
    'K': {'I', 'L'},
    'L': {'H', 'K'},
    'M': {'D', 'F'}
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
    return "Path not found"
if __name__ == "__main__":
    print("********* BFS ***********")
    start_node = input("Enter starting node: ")
    goal_node = input("Enter goal node: ")
    print("*************************")
    print()
    result = bfs(graph, start_node, goal_node)
    print(result)