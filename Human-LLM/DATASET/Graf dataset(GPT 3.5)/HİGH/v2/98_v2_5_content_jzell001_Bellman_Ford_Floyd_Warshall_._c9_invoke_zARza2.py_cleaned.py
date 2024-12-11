import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
def fonk1(b22):
    b5 = []
    print("\nEntered Bellman-Ford\n")
    b6 = b22[0]
    b7 = b22[1]
    print("\nV:", b6)
    print("\nE:", b7)
    print("\nLength of b7:", len(b7))
    b8 = list(itertools.permutations(b6, 2))
    print("\nPermutations of b6:")
    for permutation in b8:
        print(permutation)
    print("\n")
    b9 = float('b9')
    b10 = [b9] * len(b6)
    b10[0] = 0
    print("\nDist before:")
    for distance in b10:
        print(distance)
    print("\nLength of b8:", len(b8))
    print("\nU and b6 combinations:\n")
    print("|b6|:", len(b6))
    print("\n")
    for j in range(1, len(b6)):
        print("\n")
        for i in range(len(b8)):
            b11 = b8[i][0]
            b12 = b8[i][1]
            print("b11:", b11, "b12:", b12)
            print("Weight:", b7[b11][b12])
            print("\n")
            if b10[b12] > b10[b11] + float(b7[b11][b12]):
                b10[b12] = b10[b11] + float(b7[b11][b12])
    print("\nDist after:")
    for distance in b10:
        print(distance)
    print("\nChecking if negative cycle exists:")
    b13 = False
    for i in range(len(b8)):
        b11 = b8[i][0]
        b12 = b8[i][1]
        if b10[b12] > b10[b11] + float(b7[b11][b12]):
            b13 = True
    if b13:
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    b5 = [(('0', '0'), '0')]
    print(b5)
    print("\nExiting Bellman-Ford")
    return b5
def fonk2(b22):
    b5 = []
    return b5
def fonk3(filename):
    global b3
    global b4
    with open(filename, 'r') as infile:
        b14 = infile.readline()
        b15 = b1.match(b14)
        if not b15:
            print(b14 + " not properly formatted")
            quit(1)
        b3 = list(range(int(b15.group(1))))
        b4 = [[float("b9")] * len(b3) for _ in range(len(b3))]
        for b16 in infile.readlines():
            b16 = b16.strip()
            b17 = b2.match(b16)
            if b17:
                b18 = int(b17.group(1))
                b19 = int(b17.group(2))
                if b18 > len(b3) or b19 > len(b3):
                    print(f"Attempting to insert an edge between {b18} and {b19} in a b22 with {len(b3)} b3")
                    quit(1)
                b20 = b17.group(3)
                b4[b18][b19] = b20
    print("\nVertex    Edges")
    for i in range(len(b4)):
        print(f"{b3[i]}         {b4[i]}")
    print("\n")
    return (b3, b4)
def fonk4(filename, b21):
    b21 = b21[1:]
    b22 = fonk3(filename)
    print("\nAlgorithm:", b21)
    if b21 = = 'b' or b21 == 'B':
        print("\nAbout to call Bellman-Ford")
        fonk1(b22)
        print("\nCalled Bellman-Ford\n")
    if b21 = = 'f' or b21 == 'F':
        fonk2(b22)
    if b21 = = "both":
        b23 = time.clock()
        fonk1(b22)
        b24 = time.clock()
        b25 = b24 - b23
        b23 = time.clock()
        fonk2(b22)
        b24 = time.clock()
        b26 = b24 - b23
        print("Bellman-Ford timing:", b25)
        print("Floyd-Warshall timing:", b26)
if b27 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])