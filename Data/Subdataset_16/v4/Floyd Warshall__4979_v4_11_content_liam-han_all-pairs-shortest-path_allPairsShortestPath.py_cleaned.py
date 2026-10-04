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
def fonk1(b17):
    b3, b6 = b17
    b7 = []
    b4 = []
    b8 = len(b3)
    for i in range(b8):
        for j in range(b8):
            if not math.isinf(float(b6[i][j])):
                b9 = [(i, j), float(b6[i][j])]
                b4.append(b9)
    for src in range(b8):
        b10 = [float("inf")] * b8
        b10[src] = 0
        for _ in range(b8 - 1):
            for (u, v), b16 in b4:
                if b10[v] > b10[u] + b16:
                    b10[v] = b10[u] + b16
        for (u, v), b16 in b4:
            if b10[v] > b10[u] + b16:
                print("Negative cycle detected")
                return []
        for dest in range(b8):
            b11 = ((src, dest), b10[dest])
            b7.append(b11)
    print(b7)
    return b7
def fonk2(b17):
    b3, b6 = b17
    b7 = []
    b8 = len(b3)
    b12 = [row[:] for row in b6]
    for i in range(b8):
        b12[i][i] = 0
    for k in range(b8):
        for i in range(b8):
            for j in range(b8):
                if b12[i][j] > b12[i][k] + b12[k][j]:
                    b12[i][j] = b12[i][k] + b12[k][j]
    for i in range(b8):
        if b12[i][i] < 0:
            print("Negative cycle detected")
            return []
    for i in range(b8):
        for j in range(b8):
            b11 = ((i, j), b12[i][j])
            b7.append(b11)
    print(b7)
    return b7
def fonk3(filename):
    global b3
    global b4
    with open(filename, 'r') as infile:
        b13 = infile.readline()
        b14 = b1.match(b13)
        if not b14:
            print(f"{b13} not properly formatted")
            sys.exit(1)
        b8 = int(b14.group(1))
        b3 = list(range(b8))
        b4 = [[float("inf")] * b8 for _ in range(b8)]
        for line in infile.readlines():
            b15 = b2.match(line.strip())
            if b15:
                source, sink, b16 = map(int, b15.groups())
                if source > b8 or sink > b8:
                    print(f"Attempting to insert an b11 between {source} and {sink} in a b17 with {b8} b3")
                    sys.exit(1)
                b4[source - 1][sink - 1] = b16
    return b3, b4
def fonk4(a, b):
    if len(a) != len(b) or not a or not b:
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != b[i][j]:
                return False
    return True
def fonk5(filename, b19):
    b17 = fonk3(filename)
    b18 = time.time()
    if b19 = = 'a':
        print('Running both Bellman-Ford and Floyd-Warshall algorithms')
        fonk1(b17)
        fonk2(b17)
    elif b19 = = 'b':
        print('Running Bellman-Ford b19')
        fonk1(b17)
    elif b19 = = 'f':
        print('Running Floyd-Warshall b19')
        fonk2(b17)
    else:
        print("Unknown b19 selected. Use 'a', 'b', or 'f'.")
    print("--- %s seconds ---" % (time.time() - b18))
if b20 = = '__main__':
    b21 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a b17')
    b21.add_argument('--b19', b22 = 'a', help='Algorithm: Select the b19 to run, b22 is all. (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
    b21.add_argument('-v', '--verbose', b23 = 'store_true')
    b21.add_argument('--profile', b23 = 'store_true')
    b21.add_argument('filename', b24 = '<filename>', help='Input file containing b17')
    b25 = b21.parse_args()
    if b25.profile:
        b5.enable()
    fonk5(b25.filename, b25.b19)
    if b25.profile:
        b5.print_stats(b26 = 'time')