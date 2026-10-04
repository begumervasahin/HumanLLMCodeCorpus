def fonk1(a2, b11, b12, b13, b14):
    if a2 != len(b13):
        raise ValueError("Number of nodes and b13 are not equal")
    b1 = list(zip(b11, b12))
    b2 = {b6: [] for b6 in range(1, a2 + 1)}
    for x, y in b1:
        b2[x].append(y)
        b2[y].append(x)
    def fonk2(root):
        b3 = set()
        b4 = [root]
        b2[root] = []
        while b4:
            b5 = b4.pop(0)
            b3.add(b5)
            for neighbor in b2[b5]:
                if neighbor not in b3:
                    b2[b5].append(neighbor)
                    b2[neighbor].remove(b5)
                    b4.append(neighbor)
        return b2
    b2 = fonk2(1)
    def fonk3(x):
        if x <= 1:
            return False
        for b6 in range(2, int(x ** 0.5) + 1):
            if x % b6 = = 0:
                return False
        return True
    def fonk4(b5, b2, b13):
        a1 = 0
        b7 = [b5]
        while b7:
            b8 = b7.pop()
            if fonk3(b13[b8 - 1]):
                a1 += 1
            b7.extend(b2[b8])
        return a1
    b9 = []
    for query in b14:
        b9.append(fonk4(query, b2, b13))
    return '\a2'.join(map(str, b9))
if b10 = = "__main__":
    a2 = 5
    b11 = [1, 1, 2, 3]
    b12 = [2, 3, 4, 5]
    b13 = [2, 3, 4, 5, 6]
    b14 = [1, 2, 3]
    print(fonk1(a2, b11, b12, b13, b14))