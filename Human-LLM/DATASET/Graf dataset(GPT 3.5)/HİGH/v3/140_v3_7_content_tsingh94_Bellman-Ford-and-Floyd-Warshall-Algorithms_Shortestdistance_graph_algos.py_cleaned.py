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
def fonk2(b20):
    b3 = []
    b4 = fonk1(b20[1])
    b5 = b4[0][0]
    for n in range(len(b20[0])):
        b6 = [b5 if m != n else 0 for m in range(len(b20[0]))]
        for _ in range(len(b20[0])):
            b7 = []
            for i in range(len(b4)):
                b8 = b6[i]
                for k in range(len(b4[i])):
                    b9 = b4[k][i]
                    b10 = b6[k]
                    if b9 != b5 and b10 != b5:
                        if b9 + b10 < b8:
                            b8 = b9 + b10
                b7.append(b8 if i != n else 0)
            b6 = b7
        b3.append(b6)
    return b3
def fonk3(b20):
    b3 = fonk1(b20[1])
    for i in range(len(b20[0])):
        b3[i][i] = 0
    for k in range(len(b20[0])):
        for i in range(len(b3)):
            for j in range(len(b3[i])):
                b11 = b3[i][k] + b3[k][j]
                if b11 < b3[i][j]:
                    b3[i][j] = b11
    return b3
def fonk4(b18):
    with open(b18, 'r') as inFile:
        b12 = inFile.readline()
        b13 = b1.match(b12)
        if not b13:
            print(f"First b15 '{b12}' not properly formatted")
            sys.exit(1)
        b14 = list(range(int(b13.group(1))))
        b4 = [[float("inf")] * len(b14) for _ in range(len(b14))]
        for b15 in inFile.readlines():
            b15 = b15.strip()
            b16 = b2.match(b15)
            if b16:
                source, sink, b17 = map(int, b16.groups())
                if source >= len(b14) or sink >= len(b14):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(b14)} b14")
                    sys.exit(1)
                b4[source][sink] = b17
    return b14, b4
def fonk5(length_matrix, b18):
    b18 = os.path.splitext(os.path.split(b18)[1])[0]
    with open(f'output/{b18}_output.txt', 'w') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def fonk6(b18, b19):
    b19 = b19[1:]
    b20 = fonk4(b18)
    b21 = []
    if b19.lower() == 'b':
        b22 = time.clock()
        b21 = fonk2(b20)
        b23 = time.clock() - b22
        print("Bellman-Ford timing:", b23)
    elif b19.lower() == 'f':
        b22 = time.clock()
        b21 = fonk3(b20)
        b24 = time.clock() - b22
        print("Floyd-Warshall timing:", b24)
    elif b19.lower() == "both":
        b22 = time.clock()
        fonk2(b20)
        b23 = time.clock() - b22
        b22 = time.clock()
        fonk3(b20)
        b24 = time.clock() - b22
        print("Bellman-Ford timing:", b23)
        print("Floyd-Warshall timing:", b24)
    fonk5(b21, b18)
if b25 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    fonk6(sys.argv[2], sys.argv[1])