import random
def fonk1(b18):
    b1 = [[] for _ in range(b18)]
    for i in range(2, b18):
        b2 = random.randint(1, i - 1)
        for j in range(b2):
            b3 = random.randint(0, b18 - 1)
            b4 = random.randint(10, 100)
            b1[i].append((b3, b4))
            b1[b3].append((i, b4))
    b5 = [[0 for _ in range(b18)] for _ in range(b18)]
    for i in range(b18):
        for b3, matrix_weight in b1[i]:
            b5[i][b3] = matrix_weight
    return b5
def fonk2(G):
    b6 = random.randint(0, len(G) - 1)
    a1 = 0
    b7 = []
    b8 = [0] * len(G)
    b8[b6] = 1
    b7.append(b6)
    while b7:
        b2 = b7.pop(0)
        for y in range(len(G)):
            if G[b2][y] > 0 and b8[y] == 0:
                b8[y] = 1
                b7.append(y)
                a1 += G[b2][y]
    return a1
def fonk3(G):
    a1 = 0
    b9 = random.randint(0, len(G) - 1)
    b10 = [["empty"] * len(G) for _ in range(3)]
    b10[0][b9] = "N"
    for i in range(len(G)):
        if i != b9:
            b10[0][i] = "Y"
            b10[2][i] = 1000
    for i in range(len(G)):
        if G[b9][i] > 0:
            b10[1][i] = b9
            b10[2][i] = G[b9][i]
    b11 = [b9]
    while len(b11) < len(G):
        a2 = 1000
        for i in range(len(G)):
            if b10[0][i] == "Y" and b10[2][i] < a2:
                a2 = b10[2][i]
                b2 = i
        b11.append(b2)
        a1 += b10[2][b2]
        b10[0][b2] = "N"
        for y in range(len(G)):
            if G[b2][y] > 0 and b10[0][y] == "Y" and G[b2][y] < b10[2][y]:
                b10[1][y] = b2
                b10[2][y] = G[b2][y]
    return a1
def fonk4():
    b12 = [20, 30, 40, 50, 60]
    a3 = 1000
    for b18 in b12:
        a4 = 0
        for _ in range(a3):
            b13 = fonk1(b18)
            b14 = fonk2(b13)
            b15 = fonk3(b13)
            b16 = ((b14 / b15) - 1) * 100
            a4 += b16
        b17 = a4 / a3
        print(f"Average of Diff for b18 = {b18}: {b17}")
fonk4()