
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
}
unvisited_nodes = {node: None for node in nodes}
visited_nodes = {}
current_node = 'B'
current_distance = 0
unvisited_nodes[current_node] = current_distance
while True:
    for neighbor, distance in distances[current_node].items():
        if neighbor not in unvisited_nodes:
            continue
        new_distance = current_distance + distance
        if unvisited_nodes[neighbor] is None or unvisited_nodes[neighbor] > new_distance:
            unvisited_nodes[neighbor] = new_distance
    visited_nodes[current_node] = current_distance
    del unvisited_nodes[current_node]
    if not unvisited_nodes:
        break
    candidates = [node for node in unvisited_nodes.items() if node[1]]
    current_node, current_distance = sorted(candidates, key=lambda x: x[1])[0]
print("\nThe shortest path tree using Dijkstra's algorithm: ")
print(visited_nodes)