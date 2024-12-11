import math
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
num_observations, b2 = b1.shape
def fonk1(k):
    a1 = 1000000000
    b3 = np.zeros((num_observations, k))
    b4 = np.random.uniform(low=-10, high=10, size=(k, b2))
    while True:
        for obs_idx in range(num_observations):
            for cluster_idx in range(k):
                a2 = 0
                for feature_idx in range(b2):
                    a2 += (b1[obs_idx][feature_idx] - b4[cluster_idx][feature_idx])**2
                b3[obs_idx][cluster_idx] = a2
        b5 = b3.argmin(axis=1)
        b6 = fonk3(b3, b5)
        if b6 <= a1:
            break
        else:
            a1 = b6
            b4 = fonk2(k, b5)
    return b3, b5
def fonk2(k, b5):
    b7 = np.zeros((k, b2))
    for cluster_idx in range(k):
        b8 = np.zeros(b2)
        a3 = 0
        for obs_idx in range(num_observations):
            if b5[obs_idx] == cluster_idx:
                b8 += b1[obs_idx]
                a3 += 1
        if a3 > 0:
            b7[cluster_idx] = b8 / a3
    return b7
def fonk3(b3, b5):
    b6 = 0
    for obs_idx in range(num_observations):
        b6 += b3[obs_idx][b5[obs_idx]]
    return b6
def fonk4(b5):
    b9 = b1[:, 0]
    b10 = b1[:, 1]
    b11 = plt.figure()
    b12 = b11.add_subplot(1, 1, 1)
    b13 = ['r', 'g', 'b', 'y', 'c', 'm']
    for i in range(len(b1)):
        b12.scatter(b9[i], b10[i], b14 = b13[int(b5[i])])
    plt.show()
def fonk5():
    b3, b5 = fonk1(2)
    fonk4(b5)
if b15 = = '__main__':
    fonk5()