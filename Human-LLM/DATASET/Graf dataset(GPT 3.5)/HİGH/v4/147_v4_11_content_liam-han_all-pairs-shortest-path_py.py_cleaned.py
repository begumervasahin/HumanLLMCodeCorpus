import sys
import re
import time
import math
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"(({self.b1}, {self.b2}), {self.b3})"
b4 = re.compile(r"(\d+)\s(\d+)")
b5 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b6 = []
b7 = []
def fonk3(b19):
    b8 = []
    b9 = []
    for i in range(len(b6)):
        for j in range(len(b6)):
            if not math.isinf(float(b19[1][i][j])):
                b10 = class1(i, j, float(b19[1][i][j]))
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
        for i in range(len(b19[0])):
            b12 = class1(k, i, b11[i])
            b8.append(b12)
    return b8
def fonk4(b19):
    b8 = []
    b13 = []
    for i in range(len(b19[0])):
        b14 = []
        for j in range(len(b19[0])):
            b14.append(float(b7[i][j]))
        b13.append(b14)
        b13[i][i] = 0
    for k in range(len(b19[0])):
        for i in range(len(b19[0])):
            for j in range(len(b19[0])):
                if b13[i][j] > b13[i][k] + b13[k][j]:
                    b13[i][j] = b13[i][k] + b13[k][j]
    for i in range(len(b19[0])):
        for j in range(len(b19[0])):
            b12 = class1(i, j, b13[i][j])
            b8.append(b12)
    return b8
def fonk5(filename):
    global b6, b7
    with open(filename, 'r') as file:
        b15 = file.readline()
        b16 = b4.match(b15)
        if not b16:
            print(b15 + " not properly formatted")
            return [], []
        b6 = list(range(int(b16.group(1))))
        b7 = [[float("inf")] * len(b6) for _ in range(len(b6))]
        for line in file.readlines():
            b17 = b5.match(line.strip())
            if b17:
                b1, sink, b3 = map(int, b17.groups())
                if b1 > len(b6) or sink > len(b6):
                    print(f"Attempting to insert an b10 between {b1} and {sink} in a b19 with {len(b6)} b6")
                    return [], []
                b7[b1 - 1][sink - 1] = b3
    return b6, b7
def fonk6(filename, b18):
    b18 = b18[1:].lower()
    b19 = fonk5(filename)
    if b18 = = 'b':
        fonk3(b19)
    elif b18 = = 'f':
        fonk4(b19)
    elif b18 = = 'both':
        b20 = time.clock()
        fonk3(b19)
        b21 = time.clock()
        b22 = b21 - b20
        b20 = time.clock()
        fonk4(b19)
        b21 = time.clock()
        b23 = b21 - b20
        print("Bellman-Ford timing:", b22)
        print("Floyd-Warshall timing:", b23)
    else:
        print("Invalid b18 option. Please choose 'b', 'f', or 'both'.")
if b24 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py -<f|b|both> <input_file>")
        sys.exit(1)
    fonk6(sys.argv[2], sys.argv[1])