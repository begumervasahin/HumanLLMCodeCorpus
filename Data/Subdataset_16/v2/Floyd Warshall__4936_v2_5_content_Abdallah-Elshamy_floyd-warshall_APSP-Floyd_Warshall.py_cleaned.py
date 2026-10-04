import math
def fonk1(b4, b9):
    b1 = [[math.inf] * (b9 + 1) for _ in range(b9 + 1)]
    for b2 in range(1, b9 + 1):
        for j in range(1, b9 + 1):
            if b2 = = j:
                b1[b2][j] = 0
            elif (b2, j) in b4:
                b1[b2][j] = b4[(b2, j)]
    for k in range(1, b9 + 1):
        for b2 in range(1, b9 + 1):
            for j in range(1, b9 + 1):
                b1[b2][j] = min(b1[b2][j], b1[b2][k] + b1[k][j])
    for b2 in range(1, b9 + 1):
        if b1[b2][b2] < 0:
            return 'NULL'
    b3 = min(min(row[1:]) for row in b1[1:])
    return b3
def fonk2(b8):
    b4 = {}
    with open(b8) as file:
        b5 = file.readline()
        b9, b6 = map(int, b5.split())
        for line in file:
            u, v, b7 = map(int, line.split())
            if (u, v) not in b4 or b4[(u, v)] > b7:
                b4[(u, v)] = b7
    return b4, b9
def fonk3():
    b8 = 'g3.txt'
    b4, b9 = fonk2(b8)
    b10 = fonk1(b4, b9)
    print(b10)
if b11 = = '__main__':
    fonk3()