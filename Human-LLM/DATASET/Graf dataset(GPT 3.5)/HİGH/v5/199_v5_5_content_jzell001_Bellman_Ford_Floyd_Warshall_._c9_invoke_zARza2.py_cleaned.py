import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def fonk1(b19):
    b12, b3 = b19
    print("\nEntered Bellman-Ford\n")
    print("\nV:", b12)
    print("\nE:", b3)
    print("\nLength of E:", len(b3))
    b4 = list(itertools.permutations(b12, 2))
    print("\nPermutations of V:")
    for permutation in b4:
        print(permutation)
    print("\n")
    b5 = float('b5')
    b6 = [b5] * len(b12)
    b6[0] = 0
    print("\nDist before:")
    for distance in b6:
        print(distance)
    print("\nLength of b4:", len(b4))
    print("\nU and V combinations:\n")
    print("|V|:", len(b12))
    print("\n")
    for j in range(1, len(b12)):
        print("\n")
        for i in range(len(b4)):
            u, b7 = b4[i]
            print("u:", u, "b7:", b7)
            print("Weight:", b3[u][b7])
            print("\n")
            if b6[b7] > b6[u] + float(b3[u][b7]):
                b6[b7] = b6[u] + float(b3[u][b7])
    print("\nDist after:")
    for distance in b6:
        print(distance)
    print("\nChecking if negative cycle exists:")
    b8 = False
    for i in range(len(b4)):
        u, b7 = b4[i]
        if b6[b7] > b6[u] + float(b3[u][b7]):
            b8 = True
    if b8:
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    b9 = [(('0', '0'), '0')]
    print(b9)
    print("\nExiting Bellman-Ford")
    return b9
def fonk2(b19):
    b9 = []
    return b9
def fonk3(filename):
    with open(filename, 'r') as infile:
        b10 = infile.readline().strip()
        b11 = b1.match(b10)
        if not b11:
            print(f"{b10} not properly formatted")
            quit(1)
        b12 = list(range(int(b11.group(1))))
        b3 = [[float("b5")] * len(b12) for _ in range(len(b12))]
        for b13 in infile.readlines():
            b13 = b13.strip()
            b14 = b2.match(b13)
            if b14:
                b15 = int(b14.group(1))
                b16 = int(b14.group(2))
                if b15 > len(b12) or b16 > len(b12):
                    print(f"Attempting to insert an edge between {b15} and {b16} in a b19 with {len(b12)} b12")
                    quit(1)
                b17 = b14.group(3)
                b3[b15][b16] = b17
    print("\nVertex    Edges")
    for i in range(len(b3)):
        print(f"{b12[i]}         {b3[i]}")
    print("\n")
    return b12, b3
def fonk4(filename, b18):
    b18 = b18[1:]
    b19 = fonk3(filename)
    print("\nAlgorithm:", b18)
    if b18 = = 'b' or b18 == 'B':
        print("\nAbout to call Bellman-Ford")
        fonk1(b19)
        print("\nCalled Bellman-Ford\n")
    if b18 = = 'f' or b18 == 'F':
        fonk2(b19)
    if b18 = = "both":
        b20 = time.clock()
        fonk1(b19)
        b21 = time.clock()
        b22 = b21 - b20
        b20 = time.clock()
        fonk2(b19)
        b21 = time.clock()
        b23 = b21 - b20
        print("Bellman-Ford timing:", b22)
        print("Floyd-Warshall timing:", b23)
if b24 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])