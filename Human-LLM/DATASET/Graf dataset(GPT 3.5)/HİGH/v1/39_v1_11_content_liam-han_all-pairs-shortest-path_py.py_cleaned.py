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
        return "((%s,%s),%s)" % (self.b5, self.b6, self.b7)
def fonk3(b18):
    b8 = []
    b9 = []
    for i in range(len(b3)):
        for j in range(len(b3)):
            if not math.isinf(float(b18[1][i][j])):
                b10 = class1(int(i), int(j), float(b18[1][i][j]))
                b9.append(b10)
    for k in range(len(b3)):
        b11 = [float("inf")] * len(b3)
        b11[k] = 0
        for _ in range(len(b3) - 1):
            for edge in b9:
                if b11[edge.b6] > b11[edge.b5] + edge.b7:
                    b11[edge.b6] = b11[edge.b5] + edge.b7
        for edge in b9:
            if b11[edge.b6] > b11[edge.b5] + edge.b7:
                print("There is a negative cycle")
                return
        for i in range(len(b18[0])):
            b10 = class1(k, i, b11[i])
            b8.append(b10)
    return b8
def fonk4(b18):
    b8 = []
    b11 = []
    for i in range(len(b18[0])):
        b12 = []
        for j in range(len(b18[0])):
            b12.append(float(b4[i][j]))
        b11.append(b12)
        b11[i][i] = 0
    for k in range(len(b18[0])):
        for i in range(len(b18[0])):
            for j in range(len(b18[0])):
                if b11[i][j] > b11[i][k] + b11[k][j]:
                    b11[i][j] = b11[i][k] + b11[k][j]
    for i in range(len(b18[0])):
        for j in range(len(b18[0])):
            b10 = class1(i, j, b11[i][j])
            b8.append(b10)
    return b8
def fonk5(filename):
    global b3, b4
    with open(filename, 'r') as file:
        b13 = file.readline()
        b14 = b1.match(b13)
        if not b14:
            print(b13 + " not properly formatted")
            return [], []
        b3 = list(range(int(b14.group(1))))
        b4 = [[float("inf")] * len(b3) for _ in range(len(b3))]
        for line in file.readlines():
            b15 = b2.match(line.strip())
            if b15:
                source, sink, b16 = map(int, b15.groups())
                if source > len(b3) or sink > len(b3):
                    print(f"Attempting to insert an edge between {source} and {sink} in a b18 with {len(b3)} b3")
                    return [], []
                b4[source - 1][sink - 1] = b16
    return b3, b4
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