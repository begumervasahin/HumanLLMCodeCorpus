import csv
import random
import copy
import numpy as np
import sys
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python kmeans.py <input_file> <k_clusters> <output_file>")
        sys.exit(1)
    inputFile, k, b1 = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    b2 = fonk2(inputFile)
    b3 = fonk3(b2)
    b15, b4 = fonk5(b3, k)
    b5 = fonk7(b3, b4, b15)
    print(f"SSE is {b5:.2f}")
    fonk8(b15, b5, b1)
def fonk2(inputFile):
    with open(inputFile, 'r') as file:
        b6 = csv.reader(file)
        b2 = np.array([row for row in b6 if row])
    return b2
def fonk3(b2):
    b3 = b2[:, :-1].astype(float)
    b3 = fonk4(b3)
    return b3
def fonk4(b3):
    b7 = []
    for column in b3.T:
        col_min, b8 = column.min(), column.max()
        b9 = (column - col_min) / (b8 - col_min)
        b7.append(b9)
    return np.array(b7).T
def fonk5(b3, k):
    b4 = fonk6(b3, k)
    b10 = np.zeros(b4.shape)
    b11 = np.zeros(len(b3))
    while not np.array_equal(b4, b10):
        for i in range(len(b3)):
            b12 = [np.linalg.norm(b3[i] - centroid, 2) for centroid in b4]
            b13 = np.argmin(b12)
            b11[i] = b13
        b10 = copy.deepcopy(b4)
        for i in range(k):
            if len(b3[b11 = = i]) > 0:
                b4[i] = np.mean(b3[b11 = = i], axis=0)
    return b11, b4
def fonk6(b3, k):
    b4 = []
    b14 = random.sample(range(len(b3)), k)
    for index in b14:
        b4.append(b3[index])
    return np.array(b4)
def fonk7(b3, b4, b15):
    b5 = 0
    for i, centroid in enumerate(b4):
        b5 += np.sum(np.linalg.norm(b3[b15 = = i] - centroid, axis=1) ** 2)
    return b5
def fonk8(b15, b5, b1):
    b15 = list(map(int, b15))
    with open(b1, 'w') as file:
        file.write('\n'.join(map(str, b15)) + '\n')
        file.write(f"SSE is {b5:.2f}")
if b16 = = '__main__':
    fonk1()