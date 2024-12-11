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
                    b11 = float(graph[1][u][v])
                    if b10[v] > b10[u] + b11:
                        b10[v] = b10[u] + b11
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
        b12 = file.readline()
        b13 = b5.match(b12)
        if not b13:
            print(f"First b15 of {filename} is not properly formatted")
            sys.exit(1)
        b14 = int(b13.group(1))
        b7 = list(range(b14))
        b8 = [[float("inf")] * b14 for _ in range(b14)]
        for b15 in file.readlines():
            b15 = b15.strip()
            b16 = b6.match(b15)
            if b16:
                source, sink, b17 = map(int, b16.groups())
                if source > b14 or sink > b14:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {b14} b7")
                    sys.exit(1)
                b8[source - 1][sink - 1] = b17
    return b7, b8
def fonk4(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, algorithm):
    b7, b8 = fonk3(filename)
    b9 = []
    b18 = True
    if algorithm.lower() == 'b':
        b19 = timeit.default_timer()
        b9, b18 = fonk1((b7, b8))
        b20 = timeit.default_timer()
        print(b20 - b19)
    elif algorithm.lower() == 'f':
        b19 = timeit.default_timer()
        b9 = fonk2((b7, b8))
        b20 = timeit.default_timer()
        print(b20 - b19)
    elif algorithm.lower() == 'a':
        print('Running both')
        path_pairs_bellman, b21 = fonk1((b7, b8))
        b22 = fonk2((b7, b8))
        b9 = path_pairs_bellman
        b18 = b21
        if not fonk4(path_pairs_bellman, b22) or not b18:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result or negative cycle detected')
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt', 'w') as f:
        if not b18:
            f.write("Negative Cycle Detected \n")
        for row in b9:
            f.write(' '.join(map(str, row)) + '\n')
if b23 = = '__main__':
    b24 = b1.parse_args()
    fonk5(b24.filename, b24.algorithm)