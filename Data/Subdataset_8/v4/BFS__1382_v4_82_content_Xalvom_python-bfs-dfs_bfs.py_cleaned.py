
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
print("*********BFS***********")
start_node = input("Input Start Node: ")
end_node = input("Input Target Node: ")
print("***********************")
print()
def bfs(graph, start, target):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        if current_node == target:
            return path
        if current_node not in visited:
            for neighbor in graph.get(current_node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(current_node)
    return "Path not found"
print(bfs(graph, start_node, end_node))
print()
print("GitHub Repository: https: