import argparse
import os
import re
import sys
import time
import cProfile, pstats, io
import profile
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b8 in a graph')
b1.add_argument('--b28',b2 = 'a',\
    b3 = 'Algorithm: Select the b28 to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v','--verbose',b4 = 'store_true')
b1.add_argument('--profile',b4 = 'store_true')
b1.add_argument('filename',b5 = '<filename>',b3='Input file containing graph')
b6 = re.compile("(\\d+)\\b30(\\d+)")
b7 = re.compile("(\\d+)\\b30(\\d+)\\b30(-?\\d+)")
b8 = []
b9 = []
def fonk1(b27):
    b10 = []
    b11 = len(b8)
    for j in b8:
        b12 = [float("inf")] * b11
        b13 = [float(0)] * b11
        b12[j] = 0
        for i in range(0, len(b8) - 1):
            for V in range(0, len(b8)):
                for U in range(0, len(b9)):
                    b14 = float(b9[V][U])
                    b15 = b12[V] + b14
                    if b15 < b12[U]:
                        b12[U] = b15
        b10.append(b12)
    for j in b8:
        if b10[j][j] < 0:
            return [[0,0]]
    print('BellmanFord b28 is incomplete')
    return b10
def fonk2(b27):
    b10 = []
    b11 = len(b8)
    b12 = []
    for i in b8:
        b16 = [float("inf")] * b11
        b12.append(b16)
    for V in range(0, len(b8)):
        for U in range(0, len(b9)):
            b12[U][V] = float(b9[U][V])
        b12[V][V] = 0
    for k in range(0, len(b8)):
        for i in range(0, len(b8)):
            for j in range(0, len(b8)):
                b17 = b12[i][k] + b12[k][j]
                if b12[i][j] > b17:
                    b12[i][j] = b17
    for j in b8:
        if b12[j][j] < 0:
            return [[0,0]]
    b10 = b12
    print('FloydWarshall b28 is incomplete')
    return b10
def fonk3(filename):
    global b8
    global b9
    b18 = open(filename,'b16')
    b19 = b18.readline()
    b20 = b6.match(b19)
    if not b20:
        print(b19+" not properly formatted")
        quit(1)
    b8 = list(range(int(b20.group(1))))
    b9 = []
    for i in range(len(b8)):
        b21 = []
        for j in range(len(b8)):
            b21.append(float("inf"))
        b9.append(b21)
    for b22 in b18.readlines():
        b22 = b22.strip()
        b23 = b7.match(b22)
        if b23:
            b24 = b23.group(1)
            b25 = b23.group(2)
            if int(b24) > len(b8) or int(b25) > len(b8):
                print("Attempting to insert an edge between "+b24+" and "+b25+" in a graph with "+b8+" b8")
                quit(1)
            b26 = b23.group(3)
            b9[int(b24)-1][int(b25)-1]=b26
    b27 = (b8,b9)
    return (b8,b9)
def fonk4(a,b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i,b21 in enumerate(a):
        for j,value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename,b28):
    b27 = fonk3(filename)
    b10 = []
    if b28 = = 'b' or b28 == 'B':
        b29 = cProfile.Profile()
        b29.enable()
        b10 = fonk1(b27)
        b29.disable()
        b30 = io.StringIO()
        b31 = 'cumulative'
        b32 = pstats.Stats(b29, stream=b30).sort_stats(b31)
        b32.print_stats()
        print(b30.getvalue())
    if b28 = = 'f' or b28 == 'F':
        b29 = cProfile.Profile()
        b29.enable()
        b33 = fonk2(b27)
        b29.disable()
        b30 = io.StringIO()
        b31 = 'cumulative'
        b32 = pstats.Stats(b29, stream=b30).sort_stats(b31)
        b32.print_stats()
        print(b30.getvalue())
    if b28 = = 'a':
        print('running both')
        b34 = fonk1(b27)
        b33 = fonk2(b27)
        b10 = b34
        if not fonk4(b34,b33):
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt','b14') as f:
        for b21 in b10:
            for b26 in b21:
                f.write(str(b26)+' ')
            f.write('\n')
if b35 = = '__main__':
    b36 = b1.parse_args()
    fonk5(b36.filename,b36.b28)