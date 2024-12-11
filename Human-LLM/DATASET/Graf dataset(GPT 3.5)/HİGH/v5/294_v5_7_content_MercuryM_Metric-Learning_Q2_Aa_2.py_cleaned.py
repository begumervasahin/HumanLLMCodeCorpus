import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from Split import split_data
from scipy.optimize import linear_sum_assignment
def fonk1(a, b):
    return np.linalg.norm(a - b)
def fonk2(b18, true_labels):
    b1 = len(b18)
    b2 = np.zeros((b1, b1))
    for i, cluster in enumerate(b18):
        for j in range(len(cluster)):
            b3 = cluster[j]
            b4 = true_labels[0, b3]
            b2[i, :] += 1
            b2[i, b4 - 1] -= 1
    return b2
def fonk3(k, num_iterations, random_seed, b19):
    b5 = []
    b6 = []
    np.random.seed(random_seed)
    for _ in range(num_iterations):
        b7 = np.random.randint(0, 1000)
        b18, b8 = fonk5(k, b7, b19)
        b2 = fonk2(b18, b20)
        row_ind, b9 = linear_sum_assignment(b2)
        b10 = b2[row_ind, b9].sum()
        b11 = fonk4(k, b10)
        b6.append(b8)
        b5.append(b11)
    b12 = np.mean(b6)
    b13 = np.mean(b5)
    return b13, b12
def fonk4(k, b10):
    return (10 * k - b10) / (10 * k)
def fonk5(k, b7, b19):
    b14 = b19.T
    b15 = time.time()
    b16 = KMeans(n_clusters=k, b7=b7).fit(b14)
    b8 = time.time() - b15
    b17 = b16.labels_
    b18 = [[] for _ in range(k)]
    for i, label in enumerate(b17):
        b18[label].append(i)
    return b18, b8
b19 = split_data()
train_data, b20 = b19['train']
test_data, b21 = b19['test']
b22 = train_data / np.apply_along_axis(np.linalg.norm, 0, train_data)
b23 = test_data / np.apply_along_axis(np.linalg.norm, 0, test_data)
b13, b24 = fonk3(32, 1, 10, b22)