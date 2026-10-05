def fonk1(graph, start, goal):
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = goal:
            return b3
        elif b4 not in b2:
            b5 = graph.get(b4, [])
            for neighbor in b5:
                b6 = b3 + [neighbor]
                b1.append(b6)
            b2.add(b4)
    return None
b7 = 'A'
b8 = 'F'
b9 = fonk1(base, b7, b8)
if b9:
    print("Path found:", b9)
else:
    print("Path not found")