import sys
import re
import time
import math
class class1:
    def fonk1(self, u, v, w):
        self.b1 = u
        self.b2 = v
        self.b3 = w
    def fonk2(self):
        return f"(({self.b1},{self.b2}), {self.b3})"
b4 = re.compile(r"(\d+)\s(\d+)")
b5 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b6 = []
b7 = []
def fonk3(b18):
    b8 = []
    b9 = []
    for i in range(len(b6)):
        for j in range(len(b6)):
            if not math.isinf(float(b18[1][i][j])):
                b10 = class1(int(i), int(j), float(b18[1][i][j]))
                b9.append(b10)
    for k in range(len(b6)):
        b11 = [float("inf")] * len(b6)
        b11[k] = 0
        for _ in range(len(b6) - 1):
            for b10 in b9:
                if b11[b10.b2] > b11[b10.b1] + b10.b3:
                    b11[b10.b2] = b11[b10.b1] + b10.b3
        for b10 in b9:
            if b11[b10.b2] > b11[b10.b1] + b10.b3:
                print("There is a negative cycle")
                return
        for i in range(len(b18[0])):
            b12 = class1(k, i, b11[i])
            b8.append(b12)
    return b8
def fonk4(b18):
    b8 = []
    b11 = []
    for i in range(len(b18[0])):
        b13 = []
        for j in range(len(b18[0])):
            b13.append(float(b7[i][j]))
        b11.append(b13)
        b11[i][i] = 0
    for k in range(len(b18[0])):
        for i in range(len(b18[0])):
            for j in range(len(b18[0])):
                if b11[i][j] > b11[i][k] + b11[k][j]:
                    b11[i][j] = b11[i][k] + b11[k][j]
    for i in range(len(b18[0])):
        for j in range(len(b18[0])):
            b12 = class1(i, j, b11[i][j])
            b8.append(b12)
    return b8
def fonk5(filename):
    global b6, b7
    with open(filename, 'r') as file:
        b14 = file.readline()
        b15 = b4.match(b14)
        if not b15:
            print(b14 + " not properly formatted")
            return [], []
        b6 = list(range(int(b15.group(1))))
        b7 = [[float("inf")] * len(b6) for _ in range(len(b6))]
        for line in file.readlines():
            b16 = b5.match(line.strip())
            if b16:
                b1, sink, b3 = map(int, b16.groups())
                if b1 > len(b6) or sink > len(b6):
                    print(f"Attempting to insert an b10 between {b1} and {sink} in a b18 with {len(b6)} b6")
                    return [], []
                b7[b1 - 1][sink - 1] = b3
    return b6, b7
def fonk6(filename, b17):
    b17 = b17.lower()
    b18 = fonk5(filename)
    if b17 = = 'b':
        fonk3(b18)
    elif b17 = = 'f':
        fonk4(b18)
    elif b17 = = 'both':
        b19 = time.clock()
        fonk3(b18)
        b20 = time.clock()
        b21 = b20 - b19
        b19 = time.clock()
        fonk4(b18)
        b20 = time.clock()
        b22 = b20 - b19
        print("Bellman-Ford timing:", b21)
        print("Floyd-Warshall timing:", b22)
    else:
        print("Invalid b17 option. Please choose 'b', 'f', or 'both'.")
if b23 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py -<f|b|both> <input_file>")
        sys.exit(1)
    fonk6(sys.argv[2], sys.argv[1])