import argparse
import os
import re
import cProfile
import pstats
import io
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b7 in a graph')
b1.add_argument('--algorithm', b2 = 'a', help='Algorithm: Select the algorithm to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b3 = 'store_true')
b1.add_argument('--profile', b3 = 'store_true')
b1.add_argument('filename', b4 = '<filename>', help='Input file containing graph')
b5 = re.compile(r"(\d+)\b22(\d+)")
b6 = re.compile(r"(\d+)\b22(\d+)\b22(-?\d+)")
b7 = []
b8 = []
def fonk1(b20):
    b9 = []
    b10 = len(b7)
    for j in b7:
        b11 = [float("inf")] * b10
        b11[j] = 0
        for _ in range(0, len(b7) - 1):
            for V in range(0, len(b7)):
                for U in range(0, len(b8)):
                    b12 = float(b8[V][U])
                    b13 = b11[V] + b12
                    if b13 < b11[U]:
                        b11[U] = b13
        b9.append(b11)
    for j in b7:
        if b9[j][j] < 0:
            return [[0, 0]]
    print('BellmanFord algorithm is incomplete')
    return b9
def fonk2(b20):
    b9 = []
    b10 = len(b7)
    b11 = [[float("inf")] * b10 for _ in b7]
    for V in range(0, len(b7)):
        for U in range(0, len(b8)):
            b11[U][V] = float(b8[U][V])
        b11[V][V] = 0
    for k in range(0, len(b7)):
        for i in range(0, len(b7)):
            for j in range(0, len(b7)):
                b14 = b11[i][k] + b11[k][j]
                if b11[i][j] > b14:
                    b11[i][j] = b14
    for j in b7:
        if b11[j][j] < 0:
            return [[0, 0]]
    b9 = b11
    print('FloydWarshall algorithm is incomplete')
    return b9
def fonk3(filename):
    global b7, b8
    with open(filename, 'r') as inFile:
        b15 = inFile.readline()
        b16 = b5.match(b15)
        if not b16:
            print(b15 + " not properly formatted")
            quit(1)
        b7 = list(range(int(b16.group(1))))
        b8 = [[float("inf")] * len(b7) for _ in b7]
        for b17 in inFile.readlines():
            b17 = b17.strip()
            b18 = b6.match(b17)
            if b18:
                source, sink, b19 = map(int, b18.groups())
                if source > len(b7) or sink > len(b7):
                    print("Attempting to insert an edge between " + str(source) + " and " + str(sink) + " in a graph with " + str(len(b7)) + " b7")
                    quit(1)
                b8[source - 1][sink - 1] = b19
    return (b7, b8)
def fonk4(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i, row in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, algorithm):
    b20 = fonk3(filename)
    b9 = []
    if algorithm.lower() == 'b':
        b21 = cProfile.Profile()
        b21.enable()
        b9 = fonk1(b20)
        b21.disable()
        b22 = io.StringIO()
        b23 = 'cumulative'
        b24 = pstats.Stats(b21, stream=b22).sort_stats(b23)
        b24.print_stats()
        print(b22.getvalue())
    elif algorithm.lower() == 'f':
        b21 = cProfile.Profile()
        b21.enable()
        b25 = fonk2(b20)
        b21.disable()
        b22 = io.StringIO()
        b23 = 'cumulative'
        b24 = pstats.Stats(b21, stream=b22).sort_stats(b23)
        b24.print_stats()
        print(b22.getvalue())
    elif algorithm.lower() == 'a':
        print('running both')
        b26 = fonk1(b20)
        b25 = fonk2(b20)
        b9 = b26
        if not fonk4(b26, b25):
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0] + '_shortestPaths.txt', 'b12') as f:
        for row in b9:
            f.write(' '.join(map(str, row)) + '\n')
if b27 = = '__main__':
    b28 = b1.parse_args()
    fonk5(b28.filename, b28.algorithm)