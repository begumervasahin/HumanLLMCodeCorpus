def fonk1(graph, start, goal):
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = goal:
            return b3
        elif b4 not in b2:
            for neighbor in graph.get(b4, []):
                b5 = list(b3)
                b5.append(neighbor)
                b1.append(b5)
            b2.add(b4)
    print("Path not found")
b6 = 'A'
b7 = 'F'
b8 = fonk1(base, b6, b7)
print(b8)