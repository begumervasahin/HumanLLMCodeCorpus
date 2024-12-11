import argparse
import os
import re
import sys
import time
import timeit
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b8 in a graph')
b1.add_argument('--b24',b2 = 'a',\
    b3 = 'Algorithm: Select the b24 to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v','--verbose',b4 = 'store_true')
b1.add_argument('--profile',b4 = 'store_true')
b1.add_argument('filename',b5 = '<filename>',b3='Input file containing graph')
b6 = re.compile("(\\b11+)\\s(\\b11+)")
b7 = re.compile("(\\b11+)\\s(\\b11+)\\s(-?\\b11+)")
b8 = []
b9 = []
def fonk1(b22):
    b10 = []
    for b19 in range(0, len(b22[0])):
        b11 = [float("inf")] * len(b22[0])
        b11[b19] = 0.0
        for iteration in range(0, len(b22[0])-1):
            for current in range(0, len(b22[0])):
                for otherVertex in range(0, len(b22[1])):
                    if b11[otherVertex] > float(b11[current]) + float(b22[1][current][otherVertex]):
                        b11[otherVertex] = float(b11[current]) + float(b22[1][current][otherVertex])
        for current in range(0, len(b22[0])):
            for otherVertex in range(0, len(b22[1])):
                if b11[otherVertex] > float(b11[current]) + float(b22[1][current][otherVertex]):
                    return (b10,False)
        b10.append(b11)
    return (b10,True)
def fonk2(b22):
    b10 = []
    b12 = b22
    for x in range(0,len(b22[0])):
        b12[1][x][x] = 0
    for i in range(0, len(b22[0])):
        for j in range(0, len(b22[0])):
            for iteration in range(0, len(b22[0])):
                b12[1][j][iteration] = min(float(b12[1][j][iteration]), float(b12[1][j][i]) + float(b12[1][i][iteration]))
    b10 = b12[1]
    return b10
def fonk3(filename):
    global b8
    global b9
    b13 = open(filename,'r')
    b14 = b13.readline()
    b15 = b6.match(b14)
    if not b15:
        print(b14+" not properly formatted")
        quit(1)
    b8 = list(range(int(b15.group(1))))
    b9 = []
    for i in range(len(b8)):
        b16 = []
        for j in range(len(b8)):
            b16.append(float("inf"))
        b9.append(b16)
    for b17 in b13.readlines():
        b17 = b17.strip()
        b18 = b7.match(b17)
        if b18:
            b19 = b18.group(1)
            b20 = b18.group(2)
            if int(b19) > len(b8) or int(b20) > len(b8):
                print("Attempting to insert an edge between "+b19+" and "+b20+" in a graph with "+b8+" b8")
                quit(1)
            b21 = b18.group(3)
            b9[int(b19)-1][int(b20)-1]=b21
    b22 = (b8,b9)
    return (b8,b9)
def fonk4(a,b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i,b16 in enumerate(a):
        for j,value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename,b24):
    b22 = fonk3(filename)
    b10 = []
    b23 = True
    if b24 = = 'b' or b24 == 'B':
        b25 = timeit.default_timer()
        b10 = fonk1(b22)
        b26 = timeit.default_timer()
        print(b26 - b25)
        b23 = b10[1]
        b10 = b10[0]
    if b24 = = 'f' or b24 == 'F':
        b25 = timeit.default_timer()
        b10 = fonk2(b22)
        b26 = timeit.default_timer()
        print(b26 - b25)
    if b24 = = 'a':
        print('running both')
        b27 = fonk1(b22)
        b28 = fonk2(b22)
        b10 = b27[0]
        b10 = b28
        b23 = b27[1]
        if not fonk4(b27,b28) or b23 = = False:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt','w') as f:
        if b23 = = False:
            f.write("Negative Cycle Detected \n")
        for b16 in b10:
            for b21 in b16:
                f.write(str(b21)+' ')
            f.write('\n')
if b29 = = '__main__':
    b30 = b1.parse_args()
    fonk5(b30.filename,b30.b24)