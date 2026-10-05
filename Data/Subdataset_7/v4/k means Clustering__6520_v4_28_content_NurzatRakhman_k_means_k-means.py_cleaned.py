import math
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
OBS, b2 = b1.shape
def fonk1(clusters):
    a1 = 1000000000
    b3 = np.zeros((OBS, clusters))
    b4 = np.random.uniform(low=-10, high=10, size=(clusters, b2))
    while True:
        for obs_idx in range(OBS):
            for cluster_idx in range(clusters):
                a2 = 0
                for feature_idx in range(b2):
                    b5 = math.pow((b1[obs_idx][feature_idx] - b4[cluster_idx][feature_idx]), 2)
                    a2 += b5
                b3[obs_idx][cluster_idx] = a2
        b6 = b3.argmin(axis=1)
        b7 = fonk3(b3, b6)
        if b7 <= a1:
            break
        else:
            a1 = b7
            b4 = fonk2(clusters, b6)
    return b3, b6
def fonk2(clusters, b6):
    b4 = np.zeros((clusters, b2))
    for cluster_idx in range(clusters):
        a3 = 0
        b8 = np.zeros(b2)
        for obs_idx in range(OBS):
            if b6[obs_idx] == cluster_idx:
                for feature_idx in range(b2):
                    b8[feature_idx] += b1[obs_idx][feature_idx]
                a3 += 1
        for feature_idx in range(b2):
            b4[cluster_idx][feature_idx] = b8[feature_idx] / a3
    return b4
def fonk3(b3, b6):
    a4 = 0
    for obs_idx in range(OBS):
        a4 += b3[obs_idx][int(b6[obs_idx])]
    return a4
def fonk4(b3, b6):
    b9 = b1[:, 0]
    b10 = b1[:, 1]
    b11 = plt.figure()
    b12 = b11.add_subplot(1, 1, 1)
    b13 = ['r', 'g', 'b', 'y', 'c', 'm']
    for i in range(len(b1)):
        b12.scatter(b9[i], b10[i], b14 = b13[int(b6[i])])
    plt.show()
def fonk5():
    b3, b6 = fonk1(2)
    fonk4(b3, b6)
if b15 = = '__main__':
    fonk5()