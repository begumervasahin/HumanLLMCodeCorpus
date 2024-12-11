import sys
import re
import time
import itertools
import math
b1 = re.compile("(\\d+)\\s(\\d+)")
b2 = re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")
b3 = []
b4 = []
def fonk1(b26):
    b5 = []
    print("\nEntered BellmanFord")
    b6 = b26[0]
    b7 = b26[1]
    b8 = list(itertools.permutations(b6,2))
    b9 = float('b9')
    for i in range(len(b6)):
        b10 = [b9] * len(b6)
        b11 = b6[i]
        b10[b11]=0
        for j in range(1, len(b6)):
            for i in range(len(b8)):
                b12 = b8[i][0]
                b13 = b8[i][1]
                if (b10[b13] > b10[b12] + float(b7[b12][b13])):
                    b10[b13] = b10[b12] + float(b7[b12][b13])
        b14 = False
        for i in range(len(b8)):
            b12 = b8[i][0]
            b13 = b8[i][1]
            if (b10[b13] > b10[b12] + float(b7[b12][b13])):
                b14 = True
        for i in range(len(b6)):
            if b10[i] != float('b9'):
                b10[i] = int(b10[i])
            b15 = ((str(b11),str(b6[i])),str(b10[i]))
            b5.append(b15)
    print("\npathPairs")
    print(b5)
    if(b14):
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    print("\nExiting BellmanFord\n")
    return b5
def fonk2(b26):
    b5 = []
    print("\nEntered FloydWarshall")
    b6 = b26[0]
    b7 = b26[1]
    b9 = float('b9')
    b10 = b7
    for i in b6:
        for j in b6:
            b10[i][j] = float(b10[i][j])
    for b13 in b6:
        b10[b13][b13]=0
    for k in b6:
        for i in b6:
            for j in b6:
                if b10[i][j] > b10[i][k] + b10[k][j]:
                    b10[i][j] = b10[i][k] + b10[k][j]
    for i in b6:
        for j in b6:
            if b10[i][j] != float('b9'):
                b10[i][j] = int(b10[i][j])
            b15 = ( (str(i), str(j)) , str(b10[i][j]) )
            b5.append(b15)
    print("\npathPairs")
    print(b5)
    print("\nExiting FloydWarshall\n")
    return b5
def fonk3(filename):
    global b3
    global b4
    b16 = open(filename,'r')
    b17 = b16.readline()
    b18 = b1.match(b17)
    if not b18:
        print(b17+" not properly formatted")
        quit(1)
    b3 = list(range(int(b18.group(1))))
    b4 = []
    for i in range(len(b3)):
        b19 = []
        for j in range(len(b3)):
            b19.append(float("b9"))
        b4.append(b19)
    for b20 in b16.readlines():
        b20 = b20.strip()
        b21 = b2.match(b20)
        if b21:
            b22 = b21.group(1)
            b23 = b21.group(2)
            if int(b22) > len(b3) or int(b23) > len(b3):
                print("Attempting to insert an edge between "+b22+" and "+b23+" in a graph with "+b3+" b3")
                quit(1)
            b24 = b21.group(3)
            b4[int(b22)][int(b23)]=b24
    print("\nvertex    b4")
    for i in range(len(b4)):
        print(str(b3[i]) + "         " + str(b4[i]))
    print("")
    return (b3,b4)
def fonk4(filename,b25):
    b25 = b25[1:]
    b26 = fonk3(filename)
    if b25 = = 'b' or b25 == 'B':
        b27 = time.clock()
        fonk1(b26)
        b28 = time.clock()
        b29 = b28-b27
        print("\nBellman-Ford timing: "+str(b29)+"\n")
    if b25 = = 'f' or b25 == 'F':
        b27 = time.clock()
        fonk2(b26)
        b28 = time.clock()
        b30 = b28-b27
        print("Floyd-Warshall timing: "+str(b30))
    if b25 = = "both":
        print("
        b27 = time.clock()
        fonk1(b26)
        b28 = time.clock()
        b29 = b28-b27
        print("
        b27 = time.clock()
        fonk2(b26)
        b28 = time.clock()
        b30 = b28-b27
        print("
        print("\nBellman-Ford timing: "+str(b29))
        print("Floyd-Warshall timing: "+str(b30)+"\n")
if b31 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk4(sys.argv[2], sys.argv[1])