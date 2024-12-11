import os
import re
import sys
import time
b1 = re.compile(r"(\b4+)\s(\b4+)")
b2 = re.compile(r"(\b4+)\s(\b4+)\s(\b4+)")
def fonk1(b21):
    b3 = []
    b4 = []
    for a in range(len(b21[0])):
        for b in range(len(b21[0])):
            b4.append(float("inf"))
        b4[a] = 0
        for b6 in range(1, len(b21[0])-1):
            for e in range(len(b21[0])):
                for f in range(len(b21[0])):
                    if float(b21[1][e][f]) < float("inf"):
                        if b4[f] > b4[e] + float(b21[1][e][f]):
                            b4[f] = int(b4[e]) + int(float(b21[1][e][f]))
        b3.append(b4)
        b4 = []
    return b3
def fonk2(b21):
    b3 = []
    b4 = []
    for a in range(len(b21[0])):
        b5 = []
        for b in range(len(b21[0])):
            b5.append(float("inf"))
        b4.append(b5)
    for b6 in range(len(b21[0])):
        for e in range(len(b21[0])):
            if b6 = = e:
                b4[b6][b6] = 0
            elif float(b21[1][b6][e]) < float("inf"):
                b4[b6][e] = int(float(b21[1][b6][e]))
            else:
                b4[b6][e] = float("inf")
    for b6 in range(len(b21[0])):
        for a in range(len(b21[0])):
            for b in range(len(b21[0])):
                if b4[a][b] < b4[a][b6] + b4[b6][b]:
                    b4[a][b] = b4[a][b]
                else:
                    b4[a][b] = b4[a][b6] + b4[b6][b]
    b3.append(b4)
    print(b4)
    return b3
def fonk3(b18):
    b7 = open(b18, 'r')
    b8 = b7.readline()
    b9 = b1.match(b8)
    if not b9:
        print(b8 + " not properly formatted")
        quit(1)
    b10 = list(range(int(b9.group(1))))
    b11 = []
    for i in range(len(b10)):
        b12 = []
        for j in range(len(b10)):
            b12.append(float("inf"))
        b11.append(b12)
    for b13 in b7.readlines():
        b13 = b13.strip()
        b14 = b2.match(b13)
        if b14:
            b15 = b14.group(1)
            b16 = b14.group(2)
            if int(b15) >= len(b10) or int(b16) >= len(b10):
                print("Attempting to insert an edge between " + str(b15) + " and " + str(b16) + " in a b21 with " + str(len(b10)) + " b10")
                quit(1)
            b17 = b14.group(3)
            b11[int(b15)][int(b16)] = b17
    return (b10, b11)
def fonk4(length_matrix, b18):
    b18 = os.path.splitext(os.path.split(b18)[1])[0]
    b19 = open('output/' + b18 + '_output.txt', 'w+')
    for vertex in length_matrix:
        for length in vertex:
            b19.write(str(length) + ',')
        b19.write('\n')
def fonk5(b18, b20):
    b20 = b20[1:]
    b21 = fonk3(b18)
    b22 = []
    if b20 = = 'b' or b20 == 'B':
        b22 = fonk1(b21)
    if b20 = = 'f' or b20 == 'F':
        b22 = fonk2(b21)
    if b20 = = "both":
        b23 = time.clock()
        fonk1(b21)
        b24 = time.clock()
        b25 = b24 - b23
        fonk2(b21)
        b23 = time.clock()
        b24 = time.clock()
        b26 = b24 - b23
        print("Bellman-Ford timing: " + str(b25))
        print("Floyd-Warshall timing: " + str(b26))
    fonk4(b22, b18)
if b27 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk5(sys.argv[2], sys.argv[1])