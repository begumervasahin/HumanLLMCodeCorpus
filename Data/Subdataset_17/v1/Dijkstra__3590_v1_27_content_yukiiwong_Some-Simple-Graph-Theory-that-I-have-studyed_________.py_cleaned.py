def find_point(distance_dict, node_list):
    min_distance = float('inf')
    min_node = -1
    for node in node_list:
        if distance_dict[node] < min_distance:
            min_distance = distance_dict[node]
            min_node = node
    return min_node
def dijkstra(matrix, origin):
    inf = float('inf')
    nodes = [i for i in range(len(matrix))]
    visited = []
    nodes.remove(origin)
    visited.append(origin)
    min_distance = {origin: 0}
    for i in nodes:
        min_distance[i] = inf
    previous_nodes = [0] * len(matrix)
    while nodes:
        for i in visited:
            for j in nodes:
                new_distance = min_distance[i] + matrix[i][j]
                if new_distance < min_distance[j]:
                    min_distance[j] = new_distance
                    previous_nodes[j] = i
        new_point = find_point(min_distance, nodes)
        if new_point == -1:
            print(f"Cannot reach point {nodes}")
            break
        else:
            visited.append(new_point)
            nodes.remove(new_point)
            print(f"{previous_nodes[new_point]} -> {new_point}")
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
    print("Minimum distances from origin:", min_distance)
if __name__ == "__main__":
    main()