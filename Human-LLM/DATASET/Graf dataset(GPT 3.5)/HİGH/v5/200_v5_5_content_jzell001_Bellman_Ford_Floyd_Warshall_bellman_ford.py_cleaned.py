import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
def fonk1(graph):
    b5 = []
    print("\nEntered Bellman-Ford")
    V, b6 = graph
    b7 = list(itertools.b7(V, 2))
    b8 = float('b8')
    for b16 in V:
        b9 = [b8] * len(V)
        b9[b16] = 0
        for _ in range(1, len(V)):
            for u, v in b7:
                if b9[v] > b9[u] + float(b6[u][v]):
                    b9[v] = b9[u] + float(b6[u][v])
        b10 = any(b9[v] > b9[u] + float(b6[u][v]) for u, v in b7)
        for i in range(len(V)):
            if b9[i] != float('b8'):
                b9[i] = int(b9[i])
            b11 = ((str(b16), str(V[i])), str(b9[i]))
            b5.append(b11)
    print("\npathPairs")
    print(b5)
    if b10:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    print("\nExiting Bellman-Ford\n")
    return b5
def fonk2(graph):
    b5 = []
    print("\nEntered Floyd-Warshall")
    V, b6 = graph
    b8 = float('b8')
    b9 = b6
    for i in V:
        for j in V:
            b9[i][j] = float(b9[i][j])
    for v in V:
        b9[v][v] = 0
    for k in V:
        for i in V:
            for j in V:
                if b9[i][j] > b9[i][k] + b9[k][j]:
                    b9[i][j] = b9[i][k] + b9[k][j]
    for i in V:
        for j in V:
            if b9[i][j] != float('b8'):
                b9[i][j] = int(b9[i][j])
            b11 = ((str(i), str(j)), str(b9[i][j]))
            b5.append(b11)
    print("\npathPairs")
    print(b5)
    print("\nExiting Floyd-Warshall\n")
    return b5
def fonk3(filename):
    global b3, b4
    with open(filename, 'r') as infile:
        b12 = infile.readline().strip()
        b13 = b1.match(b12)
        if not b13:
            print(b12 + " not properly formatted")
            quit(1)
        b3 = list(range(int(b13.group(1))))
        b4 = [[float("b8")] * len(b3) for _ in range(len(b3))]
        for b14 in infile.readlines():
            b14 = b14.strip()
            b15 = b2.match(b14)
            if b15:
                b16 = int(b15.group(1))
                b17 = int(b15.group(2))
                if b16 > len(b3) or b17 > len(b3):
                    print(f"Attempting to insert an edge between {b16} and {b17} in a graph with {len(b3)} b3")
                    quit(1)
                b18 = b15.group(3)
                b4[b16][b17] = b18
    print("\nvertex    b4")
    for i in range(len(b4)):
        print(str(b3[i]) + "         " + str(b4[i]))
    print("")
    return b3, b4
def fonk4(filename, b19):
    b19 = b19[1:]
    b20 = fonk3(filename)
    if b19 = = 'b' or b19 == 'B':
        b21 = time.clock()
        fonk1(b20)
        b22 = time.clock()
        b23 = b22 - b21
        print("\nBellman-Ford timing: " + str(b23) + "\n")
    if b19 = = 'f' or b19 == 'F':
        b21 = time.clock()
        fonk2(b20)
        b22 = time.clock()
        b24 = b22 - b21
        print("Floyd-Warshall timing: " + str(b24))
    if b19 = = "both":
        b21 = time.clock()
        fonk1(b20)
        b22 = time.clock()
        b23 = b22 - b21
        print("\nBellman-Ford timing: " + str(b23))
        b21 = time.clock()
        fonk2(b20)
        b22 = time.clock()
        b24 = b22 - b21
        print("Floyd-Warshall timing: " + str(b24) + "\n")
if b25 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])