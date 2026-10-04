import numpy as np
import math
a1 = 100
def fonk1(b8, a3):
    a2 = 0
    b1 = fonk3(b8, a3)
    b2 = [[] for _ in range(a3)]
    while not fonk2(b2, b1, a2):
        b2 = b1
        a2 += 1
        b3 = fonk4(b8, b1, a3)
        b1 = fonk5(b3, b8, a3)
    return b1, b3, a2
def fonk2(b2, b1, a2):
    return (a2 > a1) or b2 = = b1
def fonk3(b8, a3):
    b1 = []
    for _ in range(a3):
        b1.append(b8[np.random.randint(0, len(b8))].tolist())
    return b1
def fonk4(b8, b1, a3):
    b3 = [[] for _ in range(a3)]
    for data_point in b8:
        b4 = np.argmin([fonk6(data_point, centroid) for centroid in b1])
        b3[b4].append(data_point)
    return b3
def fonk5(b3, b8, a3):
    b5 = []
    for cluster in b3:
        if not cluster:
            b5.append(b8[np.random.randint(0, len(b8))].tolist())
        else:
            b5.append(np.mean(cluster, b6 = 0).tolist())
    return b5
def fonk6(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
if b7 = = "__main__":
    b8 = np.array([
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ])
    a3 = 3
    b1, b3, a2 = fonk1(b8, a3)
    print("Centroids:")
    print(b1)
    print("\nClusters:")
    for cluster in b3:
        print(cluster)
    print("\nIterations:")
    print(a2)