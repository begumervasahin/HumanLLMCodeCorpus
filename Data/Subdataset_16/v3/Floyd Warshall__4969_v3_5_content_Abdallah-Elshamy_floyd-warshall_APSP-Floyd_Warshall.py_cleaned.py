import math
def fonk1(b4, b8):
    b1 = [[math.inf] * (b8 + 1) for b5 in range(b8 + 1)]
    for b2 in range(1, b8 + 1):
        for j in range(1, b8 + 1):
            if b2 = = j:
                b1[b2][j] = 0
            elif (b2, j) in b4:
                b1[b2][j] = b4[(b2, j)]
    for k in range(1, b8 + 1):
        for b2 in range(1, b8 + 1):
            for j in range(1, b8 + 1):
                b1[b2][j] = min(b1[b2][j], b1[b2][k] + b1[k][j])
    for b2 in range(1, b8 + 1):
        if b1[b2][b2] < 0:
            return 'NULL'
    b3 = min(min(row[1:]) for row in b1[1:])
    return b3
def fonk2(b7):
    b4 = {}
    with open(b7) as file:
        b8, b5 = map(int, file.readline().split())
        for line in file:
            u, v, b6 = map(int, line.split())
            if (u, v) not in b4 or b4[(u, v)] > b6:
                b4[(u, v)] = b6
    return b4, b8
def fonk3():
    b7 = 'g3.txt'
    b4, b8 = fonk2(b7)
    b9 = fonk1(b4, b8)
    print(b9)
if b10 = = '__main__':
    fonk3()