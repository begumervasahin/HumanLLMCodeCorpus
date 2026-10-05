import argparse
import os
import re
import sys
import time
import timeit
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b7 in a graph')
b1.add_argument('--algorithm', b2 = 'a', help='Algorithm: Select the algorithm to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b3 = 'store_true')
b1.add_argument('--profile', b3 = 'store_true')
b1.add_argument('filename', b4 = '<filename>', help='Input file containing graph')
b5 = re.compile(r"(\d+)\s(\d+)")
b6 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b7 = []
b8 = []
def fonk1(graph):
    b9 = []
    for source in range(len(graph[0])):
        b10 = [float("inf")] * len(graph[0])
        b10[source] = 0.0
        for _ in range(len(graph[0]) - 1):
            for u in range(len(graph[0])):
                for v in range(len(graph[1])):
                    if b10[v] > b10[u] + float(graph[1][u][v]):
                        b10[v] = b10[u] + float(graph[1][u][v])
        for u in range(len(graph[0])):
            for v in range(len(graph[1])):
                if b10[v] > b10[u] + float(graph[1][u][v]):
                    return (b9, False)
        b9.append(b10)
    return (b9, True)
def fonk2(graph):
    b9 = []
    b10 = [[float("inf")] * len(graph[0]) for _ in range(len(graph[0]))]
    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
            b10[i][j] = float(graph[1][i][j])
    for k in range(len(graph[0])):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                b10[i][j] = min(b10[i][j], b10[i][k] + b10[k][j])
    return b10
def fonk3(filename):
    global b7
    global b8
    with open(filename, 'r') as file:
        b11 = file.readline()
        b12 = b5.match(b11)
        if not b12:
            print(f"First b13 of {filename} is not properly formatted")
            sys.exit(1)
        b7 = list(range(int(b12.group(1))))
        b8 = [[float("inf")] * len(b7) for _ in range(len(b7))]
        for b13 in file.readlines():
            b13 = b13.strip()
            b14 = b6.match(b13)
            if b14:
                source, sink, b15 = map(int, b14.groups())
                if source > len(b7) or sink > len(b7):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(b7)} b7")
                    sys.exit(1)
                b8[source - 1][sink - 1] = b15
    return b7, b8
def fonk4(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b):
        return False
    if len(a[0]) != len(b[0]):
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, algorithm):
    b7, b8 = fonk3(filename)
    b9 = []
    b16 = True
    if algorithm.lower() == 'b':
        b17 = timeit.default_timer()
        b9, b16 = fonk1((b7, b8))
        b18 = timeit.default_timer()
        print(b18 - b17)
    elif algorithm.lower() == 'f':
        b17 = timeit.default_timer()
        b9 = fonk2((b7, b8))
        b18 = timeit.default_timer()
        print(b18 - b17)
    elif algorithm.lower() == 'a':
        print('Running both')
        path_pairs_bellman, b19 = fonk1((b7, b8))
        b20 = fonk2((b7, b8))
        b9 = path_pairs_bellman
        b16 = b19
        if not fonk4(path_pairs_bellman, b20) or not b16:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result or negative cycle detected')
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt', 'w') as f:
        if not b16:
            f.write("Negative Cycle Detected \n")
        for row in b9:
            for b15 in row:
                f.write(str(b15)+' ')
            f.write('\n')
if b21 = = '__main__':
    b22 = b1.parse_args()
    fonk5(b22.filename, b22.algorithm)