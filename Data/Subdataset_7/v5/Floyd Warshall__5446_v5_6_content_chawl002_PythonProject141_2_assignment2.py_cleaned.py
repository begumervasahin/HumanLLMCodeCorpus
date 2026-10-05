import os
import re
import sys
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def fonk1(b16):
    b3 = []
    b4 = len(b16[0])
    for _ in range(b4):
        b5 = [float("inf")] * b4
        b5[_] = 0
        for _ in range(1, b4 - 1):
            for source in range(b4):
                for destination in range(b4):
                    if float(b16[1][source][destination]) < float("inf"):
                        b6 = b5[source] + float(b16[1][source][destination])
                        if b5[destination] > b6:
                            b5[destination] = b6
        b3.append(b5)
    return b3
def fonk2(b16):
    b3 = []
    b4 = len(b16[0])
    b5 = [[float("inf")] * b4 for _ in range(b4)]
    for i in range(b4):
        b5[i][i] = 0
    for source in range(b4):
        for destination in range(b4):
            if float(b16[1][source][destination]) < float("inf"):
                b5[source][destination] = float(b16[1][source][destination])
    for intermediate in range(b4):
        for source in range(b4):
            for destination in range(b4):
                b5[source][destination] = min(
                    b5[source][destination],
                    b5[source][intermediate] + b5[intermediate][destination]
                )
    b3.append(b5)
    return b3
def fonk3(b14):
    with open(b14, 'r') as inFile:
        b7 = inFile.readline().strip()
        b8 = b1.match(b7)
        if not b8:
            print(f"First b11 '{b7}' not properly formatted")
            sys.exit(1)
        b4 = int(b8.group(1))
        b9 = list(range(b4))
        b10 = [[float("inf")] * b4 for _ in range(b4)]
        for b11 in inFile.readlines():
            b11 = b11.strip()
            b12 = b2.match(b11)
            if b12:
                source, sink, b13 = map(int, b12.groups())
                if source >= b4 or sink >= b4:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {b4} b9")
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