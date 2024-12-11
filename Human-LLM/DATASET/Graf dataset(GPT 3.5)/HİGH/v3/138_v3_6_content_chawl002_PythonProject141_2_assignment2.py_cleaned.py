import os
import re
import sys
import time
b1 = re.compile(r"(\b4+)\s(\b4+)")
b2 = re.compile(r"(\b4+)\s(\b4+)\s(\b4+)")
def fonk1(b16):
    b3 = []
    b4 = []
    for _ in range(len(b16[0])):
        b4 = [float("inf")] * len(b16[0])
        b4[_] = 0
        for _ in range(1, len(b16[0]) - 1):
            for e in range(len(b16[0])):
                for f in range(len(b16[0])):
                    if float(b16[1][e][f]) < float("inf"):
                        if b4[f] > b4[e] + float(b16[1][e][f]):
                            b4[f] = int(b4[e]) + int(float(b16[1][e][f]))
        b3.append(b4)
    return b3
def fonk2(b16):
    b3 = []
    b4 = []
    for _ in range(len(b16[0])):
        b5 = [float("inf")] * len(b16[0])
        b4.append(b5)
    for b6 in range(len(b16[0])):
        for e in range(len(b16[0])):
            if b6 = = e:
                b4[b6][b6] = 0
            elif float(b16[1][b6][e]) < float("inf"):
                b4[b6][e] = int(float(b16[1][b6][e]))
            else:
                b4[b6][e] = float("inf")
    for b6 in range(len(b16[0])):
        for a in range(len(b16[0])):
            for b in range(len(b16[0])):
                b4[a][b] = min(b4[a][b], b4[a][b6] + b4[b6][b])
    b3.append(b4)
    return b3
def fonk3(b14):
    with open(b14, 'r') as inFile:
        b7 = inFile.readline().strip()
        b8 = b1.match(b7)
        if not b8:
            print(f"First b11 '{b7}' not properly formatted")
            sys.exit(1)
        b9 = list(range(int(b8.group(1))))
        b10 = [[float("inf")] * len(b9) for _ in range(len(b9))]
        for b11 in inFile.readlines():
            b11 = b11.strip()
            b12 = b2.match(b11)
            if b12:
                source, sink, b13 = map(int, b12.groups())
                if source >= len(b9) or sink >= len(b9):
                    print(f"Attempting to insert an edge between {source} and {sink} in a b16 with {len(b9)} b9")
                    sys.exit(1)
                b10[source][sink] = b13
    return b9, b10
def fonk4(length_matrix, b14):
    b14 = os.path.splitext(os.path.split(b14)[1])[0]
    with open(f'output/{b14}_output.txt', 'w+') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def fonk5(b14, b15):
    b15 = b15[1:]
    b16 = fonk3(b14)
    b17 = []
    if b15 in {'b', 'B'}:
        b17 = fonk1(b16)
    elif b15 in {'f', 'F'}:
        b17 = fonk2(b16)
    elif b15.lower() == "both":
        b18 = time.clock()
        fonk1(b16)
        b19 = time.clock() - b18
        b18 = time.clock()
        fonk2(b16)
        b20 = time.clock() - b18
        print(f"Bellman-Ford timing: {b19}")
        print(f"Floyd-Warshall timing: {b20}")
    fonk4(b17, b14)
if b21 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    fonk5(sys.argv[2], sys.argv[1])