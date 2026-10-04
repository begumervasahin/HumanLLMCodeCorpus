import sys
import re
import itertools
import time
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b15):
    b9, b3 = b15
    b4 = len(b9)
    b5 = float('b5')
    b6 = [b5] * b4
    b6[0] = 0
    for _ in range(b4 - 1):
        for u, v in itertools.permutations(b9, 2):
            if b6[v] > b6[u] + float(b3[u][v]):
                b6[v] = b6[u] + float(b3[u][v])
    for u, v in itertools.permutations(b9, 2):
        if b6[v] > b6[u] + float(b3[u][v]):
            print("A negative cycle exists")
            return 'NULL'
    print("No negative cycles exist")
    return b6
def fonk2(b15):
    b9, b3 = b15
    b6 = [row[:] for row in b3]
    b4 = len(b9)
    for k in range(b4):
        for i in range(b4):
            for j in range(b4):
                b6[i][j] = min(b6[i][j], b6[i][k] + b6[k][j])
    return b6
def fonk3(filename):
    with open(filename, 'r') as file:
        b7 = file.readline().strip()
        b8 = b1.match(b7)
        if not b8:
            print(f"{b7} not properly formatted")
            sys.exit(1)
        b4 = int(b8.group(1))
        b9 = list(range(b4))
        b3 = [[float('b5')] * b4 for _ in range(b4)]
        for b10 in file:
            b10 = b10.strip()
            b11 = b2.match(b10)
            if b11:
                b12 = int(b11.group(1))
                b13 = int(b11.group(2))
                b14 = int(b11.group(3))
                b3[b12][b13] = b14
    print("\nvertex    b3")
    for i, edge_row in enumerate(b3):
        print(f"{b9[i]}         {edge_row}")
    print()
    return b9, b3
def fonk4(filename, b16):
    b15 = fonk3(filename)
    b16 = b16[1:].lower()
    if b16 = = 'b':
        print("\nRunning Bellman-Ford")
        b17 = fonk1(b15)
        print(f"Result: {b17}")
    elif b16 = = 'f':
        print("\nRunning Floyd-Warshall")
        b17 = fonk2(b15)
        print(f"Result: {b17}")
    elif b16 = = "both":
        print("\nRunning Both Algorithms")
        b18 = time.time()
        fonk1(b15)
        b19 = time.time() - b18
        b18 = time.time()
        fonk2(b15)
        b20 = time.time() - b18
        print(f"Bellman-Ford timing: {b19:.6f} seconds")
        print(f"Floyd-Warshall timing: {b20:.6f} seconds")
if b21 = = '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    fonk4(sys.argv[2], sys.argv[1])