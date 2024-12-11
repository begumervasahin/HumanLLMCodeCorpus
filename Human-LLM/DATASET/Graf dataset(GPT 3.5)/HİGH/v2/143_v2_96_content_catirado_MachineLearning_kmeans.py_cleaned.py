import numpy as np
a1 = 100
def fonk1(b8, a3):
    a2 = 0
    b1 = []
    b2 = [[] for _ in range(a3)]
    b1 = fonk3(b8, b1, a3)
    while not fonk2(b2, b1, a2):
        b2 = b1
        a2 += 1
        b3 = fonk4(b8, b1, a3)
        b1 = fonk5(b3, b8, a3)
    return b1, b3, a2
def fonk2(b2, b1, a2):
    return a2 > a1 or np.array_equal(b2, b1)
def fonk3(b8, b1, a3):
    for _ in range(a3):
        b1.append(b8[np.random.randint(0, len(b8), b4 = 1)])
    return b1
def fonk4(b8, b1, a3):
    b3 = [[] for _ in range(a3)]
    for x in b8:
        b5 = b1.index(min(b1, key=lambda c: fonk6(x, c)))
        b3[b5] += [x]
    return b3
def fonk5(b3, b8, a3):
    b6 = [[] for _ in range(a3)]
    for i, cluster in enumerate(b3):
        if not cluster:
            b6[i] = b8[np.random.randint(0, len(b8), b4 = 1)]
        else:
            b6[i] = np.mean(cluster, b7 = 0).tolist()
    return b6
def fonk6(x, y):
    return np.sqrt(np.sum((x - y)**2))
b8 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
a3 = 2
b1, b3, a2 = fonk1(b8, a3)
print("Final Centroids:")
print(b1)
print("Clusters:")
print(b3)
print("Number of a2:", a2)