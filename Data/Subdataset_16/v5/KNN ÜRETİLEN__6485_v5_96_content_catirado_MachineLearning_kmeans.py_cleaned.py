import numpy as np
import math
a1 = 100
def fonk1(data_set, a3):
    a2 = 0
    b1 = fonk3(data_set, a3)
    b2 = np.zeros_like(b1)
    while not fonk2(b2, b1, a2):
        b2 = b1.copy()
        a2 += 1
        b3 = fonk4(data_set, b1)
        b1 = fonk5(b3, data_set, a3)
    return b1, b3, a2
def fonk2(b2, b1, a2):
    return a2 > a1 or np.array_equal(b2, b1)
def fonk3(data_set, a3):
    b4 = np.random.choice(len(data_set), a3, replace=False)
    return data_set[b4]
def fonk4(data_set, b1):
    b3 = [[] for _ in b1]
    for point in data_set:
        b5 = np.argmin([fonk6(point, centroid) for centroid in b1])
        b3[b5].append(point)
    return b3
def fonk5(b3, data_set, a3):
    b6 = []
    for cluster in b3:
        if cluster:
            b6.append(np.mean(cluster, b7 = 0))
        else:
            b6.append(data_set[np.random.randint(0, len(data_set))])
    return np.array(b6)
def fonk6(x, y):
    return np.sqrt(np.sum((x - y) ** 2))
if b8 = = "__main__":
    b9 = np.array([
        [1.0, 2.0],
        [1.5, 1.8],
        [5.0, 8.0],
        [8.0, 8.0],
        [1.0, 0.6],
        [9.0, 11.0],
        [8.0, 2.0],
        [10.0, 2.0],
        [9.0, 3.0]
    ])
    a3 = 3
    b1, b3, a2 = fonk1(b9, a3)
    print(f"Centroids:\n{b1}")
    print(f"Iterations: {a2}")