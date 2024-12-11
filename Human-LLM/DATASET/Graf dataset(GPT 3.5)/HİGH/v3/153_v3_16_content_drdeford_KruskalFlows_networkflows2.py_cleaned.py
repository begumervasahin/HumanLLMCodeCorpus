import numpy as np
import matplotlib.pyplot as plt
import math
import time
from operator import itemgetter
def fonk1():
    b1 = [[0, 1, 3, 4, 0], [1, 0, 0, 2, 0], [3, 0, 0, 0, 5], [4, 2, 0, 0, 0], [0, 0, 5, 0, 0]]
    fonk2(b1)
def fonk2(adjacency_matrix):
    fonk3(adjacency_matrix)
    kruskal_time, b2 = fonk4(adjacency_matrix)
    prim_time, b3 = fonk10(adjacency_matrix)
    sollin_time, b4 = fonk13(adjacency_matrix)
    print('Kruskal Time:', kruskal_time, '\nKruskal Cost:', b2,
          '\nPrim Time:', prim_time, '\nPrim Cost:', b3,
          '\nSollin Time:', sollin_time, '\nSollin Cost:', b4)
    plt.show()
def fonk3(adjacency_matrix):
    b5 = len(adjacency_matrix)
    b6 = []
    b7 = []
    b8 = 2 * math.pi / b5
    plt.figure(1)
    plt.title('Original Graph')
    for i in range(b5):
        b6.append(b5 * math.cos(i * b8))
        b7.append(b5 * math.sin(i * b8))
        plt.text(b6[i], b7[i], i + 1, b9 = 15, color='green')
    for i in range(b5):
        for j in range(i, b5):
            if adjacency_matrix[i][j] != 0:
                plt.plot([b6[i], b6[j]], [b7[i], b7[j]], 'b-', b10 = 3)
                plt.text((b6[i] + b6[j]) / 2, (b7[i] + b7[j]) / 2, adjacency_matrix[i][j], b9 = 15, color='red')
    plt.scatter(b6, b7, b11 = 50)
def fonk4(adjacency_matrix):
    b12 = time.time()
    b13 = fonk5(adjacency_matrix)
    b14 = fonk6(adjacency_matrix, b13)
    b15 = time.time() - b12
    return b15, fonk9(adjacency_matrix, b14)
def fonk5(adjacency_matrix):
    b13 = []
    for i in range(len(adjacency_matrix)):
        for j in range(i, len(adjacency_matrix)):
            if adjacency_matrix[i][j] != 0:
                b13.append((i, j, adjacency_matrix[i][j]))
    return sorted(b13, b16 = itemgetter(2))
def fonk6(adjacency_matrix, b13):
    b14 = []
    b17 = [{i} for i in range(len(adjacency_matrix))]
    for edge in b13:
        u, v, b18 = edge
        if u != v and fonk7(u, b17) != fonk7(v, b17):
            b14.append(edge)
            fonk8(u, v, b17)
    return b14
def fonk7(vertex, b17):
    for i, subset in enumerate(b17):
        if vertex in subset:
            return i
def fonk8(u, v, b17):
    b19 = fonk7(u, b17)
    b20 = fonk7(v, b17)
    if b19 != b20:
        b17[b19] |= b17[b20]
        del b17[b20]
def fonk9(adjacency_matrix, b13):
    return sum(b18 for b27, b27, b18 in b13)
def fonk10(adjacency_matrix):
    b12 = time.time()
    b14 = fonk11(adjacency_matrix)
    b21 = time.time() - b12
    return b21, fonk9(adjacency_matrix, b14)
def fonk11(adjacency_matrix):
    b14 = []
    b22 = len(adjacency_matrix)
    b23 = [False] * b22
    b23[0] = True
    while len(b14) < b22 - 1:
        b24 = fonk12(adjacency_matrix, b23)
        b14.append(b24)
        b23[b24[1]] = True
    return b14
def fonk12(adjacency_matrix, b23):
    b25 = float('inf')
    b24 = None
    b22 = len(adjacency_matrix)
    for u in range(b22):
        if b23[u]:
            for v in range(b22):
                if not b23[v] and adjacency_matrix[u][v] != 0 and adjacency_matrix[u][v] < b25:
                    b25 = adjacency_matrix[u][v]
                    b24 = (u, v, b25)
    return b24
def fonk13(adjacency_matrix):
    b12 = time.time()
    b14 = fonk14(adjacency_matrix)
    b26 = time.time() - b12
    return b26, fonk9(adjacency_matrix, b14)
def fonk14(adjacency_matrix):
    b14 = []
    b22 = len(adjacency_matrix)
    b17 = [{i} for i in range(b22)]
    while len(b14) < b22 - 1:
        for i in range(b22):
            b24 = fonk15(adjacency_matrix, b17[i])
            if b24 is not None and b24 not in b14:
                b14.append(b24)
                u, v, b27 = b24
                b17[u] |= b17[v]
                del b17[v]
    return b14
def fonk15(adjacency_matrix, subset):
    b25 = float('inf')
    b24 = None
    for u in subset:
        for v in range(len(adjacency_matrix)):
            if v not in subset and adjacency_matrix[u][v] != 0 and adjacency_matrix[u][v] < b25:
                b25 = adjacency_matrix[u][v]
                b24 = (u, v, b25)
    return b24
if b28 = = "__main__":
    fonk1()