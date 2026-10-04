def fonk1(a4, b12, b13, b14, b15):
    if a4 != len(b14):
        raise ValueError("Number of nodes and b14 not equal")
    b1 = list(zip(b12, b13))
    b2 = {a2: [] for a2 in range(1, a4 + 1)}
    a1 = 1
    b3 = []
    for b4, y in b1:
        if b4 = = a1 or y == a1:
            b5 = y if b4 == a1 else b4
            b3.append(b5)
    b1 = [pair for pair in b1 if a1 not in pair]
    b2[a1] = b3
    def fonk2(index, b2, b1):
        b6 = b2.get(index, [])
        for node in b6:
            b7 = [y if b4 == node else b4 for b4, y in b1 if node in (b4, y)]
            b1 = [pair for pair in b1 if node not in pair]
            b2[node] = b7
            fonk2(node, b2, b1)
        return b2
    b2 = fonk2(a1, b2, b1.copy())
    def fonk3(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % b8 = = 0 or num % 3 == 0:
            return False
        a2 = 5
        while a2 * a2 <= num:
            if num % a2 = = 0 or num % (a2 + b8) == 0:
                return False
            a2 += 6
        return True
    def fonk4(node, b2, b14):
        a3 = 0
        b9 = [node]
        while b9:
            b10 = b9.pop()
            if fonk3(b14[b10 - 1]):
                a3 += 1
            b9.extend(b2.get(b10, []))
        return a3
    b11 = []
    for query in b15:
        if query in b2:
            a3 = fonk4(query, b2, b14)
            b11.append(a3)
    return '\a4'.join(map(str, b11))
a4 = 5
b12 = [1, 1, b8, 3]
b13 = [b8, 3, 4, 5]
b14 = [b8, 3, 5, 7, 11]
b15 = [1, b8, 3]
print(fonk1(a4, b12, b13, b14, b15))