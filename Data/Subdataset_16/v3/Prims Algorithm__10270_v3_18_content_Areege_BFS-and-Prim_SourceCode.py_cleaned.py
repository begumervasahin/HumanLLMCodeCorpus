import random
def fonk1(b10):
    b1 = [[] for _ in range(b10)]
    for i in range(2, b10):
        b2 = random.randint(1, i-1)
        for _ in range(b2):
            b3 = random.randint(0, b10-1)
            b4 = random.randint(10, 100)
            b1[i].append((b3, b4))
            b1[b3].append((i, b4))
    b5 = [[0] * b10 for _ in range(b10)]
    for i in range(b10):
        for b3, b4 in b1[i]:
            b5[i][b3] = b4
            b5[b3][i] = b4
    return b5
def fonk2(b13):
    b6 = random.randint(0, len(b13)-1)
    a1 = 0
    b7 = [b6]
    b8 = [False] * len(b13)
    b8[b6] = True
    while b7:
        b9 = b7.pop(0)
        for neighbor in range(len(b13)):
            if b13[b9][neighbor] > 0 and not b8[neighbor]:
                b8[neighbor] = True
                b7.append(neighbor)
                a1 += b13[b9][neighbor]
    return a1
def fonk3(b13):
    a1 = 0
    b10 = len(b13)
    b6 = random.randint(0, b10-1)
    b8 = [False] * b10
    b11 = [(float('inf'), -1)] * b10
    b11[b6] = (0, -1)
    for _ in range(b10):
        b9 = min((w, v) for v, (w, _) in enumerate(b11) if not b8[v])[1]
        b8[b9] = True
        a1 += b11[b9][0]
        for neighbor, b4 in enumerate(b13[b9]):
            if b4 > 0 and not b8[neighbor] and b4 < b11[neighbor][0]:
                b11[neighbor] = (b4, b9)
    return a1
def fonk4():
    b12 = [20, 30, 40, 50, 60]
    a2 = 1000
    for num_nodes in b12:
        a3 = 0
        for _ in range(a2):
            b13 = fonk1(num_nodes)
            b14 = fonk2(b13)
            b15 = fonk3(b13)
            b16 = ((b14 / b15) - 1) * 100
            a3 += b16
        b17 = a3 / a2
        print(f"Average difference for b10 = {num_nodes}: {b17:.2f}%")
if b18 = = "__main__":
    fonk4()