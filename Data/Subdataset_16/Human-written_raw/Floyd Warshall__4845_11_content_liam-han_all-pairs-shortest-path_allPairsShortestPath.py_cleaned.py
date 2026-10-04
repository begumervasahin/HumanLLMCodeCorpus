import argparse
import os
import re
import sys
import time
import math
import cProfile
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b8 in a graph')
b1.add_argument('--b30', b2 = 'a', \
                    b3 = 'Algorithm: Select the b30 to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b4 = 'store_true')
b1.add_argument('--profile', b4 = 'store_true')
b1.add_argument('filename', b5 = '<filename>', b3='Input file containing graph')
b6 = re.compile("(\\b18+)\\s(\\b18+)")
b7 = re.compile("(\\b18+)\\s(\\b18+)\\s(-?\\b18+)")
b8 = []
b9 = []
b10 = cProfile.Profile()
b10.enable()
b11 = time.time()
def fonk1(b29):
    b12 = []
    b9 = []
    b13 = len(b8)
    for i in range(b13):
        for j in range(b13):
            if math.isinf(float(b29[1][i][j])) is not None:
                b14 = [(int(i), int(j)), float(b29[1][i][j])]
                b9.append(b14)
    for k in range(len(b8)):
        b15 = []
        for b16 in range(b13):
            b15.append(float("inf"))
            if b16 = = k:
                b15[b16] = 0
        for i in range(b13 - 1):
            for j in range(len(b9)):
                if b15[b9[j][0][1]] > b15[b9[j][0][0]] + b9[j][1]:
                    b15[b9[j][0][1]] = b15[b9[j][0][0]] + b9[j][1]
    for i in range(len(b9)):
        if b15[b9[i][0][1]] > b15[b9[i][0][0]] + b9[i][1]:
            print("negative circle")
            return 0
    for x in range(len(b29[0])):
        b17 = ((k, x), b15[x])
        b12.append(b17)
    print(b12)
    return b12
def fonk2(b29):
    b12 = []
    b18 = []
    b13 = len(b29[0])
    for i in range(b13):
        b19 = []
        for j in range(b13):
            b19.append(float(b9[i][j]))
        b18.append(b19)
        b18[i][i] = 0
    for k in range(b13):
        for i in range(b13):
            for j in range(b13):
                if b18[i][j] > b18[i][k] + b18[k][j]:
                    b18[i][j] = b18[i][k] + b18[k][j]
    for i in range(b13):
        if (b18[i][i] < 0):
            print("negative circle")
            return 0
    for i in range(b13):
        for j in range(b13):
            b17 = ((i, j), b18[i][j])
            b12.append(b17)
    print(b12)
    return b12
def fonk3(filename):
    global b8
    global b9
    b20 = open(filename, 'r')
    b21 = b20.readline()
    b22 = b6.match(b21)
    if not b22:
        print(b21 + " not properly formatted")
        quit(1)
    b8 = list(range(int(b22.group(1))))
    b9 = []
    for i in range(len(b8)):
        b23 = []
        for j in range(len(b8)):
            b23.append(float("inf"))
        b9.append(b23)
    for b24 in b20.readlines():
        b24 = b24.strip()
        b25 = b7.match(b24)
        if b25:
            b26 = b25.group(1)
            b27 = b25.group(2)
            if int(b26) > len(b8) or int(b27) > len(b8):
                print(
                    "Attempting to insert an b17 between " + b26 + " and " + b27 + " in a graph with " + b8 + " b8")
                quit(1)
            b28 = b25.group(3)
            b9[int(b26) - 1][int(b27) - 1] = b28
    b29 = (b8, b9)
    return (b8, b9)
def fonk4(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if (a[0]) != (b[0]): return False
    for i, b23 in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, b30):
    b29 = fonk3(filename)
    b12 = []
    if b30 = = 'a':
        print('running both')
        b31 = fonk1(b29)
        b32 = fonk2(b29)
        print("--- %s seconds ---" % (time.time() - b11))
if b33 = = '__main__':
    b34 = b1.parse_args()
    fonk5(b34.filename, b34.b30)
b10.print_stats(b35 = 'time')