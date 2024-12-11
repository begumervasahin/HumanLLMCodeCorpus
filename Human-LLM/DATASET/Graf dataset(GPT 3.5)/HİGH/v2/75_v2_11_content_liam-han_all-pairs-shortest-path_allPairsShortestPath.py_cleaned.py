import argparse
import os
import re
import sys
import time
import math
import cProfile
b1 = re.compile(r"(\b15+)\s(\b15+)")
b2 = re.compile(r"(\b15+)\s(\b15+)\s(-?\b15+)")
b3 = []
b4 = []
b5 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a graph')
b5.add_argument('--b27', b6 = 'a', help='Select the b27 to run: (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
b5.add_argument('-v', '--verbose', b7 = 'store_true')
b5.add_argument('--profile', b7 = 'store_true')
b5.add_argument('filename', b8 = '<filename>', help='Input file containing graph')
def fonk1(b26):
    b9 = []
    b4 = []
    b10 = len(b3)
    for i in range(b10):
        for j in range(b10):
            if math.isinf(float(b26[1][i][j])) is not None:
                b11 = [(int(i), int(j)), float(b26[1][i][j])]
                b4.append(b11)
    for k in range(len(b3)):
        b12 = []
        for b13 in range(b10):
            b12.append(float("inf"))
            if b13 = = k:
                b12[b13] = 0
        for i in range(b10 - 1):
            for j in range(len(b4)):
                if b12[b4[j][0][1]] > b12[b4[j][0][0]] + b4[j][1]:
                    b12[b4[j][0][1]] = b12[b4[j][0][0]] + b4[j][1]
    for i in range(len(b4)):
        if b12[b4[i][0][1]] > b12[b4[i][0][0]] + b4[i][1]:
            print("Negative cycle detected")
            return 0
    for x in range(len(b26[0])):
        b14 = ((k, x), b12[x])
        b9.append(b14)
    print(b9)
    return b9
def fonk2(b26):
    b9 = []
    b15 = []
    b10 = len(b26[0])
    for i in range(b10):
        b16 = []
        for j in range(b10):
            b16.append(float(b4[i][j]))
        b15.append(b16)
        b15[i][i] = 0
    for k in range(b10):
        for i in range(b10):
            for j in range(b10):
                if b15[i][j] > b15[i][k] + b15[k][j]:
                    b15[i][j] = b15[i][k] + b15[k][j]
    for i in range(b10):
        if b15[i][i] < 0:
            print("Negative cycle detected")
            return 0
    for i in range(b10):
        for j in range(b10):
            b14 = ((i, j), b15[i][j])
            b9.append(b14)
    print(b9)
    return b9
def fonk3(filename):
    global b3
    global b4
    b17 = open(filename, 'r')
    b18 = b17.readline()
    b19 = b1.match(b18)
    if not b19:
        print(b18 + " not properly formatted")
        quit(1)
    b3 = list(range(int(b19.group(1))))
    b4 = []
    for i in range(len(b3)):
        b20 = []
        for j in range(len(b3)):
            b20.append(float("inf"))
        b4.append(b20)
    for b21 in b17.readlines():
        b21 = b21.strip()
        b22 = b2.match(b21)
        if b22:
            b23 = b22.group(1)
            b24 = b22.group(2)
            if int(b23) > len(b3) or int(b24) > len(b3):
                print("Attempting to insert an b14 between " + b23 + " and " + b24 + " in a graph with " + b3 + " b3")
                quit(1)
            b25 = b22.group(3)
            b4[int(b23) - 1][int(b24) - 1] = b25
    b26 = (b3, b4)
    return (b3, b4)
def fonk4(filename, b27):
    b26 = fonk3(filename)
    b9 = []
    if b27 = = 'a':
        print('Running both algorithms')
        b28 = fonk1(b26)
        b29 = fonk2(b26)
        print("--- %s seconds ---" % (time.time() - start))
if b30 = = '__main__':
    b31 = b5.parse_args()
    fonk4(b31.filename, b31.b27)
if b31.profile:
    pr.print_stats(b32 = 'time')