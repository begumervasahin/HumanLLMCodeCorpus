
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'D': {'A': 3, 'B': 1, 'E': 1, 'G': 1},
    'E': {'A': 12, 'C': 1, 'D': 1, 'F': 2},
    'F': {'A': 5, 'C': 16, 'E': 2},
    'G': {'B': 2, 'C': 2, 'D': 1}
}
def dijkstra(nodes, distances, start):
    unvisited = {node: float('inf') for node in nodes}
    visited = {}
    current_node = start
    current_distance = 0
    unvisited[current_node] = current_distance
    while unvisited:
        for neighbor, distance in distances[current_node].items():
            new_distance = current_distance + distance
            if new_distance < unvisited[neighbor]:
                unvisited[neighbor] = new_distance
        visited[current_node] = current_distance
        del unvisited[current_node]
        if not unvisited:
            break
        current_node, current_distance = min(unvisited.items(), key=lambda x: x[1])
    return visited
def main():
    start_node = 'B'
    shortest_path_tree = dijkstra(nodes, distances, start_node)
    print(f"\nThe shortest path tree using Dijkstra's algorithm starting from node '{start_node}':")
    print(shortest_path_tree)
if __name__ == "__main__":
    main()