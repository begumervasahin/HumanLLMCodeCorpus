import numpy as np
import math
a1 = 100
def fonk1(b8, a3):
    a2 = 0
    b1 = fonk2(b8, a3)
    while a2 < a1:
        b2 = b1.copy()
        b3 = fonk3(b8, b1)
        b1 = fonk4(b3, b8)
        if b2 = = b1:
            break
        a2 += 1
    return b1, b3, a2
def fonk2(b8, a3):
    b1 = []
    b4 = np.random.choice(len(b8), size=a3, replace=False)
    for idx in b4:
        b1.append(b8[idx])
    return b1
def fonk3(b8, b1):
    b3 = [[] for _ in range(len(b1))]
    for x in b8:
        b5 = np.argmin([fonk5(x, c) for c in b1])
        b3[b5].append(x)
    return b3
def fonk4(b3, b8):
    b6 = []
    for cluster in b3:
        if cluster:
            b7 = np.mean(cluster, axis=0)
        else:
            b7 = b8[np.random.randint(len(b8))]
        b6.append(b7)
    return b6
def fonk5(x, y):
    return math.sqrt(np.sum(np.square(x - y)))
b8 = np.random.rand(100, 2)
a3 = 3
b1, b3, a2 = fonk1(b8, a3)
print('Centroids:', b1)
print('Clusters:', b3)
print('Number of a2:', a2)