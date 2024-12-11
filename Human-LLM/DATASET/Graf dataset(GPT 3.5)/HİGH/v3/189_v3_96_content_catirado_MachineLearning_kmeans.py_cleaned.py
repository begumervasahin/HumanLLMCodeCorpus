import numpy as np
a1 = 100
def fonk1(b7, a2):
    b1 = fonk2(b7, a2)
    for b8 in range(a1):
        b2 = b1.copy()
        b3 = fonk3(b7, b1)
        b1 = fonk4(b3)
        if np.array_equal(b2, b1):
            break
    return b1, b3, b8 + 1
def fonk2(b7, a2):
    b4 = np.random.choice(len(b7), a2, replace=False)
    return b7[b4]
def fonk3(b7, b1):
    b3 = [[] for _ in range(len(b1))]
    for point in b7:
        b5 = np.argmin([fonk5(point, centroid) for centroid in b1])
        b3[b5].append(point)
    return b3
def fonk4(b3):
    b6 = [np.mean(cluster, axis=0) if cluster else np.random.choice(cluster) for cluster in b3]
    return b6
def fonk5(x, y):
    return np.sqrt(np.sum((x - y)**2))
b7 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
a2 = 2
b1, b3, b8 = fonk1(b7, a2)
print("Final Centroids:")
print(b1)
print("Clusters:")
print(b3)
print("Number of b8:", b8)