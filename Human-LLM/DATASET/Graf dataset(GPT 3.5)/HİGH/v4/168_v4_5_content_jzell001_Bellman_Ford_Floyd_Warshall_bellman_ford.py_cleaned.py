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
    for index in range(len(V)):
        b9 = [b8] * len(V)
        b10 = V[index]
        b9[b10] = 0
        for _ in range(1, len(V)):
            for i in range(len(b7)):
                u, b11 = b7[i]
                if b9[b11] > b9[u] + float(b6[u][b11]):
                    b9[b11] = b9[u] + float(b6[u][b11])
        b12 = False
        for i in range(len(b7)):
            u, b11 = b7[i]
            if b9[b11] > b9[u] + float(b6[u][b11]):
                b12 = True
        for i in range(len(V)):
            if b9[i] != float('b8'):
                b9[i] = int(b9[i])
            b13 = ((str(b10), str(V[i])), str(b9[i]))
            b5.append(b13)
    print("\npathPairs")
    print(b5)
    if b12:
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
    for b11 in V:
        b9[b11][b11] = 0
    for k in V:
        for i in V:
            for j in V:
                if b9[i][j] > b9[i][k] + b9[k][j]:
                    b9[i][j] = b9[i][k] + b9[k][j]
    for i in V:
        for j in V:
            if b9[i][j] != float('b8'):
                b9[i][j] = int(b9[i][j])
            b13 = ((str(i), str(j)), str(b9[i][j]))
            b5.append(b13)
    print("\npathPairs")
    print(b5)
    print("\nExiting Floyd-Warshall\n")
    return b5
def fonk3(filename):
    global b3, b4
    b14 = open(filename, 'r')
    b15 = b14.readline().strip()
    b16 = b1.match(b15)
    if not b16:
        print(b15 + " not properly formatted")
        quit(1)
    b3 = list(range(int(b16.group(1))))
    b4 = [[float("b8")] * len(b3) for _ in range(len(b3))]
    for b17 in b14.readlines():
        b17 = b17.strip()
        b18 = b2.match(b17)
        if b18:
            b10 = int(b18.group(1))
            b19 = int(b18.group(2))
            if b10 > len(b3) or b19 > len(b3):
                print(f"Attempting to insert an edge between {b10} and {b19} in a graph with {len(b3)} b3")
                quit(1)
            b20 = b18.group(3)
            b4[b10][b19] = b20
    print("\nvertex    b4")
    for i in range(len(b4)):
        print(str(b3[i]) + "         " + str(b4[i]))
    print("")
    return b3, b4
def fonk4(filename, b21):
    b21 = b21[1:]
    b22 = fonk3(filename)
    if b21 = = 'b' or b21 == 'B':
        b23 = time.clock()
        fonk1(b22)
        b24 = time.clock()
        b25 = b24 - b23
        print("\nBellman-Ford timing: " + str(b25) + "\n")
    if b21 = = 'f' or b21 == 'F':
        b23 = time.clock()
        fonk2(b22)
        b24 = time.clock()
        b26 = b24 - b23
        print("Floyd-Warshall timing: " + str(b26))
    if b21 = = "both":
        b23 = time.clock()
        fonk1(b22)
        b24 = time.clock()
        b25 = b24 - b23
        print("\nBellman-Ford timing: " + str(b25))
        b23 = time.clock()
        fonk2(b22)
        b24 = time.clock()
        b26 = b24 - b23
        print("Floyd-Warshall timing: " + str(b26) + "\n")
if b27 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])