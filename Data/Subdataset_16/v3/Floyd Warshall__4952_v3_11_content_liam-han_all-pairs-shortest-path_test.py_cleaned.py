import argparse
import re
import sys
import time
import math
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
class class1:
    def fonk1(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return f"(({self.b3}, {self.b4}), {self.b5})"
def fonk3(filename):
    with open(filename, 'r') as infile:
        b6 = infile.readline()
        b7 = b1.match(b6)
        if not b7:
            print(f"{b6.strip()} not properly formatted")
            sys.exit(1)
        b8 = int(b7.group(1))
        b9 = list(range(b8))
        b10 = [[float("inf")] * b8 for _ in range(b8)]
        for line in infile:
            b11 = b2.match(line.strip())
            if b11:
                source, sink, b12 = map(int, b11.groups())
                if source >= b8 or sink >= b8:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b16 with {b8} b9")
                    sys.exit(1)
                b10[source - 1][sink - 1] = b12
    return b9, b10
def fonk4(b16):
    b9, b10 = b16
    b13 = []
    b14 = []
    for i in range(len(b9)):
        for j in range(len(b9)):
            if not math.isinf(b10[i][j]):
                b14.append(class1(i, j, b10[i][j]))
    for src in range(len(b9)):
        b15 = [float("inf")] * len(b9)
        b15[src] = 0
        for _ in range(len(b9) - 1):
            for edge in b14:
                if b15[edge.b4] > b15[edge.b3] + edge.b5:
                    b15[edge.b4] = b15[edge.b3] + edge.b5
        for edge in b14:
            if b15[edge.b4] > b15[edge.b3] + edge.b5:
                print("There is a negative cycle")
                return []
        for dest in range(len(b9)):
            b13.append(class1(src, dest, b15[dest]))
    return b13
def fonk5(b16):
    b9, b10 = b16
    b13 = []
    b15 = [[b10[i][j] for j in range(len(b9))] for i in range(len(b9))]
    for i in range(len(b9)):
        b15[i][i] = 0
    for k in range(len(b9)):
        for i in range(len(b9)):
            for j in range(len(b9)):
                if b15[i][j] > b15[i][k] + b15[k][j]:
                    b15[i][j] = b15[i][k] + b15[k][j]
    for i in range(len(b9)):
        for j in range(len(b9)):
            b13.append(class1(i, j, b15[i][j]))
    return b13
def fonk6(filename, b17):
    b16 = fonk3(filename)
    if b17 = = 'b':
        b18 = fonk4(b16)
        print(b18)
    elif b17 = = 'f':
        b18 = fonk5(b16)
        print(b18)
    elif b17 = = 'both':
        b19 = time.perf_counter()
        b20 = fonk4(b16)
        b21 = time.perf_counter() - b19
        print(b20)
        print(f"Bellman-Ford timing: {b21:.6f} seconds")
        b19 = time.perf_counter()
        b22 = fonk5(b16)
        b23 = time.perf_counter() - b19
        print(b22)
        print(f"Floyd-Warshall timing: {b23:.6f} seconds")
    else:
        print("Unknown b17 selected. Use 'b' for Bellman-Ford, 'f' for Floyd-Warshall, or 'both' for both.")
if b24 = = '__main__':
    b25 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b9 in a b16')
    b25.add_argument('--b17', b26 = True, choices=['b', 'f', 'both'], help='Algorithm to run: (b)ellman-ford, (f)loyd-warshall, or (both)')
    b25.add_argument('filename', b27 = '<filename>', help='Input file containing b16')
    b28 = b25.parse_args()
    fonk6(b28.filename, b28.b17)