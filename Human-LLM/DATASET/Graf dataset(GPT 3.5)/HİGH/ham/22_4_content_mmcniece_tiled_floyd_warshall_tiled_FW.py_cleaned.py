import random
import timeit
from pprint import pprint
from copy import deepcopy
import click
a1 = 100000000
a2 = 9
a3 = 3
b1 = False
b2 = True
def fonk1(dim, b3 = .5):
    global b2
    b4 = []
    if b2:
        a4 = -1
    else:
        a4 = 1
    for b6 in range(0, dim):
        b4.append([0] * dim)
    a5 = 0
    a6 = 0
    for b6 in range(0, int(b3 * (dim**2))):
        a5 = random.randint(0, dim-1)
        a6 = random.randint(0, dim-1)
        if(a6 = = a5):
            pass
        else:
            b5 = random.randint(a4, 20)
            b4[a5][a6] = b5
    for b6 in range(0, dim):
        for b14 in range(0, dim):
            if(b6 = = b14):
                pass
            elif(b4[b6][b14] != 0):
                pass
            else:
                b4[b6][b14] = a1
    return b4
def fonk2(graph):
    b7 = [deepcopy(b6) for b6 in graph]
    a2 = len(graph[0])
    for k in range(a2):
        for b6 in range(a2):
            for b14 in range(a2):
                b7[b6][b14] = min(b7[b6][b14], b7[b6][k]+ b7[k][b14])
    return b7
def fonk3(b4, a3):
    b8 = (len(b4[0]) % a3)
    if b8 = = 0:
        return b4
    else:
        b9 = a3 - b8
    b10 = len(b4[0]) + b9
    for b6 in range(len(b4)):
        for b14 in range(b9):
            b4[b6].append(a1)
    for b6 in range(b9):
        b4.append([a1 for b6 in range(b10)])
    assert len(b4) == b10
    assert len(b4[0]) == b10
    return b4
def fonk4(a_row, a_col, b_row, b_col, c_row, c_col, b4, a7, b11 = False):
    for k in range(0, a7):
        for b6 in range(0, a7):
            for b14 in range(0, a7):
                b4[a_row + b6][a_col + b14] = min(b4[a_row + b6][a_col + b14],
                                                   b4[b_row + b6][b_col + k] + b4[c_row + k][c_col + b14])
                if b11:
                    print("Ai, Aj", a_row + b6, a_col + b14, "Bi, Bk", b_row+b6, b_col+k, "Ck, Cj", c_row+k, c_col+b14)
    return b4
def fonk5(b4, a3):
    b4 = fonk3(b4, a3)
    b12 = int(len(b4)/a3)
    b13 = int(len(b4)/b12)
    for d in range(b12):
        fonk4(d*b13, d*b13, d*b13, d*b13, d*b13, d*b13, b4, a3)
        for b14 in range(b12):
            if b14 = = d:
                pass
            else:
                fonk4(d*b13, b14*b13,
                                d*b13, d*b13,
                                d*b13, b14*b13,
                                b4, a3)
        for b6 in range(b12):
            if b6 = = d:
                pass
            else:
                fonk4(b6*b13, d*b13,
                                b6*b13, d*b13,
                                d*b13, d*b13,
                                b4, a3)
        for b6 in range(b12):
            for b14 in range(b12):
                if b6 = = d or b14 == d:
                    pass
                else:
                    fonk4(b6*b13, b14*b13,
                                    b6*b13, d*b13,
                                    d*b13, b14*b13,
                                    b4, a3)
    return b4
def fonk6(b16, tile, b11 = False):
    b15 = fonk1(b16)
    print("Running Naieve FW on b16 x b16, b16 = %s" % b16)
    b17 = timeit.default_timer()
    b18 = fonk2(b15)
    b19 = timeit.default_timer() - b17
    print("Finished, took %s seconds" % b19)
    print("Running Tiled FW on same b16 x b16 b4, b16 = %s, a3 = %s" % (b16, tile))
    b17 = timeit.default_timer()
    b20 = fonk5(b15, tile)
    b19 = timeit.default_timer() - b17
    print("Finished, took %s seconds" % b19)
    print("Correctness Info:")
    for b6 in range(b16):
        for b14 in range(b16):
            if b18[b6][b14] != b20[b6][b14]:
                print("Error, elements (%s, %s) differ" % (b6, b14))
                if b11:
                    print("Dumping distance naieve:")
                    pprint(b18)
                    print("Dumping distance tiled:")
                    pprint(b20)
                return False
    print("Correctness Check Passed!!")
    if b11:
        print("Dumping distance naieve:")
        pprint(b18)
        print("Dumping distance tiled:")
        pprint(b20)
    return True
def fonk7():
    global a2
    global a3
    global b1
    b21 = [
    [0, a1, -2, a1],
    [4, 0, 3, a1],
    [a1, a1, 0, 2],
    [a1, -1, a1, 0]
    ]
    a7 = 2
    print("****WIKI MATRIX TESTING****")
    fonk3(b21, a7)
    print("Initial Matrix:")
    pprint(b21)
    print("Solved with normal FW:")
    pprint(fonk2(b21))
    print("Solved with tiled:")
    pprint(fonk5(b21, a7))
    print("****RAND GENERATED MATRIX****")
    b22 = fonk6(a2, a3, b11=b1)
if b23 = = '__main__':
    fonk7()