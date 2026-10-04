import argparse
import os
import re
import sys
import cProfile
import pstats
import io
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b8 in a graph')
b1.add_argument('--algorithm', b2 = 'a', choices=['a', 'b', 'f'],
                    b3 = 'Algorithm: Select the algorithm to run, b2 is all. (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b4 = 'store_true')
b1.add_argument('--profile', b4 = 'store_true')
b1.add_argument('filename', b5 = '<filename>', b3='Input file containing graph')
b6 = re.compile(r"(\d+)\b20(\d+)")
b7 = re.compile(r"(\d+)\b20(\d+)\b20(-?\d+)")
b8 = []
b9 = []
def fonk1():
    b10 = len(b8)
    b11 = []
    for src in b8:
        b12 = [float("inf")] * b10
        b12[src] = 0
        for _ in range(b10 - 1):
            for u in range(b10):
                for v in range(b10):
                    b13 = float(b9[u][v])
                    if b12[u] != float("inf") and b12[u] + b13 < b12[v]:
                        b12[v] = b12[u] + b13
        b11.append(b12)
    for src in b8:
        if b11[src][src] < 0:
            return [[0, 0]]
    return b11
def fonk2():
    b10 = len(b8)
    b12 = [[float("inf")] * b10 for _ in range(b10)]
    for u in range(b10):
        for v in range(b10):
            b12[u][v] = float(b9[u][v])
        b12[u][u] = 0
    for k in range(b10):
        for i in range(b10):
            for j in range(b10):
                if b12[i][j] > b12[i][k] + b12[k][j]:
                    b12[i][j] = b12[i][k] + b12[k][j]
    for src in b8:
        if b12[src][src] < 0:
            return [[0, 0]]
    return b12
def fonk3(filename):
    global b8, b9
    with open(filename, 'r') as infile:
        b14 = infile.readline().strip()
        b15 = b6.match(b14)
        if not b15:
            print(f"Error: {b14} not properly formatted")
            sys.exit(1)
        b10 = int(b15.group(1))
        b8 = list(range(b10))
        b9 = [[float("inf")] * b10 for _ in range(b10)]
        for b16 in infile:
            b16 = b16.strip()
            b17 = b7.match(b16)
            if b17:
                source, sink, b13 = map(int, b17.groups())
                if source > b10 or sink > b10:
                    print(f"Error: Attempting to insert an edge between {source} and {sink} in a graph with {b10} b8")
                    sys.exit(1)
                b9[source - 1][sink - 1] = b13
def fonk4(a, b):
    if len(a) != len(b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(a, b)):
        return False
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[i])))
def fonk5(func, *b26):
    b18 = cProfile.Profile()
    b18.enable()
    b19 = func(*b26)
    b18.disable()
    b20 = io.StringIO()
    b21 = pstats.Stats(b18, stream=b20).sort_stats('cumulative')
    b21.print_stats()
    print(b20.getvalue())
    return b19
def fonk6(filename, algorithm):
    fonk3(filename)
    b11 = []
    if algorithm.lower() == 'b':
        b11 = fonk5(bellman_ford) if b26.profile else fonk1()
    elif algorithm.lower() == 'f':
        b11 = fonk5(floyd_warshall) if b26.profile else fonk2()
    elif algorithm.lower() == 'a':
        print('Running both algorithms')
        b22 = fonk5(bellman_ford) if b26.profile else fonk1()
        b23 = fonk5(floyd_warshall) if b26.profile else fonk2()
        if not fonk4(b22, b23):
            print('Error: Floyd-Warshall and Bellman-Ford did not produce the same b19')
        b11 = b22
    b24 = os.path.splitext(filename)[0] + '_shortestPaths.txt'
    with open(b24, 'w') as f:
        for row in b11:
            f.write(' '.join(map(str, row)) + '\n')
if b25 = = '__main__':
    b26 = b1.parse_args()
    fonk6(b26.filename, b26.algorithm)