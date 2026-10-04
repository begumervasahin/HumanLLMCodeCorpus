import random
import timeit
from pprint import pprint
from copy import deepcopy
a1 = 100000000
a2 = 9
a3 = 3
b1 = True
def fonk1(dim, b2 = 0.5):
    b3 = [[0] * dim for _ in range(dim)]
    b4 = -1 if b1 else 1
    for _ in range(int(b2 * (dim ** 2))):
        b5 = random.randint(0, dim - 1)
        b6 = random.randint(0, dim - 1)
        if b5 != b6:
            b7 = random.randint(b4, 20)
            b3[b5][b6] = b7
    for i in range(dim):
        for j in range(dim):
            if i != j and b3[i][j] == 0:
                b3[i][j] = a1
    return b3
def fonk2(graph):
    b8 = deepcopy(graph)
    a2 = len(graph)
    for k in range(a2):
        for i in range(a2):
            for j in range(a2):
                b8[i][j] = min(b8[i][j], b8[i][k] + b8[k][j])
    return b8
def fonk3(b3, tile_size):
    b9 = tile_size - (len(b3) % tile_size)
    b10 = len(b3) + b9
    for row in b3:
        row.extend([a1] * b9)
    for _ in range(b9):
        b3.append([a1] * b10)
    return b3
def fonk4(a_row, a_col, b_row, b_col, c_row, c_col, b3, a4, b11 = False):
    for k in range(a4):
        for i in range(a4):
            for j in range(a4):
                b3[a_row + i][a_col + j] = min(
                    b3[a_row + i][a_col + j],
                    b3[b_row + i][b_col + k] + b3[c_row + k][c_col + j]
                )
                if b11:
                    print(f"Ai, Aj ({a_row + i}, {a_col + j}) Bi, Bk ({b_row + i}, {b_col + k}) Ck, Cj ({c_row + k}, {c_col + j})")
    return b3
def fonk5(b3, tile_size):
    b3 = fonk3(b3, tile_size)
    b12 = len(b3)
    for d in range(b12):
        fonk4(d*tile_size, d*tile_size, d*tile_size, d*tile_size, d*tile_size, d*tile_size, b3, tile_size)
        for j in range(b12):
            if j != d:
                fonk4(d*tile_size, j*tile_size, d*tile_size, d*tile_size, d*tile_size, j*tile_size, b3, tile_size)
        for i in range(b12):
            if i != d:
                fonk4(i*tile_size, d*tile_size, i*tile_size, d*tile_size, d*tile_size, d*tile_size, b3, tile_size)
        for i in range(b12):
            for j in range(b12):
                if i != d and j != d:
                    fonk4(i*tile_size, j*tile_size, i*tile_size, d*tile_size, d*tile_size, j*tile_size, b3, tile_size)
    return b3
def fonk6(b14, tile, b11 = False):
    b13 = fonk1(b14)
    print(f"Running Naive FW on {b14} x {b14}, b14 = {b14}")
    b15 = timeit.default_timer()
    b16 = fonk2(b13)
    b17 = timeit.default_timer() - b15
    print(f"Finished, took {b17} seconds")
    print(f"Running Tiled FW on same {b14} x {b14} b3, b14 = {b14}, tile_size = {tile}")
    b15 = timeit.default_timer()
    b18 = fonk5(b13, tile)
    b17 = timeit.default_timer() - b15
    print(f"Finished, took {b17} seconds")
    print("Correctness Info:")
    for i in range(b14):
        for j in range(b14):
            if b16[i][j] != b18[i][j]:
                print(f"Error, elements ({i}, {j}) differ")
                if b11:
                    print("Dumping distance naive:")
                    pprint(b16)
                    print("Dumping distance tiled:")
                    pprint(b18)
                return False
    print("Correctness Check Passed!!")
    if b11:
        print("Dumping distance naive:")
        pprint(b16)
        print("Dumping distance tiled:")
        pprint(b18)
    return True
def fonk7():
    b19 = [
        [0, a1, -2, a1],
        [4, 0, 3, a1],
        [a1, a1, 0, 2],
        [a1, -1, a1, 0]
    ]
    a4 = 2
    print("****WIKI MATRIX TESTING****")
    b20 = fonk3(b19, a4)
    print("Initial Matrix:")
    pprint(b20)
    print("Solved with normal FW:")
    pprint(fonk2(b20))
    print("Solved with tiled FW:")
    pprint(fonk5(b20, a4))
    print("****RAND GENERATED MATRIX****")
    b21 = fonk6(a2, a3)
    print(f"Test status: {'Passed' if b21 else 'Failed'}")
if b22 = = '__main__':
    fonk7()