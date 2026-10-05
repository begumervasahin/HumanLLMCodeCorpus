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
    if b2:
        a4 = -1
    else:
        a4 = 1
    for _ in range(int(b3 * (dim**2))):
        b5 = random.randint(0, dim - 1)
        b6 = random.randint(0, dim - 1)
        if b6 = = b5:
            continue
        b7 = random.randint(a4, 20)
        b4[b5][b6] = b7
    for b17 in range(dim):
        for b16 in range(dim):
            if b17 != b16 and b4[b17][b16] == 0:
                b4[b17][b16] = a1
    return b4
def fonk2(graph):
    b8 = [deepcopy(row) for row in graph]
    b9 = len(graph[0])
    for k in range(b9):
        for b17 in range(b9):
            for b16 in range(b9):
                b8[b17][b16] = min(b8[b17][b16], b8[b17][k] + b8[k][b16])
    return b8
def fonk3(b4, a3):
    b10 = len(b4[0]) % a3
    if b10 = = 0:
        return b4
    else:
        b11 = a3 - b10
    b12 = len(b4[0]) + b11
    for b17 in range(len(b4)):
        b4[b17].extend([a1] * b11)
    b4.extend([[a1] * b12 for _ in range(b11)])
    assert len(b4) == b12
    assert len(b4[0]) == b12
    return b4
def fonk4(a_row, a_col, b_row, b_col, c_row, c_col, b4, a5, b13 = False):
    for k in range(a5):
        for b17 in range(a5):
            for b16 in range(a5):
                b4[a_row + b17][a_col + b16] = min(b4[a_row + b17][a_col + b16],
                                                   b4[b_row + b17][b_col + k] + b4[c_row + k][c_col + b16])
                if b13:
                    print("Ai, Aj", a_row + b17, a_col + b16, "Bi, Bk", b_row+b17, b_col+k, "Ck, Cj", c_row+k, c_col+b16)
    return b4
def fonk5(b4, a3):
    b4 = fonk3(b4, a3)
    b14 = len(b4)
    b15 = len(b4)
    for d in range(b14):
        fonk4(d * b15, d * b15, d * b15, d * b15, d * b15, d * b15, b4, a3)
        for b16 in range(b14):
            if b16 = = d:
                continue
            fonk4(d * b15, b16 * b15,
                             d * b15, d * b15,
                             d * b15, b16 * b15,
                             b4, a3)
        for b17 in range(b14):
            if b17 = = d:
                continue
            fonk4(b17 * b15, d * b15,
                             b17 * b15, d * b15,
                             d * b15, d * b15,
                             b4, a3)
        for b17 in range(b14):
            for b16 in range(b14):
                if b17 = = d or b16 == d:
                    continue
                fonk4(b17 * b15, b16 * b15,
                                 b17 * b15, d * b15,
                                 d * b15, b16 * b15,
                                 b4, a3)
    return b4
def fonk6(b9, tile, b13 = False):
    b18 = fonk1(b9)
    print("Running Naive Floyd-Warshall on b9 x b9, b9 = ", b9)
    b19 = timeit.default_timer()
    b20 = fonk2(b18)
    b21 = timeit.default_timer() - b19
    print("Finished, took", b21, "seconds")
    print("Running Tiled Floyd-Warshall on same b9 x b9 b4, b9 = ", b9, ", a3 =", tile)
    b19 = timeit.default_timer()
    b22 = fonk5(b18, tile)
    b21 = timeit.default_timer() - b19
    print("Finished, took", b21, "seconds")
    print("Correctness Info:")
    for b17 in range(b9):
        for b16 in range(b9):
            if b20[b17][b16] != b22[b17][b16]:
                print("Error, elements (", b17, ",", b16, ") differ")
                if b13:
                    print("Dumping distance naive:")
                    pprint(b20)
                    print("Dumping distance tiled:")
                    pprint(b22)
                return False
    print("Correctness Check Passed!!")
    if b13:
        print("Dumping distance naive:")
        pprint(b20)
        print("Dumping distance tiled:")
        pprint(b22)
    return True
def fonk7():
    global a2
    global a3
    global b1
    b23 = [
        [0, a1, -2, a1],
        [4, 0, 3, a1],
        [a1, a1, 0, 2],
        [a1, -1, a1, 0]
    ]
    a5 = 2
    print("****WIKI MATRIX TESTING****")
    fonk3(b23, a5)
    print("Initial Matrix:")
    pprint(b23)
    print("Solved with normal Floyd-Warshall:")
    pprint(fonk2(b23))
    print("Solved with tiled:")
    pprint(fonk5(b23, a5))
    print("****RANDOMLY GENERATED MATRIX****")
    b24 = fonk6(a2, a3, b13=b1)
if b25 = = '__main__':
    fonk7()