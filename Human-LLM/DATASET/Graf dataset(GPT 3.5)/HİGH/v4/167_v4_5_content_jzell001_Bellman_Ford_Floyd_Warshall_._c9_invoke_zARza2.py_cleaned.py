import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
def fonk1(b20):
    b5 = []
    print("\nEntered Bellman-Ford\n")
    V, b6 = b20
    print("\nV:", V)
    print("\nE:", b6)
    print("\nLength of b6:", len(b6))
    b7 = list(itertools.permutations(V, 2))
    print("\nPermutations of V:")
    for permutation in b7:
        print(permutation)
    print("\n")
    b8 = float('b8')
    b9 = [b8] * len(V)
    b9[0] = 0
    print("\nDist before:")
    for distance in b9:
        print(distance)
    print("\nLength of b7:", len(b7))
    print("\nU and V combinations:\n")
    print("|V|:", len(V))
    print("\n")
    for j in range(1, len(V)):
        print("\n")
        for i in range(len(b7)):
            u, b10 = b7[i]
            print("u:", u, "b10:", b10)
            print("Weight:", b6[u][b10])
            print("\n")
            if b9[b10] > b9[u] + float(b6[u][b10]):
                b9[b10] = b9[u] + float(b6[u][b10])
    print("\nDist after:")
    for distance in b9:
        print(distance)
    print("\nChecking if negative cycle exists:")
    b11 = False
    for i in range(len(b7)):
        u, b10 = b7[i]
        if b9[b10] > b9[u] + float(b6[u][b10]):
            b11 = True
    if b11:
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    b5 = [(('0', '0'), '0')]
    print(b5)
    print("\nExiting Bellman-Ford")
    return b5
def fonk2(b20):
    b5 = []
    return b5
def fonk3(filename):
    global b3, b4
    with open(filename, 'r') as infile:
        b12 = infile.readline().strip()
        b13 = b1.match(b12)
        if not b13:
            print(f"{b12} not properly formatted")
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
                    print(f"Attempting to insert an edge between {b16} and {b17} in a b20 with {len(b3)} b3")
                    quit(1)
                b18 = b15.group(3)
                b4[b16][b17] = b18
    print("\nVertex    Edges")
    for i in range(len(b4)):
        print(f"{b3[i]}         {b4[i]}")
    print("\n")
    return b3, b4
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