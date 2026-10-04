def fonk1(graph):
    b1 = len(graph)
    b2 = {}
    for b3 in range(b1):
        b2.setdefault(b3, {})
        for j in range(b1):
            if b3 = = j:
                continue
            b2[b3][j] = [b3, j]
            b4 = None
            for b5 in range(b1):
                if b5 = = j:
                    continue
                b6 = graph[b3][b5] + graph[b5][j]
                if graph[b3][j] > b6:
                    graph[b3][j] = b6
                    b4 = b5
            if b4 is not None:
                b2[b3][j].insert(-1, b4)
    return graph, b2
def fonk2(graph):
    b2 = {}
    for b7 in graph:
        b2.setdefault(b7, {})
        for dst in graph[b7]:
            if b7 = = dst:
                continue
            b2[b7][dst] = [b7, dst]
            b4 = None
            for b8 in graph:
                if b8 = = dst:
                    continue
                b6 = graph[b7][b8] + graph[b8][dst]
                if graph[b7][dst] > b6:
                    graph[b7][dst] = b6
                    b4 = b8
            if b4 is not None:
                b2[b7][dst].insert(-1, b4)
    return graph, b2
if b9 = = '__main__':
    b10 = float('inf')
    b11 = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    b12 = {
        "s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0}
    }
    new_graph, b2 = fonk1(b11)
    print("Updated graph (list representation):")
    for row in new_graph:
        print(row)
    print("\nPath (list representation):")
    print(b2)
    new_graph_dict, b13 = fonk2(b12)
    print("\nUpdated graph (dictionary representation):")
    for key, value in new_graph_dict.items():
        print(f"{key}: {value}")
    print("\nPath (dictionary representation):")
    print(b13)