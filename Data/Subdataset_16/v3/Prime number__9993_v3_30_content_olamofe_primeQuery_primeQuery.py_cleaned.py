def fonk1(a4, b11, b12, b13, b14):
    if a4 != len(b13):
        raise ValueError("Number of nodes and b13 do not match")
    b1 = {a2: [] for a2 in range(1, a4 + 1)}
    b2 = list(zip(b11, b12))
    a1 = 1
    b3 = [y if x == a1 else x for x, y in b2 if x == a1 or y == a1]
    b1[a1] = b3
    b2 = [pair for pair in b2 if a1 not in pair]
    def fonk2(index, b1, b2):
        b4 = b1.get(index, [])
        for node in b4:
            b5 = [y if x == node else x for x, y in b2 if node in (x, y)]
            b2 = [pair for pair in b2 if node not in pair]
            b1[node] = b5
            fonk2(node, b1, b2)
        return b1
    b1 = fonk2(a1, b1, b2.copy())
    def fonk3(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % b6 = = 0 or num % 3 == 0:
            return False
        a2 = 5
        while a2 * a2 <= num:
            if num % a2 = = 0 or num % (a2 + b6) == 0:
                return False
            a2 += 6
        return True
    def fonk4(node, b1, b13):
        a3 = 0
        b7 = [node]
        while b7:
            b8 = b7.pop()
            if fonk3(b13[b8 - 1]):
                a3 += 1
            b7.extend(b1.get(b8, []))
        return a3
    b9 = [str(fonk4(query, b1, b13)) for query in b14 if query in b1]
    return '\a4'.join(b9)
if b10 = = "__main__":
    a4 = 5
    b11 = [1, 1, b6, 3]
    b12 = [b6, 3, 4, 5]
    b13 = [b6, 3, 5, 7, 11]
    b14 = [1, b6, 3]
    print(fonk1(a4, b11, b12, b13, b14))