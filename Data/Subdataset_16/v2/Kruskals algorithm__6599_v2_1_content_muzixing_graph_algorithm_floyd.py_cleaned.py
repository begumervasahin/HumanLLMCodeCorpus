def fonk1(graph):
    b1 = len(graph)
    b2 = {}
    for b3 in range(b1):
        b2[b3] = {}
        for j in range(b1):
            if b3 = = j:
                continue
            b2[b3][j] = [b3, j]
            for b4 in range(b1):
                if b4 = = j:
                    continue
                b5 = graph[b3][b4] + graph[b4][j]
                if graph[b3][j] > b5:
                    graph[b3][j] = b5
                    b2[b3][j] = [b3, b4, j]
    return graph, b2
def fonk2(graph):
    b2 = {}
    for b6 in graph:
        b2[b6] = {}
        for dst in graph[b6]:
            if b6 = = dst:
                continue
            b2[b6][dst] = [b6, dst]
            for b7 in graph:
                if b7 = = dst:
                    continue
                b5 = graph[b6][b7] + graph[b7][dst]
                if graph[b6][dst] > b5:
                    graph[b6][dst] = b5
                    b2[b6][dst] = [b6, b7, dst]
    return graph, b2
if b8 = = '__main__':
    b9 = float('inf')
    b10 = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    b11 = {
        "s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0},
    }
    shortest_paths_matrix, b12 = fonk1(b10)
    print("Shortest paths for adjacency matrix:\n", shortest_paths_matrix)
    print("\nPath reconstruction for adjacency matrix:\n", b12)
    shortest_paths_dict, b13 = fonk2(b11)
    print("\nShortest paths for dictionary representation:\n", shortest_paths_dict)
    print("\nPath reconstruction for dictionary representation:\n", b13)