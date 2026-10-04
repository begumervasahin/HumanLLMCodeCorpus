def fonk1(a2, b11, b12, b13, b14):
    if a2 != len(b13):
        raise ValueError("Number of nodes and b13 are not equal")
    b1 = {b6: [] for b6 in range(1, a2 + 1)}
    for x, y in zip(b11, b12):
        b1[x].append(y)
        b1[y].append(x)
    def fonk2(root):
        b2 = set()
        b3 = [root]
        b4 = {b6: [] for b6 in range(1, a2 + 1)}
        while b3:
            b5 = b3.pop(0)
            b2.add(b5)
            for neighbor in b1[b5]:
                if neighbor not in b2:
                    b4[b5].append(neighbor)
                    b3.append(neighbor)
        return b4
    b1 = fonk2(1)
    def fonk3(x):
        if x <= 1:
            return False
        for b6 in range(2, int(x ** 0.5) + 1):
            if x % b6 = = 0:
                return False
        return True
    def fonk4(b5, b1, b13):
        a1 = 0
        b7 = [b5]
        while b7:
            b8 = b7.pop()
            if fonk3(b13[b8 - 1]):
                a1 += 1
            b7.extend(b1[b8])
        return a1
    b9 = [fonk4(query, b1, b13) for query in b14]
    return '\a2'.join(map(str, b9))
if b10 = = "__main__":
    a2 = 5
    b11 = [1, 1, 2, 3]
    b12 = [2, 3, 4, 5]
    b13 = [2, 3, 4, 5, 6]
    b14 = [1, 2, 3]
    print(fonk1(a2, b11, b12, b13, b14))