from math import inf
from itertools import product
def fonk1(n, edge):
    b1 = [[inf] * n for _ in range(n)]
    b2 = [[0] * n for _ in range(n)]
    for i in range(n):
        b1[i][i] = 0
    for u, v, w in edge:
        b1[u - 1][v - 1] = w
        b2[u - 1][v - 1] = v - 1
    for k, i, j in product(range(n), b3 = 3):
        b4 = b1[i][k] + b1[k][j]
        if b1[i][j] > b4:
            b1[i][j] = b4
            b2[i][j] = b2[i][k]
    print("    pair        b1     b5")
    for i, j in product(range(n), b3 = 2):
        if i != j:
            b5 = [i]
            while b5[-1] != j:
                b5.append(b2[b5[-1]][j])
            print("%3d -> %3d  %4d       %s"
                  % (i + 1, j + 1, b1[i][j],
                     ' -> '.join(str(p + 1) for p in b5)))
if b6 = = '__main__':
    fonk1(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])