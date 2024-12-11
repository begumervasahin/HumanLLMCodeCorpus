def fonk1(graph):
    assert isinstance(graph, dict)
    b1 = list(graph.keys())
    b2 = set()
    b3 = []
    while len(b2) < len(b1):
        b4 = float('inf')
        b5 = None
        b6 = None
        for b7 in b1:
            for destination in b1:
                if b7 in b2 and destination in b2 or b7 = = destination:
                    continue
                if graph[b7][destination] < b4:
                    b4 = graph[b7][destination]
                    b5 = b7
                    b6 = destination
        b3.append((b5, b6))
        b2.add(b5)
        b2.add(b6)
    return b3
if b8 = = '__main__':
    b9 = {
        "s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0},
    }
    b10 = fonk1(b9)
    print(b10)