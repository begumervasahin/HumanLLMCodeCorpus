import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b20):
    print("\nEntered Bellman-Ford\n")
    b13, b3 = b20
    print("\nV:", b13)
    print("\nE:", b3)
    print("\nLength of E:", len(b3))
    b4 = list(itertools.permutations(b13, 2))
    print("\nPermutations of V:")
    for permutation in b4:
        print(permutation)
    print("\n")
    b5 = float('b5')
    b6 = [b5] * len(b13)
    b6[0] = 0
    print("\nDist before:")
    print(*b6, b7 = '\n')
    print("\nLength of b4:", len(b4))
    print("\nU and V combinations:\n")
    print("|V|:", len(b13))
    print("\n")
    for j in range(1, len(b13)):
        print("\n")
        for i in range(len(b4)):
            u, b8 = b4[i]
            print("u:", u, "b8:", b8)
            print("Weight:", b3[u][b8])
            print("\n")
            if b6[b8] > b6[u] + float(b3[u][b8]):
                b6[b8] = b6[u] + float(b3[u][b8])
    print("\nDist after:")
    print(*b6, b7 = '\n')
    print("\nChecking if negative cycle exists:")
    b9 = any(b6[b8] > b6[u] + float(b3[u][b8]) for u, b8 in b4)
    if b9:
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    b10 = [(('0', '0'), '0')]
    print(b10)
    print("\nExiting Bellman-Ford")
    return b10
def fonk2(b20):
    b10 = []
    return b10
def fonk3(filename):
    with open(filename, 'r') as infile:
        b11 = infile.readline().strip()
        b12 = b1.match(b11)
        if not b12:
            print(f"{b11} not properly formatted")
            quit(1)
        b13 = list(range(int(b12.group(1))))
        b3 = [[float("b5")] * len(b13) for _ in range(len(b13))]
        for b14 in infile.readlines():
            b14 = b14.strip()
            b15 = b2.match(b14)
            if b15:
                b16 = int(b15.group(1))
                b17 = int(b15.group(2))
                if b16 > len(b13) or b17 > len(b13):
                    print(f"Attempting to insert an edge between {b16} and {b17} in a b20 with {len(b13)} b13")
                    quit(1)
                b18 = b15.group(3)
                b3[b16][b17] = b18
    print("\nVertex    Edges")
    for i in range(len(b3)):
        print(f"{b13[i]}         {b3[i]}")
    print("\n")
    return b13, b3
def fonk4(filename, b19):
    b19 = b19[1:]
    b20 = fonk3(filename)
    print("\nAlgorithm:", b19)
    if b19 = = 'b' or b19 == 'B':
        print("\nAbout to call Bellman-Ford")
        fonk1(b20)
        print("\nCalled Bellman-Ford\n")
    if b19 = = 'f' or b19 == 'F':
        fonk2(b20)
    if b19 = = "both":
        b21 = time.clock()
        fonk1(b20)
        b22 = time.clock()
        b23 = b22 - b21
        b21 = time.clock()
        fonk2(b20)
        b22 = time.clock()
        b24 = b22 - b21
        print("Bellman-Ford timing:", b23)
        print("Floyd-Warshall timing:", b24)
if b25 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])