def floyd(graph):
    num_nodes = len(graph)
    path = {i: {j: [i, j] for j in range(num_nodes) if i != j} for i in range(num_nodes)}
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j].insert(-1, k)
    return graph, path
def floyd_dict(graph):
    path = {src: {dst: [src, dst] for dst in graph[src] if src != dst} for src in graph}
    for mid in graph:
        for src in graph:
            for dst in graph[src]:
                if graph[src][dst] > graph[src][mid] + graph[mid][dst]:
                    graph[src][dst] = graph[src][mid] + graph[mid][dst]
                    path[src][dst].insert(-1, mid)
    return graph, path
if __name__ == '__main__':
    INF = float('inf')
    graph_matrix = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    graph_dict = {
        "s1": {"s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2}
    }
    updated_matrix, paths_matrix = floyd(graph_matrix)
    print("Updated graph (matrix):\n", updated_matrix)
    print("\nPaths (matrix):\n", paths_matrix)
    updated_dict, paths_dict = floyd_dict(graph_dict)
    print("\nUpdated graph (dict):\n", updated_dict)
    print("\nPaths (dict):\n", paths_dict)