def fonk1(graph):
    b1 = len(graph)
    b2 = {}
    for i in range(b1):
        b2.setdefault(i, {})
        for j in range(b1):
            if i != j:
                b2[i].setdefault(j, [i, j])
    for k in range(b1):
        for i in range(b1):
            for j in range(b1):
                if i != j and i != k and j != k:
                    b3 = graph[i][k] + graph[k][j]
                    if graph[i][j] > b3:
                        graph[i][j] = b3
                        b2[i][j].insert(-1, k)
    return graph, b2
def fonk2(graph):
    b2 = {}
    for src in graph:
        b2.setdefault(src, {})
        for dst in graph[src]:
            if src != dst:
                b2[src].setdefault(dst, [src, dst])
    for mid in graph:
        for src in graph:
            for dst in graph[src]:
                if src != dst and src != mid and dst != mid:
                    b3 = graph[src][mid] + graph[mid][dst]
                    if graph[src][dst] > b3:
                        graph[src][dst] = b3
                        b2[src][dst].insert(-1, mid)
    return graph, b2
if b4 = = '__main__':
    b5 = float('inf')
    b6 = [
        [0, 2, 1, 4, 5, 1],
        [1, 0, 4, 2, 3, 4],
        [2, 1, 0, 1, 2, 4],
        [3, 5, 2, 0, 3, 3],
        [2, 4, 3, 4, 0, 1],
        [3, 4, 7, 3, 1, 0]
    ]
    b7 = {
        "s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
        "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0}
    }
    new_graph, b2 = fonk1(b6)
    print(new_graph, '\n\n\n', b2)