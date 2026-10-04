import os
import re
import sys
import time
import math
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def fonk1(b3):
    for v in range(len(b3)):
        for e in range(len(b3[v])):
            if isinstance(b3[v][e], str):
                b3[v][e] = int(b3[v][e])
    return b3
def fonk2(b19):
    b10, b3 = b19
    b4 = []
    b5 = float('inf')
    b3 = fonk1(b3)
    for src in range(len(b10)):
        b6 = [b5] * len(b10)
        b6[src] = 0
        for _ in range(len(b10) - 1):
            for u in range(len(b10)):
                for v in range(len(b10)):
                    if b3[u][v] != b5 and b6[u] != b5:
                        if b6[v] > b6[u] + b3[u][v]:
                            b6[v] = b6[u] + b3[u][v]
        b4.append(b6)
    return b4
def fonk3(b19):
    b10, b3 = b19
    b6 = fonk1(b3)
    b7 = len(b10)
    for i in range(b7):
        b6[i][i] = 0
    for k in range(b7):
        for i in range(b7):
            for j in range(b7):
                if b6[i][j] > b6[i][k] + b6[k][j]:
                    b6[i][j] = b6[i][k] + b6[k][j]
    return b6
def fonk4(filename):
    with open(filename, 'r') as file:
        b8 = file.readline().strip()
        b9 = b1.match(b8)
        if not b9:
            print(f"{b8} not properly formatted")
            sys.exit(1)
        b7 = int(b9.group(1))
        b10 = list(range(b7))
        b3 = [[float('inf')] * b7 for _ in range(b7)]
        for b11 in file:
            b11 = b11.strip()
            b12 = b2.match(b11)
            if b12:
                b13 = int(b12.group(1))
                b14 = int(b12.group(2))
                b15 = int(b12.group(3))
                if b13 >= b7 or b14 >= b7:
                    print(f"Attempting to insert an edge between {b13} and {b14} in a b19 with {b7} b10")
                    sys.exit(1)
                b3[b13][b14] = b15
    return b10, b3
def fonk5(length_matrix, filename):
    b16 = os.path.splitext(os.path.basename(filename))[0]
    b17 = f'output/{b16}_output.txt'
    os.makedirs(os.path.dirname(b17), b18 = True)
    with open(b17, 'w') as out_file:
        for row in length_matrix:
            out_file.write(','.join(map(str, row)) + '\n')
def fonk6(filename, algorithm):
    b19 = fonk4(filename)
    b20 = []
    if algorithm.lower() == 'b':
        b21 = time.time()
        b20 = fonk2(b19)
        b22 = time.time()
        print(f"Bellman-Ford timing: {b22 - b21:.6f} seconds")
    elif algorithm.lower() == 'f':
        b21 = time.time()
        b20 = fonk3(b19)
        b22 = time.time()
        print(f"Floyd-Warshall timing: {b22 - b21:.6f} seconds")
    elif algorithm.lower() == 'both':
        b21 = time.time()
        fonk2(b19)
        b23 = time.time() - b21
        b21 = time.time()
        fonk3(b19)
        b24 = time.time() - b21
        print(f"Bellman-Ford timing: {b23:.6f} seconds")
        print(f"Floyd-Warshall timing: {b24:.6f} seconds")
    fonk5(b20, filename)
if b25 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b|both> <input_file>")
        sys.exit(1)
    fonk6(sys.argv[2], sys.argv[1])