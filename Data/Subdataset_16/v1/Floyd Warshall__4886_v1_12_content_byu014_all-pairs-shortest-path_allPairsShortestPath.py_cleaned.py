import argparse
import os
import re
import sys
import timeit
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b13):
    b10, b3 = b13
    b4 = []
    for source in range(len(b10)):
        b5 = [float("inf")] * len(b10)
        b5[source] = 0.0
        for _ in range(len(b10) - 1):
            for current in range(len(b10)):
                for other_vertex in range(len(b3[current])):
                    if b5[other_vertex] > b5[current] + b3[current][other_vertex]:
                        b5[other_vertex] = b5[current] + b3[current][other_vertex]
        for current in range(len(b10)):
            for other_vertex in range(len(b3[current])):
                if b5[other_vertex] > b5[current] + b3[current][other_vertex]:
                    return b4, False
        b4.append(b5)
    return b4, True
def fonk2(b13):
    b10, b3 = b13
    b6 = [row[:] for row in b3]
    for k in range(len(b10)):
        for i in range(len(b10)):
            for j in range(len(b10)):
                b6[i][j] = min(b6[i][j], b6[i][k] + b6[k][j])
    return b6
def fonk3(filename):
    with open(filename, 'r') as infile:
        b7 = infile.readline().strip()
        b8 = b1.match(b7)
        if not b8:
            print(f"{b7} not properly formatted")
            sys.exit(1)
        b9 = int(b8.group(1))
        b10 = list(range(b9))
        b3 = [[float("inf")] * b9 for _ in range(b9)]
        for line in infile:
            b11 = b2.match(line.strip())
            if b11:
                source, sink, b12 = map(int, b11.groups())
                if source >= b9 or sink >= b9:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b13 with {b9} b10")
                    sys.exit(1)
                b3[source - 1][sink - 1] = b12
    return b10, b3
def fonk4(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, b17):
    b13 = fonk3(filename)
    b4 = []
    b14 = True
    if b17 in ('b', 'B'):
        b15 = timeit.default_timer()
        b4, b14 = fonk1(b13)
        b16 = timeit.default_timer()
        print(f"Bellman-Ford Time: {b16 - b15:.6f} seconds")
    elif b17 in ('f', 'F'):
        b15 = timeit.default_timer()
        b4 = fonk2(b13)
        b16 = timeit.default_timer()
        print(f"Floyd-Warshall Time: {b16 - b15:.6f} seconds")
    elif b17 = = 'a':
        print('Running both Bellman-Ford and Floyd-Warshall algorithms')
        path_pairs_bellman, b14 = fonk1(b13)
        b18 = fonk2(b13)
        if not fonk4(path_pairs_bellman, b18) or not b14:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
        b4 = path_pairs_bellman
    b19 = os.path.splitext(filename)[0] + '_shortestPaths.txt'
    with open(b19, 'w') as outfile:
        if not b14:
            outfile.write("Negative Cycle Detected\n")
        for row in b4:
            outfile.write(' '.join(map(str, row)) + '\n')
if b20 = = '__main__':
    b21 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b10 in a b13')
    b21.add_argument('--b17', b22 = 'a', help='Algorithm: Select the b17 to run, b22 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
    b21.add_argument('-v', '--verbose', b23 = 'store_true')
    b21.add_argument('--profile', b23 = 'store_true')
    b21.add_argument('filename', b24 = '<filename>', help='Input file containing b13')
    b25 = b21.parse_args()
    fonk5(b25.filename, b25.b17)