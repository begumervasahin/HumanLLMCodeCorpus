from collections import deque
def breadth_first_search(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state == goal:
            return path
        elif state not in visited:
            for neighbor in graph.get(state, []):
                new_path = path + [neighbor]
                queue.append(new_path)
            visited.add(state)
    print("Tidak ditemukan")
    return None
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
start = input("Input Awal: ")
goal = input("Input Tujuan: ")
print("**************************")
print()
result = breadth_first_search(graph, start, goal)
if result:
    print("Jalur BFS:", result)
else:
    print("Tidak ditemukan")
print()
print("Link Github: https: