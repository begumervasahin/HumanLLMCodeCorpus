import argparse
import os
import re
import sys
import time
import timeit
b1 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b7 in a graph')
b1.add_argument('--algorithm', b2 = 'a', help='Algorithm: Select the algorithm to run, b2 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b1.add_argument('-v', '--verbose', b3 = 'store_true')
b1.add_argument('--profile', b3 = 'store_true')
b1.add_argument('filename', b4 = '<filename>', help='Input file containing graph')
b5 = re.compile(r"(\b10+)\s(\b10+)")
b6 = re.compile(r"(\b10+)\s(\b10+)\s(-?\b10+)")
b7 = []
b8 = []
def fonk1(b20):
    b9 = []
    for b17 in range(0, len(b20[0])):
        b10 = [float("inf")] * len(b20[0])
        b10[b17] = 0.0
        for iteration in range(0, len(b20[0])-1):
            for current in range(0, len(b20[0])):
                for otherVertex in range(0, len(b20[1])):
                    if b10[otherVertex] > float(b10[current]) + float(b20[1][current][otherVertex]):
                        b10[otherVertex] = float(b10[current]) + float(b20[1][current][otherVertex])
        for current in range(0, len(b20[0])):
            for otherVertex in range(0, len(b20[1])):
                if b10[otherVertex] > float(b10[current]) + float(b20[1][current][otherVertex]):
                    return (b9, False)
        b9.append(b10)
    return (b9, True)
def fonk2(b20):
    b9 = []
    b11 = b20
    for x in range(0,len(b20[0])):
        b11[1][x][x] = 0
    for i in range(0, len(b20[0])):
        for j in range(0, len(b20[0])):
            for iteration in range(0, len(b20[0])):
                b11[1][j][iteration] = min(float(b11[1][j][iteration]), float(b11[1][j][i]) + float(b11[1][i][iteration]))
    b9 = b11[1]
    return b9
def fonk3(filename):
    global b7
    global b8
    with open(filename,'r') as inFile:
        b12 = inFile.readline()
        b13 = b5.match(b12)
        if not b13:
            print(f"First b15 of {filename} is not properly formatted")
            sys.exit(1)
        b7 = list(range(int(b13.group(1))))
        b8 = []
        for i in range(len(b7)):
            b14 = []
            for j in range(len(b7)):
                b14.append(float("inf"))
            b8.append(b14)
        for b15 in inFile.readlines():
            b15 = b15.strip()
            b16 = b6.match(b15)
            if b16:
                b17 = b16.group(1)
                b18 = b16.group(2)
                if int(b17) > len(b7) or int(b18) > len(b7):
                    print(f"Attempting to insert an edge between {b17} and {b18} in a graph with {len(b7)} b7")
                    sys.exit(1)
                b19 = b16.group(3)
                b8[int(b17)-1][int(b18)-1] = b19
    b20 = (b7, b8)
    return b20
def fonk4(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b):
        return False
    if len(a[0]) != len(b[0]):
        return False
    for i, b14 in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def fonk5(filename, algorithm):
    b20 = fonk3(filename)
    b9 = []
    b21 = True
    if algorithm.lower() == 'b':
        b22 = timeit.default_timer()
        b9, b21 = fonk1(b20)
        b23 = timeit.default_timer()
        print(b23 - b22)
    elif algorithm.lower() == 'f':
        b22 = timeit.default_timer()
        b9 = fonk2(b20)
        b23 = timeit.default_timer()
        print(b23 - b22)
    elif algorithm.lower() == 'a':
        print('Running both')
        pathPairsBellman, b24 = fonk1(b20)
        b25 = fonk2(b20)
        b9 = pathPairsBellman
        b21 = b24
        if not fonk4(pathPairsBellman, b25) or not b21:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result or negative cycle detected')
    else:
        print("Invalid algorithm option. Please choose 'b', 'f', or 'a'.")
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt', 'w') as f:
        if not b21:
            f.write("Negative Cycle Detected \n")
        for b14 in b9:
            for b19 in b14:
                f.write(str(b19)+' ')
            f.write('\n')
if b26 = = '__main__':
    b27 = b1.parse_args()
    fonk5(b27.filename, b27.algorithm)