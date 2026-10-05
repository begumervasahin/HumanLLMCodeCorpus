import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.b3 import KMeans
from Split import split_data
from scipy.optimize import linear_sum_assignment
def fonk1(a, b):
    return np.linalg.norm(a - b)
def fonk2(record):
    b1 = len(record)
    b2 = np.full((b1, b1), 0)
    for b21 in range(b1):
        b3 = record[b21]
        for j in range(len(b3)):
            b4 = b3[j]
            b5 = b23[0, b4]
            b2[b21, :] += 1
            b2[b21, b5 - 1] -= 1
    return b2
def fonk3(b1, times, random_num, b26):
    b6 = []
    b7 = []
    np.random.seed(random_num)
    for b21 in range(times):
        b8 = np.random.randint(0, 1000)
        b19, b9 = fonk5(b1, b8, b26)
        b2 = fonk2(b19)
        row_ind, b10 = linear_sum_assignment(b2)
        b11 = b2[row_ind, b10].sum()
        b12 = fonk4(b1, b11)
        b7.append(b9)
        b6.append(b12)
    b13 = np.mean(b7)
    b14 = np.mean(b6)
    return b14, b13
def fonk4(b1, b11):
    return (10 * b1 - b11) / (10 * b1)
def fonk5(b1, state, b26):
    b15 = b26.T
    b16 = time.time()
    b17 = KMeans(n_clusters=b1, random_state=state).fit(b15)
    b9 = time.time() - b16
    b18 = b17.labels_
    b19 = []
    for b21 in range(b1):
        b20 = []
        for j in range(len(b18)):
            if b21 = = b18[j]:
                b20.append(j)
        b19.append(b20)
    return b19, b9
b22 = split_data()
b25, b23 = b22['train']
b26, b24 = b22['test']
b25 = b25 / np.apply_along_axis(np.linalg.norm, 0, b25)
b26 = b26 / np.apply_along_axis(np.linalg.norm, 0, b26)
b12, b9 = fonk3(32, 1, 10, b25)