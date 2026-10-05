
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
print("********* BFS ***********")
start_node = input("Enter Start Node: ")
end_node = input("Enter Target Node: ")
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
                new_path = path + [neighbor]
                queue.append(new_path)
            visited.add(current_node)
    return "Path not found"
print(bfs(graph, start_node, end_node))
print()
print("GitHub Repository: https: