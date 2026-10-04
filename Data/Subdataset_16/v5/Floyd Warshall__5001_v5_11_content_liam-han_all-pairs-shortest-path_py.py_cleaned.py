import sys
import re
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
def fonk3(b16):
    b8 = [[0 if i == j else b16[i][j] for j in range(len(b3))] for i in range(len(b3))]
    for k in range(len(b3)):
        for i in range(len(b3)):
            for j in range(len(b3)):
                if b8[i][k] + b8[k][j] < b8[i][j]:
                    b8[i][j] = b8[i][k] + b8[k][j]
    for i in range(len(b3)):
        if b8[i][i] < 0:
            return True
    return False
def fonk4(b16):
    b9 = []
    b10 = []
    for i in range(len(b3)):
        for j in range(len(b3)):
            if not math.isinf(float(b16[1][i][j])):
                b10.append(class1(i, j, float(b16[1][i][j])))
    for k in range(len(b3)):
        b8 = [float("inf")] * len(b3)
        b8[k] = 0
        for _ in range(len(b3) - 1):
            for edge in b10:
                if b8[edge.b6] > b8[edge.b5] + edge.b7:
                    b8[edge.b6] = b8[edge.b5] + edge.b7
        for edge in b10:
            if b8[edge.b6] > b8[edge.b5] + edge.b7:
                print("There is a negative cycle")
                return []
        for i in range(len(b16[0])):
            b9.append(class1(k, i, b8[i]))
    return b9
def fonk5(b16):
    b9 = []
    b8 = [[float(b16[1][i][j]) for j in range(len(b16[0]))] for i in range(len(b16[0]))]
    for i in range(len(b16[0])):
        b8[i][i] = 0
    for k in range(len(b16[0])):
        for i in range(len(b16[0])):
            for j in range(len(b16[0])):
                if b8[i][j] > b8[i][k] + b8[k][j]:
                    b8[i][j] = b8[i][k] + b8[k][j]
    for i in range(len(b16[0])):
        for j in range(len(b16[0])):
            b9.append(class1(i, j, b8[i][j]))
    return b9
def fonk6(filename):
    global b3
    global b4
    with open(filename, 'r') as infile:
        b11 = infile.readline()
        b12 = b1.match(b11)
        if not b12:
            print(f"{b11} not properly formatted")
            sys.exit(1)
        b13 = int(b12.group(1))
        b3 = list(range(b13))
        b4 = [[float("inf")] * b13 for _ in range(b13)]
        for line in infile.readlines():
            b14 = b2.match(line.strip())
            if b14:
                source, sink, b15 = map(int, b14.groups())
                if source > b13 or sink > b13:
                    print(f"Attempting to insert an edge between {source} and {sink} in a b16 with {b13} b3")
                    sys.exit(1)
                b4[source - 1][sink - 1] = b15
    return b3, b4
def fonk7(filename, b17):
    b16 = fonk6(filename)
    b17 = b17[1:].lower()
    if b17 = = 'b':
        b18 = fonk4(b16)
        print(b18)
    elif b17 = = 'f':
        b18 = fonk5(b16)
        print(b18)
    elif b17 = = 'both':
        b19 = time.perf_counter()
        b20 = fonk4(b16)
        print(b20)
        b21 = time.perf_counter() - b19
        b19 = time.perf_counter()
        b22 = fonk5(b16)
        print(b22)
        b23 = time.perf_counter() - b19
        print(f"Bellman-Ford timing: {b21:.6f} seconds")
        print(f"Floyd-Warshall timing: {b23:.6f} seconds")
    else:
        print("Unknown b17 selected. Use '-b' for Bellman-Ford, '-f' for Floyd-Warshall, or '-both' for both.")
if b24 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py -<f|b|both> <input_file>")
        sys.exit(1)
    fonk7(sys.argv[2], sys.argv[1])