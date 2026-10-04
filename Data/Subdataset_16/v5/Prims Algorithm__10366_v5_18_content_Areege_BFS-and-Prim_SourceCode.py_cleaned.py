import random
def fonk1(b22):
    b1 = [[] for _ in range(b22)]
    for i in range(2, b22):
        b2 = random.randint(1, i - 1)
        for _ in range(b2):
            b3 = random.randint(0, b22 - 1)
            b4 = random.randint(10, 100)
            b1[i].append((b3, b4))
            b1[b3].append((i, b4))
    b5 = [[0 for _ in range(b22)] for _ in range(b22)]
    for i in range(b22):
        for b3, b4 in b1[i]:
            b5[i][b3] = b4
    return b5
def fonk2(b17):
    b6 = random.randint(0, len(b17) - 1)
    a1 = 0
    b7 = []
    b8 = [False] * len(b17)
    b8[b6] = True
    b7.append(b6)
    while b7:
        b9 = b7.pop(0)
        for neighbor in range(len(b17)):
            if b17[b9][neighbor] > 0 and not b8[neighbor]:
                b8[neighbor] = True
                b7.append(neighbor)
                a1 += b17[b9][neighbor]
    return a1
def fonk3(b17):
    a1 = 0
    b6 = random.randint(0, len(b17) - 1)
    b10 = len(b17)
    b11 = ["N"] + ["Y"] * (b10 - 1)
    b12 = ["empty"] * b10
    b13 = [1000] * b10
    b11[b6] = "N"
    b13[b6] = 0
    for i in range(b10):
        if b17[b6][i] > 0:
            b12[i] = b6
            b13[i] = b17[b6][i]
    b14 = [b6]
    while len(b14) < b10:
        a2 = 1000
        for i in range(b10):
            if b11[i] == "Y" and b13[i] < a2:
                a2 = b13[i]
                b15 = i
        b14.append(b15)
        a1 += b13[b15]
        b11[b15] = "N"
        for v in range(b10):
            if b17[b15][v] > 0 and b11[v] == "Y" and b17[b15][v] < b13[v]:
                b12[v] = b15
                b13[v] = b17[b15][v]
    return a1
def fonk4():
    b16 = [20, 30, 40, 50, 60]
    a3 = 1000
    for b22 in b16:
        a4 = 0
        for _ in range(a3):
            b17 = fonk1(b22)
            b18 = fonk2(b17)
            b19 = fonk3(b17)
            b20 = ((b18 / b19) - 1) * 100
            a4 += b20
        b21 = a4 / a3
        print(f"Average of Diff for b22 = {b22}: {b21}")
fonk4()