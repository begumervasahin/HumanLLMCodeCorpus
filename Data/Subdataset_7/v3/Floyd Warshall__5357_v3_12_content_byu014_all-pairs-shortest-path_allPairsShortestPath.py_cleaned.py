import argparse
import os
import re
import sys
import time
import timeit
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
b3 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b1 in a b15')
b3.add_argument('--algorithm', b4 = 'a', help='Algorithm: Select the algorithm to run, b4 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b3.add_argument('-v', '--verbose', b5 = 'store_true')
b3.add_argument('--profile', b5 = 'store_true')
b3.add_argument('filename', b6 = '<filename>', help='Input file containing b15')
b7 = re.compile(r"(\d+)\s(\d+)")
b8 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk2(b15):
    b9 = []
    for source in range(len(b15.b1)):
        b10 = [float("inf")] * len(b15.b1)
        b10[source] = 0.0
        for _ in range(len(b15.b1) - 1):
            for u in range(len(b15.b1)):
                for v in range(len(b15.b1)):
                    if b10[v] > b10[u] + b15.b2[u][v]:
                        b10[v] = b10[u] + b15.b2[u][v]
        for u in range(len(b15.b1)):
            for v in range(len(b15.b1)):
                if b10[v] > b10[u] + b15.b2[u][v]:
                    return (b9, False)
        b9.append(b10)
    return (b9, True)
def fonk3(b15):
    b9 = []
    b10 = [[float("inf")] * len(b15.b1) for _ in range(len(b15.b1))]
    for i in range(len(b15.b1)):
        for j in range(len(b15.b1)):
            b10[i][j] = b15.b2[i][j]
    for k in range(len(b15.b1)):
        for i in range(len(b15.b1)):
            for j in range(len(b15.b1)):
                b10[i][j] = min(b10[i][j], b10[i][k] + b10[k][j])
    return b10
def fonk4(filename):
    with open(filename, 'r') as file:
        b11 = file.readline()
        b12 = b7.match(b11)
        if not b12:
            print(f"First line of {filename} is not properly formatted")
            sys.exit(1)
        b1 = list(range(int(b12.group(1))))
        b2 = [[float("inf")] * len(b1) for _ in range(len(b1))]
        for line in file.readlines():
            b13 = b8.match(line.strip())
            if b13:
                source, sink, b14 = map(int, b13.groups())
                if source > len(b1) or sink > len(b1):
                    print(f"Attempting to insert an edge between {source} and {sink} in a b15 with {len(b1)} b1")
                    sys.exit(1)
                b2[source - 1][sink - 1] = b14
    return class1(b1, b2)
def fonk5(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk6(filename, algorithm):
    b15 = fonk4(filename)
    b9 = []
    b16 = True
    if algorithm.lower() == 'b':
        b17 = timeit.default_timer()
        b9, b16 = fonk2(b15)
        b18 = timeit.default_timer()
        print(b18 - b17)
    elif algorithm.lower() == 'f':
        b17 = timeit.default_timer()
        b9 = fonk3(b15)
        b18 = timeit.default_timer()
        print(b18 - b17)
    elif algorithm.lower() == 'a':
        print('Running both')
        path_pairs_bellman, b19 = fonk2(b15)
        b20 = fonk3(b15)
        b9 = path_pairs_bellman
        b16 = b19
        if not fonk5(path_pairs_bellman, b20) or not b16:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result or negative cycle detected')
    else:
        print("Invalid algorithm option. Please choose 'b', 'f', or 'a'.")
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt', 'w') as f:
        if not b16:
            f.write("Negative Cycle Detected \n")
        for row in b9:
            for b14 in row:
                f.write(str(b14)+' ')
            f.write('\n')
if b21 = = '__main__':
    b22 = b3.parse_args()
    fonk6(b22.filename, b22.algorithm)