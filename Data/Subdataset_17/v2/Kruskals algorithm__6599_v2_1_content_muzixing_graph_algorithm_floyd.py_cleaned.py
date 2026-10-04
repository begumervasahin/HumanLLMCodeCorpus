def floyd(graph):
    length = len(graph)
    path = {}
    for i in range(length):
        path[i] = {}
        for j in range(length):
            if i == j:
                continue
            path[i][j] = [i, j]
            for k in range(length):
                if k == j:
                    continue
                new_distance = graph[i][k] + graph[k][j]
                if graph[i][j] > new_distance:
                    graph[i][j] = new_distance
                    path[i][j] = [i, k, j]
    return graph, path
def floyd_dict(graph):
    path = {}
    for src in graph:
        path[src] = {}
        for dst in graph[src]:
            if src == dst:
                continue
            path[src][dst] = [src, dst]
            for mid in graph:
                if mid == dst:
                    continue
                new_distance = graph[src][mid] + graph[mid][dst]
                if graph[src][dst] > new_distance:
                    graph[src][dst] = new_distance
                    path[src][dst] = [src, mid, dst]
    return graph, path
if __name__ == '__main__':
    infinity = float('inf')
    graph_matrix = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    graph_dict = {
        "s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0},
    }
    shortest_paths_matrix, path_reconstruction_matrix = floyd(graph_matrix)
    print("Shortest paths for adjacency matrix:\n", shortest_paths_matrix)
    print("\nPath reconstruction for adjacency matrix:\n", path_reconstruction_matrix)
    shortest_paths_dict, path_reconstruction_dict = floyd_dict(graph_dict)
    print("\nShortest paths for dictionary representation:\n", shortest_paths_dict)
    print("\nPath reconstruction for dictionary representation:\n", path_reconstruction_dict)