import argparse
import os
import re
import cProfile
import pstats
import io
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b7 in a graph')
b1.add_argument('--b27', b2 = 'a', help='Algorithm: Select the b27 to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b3 = 'store_true')
b1.add_argument('--profile', b3 = 'store_true')
b1.add_argument('filename', b4 = '<filename>', help='Input file containing graph')
b5 = re.compile("(\\d+)\\b29(\\d+)")
b6 = re.compile("(\\d+)\\b29(\\d+)\\b29(-?\\d+)")
b7 = []
b8 = []
def fonk1(b26):
    b9 = []
    b10 = len(b7)
    for j in b7:
        b11 = [float("inf")] * b10
        b12 = [float(0)] * b10
        b11[j] = 0
        for i in range(0, len(b7) - 1):
            for V in range(0, len(b7)):
                for U in range(0, len(b8)):
                    b13 = float(b8[V][U])
                    b14 = b11[V] + b13
                    if b14 < b11[U]:
                        b11[U] = b14
        b9.append(b11)
    for j in b7:
        if b9[j][j] < 0:
            return [[0, 0]]
    print('BellmanFord b27 is incomplete')
    return b9
def fonk2(b26):
    b9 = []
    b10 = len(b7)
    b11 = []
    for i in b7:
        b15 = [float("inf")] * b10
        b11.append(b15)
    for V in range(0, len(b7)):
        for U in range(0, len(b8)):
            b11[U][V] = float(b8[U][V])
        b11[V][V] = 0
    for k in range(0, len(b7)):
        for i in range(0, len(b7)):
            for j in range(0, len(b7)):
                b16 = b11[i][k] + b11[k][j]
                if b11[i][j] > b16:
                    b11[i][j] = b16
    for j in b7:
        if b11[j][j] < 0:
            return [[0, 0]]
    b9 = b11
    print('FloydWarshall b27 is incomplete')
    return b9
def fonk3(filename):
    global b7
    global b8
    b17 = open(filename, 'b15')
    b18 = b17.readline()
    b19 = b5.match(b18)
    if not b19:
        print(b18 + " not properly formatted")
        quit(1)
    b7 = list(range(int(b19.group(1))))
    b8 = []
    for i in range(len(b7)):
        b20 = []
        for j in range(len(b7)):
            b20.append(float("inf"))
        b8.append(b20)
    for b21 in b17.readlines():
        b21 = b21.strip()
        b22 = b6.match(b21)
        if b22:
            b23 = b22.group(1)
            b24 = b22.group(2)
            if int(b23) > len(b7) or int(b24) > len(b7):
                print("Attempting to insert an edge between " + b23 + " and " + b24 + " in a graph with " + b7 + " b7")
                quit(1)
            b25 = b22.group(3)
            b8[int(b23) - 1][int(b24) - 1] = b25
    b26 = (b7, b8)
    return (b7, b8)
def fonk4(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i, b20 in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, b27):
    b26 = fonk3(filename)
    b9 = []
    if b27 = = 'b' or b27 == 'B':
        b28 = cProfile.Profile()
        b28.enable()
        b9 = fonk1(b26)
        b28.disable()
        b29 = io.StringIO()
        b30 = 'cumulative'
        b31 = pstats.Stats(b28, stream=b29).sort_stats(b30)
        b31.print_stats()
        print(b29.getvalue())
    if b27 = = 'f' or b27 == 'F':
        b28 = cProfile.Profile()
        b28.enable()
        b32 = fonk2(b26)
        b28.disable()
        b29 = io.StringIO()
        b30 = 'cumulative'
        b31 = pstats.Stats(b28, stream=b29).sort_stats(b30)
        b31.print_stats()
        print(b29.getvalue())
    if b27 = = 'a':
        print('running both')
        b33 = fonk1(b26)
        b32 = fonk2(b26)
        b9 = b33
        if not fonk4(b33, b32):
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0] + '_shortestPaths.txt', 'b13') as f:
        for b20 in b9:
            for b25 in b20:
                f.write(str(b25) + ' ')
            f.write('\n')
if b34 = = '__main__':
    b35 = b1.parse_args()
    fonk5(b35.filename, b35.b27)