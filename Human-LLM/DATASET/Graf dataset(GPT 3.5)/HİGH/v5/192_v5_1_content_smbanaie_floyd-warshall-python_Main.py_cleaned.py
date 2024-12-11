from math import inf
from itertools import product
def fonk1(num_vertices, edges):
    b1 = [[inf] * num_vertices for _ in range(num_vertices)]
    b2 = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        b1[i][i] = 0
    for source, destination, weight in edges:
        b1[source - 1][destination - 1] = weight
        b2[source - 1][destination - 1] = destination - 1
    for k, i, j in product(range(num_vertices), b3 = 3):
        b4 = b1[i][k] + b1[k][j]
        if b1[i][j] > b4:
            b1[i][j] = b4
            b2[i][j] = b2[i][k]
    print("    Pair        Distance     Path")
    for i, j in product(range(num_vertices), b3 = 2):
        if i != j:
            b5 = [i]
            while b5[-1] != j:
                b5.append(b2[b5[-1]][j])
            print("%3d -> %3d  %7d       %s"
                  % (i + 1, j + 1, b1[i][j],
                     ' -> '.join(str(p + 1) for p in b5)))
if b6 = = '__main__':
    fonk1(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])