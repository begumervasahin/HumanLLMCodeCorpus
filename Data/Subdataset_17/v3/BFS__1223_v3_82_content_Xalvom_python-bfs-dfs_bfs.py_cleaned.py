
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
    """
    Perform Breadth-First Search (BFS) to find the shortest path from start to goal.
    :param graph: The graph represented as an adjacency list.
    :param start: The starting node for the BFS.
    :param goal: The goal node to reach.
    :return: A list representing the path from start to goal if found, otherwise "Path not found".
    """
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
    start_node = input("Enter starting node: ").strip().upper()
    goal_node = input("Enter goal node: ").strip().upper()
    print("*************************")
    print()
    result = bfs(graph, start_node, goal_node)
    print(result)