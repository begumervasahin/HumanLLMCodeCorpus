import os
import re
import sys
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def fonk1(b4):
    for v in range(len(b4)):
        for e in range(len(b4[v])):
            if isinstance(b4[v][e], str):
                b4[v][e] = int(b4[v][e])
    return b4
def fonk2(b19):
    b3 = []
    b4 = fonk1(b19[1])
    b5 = b4[0][0]
    for n in range(len(b19[0])):
        b6 = [b5 if m != n else 0 for m in range(len(b19[0]))]
        for _ in range(len(b19[0])):
            b7 = []
            for i in range(len(b4)):
                b8 = b6[i]
                for k in range(len(b4[i])):
                    b9 = b4[k][i]
                    b10 = b6[k]
                    if b9 != b5 and b10 != b5:
                        b8 = min(b8, b9 + b10)
                b7.append(b8 if i != n else 0)
            b6 = b7
        b3.append(b6)
    return b3
def fonk3(b19):
    b3 = fonk1(b19[1])
    for i in range(len(b19[0])):
        b3[i][i] = 0
    for k in range(len(b19[0])):
        for i in range(len(b3)):
            for j in range(len(b3[i])):
                b3[i][j] = min(b3[i][j], b3[i][k] + b3[k][j])
    return b3
def fonk4(b17):
    with open(b17, 'r') as inFile:
        b11 = inFile.readline()
        b12 = b1.match(b11)
        if not b12:
            print(f"First b14 '{b11}' not properly formatted")
            sys.exit(1)
        b13 = list(range(int(b12.group(1))))
        b4 = [[float("inf")] * len(b13) for _ in range(len(b13))]
        for b14 in inFile.readlines():
            b14 = b14.strip()
            b15 = b2.match(b14)
            if b15:
                source, sink, b16 = map(int, b15.groups())
                if source >= len(b13) or sink >= len(b13):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(b13)} b13")
                    sys.exit(1)
                b4[source][sink] = b16
    return b13, b4
def fonk5(length_matrix, b17):
    b17 = os.path.splitext(os.path.split(b17)[1])[0]
    with open(f'output/{b17}_output.txt', 'w') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def fonk6(b17, b18):
    b18 = b18[1:]
    b19 = fonk4(b17)
    b20 = []
    if b18.lower() == 'b':
        b21 = time.clock()
        b20 = fonk2(b19)
        b22 = time.clock() - b21
        print("Bellman-Ford timing:", b22)
    elif b18.lower() == 'f':
        b21 = time.clock()
        b20 = fonk3(b19)
        b23 = time.clock() - b21
        print("Floyd-Warshall timing:", b23)
    elif b18.lower() == "both":
        b21 = time.clock()
        fonk2(b19)
        b22 = time.clock() - b21
        b21 = time.clock()
        fonk3(b19)
        b23 = time.clock() - b21
        print("Bellman-Ford timing:", b22)
        print("Floyd-Warshall timing:", b23)
    fonk5(b20, b17)
if b24 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    fonk6(sys.argv[2], sys.argv[1])