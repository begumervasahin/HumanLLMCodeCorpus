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
    print("Tidak ditemukan")
    return None
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
print("********* BFS ***********")
start = input("Input Awal: ")
goal = input("Input Tujuan: ")
print("**************************")
print()
result = bfs(graph, start, goal)
if result:
    print("Jalur BFS:", result)
else:
    print("Tidak ditemukan")
print()
print("Link Github: https: