import argparse
import re
import sys
import time
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
        for line in infile.readlines():
            b11 = b2.match(line.strip())
            if b11:
                source, sink, b12 = map(int, b11.groups())
                if source > b10 or sink > b10:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b16 with {b10} b3")
                    sys.exit(1)
                b4[source - 1][sink - 1] = b12
    return b3, b4
def fonk4(b16):
    b13 = [[0 if i == j else b16[i][j] for j in range(len(b3))] for i in range(len(b3))]
    for k in range(len(b3)):
        for i in range(len(b3)):
            for j in range(len(b3)):
                if b13[i][k] + b13[k][j] < b13[i][j]:
                    b13[i][j] = b13[i][k] + b13[k][j]
    for i in range(len(b3)):
        if b13[i][i] < 0:
            return True
    return False
def fonk5(b16):
    b14 = []
    b15 = []
    for i in range(len(b3)):
        for j in range(len(b3)):
            if not math.isinf(float(b16[1][i][j])):
                b15.append(class1(i, j, float(b16[1][i][j])))
    for k in range(len(b3)):
        b13 = [float("inf")] * len(b3)
        b13[k] = 0
        for _ in range(len(b3) - 1):
            for edge in b15:
                if b13[edge.b6] > b13[edge.b5] + edge.b7:
                    b13[edge.b6] = b13[edge.b5] + edge.b7
        for edge in b15:
            if b13[edge.b6] > b13[edge.b5] + edge.b7:
                print("There is a negative cycle")
                return []
        for i in range(len(b16[0])):
            b14.append(class1(k, i, b13[i]))
    return b14
def fonk6(b16):
    b14 = []
    b13 = [[float(b16[1][i][j]) for j in range(len(b16[0]))] for i in range(len(b16[0]))]
    for i in range(len(b16[0])):
        b13[i][i] = 0
    for k in range(len(b16[0])):
        for i in range(len(b16[0])):
            for j in range(len(b16[0])):
                if b13[i][j] > b13[i][k] + b13[k][j]:
                    b13[i][j] = b13[i][k] + b13[k][j]
    for i in range(len(b16[0])):
        for j in range(len(b16[0])):
            b14.append(class1(i, j, b13[i][j]))
    return b14
def fonk7(filename, b17):
    b16 = fonk3(filename)
    b17 = b17[1:].lower()
    if b17 = = 'b':
        b18 = fonk5(b16)
        print(b18)
    elif b17 = = 'f':
        b18 = fonk6(b16)
        print(b18)
    elif b17 = = 'both':
        b19 = time.perf_counter()
        b20 = fonk5(b16)
        print(b20)
        b21 = time.perf_counter() - b19
        b19 = time.perf_counter()
        b22 = fonk6(b16)
        print(b22)
        b23 = time.perf_counter() - b19
        print(f"Bellman-Ford timing: {b21:.6f} seconds")
        print(f"Floyd-Warshall timing: {b23:.6f} seconds")
    else:
        print("Unknown b17 selected. Use '-b' for Bellman-Ford, '-f' for Floyd-Warshall, or '-both' for both.")
if b24 = = '__main__':
    b25 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a b16')
    b25.add_argument('--b17', b26 = True, help='Algorithm to run: (b)ellman-ford, (f)loyd-warshall, or (both)')
    b25.add_argument('filename', b27 = '<filename>', help='Input file containing b16')
    b28 = b25.parse_args()
    fonk7(b28.filename, b28.b17)