import sys
import re
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b20):
    b3 = []
    print("\nEntered Bellman-Ford")
    V, b4 = b20
    b5 = [(u, v) for u in V for v in V if u != v]
    b6 = float('b6')
    for index in range(len(V)):
        b7 = [b6] * len(V)
        b8 = V[index]
        b7[b8] = 0
        for _ in range(1, len(V)):
            for u, v in b5:
                if b7[v] > b7[u] + float(b4[u][v]):
                    b7[v] = b7[u] + float(b4[u][v])
        b9 = False
        for u, v in b5:
            if b7[v] > b7[u] + float(b4[u][v]):
                b9 = True
        for i in range(len(V)):
            if b7[i] != float('b6'):
                b7[i] = int(b7[i])
            b10 = ((str(b8), str(V[i])), str(b7[i]))
            b3.append(b10)
    print("\npathPairs")
    print(b3)
    if b9:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    print("\nExiting Bellman-Ford\n")
    return b3
def fonk2(b20):
    b3 = []
    print("\nEntered Floyd-Warshall")
    V, b4 = b20
    b6 = float('b6')
    b7 = b4
    for i in V:
        for j in V:
            b7[i][j] = float(b7[i][j])
    for v in V:
        b7[v][v] = 0
    for k in V:
        for i in V:
            for j in V:
                if b7[i][j] > b7[i][k] + b7[k][j]:
                    b7[i][j] = b7[i][k] + b7[k][j]
    for i in V:
        for j in V:
            if b7[i][j] != float('b6'):
                b7[i][j] = int(b7[i][j])
            b10 = ((str(i), str(j)), str(b7[i][j]))
            b3.append(b10)
    print("\npathPairs")
    print(b3)
    print("\nExiting Floyd-Warshall\n")
    return b3
def fonk3(filename):
    b11 = []
    b12 = []
    with open(filename, 'r') as infile:
        b13 = infile.readline().strip()
        b14 = b1.match(b13)
        if not b14:
            print(b13 + " not properly formatted")
            quit(1)
        b11 = list(range(int(b14.group(1))))
        b12 = [[float("b6")] * len(b11) for _ in range(len(b11))]
        for b15 in infile.readlines():
            b15 = b15.strip()
            b16 = b2.match(b15)
            if b16:
                b8 = int(b16.group(1))
                b17 = int(b16.group(2))
                if b8 > len(b11) or b17 > len(b11):
                    print(f"Attempting to insert an edge between {b8} and {b17} in a b20 with {len(b11)} b11")
                    quit(1)
                b18 = b16.group(3)
                b12[b8][b17] = b18
    print("\nvertex    b12")
    for i in range(len(b12)):
        print(str(b11[i]) + "         " + str(b12[i]))
    print("")
    return b11, b12
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