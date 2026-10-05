import numpy as np
import math
a1 = 100
def fonk1(data_set, k):
    a2 = 0
    b1 = []
    b2 = [[] for _ in range(k)]
    b1 = fonk3(data_set, b1, k)
    while not fonk2(b2, b1, a2):
        b2 = b1
        a2 += 1
        b3 = fonk4(data_set, b1, k)
        b1 = fonk5(b3, data_set, k)
    return b1, b3, a2
def fonk2(b2, b1, a2):
    return a2 > a1 or b2 = = b1
def fonk3(data_set, b1, k):
    for cluster in range(k):
        b1.append(data_set[np.random.randint(0, len(data_set), b4 = 1)])
    return b1
def fonk4(data_set, b1, k):
    b3 = [[] for _ in range(k)]
    for x in data_set:
        b5 = b1.index(min(b1, key=lambda c: fonk6(x, c)))
        b3[b5].append(x)
    return b3
def fonk5(b3, data_set, k):
    b6 = [[] for _ in range(k)]
    for i, cluster in enumerate(b3):
        if not cluster:
            b6[i] = data_set[np.random.randint(0, len(data_set), b4 = 1)]
        else:
            b6[i] = np.mean(cluster, b7 = 0).tolist()
    return b6
def fonk6(x, y):
    a3 = 0
    for i in range(len(x)):
        a3 += pow((x[i] - y[i]), 2)
    return math.sqrt(a3)