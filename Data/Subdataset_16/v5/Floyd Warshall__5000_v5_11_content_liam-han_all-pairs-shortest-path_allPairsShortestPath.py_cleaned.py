import argparse
import re
import sys
import time
import math
import cProfile
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
b5 = cProfile.Profile()
def fonk1(b15):
    b3, b6 = b15
    b7 = []
    b4 = []
    b8 = len(b3)
    for i in range(b8):
        for j in range(b8):
            if not math.isinf(float(b6[i][j])):
                b4.append(((i, j), float(b6[i][j])))
    for src in range(b8):
        b9 = [float("inf")] * b8
        b9[src] = 0
        for _ in range(b8 - 1):
            for (u, v), b14 in b4:
                if b9[v] > b9[u] + b14:
                    b9[v] = b9[u] + b14
        for (u, v), b14 in b4:
            if b9[v] > b9[u] + b14:
                print("Negative cycle detected")
                return []
        for dest in range(b8):
            b7.append(((src, dest), b9[dest]))
    print(b7)
    return b7
def fonk2(b15):
    b3, b6 = b15
    b7 = []
    b8 = len(b3)
    b10 = [row[:] for row in b6]
    for i in range(b8):
        b10[i][i] = 0
    for k in range(b8):
        for i in range(b8):
            for j in range(b8):
                if b10[i][j] > b10[i][k] + b10[k][j]:
                    b10[i][j] = b10[i][k] + b10[k][j]
    for i in range(b8):
        if b10[i][i] < 0:
            print("Negative cycle detected")
            return []
    for i in range(b8):
        for j in range(b8):
            b7.append(((i, j), b10[i][j]))
    print(b7)
    return b7
def fonk3(filename):
    global b3
    global b4
    with open(filename, 'r') as infile:
        b11 = infile.readline()
        b12 = b1.match(b11)
        if not b12:
            print(f"{b11} not properly formatted")
            sys.exit(1)
        b8 = int(b12.group(1))
        b3 = list(range(b8))
        b4 = [[float("inf")] * b8 for _ in range(b8)]
        for line in infile.readlines():
            b13 = b2.match(line.strip())
            if b13:
                source, sink, b14 = map(int, b13.groups())
                if source > b8 or sink > b8:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b15 with {b8} b3")
                    sys.exit(1)
                b4[source - 1][sink - 1] = b14
    return b3, b4
def fonk4(a, b):
    if len(a) != len(b) or not a or not b:
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != b[i][j]:
                return False
    return True
def fonk5(filename, b17):
    b15 = fonk3(filename)
    b16 = time.time()
    if b17 = = 'a':
        print('Running both Bellman-Ford and Floyd-Warshall algorithms')
        fonk1(b15)
        fonk2(b15)
    elif b17 = = 'b':
        print('Running Bellman-Ford b17')
        fonk1(b15)
    elif b17 = = 'f':
        print('Running Floyd-Warshall b17')
        fonk2(b15)
    else:
        print("Unknown b17 selected. Use 'a', 'b', or 'f'.")
    print(f"--- {time.time() - b16} seconds ---")
if b18 = = '__main__':
    b19 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a b15')
    b19.add_argument('--b17', b20 = 'a', help='Algorithm: Select the b17 to run, b20 is all. (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
    b19.add_argument('-v', '--verbose', b21 = 'store_true')
    b19.add_argument('--profile', b21 = 'store_true')
    b19.add_argument('filename', b22 = '<filename>', help='Input file containing b15')
    b23 = b19.parse_args()
    if b23.profile:
        b5.enable()
    fonk5(b23.filename, b23.b17)
    if b23.profile:
        b5.print_stats(b24 = 'time')