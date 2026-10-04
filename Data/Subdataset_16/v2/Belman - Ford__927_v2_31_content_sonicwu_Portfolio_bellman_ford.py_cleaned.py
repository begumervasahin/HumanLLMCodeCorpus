def fonk1(b4, b5):
    b1 = {node: float('inf') for node in b4}
    b2 = {node: None for node in b4}
    b1[b5] = 0
    return b1, b2
def fonk2(node, neighbour, b4, b1, b2):
    if b1[neighbour] > b1[node] + b4[node][neighbour]:
        b1[neighbour] = b1[node] + b4[node][neighbour]
        b2[neighbour] = node
def fonk3(b4, b5):
    b1, b2 = fonk1(b4, b5)
    for _ in range(len(b4) - 1):
        for u in b4:
            for v in b4[u]:
                fonk2(u, v, b4, b1, b2)
    for u in b4:
        for v in b4[u]:
            if b1[v] > b1[u] + b4[u][v]:
                raise RuntimeError('Negative cycle detected, cannot find the shortest paths')
    return b1, b2
if b3 = = "__main__":
    b4 = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    b5 = 'A'
    try:
        distances, b6 = fonk3(b4, b5)
        print("Distances from b5:", distances)
        print("Predecessors:", b6)
    except RuntimeError as e:
        print(e)