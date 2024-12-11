import math
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
[OBS, FEATURES] = b1.shape
def fonk1(clusters):
    a1 = 1000000000
    b2 = (OBS, clusters)
    b3 = np.zeros(b2)
    b4 = np.random.uniform(low=-10, high=10, size=(clusters, FEATURES))
    b5 = np.zeros(OBS)
    while True:
        for o_b in range(OBS):
            for cluster in range(clusters):
                a2 = 0
                for j in range(FEATURES):
                    b6 = math.pow((b1[o_b][j] - b4[cluster][j]), 2)
                    a2 = a2 + b6
                b3[o_b][cluster] = a2
            b5[o_b] = b3[o_b].argmin(b7 = 0)
        b8 = fonk3(b3, b5)
        if b8 <= a1:
            break
        else:
            a1 = b8
            b4 = fonk2(clusters, b5)
    return b3, b5
def fonk2(clusters, b5):
    b4 = np.zeros((clusters, FEATURES))
    for cluster in range(clusters):
        a3 = 0
        b9 = np.zeros(FEATURES)
        for f_point in range(FEATURES):
            if b5[f_point] == cluster:
                for point in range(FEATURES):
                    b9[point] += b1[f_point][point]
                    a3 += 1
        for point in range(FEATURES):
            b4[cluster][point] = b9[point]/a3
    return b4
def fonk3(b3, b5):
    b8 = 0
    for point in range(OBS):
        b8 = b8 + b3[point][int(b5[point])]
    return b8
def fonk4(b3, b5):
    b10 = b3[:, 0]
    b11 = b3[:, 1]
    b12 = plt.figure()
    b13 = b12.add_subplot(1, 1, 1)
    b14 = ["
    for i in range(len(b1)):
        b13.scatter(b10[i], b11[i], b15 = b14[int(b5[i])])
    plt.show()
def fonk5():
    b3, b5 = fonk1(2)
    fonk4(b3, b5)
if b16 = = '__main__':
    fonk5()