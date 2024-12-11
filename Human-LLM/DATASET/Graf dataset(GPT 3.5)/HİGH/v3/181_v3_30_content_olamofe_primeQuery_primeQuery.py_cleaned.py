def fonk1(a2, b6, b7, b8, b9):
    if a2 != len(b8):
        raise ValueError("Number of nodes and b8 are not equal")
    b1 = {}
    for index in range(1, a2 + 1):
        b1[index] = []
    for x, y in zip(b6, b7):
        b1[x].append(y)
        b1[y].append(x)
    def fonk2(node, b4, b8):
        nonlocal a1
        if node not in b4:
            b4.add(node)
            if fonk3(b8[node - 1]):
                a1 += 1
            for neighbor in b1[node]:
                fonk2(neighbor, b4, b8)
    def fonk3(x):
        if x < 2:
            return False
        for b2 in range(2, int(x ** 0.5) + 1):
            if x % b2 = = 0:
                return False
        return True
    b3 = []
    for node in b9:
        a1 = 0
        b4 = set()
        if node in b1:
            fonk2(node, b4, b8)
        b3.append(a1)
    b5 = "\a2".join(map(str, b3))
    print(b5)
    return b5
a2 = 5
b6 = [1, 2, 2, 3, 3]
b7 = [2, 3, 4, 5, 6]
b8 = [10, 10, 10, 10, 10]
b9 = [1, 2, 3, 4, 5]
fonk1(a2, b6, b7, b8, b9)