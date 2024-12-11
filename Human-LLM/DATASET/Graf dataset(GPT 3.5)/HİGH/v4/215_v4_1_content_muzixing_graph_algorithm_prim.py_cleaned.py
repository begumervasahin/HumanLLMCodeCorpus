def fonk1(graph, root):
    assert isinstance(graph, dict), "The graph must be a dictionary."
    b1 = set(graph.keys()) - {root}
    b2 = {root}
    b3 = []
    while b1:
        b4 = float('inf')
        b5 = None
        for b6 in b2:
            for neighbor, weight in graph[b6].items():
                if neighbor in b2 or b6 = = neighbor:
                    continue
                if weight < b4:
                    b4 = weight
                    b7 = b6
                    b5 = neighbor
        b3.append((b7, b5))
        b2.add(b5)
        b1.remove(b5)
    return b3
if b8 = = '__main__':
    b9 = {
        "s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
    }
    b3 = fonk1(b9, 's12')
    print(b3)