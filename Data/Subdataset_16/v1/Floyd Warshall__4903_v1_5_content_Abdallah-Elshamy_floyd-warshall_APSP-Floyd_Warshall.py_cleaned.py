import math
def fonk1(b5, b11):
    b1 = [[[0 if b4 == 0 else 0 for b4 in range(2)] for j in range(b11 + 1)] for b2 in range(b11 + 1)]
    for b2 in range(1, b11 + 1):
        for j in range(1, b11 + 1):
            if b2 = = j:
                b1[b2][j][0] = 0
            elif b5.get((b2, j)) is not None:
                b1[b2][j][0] = b5[(b2, j)]
            else:
                b1[b2][j][0] = math.inf
    b3 = math.inf
    for b4 in range(1, b11 + 1):
        for b2 in range(1, b11 + 1):
            for j in range(1, b11 + 1):
                b1[b2][j][1] = min(b1[b2][j][0], b1[b2][b4][0] + b1[b4][j][0])
                if b4 = = b11 and b3 > b1[b2][j][1]:
                    b3 = b1[b2][j][1]
                if b2 = = j and b1[b2][j][1] < 0:
                    return 'NULL'
                b1[b2][j][0] = b1[b2][j][1]
    return b3
def fonk2(b10):
    b5 = {}
    with open(b10) as file:
        b6 = file.readline()
        b11, b7 = map(int, b6.split())
        b8 = file.readlines()
        for line in b8:
            u, v, b9 = map(int, line.split())
            if (u, v) not in b5 or b5[(u, v)] > b9:
                b5[(u, v)] = b9
    return b5, b11
def fonk3():
    b10 = 'g3.txt'
    b5, b11 = fonk2(b10)
    b12 = fonk1(b5, b11)
    print(b12)
if b13 = = '__main__':
    fonk3()