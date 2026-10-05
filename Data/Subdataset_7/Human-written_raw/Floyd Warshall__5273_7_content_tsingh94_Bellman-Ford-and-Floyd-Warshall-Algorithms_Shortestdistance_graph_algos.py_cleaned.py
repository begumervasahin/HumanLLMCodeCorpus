import os
import re
import sys
import time
import math
b1 = re.compile("(\\d+)\\s(\\d+)")
b2 = re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")
def change_edge_matrix (b4):
    for v in range(0 , len(b4)):
        for e in range(0 , len(b4[v])):
            if type(b4[v][e]) is str:
                b4[v][e] = int(b4[v][e])
    return b4
def fonk1(b27):
    b3 = []
    b4 = change_edge_matrix(b27[1])
    b5 = b4[0][0]
    for n in range(0, len(b27[0])):
        b6 = []
        b7 = []
        for b8 in range(0, len(b27[0])):
            if b8 = = n:
                b7.append(0)
            else:
                b7.append(b5)
        b6 = b7
        for j in range(0, len(b27[0])):
            if j > 0:
                b9 = []
                for i in range(0, len(b4)):
                    if i != n:
                        b10 = b6[i]
                        for k in range(0, len(b4[i])):
                            b11 = b4[k][i]
                            b12 = b6[k]
                            if (b11 != b5) and (b12 != b5):
                                if b11 + b12 < b10:
                                        b10 = b11 + b12
                        b9.append(b10)
                    else:
                        b9.append(0)
                b6 = b9
        b3.append(b6)
    return b3
def fonk2(b27):
    b3 = []
    b3 = change_edge_matrix(b27[1])
    for i in range(0, len(b27[0])):
    	b3[i][i] = 0
    for k in range(0, len(b27[0])):
        for i in range(0, len(b3)):
            for j in range(0, len(b3[i])):
                b13 = b3[i][k] + b3[k][j]
                if b13 < b3[i][j]:
                    b3[i][j] = b13
    return b3
def fonk3(b24):
    b14 = open(b24,'r')
    b15 = b14.readline()
    b16 = b1.match(b15)
    if not b16:
        print(b15+" not properly formatted")
        quit(1)
    b17 = list(range(int(b16.group(1))))
    b4 = []
    for i in range(len(b17)):
        b18 = []
        for j in range(len(b17)):
            b18.append(float("inf"))
        b4.append(b18)
    for b19 in b14.readlines():
        b19 = b19.strip()
        b20 = b2.match(b19)
        if b20:
            b21 = b20.group(1)
            b22 = b20.group(2)
            if int(b21) >= len(b17) or int(b22) >= len(b17):
                print("Attempting to insert an edge between "+str(b21)+" and "+str(b22)+" in a graph with "+str(len(b17))+" b17")
                quit(1)
            b23 = b20.group(3)
            b4[int(b21)][int(b22)]=b23
    return (b17,b4)
def fonk4(lengthMatrix,b24):
    b24 = os.path.splitext(os.path.split(b24)[1])[0]
    b25 = open('output/'+b24+'_output.txt','w')
    for vertex in lengthMatrix:
        for length in vertex:
            b25.write(str(length)+',')
        b25.write('\n')
def fonk5(b24,b26):
    b26 = b26[1:]
    b27 = fonk3(b24)
    b28 = []
    if b26 = = 'b' or b26 == 'B':
        b29 = time.clock()
        b28 = fonk1(b27)
        b30 = time.clock()
        b31 = b30-b29
        print("Bellman-Ford timing: "+str(b31))
    if b26 = = 'f' or b26 == 'F':
        b29 = time.clock()
        b28 = fonk2(b27)
        b30 = time.clock()
        b32 = b30-b29
        print("Floyd-Warshall timing: "+str(b32))
    if b26 = = "both":
        b29 = time.clock()
        fonk1(b27)
        b30 = time.clock()
        b31 = b30-b29
        b29 = time.clock()
        fonk2(b27)
        b30 = time.clock()
        b32 = b30-b29
        print("Bellman-Ford timing: "+str(b31))
        print("Floyd-Warshall timing: "+str(b32))
    fonk4(b28,b24)
if b33 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk5(sys.argv[2],sys.argv[1])