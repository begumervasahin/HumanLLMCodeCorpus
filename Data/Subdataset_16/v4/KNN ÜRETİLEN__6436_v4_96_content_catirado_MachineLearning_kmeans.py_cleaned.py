import numpy as np
import math
a1 = 100
def fonk1(data_set, k):
    a2 = 0
    b1 = []
    b2 = [[] for _ in range(k)]
    b1 = fonk3(data_set, k)
    while not fonk2(b2, b1, a2):
        b2 = b1
        a2 += 1
        b3 = fonk4(data_set, b1, k)
        b1 = fonk5(b3, data_set, k)
    return b1, b3, a2
def fonk2(b2, b1, a2):
    return (a2 > a1) or b2 = = b1
def fonk3(data_set, k):
    return [data_set[np.random.randint(0, len(data_set))] for _ in range(k)]
def fonk4(data_set, b1, k):
    b3 = [[] for _ in range(k)]
    for x in data_set:
        b4 = min(range(len(b1)), key=lambda c: fonk6(x, b1[c]))
        b3[b4].append(x)
    return b3
def fonk5(b3, data_set, k):
    b5 = []
    for cluster in b3:
        if not cluster:
            b5.append(data_set[np.random.randint(0, len(data_set))])
        else:
            b5.append(np.mean(cluster, b6 = 0).tolist())
    return b5
def fonk6(x, y):
    return math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))