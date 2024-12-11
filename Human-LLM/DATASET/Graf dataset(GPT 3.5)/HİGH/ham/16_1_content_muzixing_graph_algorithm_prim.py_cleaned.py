def fonk1(graph, root):
    assert type(graph)==dict
    b1 = graph.keys()
    b1.remove(root)
    b2 = [root]
    b3 = []
    b4 = None
    while b1:
        b5 = float('inf')
        for b6 in b2:
            for d in graph[b6]:
                if d in b2 or b6 = = d:
                    continue
                if graph[b6][d] < b5:
                    b5 = graph[b6][d]
                    b7 = b6
                    b4 = d
        b3.append((b7, b4))
        b2.append(b4)
        b1.remove(b4)
    return b3
if b8 = = '__main__':
    b9 = {  "s1":{"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5":3},
                    "s2":{"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5":2},
                    "s10":{"s1": 2, "s2": 6, "s10": 0, "s12":3, "s5":4},
                    "s12":{"s1": 3, "s2": 5, "s10": 2, "s12":0,"s5":2},
                    "s5":{"s1": 3, "s2": 5, "s10": 2, "s12":4,"s5":0},
    }
    b3 = fonk1(b9, 's12')
    print b3