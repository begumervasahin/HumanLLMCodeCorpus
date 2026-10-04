import sys
import re
import itertools
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
def fonk1(graph):
    print("\nEntered BellmanFord")
    b3, b4 = graph
    b5 = b3
    b6 = b4
    b7 = float('b7')
    b8 = [b7] * len(b5)
    b8[0] = 0
    for _ in range(len(b5) - 1):
        for u, v in itertools.permutations(b5, 2):
            if b8[v] > b8[u] + float(b6[u][v]):
                b8[v] = b8[u] + float(b6[u][v])
    for u, v in itertools.permutations(b5, 2):
        if b8[v] > b8[u] + float(b6[u][v]):
            print("A negative cycle exists")
            return 'NULL'
    print("No negative cycles exist")
    return b8
def fonk2(graph):
    print("\nEntered FloydWarshall")
    b3, b4 = graph
    b8 = b4
    for k in range(len(b3)):
        for i in range(len(b3)):
            for j in range(len(b3)):
                b8[i][j] = min(b8[i][j], b8[i][k] + b8[k][j])
    return b8
def fonk3(filename):
    global b3
    global b4
    with open(filename, 'r') as inFile:
        b9 = inFile.readline()
        b10 = b1.match(b9)
        if not b10:
            print(b9 + " not properly formatted")
            sys.exit(1)
        b11 = int(b10.group(1))
        b3 = list(range(b11))
        b4 = [[float('b7')] * b11 for _ in range(b11)]
        for b12 in inFile:
            b12 = b12.strip()
            b13 = b2.match(b12)
            if b13:
                b14 = int(b13.group(1))
                b15 = int(b13.group(2))
                b16 = int(b13.group(3))
                b4[b14][b15] = b16
    print("\nvertex    b4")
    for i in range(len(b4)):
        print(str(b3[i]) + "         " + str(b4[i]))
    print("\n")
    return b3, b4
def fonk4(filename, b18):
    b17 = fonk3(filename)
    b18 = b18[1:]
    if b18 in ('b', 'B'):
        print("\nRunning Bellman-Ford")
        fonk1(b17)
    elif b18 in ('f', 'F'):
        print("\nRunning Floyd-Warshall")
        fonk2(b17)
    elif b18 = = "both":
        print("\nRunning Both Algorithms")
        b19 = time.time()
        fonk1(b17)
        b20 = time.time() - b19
        b19 = time.time()
        fonk2(b17)
        b21 = time.time() - b19
        print(f"Bellman-Ford timing: {b20}")
        print(f"Floyd-Warshall timing: {b21}")
if b22 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    fonk4(sys.argv[2], sys.argv[1])