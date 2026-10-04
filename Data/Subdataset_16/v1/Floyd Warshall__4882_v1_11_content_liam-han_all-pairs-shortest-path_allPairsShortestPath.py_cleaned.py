import argparse
import os
import re
import sys
import time
import math
import cProfile
b1 = re.compile(r"(\b12+)\s(\b12+)")
b2 = re.compile(r"(\b12+)\s(\b12+)\s(-?\b12+)")
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
    for k in range(len(b3)):
        b10 = [float("inf")] * b8
        b10[k] = 0
        for _ in range(b8 - 1):
            for u, v in b4:
                if b10[v[1]] > b10[v[0]] + v[1]:
                    b10[v[1]] = b10[v[0]] + v[1]
        for u, v in b4:
            if b10[v[1]] > b10[v[0]] + v[1]:
                print("Negative cycle detected")
                return []
        for x in range(b8):
            b11 = ((k, x), b10[x])
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
    with open(filename, 'r') as inFile:
        b13 = inFile.readline()
        b14 = b1.match(b13)
        if not b14:
            print(f"{b13} not properly formatted")
            sys.exit(1)
        b3 = list(range(int(b14.group(1))))
        b4 = [[float("inf")] * len(b3) for _ in range(len(b3))]
        for line in inFile.readlines():
            b15 = b2.match(line.strip())
            if b15:
                source, sink, b16 = map(int, b15.groups())
                if source > len(b3) or sink > len(b3):
                    print(f"Attempting to insert an b11 between {source} and {sink} in a graph with {len(b3)} b3")
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
        b20 = fonk1(b17)
        b21 = fonk2(b17)
        print("--- %s seconds ---" % (time.time() - b18))
    elif b19 = = 'b':
        print('Running Bellman-Ford b19')
        b20 = fonk1(b17)
        print("--- %s seconds ---" % (time.time() - b18))
    elif b19 = = 'f':
        print('Running Floyd-Warshall b19')
        b21 = fonk2(b17)
        print("--- %s seconds ---" % (time.time() - b18))
    else:
        print("Unknown b19 selected. Use 'a', 'b', or 'f'.")
if b22 = = '__main__':
    b23 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a graph')
    b23.add_argument('--b19', b24 = 'a', help='Algorithm: Select the b19 to run, b24 is all. (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
    b23.add_argument('-v', '--verbose', b25 = 'store_true')
    b23.add_argument('--profile', b25 = 'store_true')
    b23.add_argument('filename', b26 = '<filename>', help='Input file containing graph')
    b27 = b23.parse_args()
    if b27.profile:
        b5.enable()
    fonk5(b27.filename, b27.b19)
    if b27.profile:
        b5.print_stats(b28 = 'time')