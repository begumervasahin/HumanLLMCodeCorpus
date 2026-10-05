import sys
import re
import time
import itertools
b1 = re.compile(r"(\d+)\s(\d+)")
b2 = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
b3 = []
b4 = []
def fonk1(b25):
    b5 = []
    print("\nEntered BellmanFord\n")
    for i in b25:
        print(i)
    b6 = b25[0]
    b7 = b25[1]
    print("\nV")
    print(b6)
    print("\nE")
    print(b7)
    print("\nLength of b7")
    print(len(b7))
    print("\nPermutations of b6")
    b8 = list(itertools.permutations(b6, 2))
    for i in b8:
        print(i)
    print("\n")
    print(b8[1][1])
    b9 = float('b9')
    b10 = [b9] * len(b6)
    b10[0] = 0
    print("\nDist before: ")
    for i in b10:
        print(i)
    print("\nLength(b8)")
    print(len(b8))
    print("\nU and b6 combinations: \n")
    print("|b6|")
    print(len(b6))
    print("\n")
    for j in range(1, len(b6)):
        print("\n")
        for i in range(len(b8)):
            b11 = b8[i][0]
            b12 = b8[i][1]
            print("b11: " + str(b11) + "   b12: " + str(b12))
            print("Weight: " + str(b7[b11][b12]))
            print("\n")
            if (b10[b12] > b10[b11] + float(b7[b11][b12])):
                b10[b12] = b10[b11] + float(b7[b11][b12])
    print("\n")
    print("\nDist after: ")
    for i in b10:
        print(i)
    print("\nChecking if negative cycle exists: ")
    b13 = False
    for i in range(len(b8)):
        b11 = b8[i][0]
        b12 = b8[i][1]
        if (b10[b12] > b10[b11] + float(b7[b11][b12])):
            b13 = True
    if(b13):
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    b14 = [(('0', '0'), '0')]
    print(b14)
    print("\nExiting BellmanFord")
    return b5
def fonk2(b25):
    b5 = []
    return b5
def fonk3(filename):
    global b3
    global b4
    b15 = open(filename, 'r')
    b16 = b15.readline()
    b17 = b1.match(b16)
    if not b17:
        print(b16 + " not properly formatted")
        quit(1)
    b3 = list(range(int(b17.group(1))))
    b4 = []
    for i in range(len(b3)):
        b18 = []
        for j in range(len(b3)):
            b18.append(float("b9"))
        b4.append(b18)
    for b19 in b15.readlines():
        b19 = b19.strip()
        b20 = b2.match(b19)
        if b20:
            b21 = b20.group(1)
            b22 = b20.group(2)
            if int(b21) > len(b3) or int(b22) > len(b3):
                print("Attempting to insert an edge between " + b21 + " and " + b22 + " in a graph with " + b3 + " b3")
                quit(1)
            b23 = b20.group(3)
            b4[int(b21)][int(b22)] = b23
    print("\n")
    print("Vertex    Edges")
    for i in range(len(b4)):
        print(str(b3[i]) + "         " + str(b4[i]))
    print("\n")
    return (b3, b4)
def fonk4(filename, b24):
    b24 = b24[1:]
    b25 = fonk3(filename)
    print("\nAlgorithm: ")
    print(b24)
    if b24 = = 'b' or b24 == 'B':
        print("\nAbout to call BellmanFord")
        fonk1(b25)
        print("\nCalled BellmanFord\n")
    if b24 = = 'f' or b24 == 'F':
        fonk2(b25)
    if b24 = = "both":
        b26 = time.clock()
        fonk1(b25)
        b27 = time.clock()
        b28 = b27 - b26
        b26 = time.clock()
        fonk2(b25)
        b27 = time.clock()
        b29 = b27 - b26
        print("Bellman-Ford timing: " + str(b28))
        print("Floyd-Warshall timing: " + str(b29))
if b30 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])