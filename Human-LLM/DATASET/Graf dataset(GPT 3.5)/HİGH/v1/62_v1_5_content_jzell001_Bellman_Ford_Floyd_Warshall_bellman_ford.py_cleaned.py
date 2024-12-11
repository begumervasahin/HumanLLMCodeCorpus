import sys
import re
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b22):
    b3 = []
    print("\nEntered BellmanFord")
    V, b4 = b22
    b5 = [(u, b9) for u in V for b9 in V if u != b9]
    b6 = float('b6')
    for i in range(len(V)):
        b7 = [b6] * len(V)
        b8 = V[i]
        b7[b8] = 0
        for j in range(1, len(V)):
            for k in range(len(b5)):
                u, b9 = b5[k]
                if b7[b9] > b7[u] + float(b4[u][b9]):
                    b7[b9] = b7[u] + float(b4[u][b9])
        b10 = False
        for k in range(len(b5)):
            u, b9 = b5[k]
            if b7[b9] > b7[u] + float(b4[u][b9]):
                b10 = True
        for i in range(len(V)):
            if b7[i] != float('b6'):
                b7[i] = int(b7[i])
            b11 = ((str(b8), str(V[i])), str(b7[i]))
            b3.append(b11)
    print("\npathPairs")
    print(b3)
    if b10:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    print("\nExiting BellmanFord\n")
    return b3
def fonk2(b22):
    b3 = []
    print("\nEntered FloydWarshall")
    V, b4 = b22
    b6 = float('b6')
    b7 = b4
    for i in V:
        for j in V:
            b7[i][j] = float(b7[i][j])
    for b9 in V:
        b7[b9][b9] = 0
    for k in V:
        for i in V:
            for j in V:
                if b7[i][j] > b7[i][k] + b7[k][j]:
                    b7[i][j] = b7[i][k] + b7[k][j]
    for i in V:
        for j in V:
            if b7[i][j] != float('b6'):
                b7[i][j] = int(b7[i][j])
            b11 = ((str(i), str(j)), str(b7[i][j]))
            b3.append(b11)
    print("\npathPairs")
    print(b3)
    print("\nExiting FloydWarshall\n")
    return b3
def fonk3(filename):
    b12 = []
    b13 = []
    with open(filename, 'r') as infile:
        b14 = infile.readline().strip()
        b15 = b1.match(b14)
        if not b15:
            print(b14 + " not properly formatted")
            quit(1)
        b12 = list(range(int(b15.group(1))))
        b13 = [[float("b6")] * len(b12) for _ in range(len(b12))]
        for b16 in infile.readlines():
            b16 = b16.strip()
            b17 = b2.match(b16)
            if b17:
                b18 = int(b17.group(1))
                b19 = int(b17.group(2))
                if b18 > len(b12) or b19 > len(b12):
                    print(f"Attempting to insert an edge between {b18} and {b19} in a b22 with {len(b12)} b12")
                    quit(1)
                b20 = b17.group(3)
                b13[b18][b19] = b20
    print("\nvertex    b13")
    for i in range(len(b13)):
        print(str(b12[i]) + "         " + str(b13[i]))
    print("")
    return b12, b13
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