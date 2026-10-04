import itertools
def fonk1(b1, a2):
    for k in range(a2):
        for i, j in itertools.product(range(a2), range(a2)):
            if b1[i][j] > b1[i][k] + b1[k][j]:
                b1[i][j] = b1[i][k] + b1[k][j]
def fonk2(a2):
    a1 = 1000
    b1 = [[a1 for _ in range(a2)] for _ in range(a2)]
    for i in range(a2):
        b1[i][i] = 0
    b1[0][2] = -2
    b1[1][0] = 4
    b1[1][2] = 3
    b1[2][3] = 2
    b1[3][1] = -1
    return b1
def fonk3(b1):
    for row in b1:
        print(row)
def fonk4():
    a2 = 4
    b1 = fonk2(a2)
    print("Initial b1:")
    fonk3(b1)
    print("\nAfter Floyd-Warshall algorithm:")
    fonk1(b1, a2)
    fonk3(b1)
if b2 = = '__main__':
    fonk4()