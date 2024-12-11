import csv
import random
import copy
import numpy as np
import sys
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python kmeans.py <input_file> <k_clusters> <output_file>")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = int(sys.argv[2])
    b3 = sys.argv[3]
    with open(b1, 'r') as file:
        b4 = csv.reader(file)
        b5 = np.array([row for row in b4 if row])
    b7, b6 = b5[:, :-1].astype(float), b5[:, -1]
    b7 = fonk2(b7)
    b10, b8 = fonk4(b7, b2)
    b9 = fonk5(b7, b2, b8, b10)
    print(f"SSE is {b9:.2f}")
    b10 = list(map(int, b10))
    with open(b3, 'w') as file:
        for cluster_id in b10:
            file.write(str(cluster_id) + '\n')
        file.write(f"SSE is {b9:.2f}")
def fonk2(b7):
    b11 = []
    for column in b7.T:
        b12 = column.min()
        b13 = column.max()
        b14 = (column - b12) / (b13 - b12)
        b11.append(b14)
    return np.array(b11).T
def fonk3(b8, b17):
    a1 = 0
    for i in range(len(b8)):
        a1 += np.linalg.norm(b8[i] - b17[i], 2)
    return a1
def fonk4(b7, b2):
    b8 = []
    b15 = set()
    for _ in range(b2):
        b16 = random.randint(0, len(b7) - 1)
        while b16 in b15:
            b16 = random.randint(0, len(b7) - 1)
        b8.append(b7[b16])
        b15.add(b16)
    b8 = np.array(b8)
    b17 = np.zeros(b8.shape)
    b18 = fonk3(b8, b17)
    b19 = np.zeros(len(b7))
    while b18 != 0:
        for i in range(len(b7)):
            b20 = []
            for centroid in b8:
                b20.append(np.linalg.norm(b7[i] - centroid, 2))
            b21 = np.argmin(b20)
            b19[i] = b21
        b17 = copy.deepcopy(b8)
        for i in range(b2):
            if len(b7[b19 = = i]) > 0:
                b8[i] = np.mean(b7[b19 = = i], axis=0)
        b18 = fonk3(b8, b17)
    return b19, b8
def fonk5(b7, b2, b8, b10):
    b9 = 0
    for i in range(b2):
        for j in b7[b10 = = i]:
            b9 += np.linalg.norm(j - b8[i], 2) ** 2
    return b9
if b22 = = '__main__':
    fonk1()