def fonk1(graph):
    b1 = len(graph)
    b2 = {i: {j: [i, j] for j in range(b1) if i != j} for i in range(b1)}
    for k in range(b1):
        for i in range(b1):
            for j in range(b1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    b2[i][j].insert(-1, k)
    return graph, b2
def fonk2(graph):
    b2 = {src: {dst: [src, dst] for dst in graph[src] if src != dst} for src in graph}
    for mid in graph:
        for src in graph:
            for dst in graph[src]:
                if graph[src][dst] > graph[src][mid] + graph[mid][dst]:
                    graph[src][dst] = graph[src][mid] + graph[mid][dst]
                    b2[src][dst].insert(-1, mid)
    return graph, b2
if b3 = = '__main__':
    b4 = float('inf')
    b5 = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    b6 = {
        "s1": {"s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2}
    }
    updated_matrix, b7 = fonk1(b5)
    print("Updated graph (matrix):\n", updated_matrix)
    print("\nPaths (matrix):\n", b7)
    updated_dict, b8 = fonk2(b6)
    print("\nUpdated graph (dict):\n", updated_dict)
    print("\nPaths (dict):\n", b8)