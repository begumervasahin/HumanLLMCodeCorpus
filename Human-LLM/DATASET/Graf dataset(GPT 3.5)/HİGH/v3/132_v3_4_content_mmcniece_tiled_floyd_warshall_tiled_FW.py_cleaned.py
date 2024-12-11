import random
import timeit
from pprint import pprint
from copy import deepcopy
a1 = 100000000
a2 = 9
a3 = 3
b1 = False
b2 = True
def fonk1(dim, b3 = 0.5):
    global b2
    b4 = [[0] * dim for _ in range(dim)]
    b5 = -1 if b2 else 1
    for _ in range(int(b3 * (dim ** 2))):
        b6 = random.randint(0, dim - 1)
        b7 = random.randint(0, dim - 1)
        if b7 = = b6:
            continue
        b8 = random.randint(b5, 20)
        b4[b6][b7] = b8
    for b18 in range(dim):
        for b17 in range(dim):
            if b18 != b17 and b4[b18][b17] == 0:
                b4[b18][b17] = a1
    return b4
def fonk2(graph):
    b9 = [deepcopy(row) for row in graph]
    b10 = len(graph[0])
    for k in range(b10):
        for b18 in range(b10):
            for b17 in range(b10):
                b9[b18][b17] = min(b9[b18][b17], b9[b18][k] + b9[k][b17])
    return b9
def fonk3(b4, a3):
    b11 = len(b4[0]) % a3
    if b11 = = 0:
        return b4
    else:
        b12 = a3 - b11
        b13 = len(b4[0]) + b12
        for row in b4:
            row.extend([a1] * b12)
        b4.extend([[a1] * b13 for _ in range(b12)])
        assert len(b4) == b13
        assert len(b4[0]) == b13
    return b4
def fonk4(a_row, a_col, b_row, b_col, c_row, c_col, b4, a4, b14 = False):
    for k in range(a4):
        for b18 in range(a4):
            for b17 in range(a4):
                b4[a_row + b18][a_col + b17] = min(b4[a_row + b18][a_col + b17],
                                                   b4[b_row + b18][b_col + k] + b4[c_row + k][c_col + b17])
                if b14:
                    print("Ai, Aj", a_row + b18, a_col + b17, "Bi, Bk", b_row + b18, b_col + k, "Ck, Cj", c_row + k, c_col + b17)
    return b4
def fonk5(b4, a3):
    b4 = fonk3(b4, a3)
    b15 = len(b4)
    b16 = len(b4)
    for d in range(b15):
        fonk4(d * b16, d * b16, d * b16, d * b16, d * b16, d * b16, b4, a3)
        for b17 in range(b15):
            if b17 = = d:
                continue
            fonk4(d * b16, b17 * b16,
                             d * b16, d * b16,
                             d * b16, b17 * b16,
                             b4, a3)
        for b18 in range(b15):
            if b18 = = d:
                continue
            fonk4(b18 * b16, d * b16,
                             b18 * b16, d * b16,
                             d * b16, d * b16,
                             b4, a3)
        for b18 in range(b15):
            for b17 in range(b15):
                if b18 = = d or b17 == d:
                    continue
                fonk4(b18 * b16, b17 * b16,
                                 b18 * b16, d * b16,
                                 d * b16, b17 * b16,
                                 b4, a3)
    return b4
def fonk6(b10, tile, b14 = False):
    b19 = fonk1(b10)
    print(f"Running Naive Floyd-Warshall on b10 x b10, b10 = {b10}")
    b20 = timeit.default_timer()
    b21 = fonk2(b19)
    b22 = timeit.default_timer() - b20
    print(f"Finished, took {b22} seconds")
    print(f"Running Tiled Floyd-Warshall on same b10 x b10 b4, b10 = {b10}, a3 = {tile}")
    b20 = timeit.default_timer()
    b23 = fonk5(b19, tile)
    b22 = timeit.default_timer() - b20
    print(f"Finished, took {b22} seconds")
    print("Correctness Info:")
    for b18 in range(b10):
        for b17 in range(b10):
            if b21[b18][b17] != b23[b18][b17]:
                print(f"Error, elements ({b18}, {b17}) differ")
                if b14:
                    print("Dumping distance naive:")
                    pprint(b21)
                    print("Dumping distance tiled:")
                    pprint(b23)
                return False
    print("Correctness Check Passed!!")
    if b14:
        print("Dumping distance naive:")
        pprint(b21)
        print("Dumping distance tiled:")
        pprint(b23)
    return True
def fonk7():
    global a2
    global a3
    global b1
    b24 = [
        [0, a1, -2, a1],
        [4, 0, 3, a1],
        [a1, a1, 0, 2],
        [a1, -1, a1, 0]
    ]
    a4 = 2
    print("****WIKI MATRIX TESTING****")
    fonk3(b24, a4)
    print("Initial Matrix:")
    pprint(b24)
    print("Solved with normal Floyd-Warshall:")
    pprint(fonk2(b24))
    print("Solved with tiled:")
    pprint(fonk5(b24, a4))
    print("****RANDOMLY GENERATED MATRIX****")
    b25 = fonk6(a2, a3, b14=b1)
if b26 = = '__main__':
    fonk7()