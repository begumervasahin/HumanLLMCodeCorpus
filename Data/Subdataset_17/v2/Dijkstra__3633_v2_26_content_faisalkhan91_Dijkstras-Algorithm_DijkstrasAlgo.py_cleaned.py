
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
def dijkstra(nodes, distances, start):
    unvisited = {node: None for node in nodes}
    visited = {}
    current_node = start
    current_distance = 0
    unvisited[current_node] = current_distance
    while unvisited:
        for neighbor, distance in distances[current_node].items():
            if neighbor not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbor] is None or new_distance < unvisited[neighbor]:
                unvisited[neighbor] = new_distance
        visited[current_node] = current_distance
        del unvisited[current_node]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1] is not None]
        current_node, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return visited
def main():
    start_node = 'B'
    shortest_path_tree = dijkstra(nodes, distances, start_node)
    print(f"\nThe shortest path tree using Dijkstra's algorithm starting from node '{start_node}':")
    print(shortest_path_tree)
if __name__ == "__main__":
    main()