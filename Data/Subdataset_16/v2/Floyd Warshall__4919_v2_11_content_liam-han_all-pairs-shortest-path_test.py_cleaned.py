import argparse
import re
import sys
import time
import math
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
class class1:
    def fonk1(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk2(self):
        return f"(({self.b5}, {self.b6}), {self.b7})"
def fonk3(filename):
    global b3
    global b4
    with open(filename, 'r') as infile:
        b8 = infile.readline()
        b9 = b1.match(b8)
        if not b9:
            print(f"{b8} not properly formatted")
            sys.exit(1)
        b10 = int(b9.group(1))
        b3 = list(range(b10))
        b4 = [[float("inf")] * b10 for _ in range(b10)]
        for line in infile:
            b11 = b2.match(line.strip())
            if b11:
                source, sink, b12 = map(int, b11.groups())
                if source >= b10 or sink >= b10:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b16 with {b10} b3")
                    sys.exit(1)
                b4[source - 1][sink - 1] = b12
    return b3, b4
def fonk4(b16):
    b3, b4 = b16
    b13 = []
    b14 = []
    for i in range(len(b3)):
        for j in range(len(b3)):
            if not math.isinf(float(b4[i][j])):
                b14.append(class1(i, j, float(b4[i][j])))
    for src in range(len(b3)):
        b15 = [float("inf")] * len(b3)
        b15[src] = 0
        for _ in range(len(b3) - 1):
            for edge in b14:
                if b15[edge.b6] > b15[edge.b5] + edge.b7:
                    b15[edge.b6] = b15[edge.b5] + edge.b7
        for edge in b14:
            if b15[edge.b6] > b15[edge.b5] + edge.b7:
                print("There is a negative cycle")
                return []
        for dest in range(len(b3)):
            b13.append(class1(src, dest, b15[dest]))
    return b13
def fonk5(b16):
    b3, b4 = b16
    b13 = []
    b15 = [[float(b4[i][j]) for j in range(len(b3))] for i in range(len(b3))]
    for i in range(len(b3)):
        b15[i][i] = 0
    for k in range(len(b3)):
        for i in range(len(b3)):
            for j in range(len(b3)):
                if b15[i][j] > b15[i][k] + b15[k][j]:
                    b15[i][j] = b15[i][k] + b15[k][j]
    for i in range(len(b3)):
        for j in range(len(b3)):
            b13.append(class1(i, j, b15[i][j]))
    return b13
def fonk6(filename, b17):
    b16 = fonk3(filename)
    b17 = b17.lower()
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
    b25 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a b16')
    b25.add_argument('--b17', b26 = True, choices=['b', 'f', 'both'], help='Algorithm to run: (b)ellman-ford, (f)loyd-warshall, or (both)')
    b25.add_argument('filename', b27 = '<filename>', help='Input file containing b16')
    b28 = b25.parse_args()
    fonk6(b28.filename, b28.b17)