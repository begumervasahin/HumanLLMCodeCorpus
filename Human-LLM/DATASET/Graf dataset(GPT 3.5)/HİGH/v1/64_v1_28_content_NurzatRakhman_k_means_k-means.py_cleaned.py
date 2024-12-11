import math
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
OBS, b2 = b1.shape
def fonk1(clusters):
    a1 = 1000000000
    b3 = (OBS, clusters)
    b4 = np.zeros(b3)
    b5 = np.random.uniform(low=-10, high=10, size=(clusters, b2))
    b6 = np.zeros(OBS)
    while True:
        for o_b in range(OBS):
            for cluster in range(clusters):
                a2 = 0
                for j in range(b2):
                    b7 = math.pow((b1[o_b][j] - b5[cluster][j]), 2)
                    a2 = a2 + b7
                b4[o_b][cluster] = a2
            b6[o_b] = b4[o_b].argmin(b8 = 0)
        b9 = fonk3(b4, b6)
        if b9 <= a1:
            break
        else:
            a1 = b9
            b5 = fonk2(clusters, b6)
    return b4, b6
def fonk2(clusters, b6):
    b5 = np.zeros((clusters, b2))
    for cluster in range(clusters):
        a3 = 0
        b10 = np.zeros(b2)
        for f_point in range(b2):
            if b6[f_point] == cluster:
                for point in range(b2):
                    b10[point] += b1[f_point][point]
                    a3 += 1
        for point in range(b2):
            b5[cluster][point] = b10[point]/a3
    return b5
def fonk3(b4, b6):
    b9 = 0
    for point in range(OBS):
        b9 = b9 + b4[point][int(b6[point])]
    return b9
def fonk4(b4, b6):
    b11 = b1[:, 0]
    b12 = b1[:, 1]
    b13 = plt.figure()
    b14 = b13.add_subplot(1, 1, 1)
    b15 = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(len(b1)):
        b14.scatter(b11[i], b12[i], b16 = b15[int(b6[i])])
    plt.show()
def fonk5():
    b4, b6 = fonk1(2)
    fonk4(b4, b6)
if b17 = = '__main__':
    fonk5()