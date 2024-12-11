import math
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
num_observations, b2 = b1.shape
def fonk1(num_clusters):
    a1 = 1000000000
    b3 = np.zeros((num_observations, num_clusters))
    b4 = np.random.uniform(low=-10, high=10, size=(num_clusters, b2))
    b5 = np.zeros(num_observations)
    while True:
        for observation_idx in range(num_observations):
            for cluster_idx in range(num_clusters):
                a2 = 0
                for feature_idx in range(b2):
                    a2 += math.pow((b1[observation_idx][feature_idx] - b4[cluster_idx][feature_idx]), 2)
                b3[observation_idx][cluster_idx] = a2
            b5[observation_idx] = b3[observation_idx].argmin(b6 = 0)
        b7 = fonk3(b3, b5)
        if b7 <= a1:
            break
        else:
            a1 = b7
            b4 = fonk2(num_clusters, b5)
    return b3, b5
def fonk2(num_clusters, b5):
    b4 = np.zeros((num_clusters, b2))
    for cluster_idx in range(num_clusters):
        a3 = 0
        b8 = np.zeros(b2)
        for observation_idx in range(num_observations):
            if b5[observation_idx] == cluster_idx:
                for feature_idx in range(b2):
                    b8[feature_idx] += b1[observation_idx][feature_idx]
                a3 += 1
        for feature_idx in range(b2):
            b4[cluster_idx][feature_idx] = b8[feature_idx] / a3
    return b4
def fonk3(b3, b5):
    a4 = 0
    for observation_idx in range(num_observations):
        a4 += b3[observation_idx][int(b5[observation_idx])]
    return a4
def fonk4(b3, b5):
    b9 = b1[:, 0]
    b10 = b1[:, 1]
    b11 = plt.figure()
    b12 = b11.add_subplot(1, 1, 1)
    b13 = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(len(b1)):
        b12.scatter(b9[i], b10[i], b14 = b13[int(b5[i])])
    plt.show()
def fonk5():
    b3, b5 = fonk1(2)
    fonk4(b3, b5)
if b15 = = '__main__':
    fonk5()