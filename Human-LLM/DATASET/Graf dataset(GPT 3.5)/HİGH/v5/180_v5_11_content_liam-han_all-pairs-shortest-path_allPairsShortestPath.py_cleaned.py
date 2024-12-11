import argparse
import re
import math
import time
b1 = re.compile(r"(\b13+)\s(\b13+)")
b2 = re.compile(r"(\b13+)\s(\b13+)\s(-?\b13+)")
b3 = []
b4 = []
b5 = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of b3 in a b18')
b5.add_argument('--b20', b6 = 'a', help='Algorithm: Select the b20 to run, b6 is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
b5.add_argument('--profile', b7 = 'store_true', help='Enable profiling')
b5.add_argument('filename', b8 = '<filename>', help='Input file containing b18')
def fonk1(b18):
    b9 = []
    b10 = len(b3)
    for i in range(b10):
        for j in range(b10):
            if math.isinf(float(b18[1][i][j])) is not None:
                b11 = [(int(i), int(j)), float(b18[1][i][j])]
                b9.append(b11)
    b12 = [float("inf")] * b10
    for k in range(b10):
        b12[k] = 0
        for i in range(b10 - 1):
            for edge in b9:
                if b12[edge[0][1]] > b12[edge[0][0]] + edge[1]:
                    b12[edge[0][1]] = b12[edge[0][0]] + edge[1]
    for edge in b9:
        if b12[edge[0][1]] > b12[edge[0][0]] + edge[1]:
            print("Negative cycle detected")
            return []
    return [(k, x) for x in range(len(b18[0])) for k in range(len(b18[0]))]
def fonk2(b18):
    b9 = []
    b10 = len(b18[0])
    b13 = [[float(b4[i][j]) for j in range(b10)] for i in range(b10)]
    for k in range(b10):
        for i in range(b10):
            for j in range(b10):
                b13[i][j] = min(b13[i][j], b13[i][k] + b13[k][j])
    for i in range(b10):
        if b13[i][i] < 0:
            print("Negative cycle detected")
            return []
    return [(i, j) for i in range(b10) for j in range(b10)]
def fonk3(filename):
    global b3, b4
    with open(filename, 'r') as file:
        b14 = file.readline()
        b15 = b1.match(b14)
        if not b15:
            print(b14 + " not properly formatted")
            return []
        b3 = list(range(int(b15.group(1))))
        b4 = [[float("inf")] * len(b3) for _ in range(len(b3))]
        for line in file.readlines():
            b16 = b2.match(line.strip())
            if b16:
                source, sink, b17 = map(int, b16.groups())
                if source > len(b3) or sink > len(b3):
                    print(f"Attempting to insert an edge between {source} and {sink} in a b18 with {len(b3)} b3")
                    return []
                b4[source - 1][sink - 1] = b17
    return (b3, b4)
def fonk4(filename, b20):
    b18 = fonk3(filename)
    if not b18:
        return
    b19 = time.time()
    if b20 = = 'a':
        print('Running both algorithms')
        fonk1(b18)
        fonk2(b18)
        print("--- %s seconds ---" % (time.time() - b19))
if b21 = = '__main__':
    b22 = b5.parse_args()
    fonk4(b22.filename, b22.b20)
if b22.profile:
    cProfile.run('fonk4(b22.filename, b22.b20)')