def find_min_distance_node(distance_dict, nodes):
    min_distance = float('inf')
    min_node = -1
    for node in nodes:
        if distance_dict[node] < min_distance:
            min_distance = distance_dict[node]
            min_node = node
    return min_node
def dijkstra(matrix, origin):
    inf = float('inf')
    num_nodes = len(matrix)
    nodes = list(range(num_nodes))
    visited = []
    nodes.remove(origin)
    visited.append(origin)
    min_distance = {i: inf for i in range(num_nodes)}
    min_distance[origin] = 0
    previous_nodes = [-1] * num_nodes
    while nodes:
        for current in visited:
            for neighbor in nodes:
                if matrix[current][neighbor] < inf:
                    new_distance = min_distance[current] + matrix[current][neighbor]
                    if new_distance < min_distance[neighbor]:
                        min_distance[neighbor] = new_distance
                        previous_nodes[neighbor] = current
        next_node = find_min_distance_node(min_distance, nodes)
        if next_node == -1:
            print(f"Cannot reach points {nodes}")
            break
        else:
            visited.append(next_node)
            nodes.remove(next_node)
            print(f"{previous_nodes[next_node]} -> {next_node}")
    return min_distance, previous_nodes
def main():
    inf = float('inf')
    matrix = [
        [0, 1, inf, 2, inf, inf],
        [inf, 0, 3, 4, inf, inf],
        [inf, inf, 0, 5, 1, inf],
        [inf, 4, inf, 0, inf, inf],
        [inf, inf, 2, 3, 0, inf],
        [inf, inf, 2, inf, 2, 0]
    ]
    origin = 1
    min_distance, previous_nodes = dijkstra(matrix, origin)
    print("\nMinimum distances from origin:", min_distance)
if __name__ == "__main__":
    main()