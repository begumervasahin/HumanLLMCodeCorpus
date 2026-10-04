import math
def fonk1(b5, b9):
    b1 = [[[0, 0] for b6 in range(b9 + 1)] for b6 in range(b9 + 1)]
    for b2 in range(1, b9 + 1):
        for j in range(1, b9 + 1):
            if b2 = = j:
                b1[b2][j][0] = 0
            elif (b2, j) in b5:
                b1[b2][j][0] = b5[(b2, j)]
            else:
                b1[b2][j][0] = math.inf
    for b3 in range(1, b9 + 1):
        for b2 in range(1, b9 + 1):
            for j in range(1, b9 + 1):
                b1[b2][j][1] = min(b1[b2][j][0], b1[b2][b3][0] + b1[b3][j][0])
                if b3 = = b9 and b1[b2][j][1] < b1[b2][j][0]:
                    b1[b2][j][0] = b1[b2][j][1]
                if b2 = = j and b1[b2][j][1] < 0:
                    return 'NULL'
                b1[b2][j][0] = b1[b2][j][1]
    b4 = min(min(row[1:]) for row in b1[1:])
    return b4
def fonk2(b8):
    b5 = {}
    with open(b8) as file:
        b9, b6 = map(int, file.readline().split())
        for line in file:
            u, v, b7 = map(int, line.split())
            if (u, v) not in b5 or b5[(u, v)] > b7:
                b5[(u, v)] = b7
    return b5, b9
def fonk3():
    b8 = 'g3.txt'
    b5, b9 = fonk2(b8)
    b10 = fonk1(b5, b9)
    print(b10)
if b11 = = '__main__':
    fonk3()