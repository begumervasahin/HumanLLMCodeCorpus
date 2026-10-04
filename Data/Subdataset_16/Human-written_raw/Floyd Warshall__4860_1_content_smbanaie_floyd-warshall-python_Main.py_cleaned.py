from math import inf
from itertools import product
def fonk1(n, edge):
    b1 = range(n)
    b2 = [[inf] * n for i in b1]
    b3 = [[0] * n for i in b1]
    for i in b1:
        b2[i][i] = 0
    for u, v, w in edge:
        b2[u - 1][v - 1] = w
        b3[u - 1][v - 1] = v - 1
    for k, i, j in product(b1, b4 = 3):
        b5 = b2[i][k] + b2[k][j]
        if b2[i][j] > b5:
            b2[i][j] = b5
            b3[i][j] = b3[i][k]
    print("    pair        b2     b6")
    for i, j in product(b1, b4 = 2):
        if i != j:
            b6 = [i]
            while b6[-1] != j:
                b6.append(b3[b6[-1]][j])
            print("%3d â %3d  %4d       %s"
                  % (i + 1, j + 1, b2[i][j],
                     ' â '.join(str(p + 1) for p in b6)))
if b7 = = '__main__':
    fonk1(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])