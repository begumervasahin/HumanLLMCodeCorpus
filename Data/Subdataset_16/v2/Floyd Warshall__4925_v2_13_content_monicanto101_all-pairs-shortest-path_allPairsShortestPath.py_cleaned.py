import argparse
import os
import re
import sys
import cProfile
import pstats
import io
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b8 in a graph')
b1.add_argument('--algorithm', b2 = 'a',
                    b3 = 'Algorithm: Select the algorithm to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b4 = 'store_true')
b1.add_argument('--profile', b4 = 'store_true')
b1.add_argument('filename', b5 = '<filename>', b3='Input file containing graph')
b6 = re.compile(r"(\d+)\b20(\d+)")
b7 = re.compile(r"(\d+)\b20(\d+)\b20(-?\d+)")
b8 = []
b9 = []
def fonk1():
    b10 = []
    b11 = len(b8)
    for j in b8:
        b12 = [float("inf")] * b11
        b12[j] = 0
        for _ in range(b11 - 1):
            for V in range(b11):
                for U in range(b11):
                    b13 = float(b9[V][U])
                    if b12[V] != float("inf") and b12[V] + b13 < b12[U]:
                        b12[U] = b12[V] + b13
        b10.append(b12)
    for j in b8:
        if b10[j][j] < 0:
            return [[0, 0]]
    return b10
def fonk2():
    b11 = len(b8)
    b12 = [[float("inf")] * b11 for _ in range(b11)]
    for V in range(b11):
        for U in range(b11):
            b12[U][V] = float(b9[U][V])
        b12[V][V] = 0
    for k in range(b11):
        for i in range(b11):
            for j in range(b11):
                if b12[i][j] > b12[i][k] + b12[k][j]:
                    b12[i][j] = b12[i][k] + b12[k][j]
    for j in b8:
        if b12[j][j] < 0:
            return [[0, 0]]
    return b12
def fonk3(filename):
    global b8, b9
    with open(filename, 'r') as infile:
        b14 = infile.readline().strip()
        b15 = b6.match(b14)
        if not b15:
            print(f"{b14} not properly formatted")
            sys.exit(1)
        b11 = int(b15.group(1))
        b8 = list(range(b11))
        b9 = [[float("inf")] * b11 for _ in range(b11)]
        for b16 in infile:
            b16 = b16.strip()
            b17 = b7.match(b16)
            if b17:
                source, sink, b13 = int(b17.group(1)), int(b17.group(2)), float(b17.group(3))
                if source > b11 or sink > b11:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {b11} b8")
                    sys.exit(1)
                b9[source - 1][sink - 1] = b13
    return b8, b9
def fonk4(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(func, *b26):
    b18 = cProfile.Profile()
    b18.enable()
    b19 = func(*b26)
    b18.disable()
    b20 = io.StringIO()
    b21 = 'cumulative'
    b22 = pstats.Stats(b18, stream=b20).sort_stats(b21)
    b22.print_stats()
    print(b20.getvalue())
    return b19
def fonk6(filename, algorithm):
    fonk3(filename)
    b10 = []
    if algorithm.lower() == 'b':
        if b26.profile:
            b10 = fonk5(bellman_ford)
        else:
            b10 = fonk1()
    elif algorithm.lower() == 'f':
        if b26.profile:
            b10 = fonk5(floyd_warshall)
        else:
            b10 = fonk2()
    elif algorithm.lower() == 'a':
        print('Running both algorithms')
        if b26.profile:
            b23 = fonk5(bellman_ford)
            b24 = fonk5(floyd_warshall)
        else:
            b23 = fonk1()
            b24 = fonk2()
        if not fonk4(b23, b24):
            print('Floyd-Warshall and Bellman-Ford did not produce the same b19')
        b10 = b23
    with open(os.path.splitext(filename)[0] + '_shortestPaths.txt', 'w') as f:
        for row in b10:
            f.write(' '.join(map(str, row)) + '\n')
if b25 = = '__main__':
    b26 = b1.parse_args()
    fonk6(b26.filename, b26.algorithm)