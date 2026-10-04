import sys
import re
import itertools
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b17):
    b11, b3 = b17
    b4 = len(b11)
    b5 = float('b5')
    b6 = []
    for i in range(b4):
        b7 = [b5] * b4
        b7[i] = 0
        for _ in range(b4 - 1):
            for u, v in itertools.permutations(b11, 2):
                if b7[v] > b7[u] + float(b3[u][v]):
                    b7[v] = b7[u] + float(b3[u][v])
        b8 = False
        for u, v in itertools.permutations(b11, 2):
            if b7[v] > b7[u] + float(b3[u][v]):
                b8 = True
        for j in range(b4):
            if b7[j] != b5:
                b7[j] = int(b7[j])
            b6.append(((str(i), str(j)), str(b7[j])))
    if b8:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    return b6
def fonk2(b17):
    b11, b3 = b17
    b4 = len(b11)
    b7 = [[float(b3[i][j]) for j in range(b4)] for i in range(b4)]
    for v in b11:
        b7[v][v] = 0
    for k in b11:
        for i in b11:
            for j in b11:
                if b7[i][j] > b7[i][k] + b7[k][j]:
                    b7[i][j] = b7[i][k] + b7[k][j]
    b6 = []
    for i in b11:
        for j in b11:
            if b7[i][j] != float('b5'):
                b7[i][j] = int(b7[i][j])
            b6.append(((str(i), str(j)), str(b7[i][j])))
    return b6
def fonk3(filename):
    with open(filename, 'r') as file:
        b9 = file.readline().strip()
        b10 = b1.match(b9)
        if not b10:
            print(f"{b9} not properly formatted")
            sys.exit(1)
        b4 = int(b10.group(1))
        b11 = list(range(b4))
        b3 = [[float('b5')] * b4 for _ in range(b4)]
        for b12 in file:
            b12 = b12.strip()
            b13 = b2.match(b12)
            if b13:
                b14 = int(b13.group(1))
                b15 = int(b13.group(2))
                b16 = int(b13.group(3))
                b3[b14][b15] = b16
    print("\nvertex    b3")
    for i, edge_row in enumerate(b3):
        print(f"{b11[i]}         {edge_row}")
    print()
    return b11, b3
def fonk4(filename, b18):
    b17 = fonk3(filename)
    b18 = b18[1:].lower()
    if b18 = = 'b':
        b19 = time.time()
        b20 = fonk1(b17)
        b21 = time.time()
        print(f"\nBellman-Ford timing: {b21 - b19:.6f} seconds")
        print(f"Result: {b20}")
    elif b18 = = 'f':
        b19 = time.time()
        b20 = fonk2(b17)
        b21 = time.time()
        print(f"\nFloyd-Warshall timing: {b21 - b19:.6f} seconds")
        print(f"Result: {b20}")
    elif b18 = = "both":
        print("\nRunning Both Algorithms")
        b19 = time.time()
        fonk1(b17)
        b22 = time.time() - b19
        b19 = time.time()
        fonk2(b17)
        b23 = time.time() - b19
        print(f"Bellman-Ford timing: {b22:.6f} seconds")
        print(f"Floyd-Warshall timing: {b23:.6f} seconds")
if b24 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b|both> <input_file>")
        sys.exit(1)
    fonk4(sys.argv[2], sys.argv[1])