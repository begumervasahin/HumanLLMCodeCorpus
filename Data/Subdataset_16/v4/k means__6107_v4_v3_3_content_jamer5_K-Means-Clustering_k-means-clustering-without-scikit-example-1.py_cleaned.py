import numpy as np
import os
def fonk1(point, centroid):
    return np.linalg.norm(point - centroid)
def fonk2(b6, data_point, b12):
    b1 = min(b6, key=b6.get)
    return [b1, data_point, b12[b1]]
def fonk3(cluster_points):
    return np.mean(cluster_points, b2 = 0)
def fonk4(b11, b12, a1):
    b3 = []
    b4 = len(b12)
    for b8 in range(a1):
        b5 = {i: [] for i in range(b4)}
        for data_point in b11:
            b6 = {i: fonk1(data_point, b12[i]) for i in range(b4)}
            b7 = fonk2(b6, data_point, b12)
            b5[b7[0]].append(data_point)
            if b8 = = a1 - 1:
                b3.append(b7)
        for i in range(b4):
            if b5[i]:
                b12[i] = fonk3(b5[i])
    return b3, b12
def fonk5(b3, b12):
    print("Result of b4-Means Clustering:\n")
    for b7 in b3:
        print("Data point:", b7[1])
        print("Cluster number:", b7[0], "\n")
    print("Last b12 position:\n", b12)
def fonk6():
    return np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
if b9 = = "__main__":
    b10 = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    b11 = np.genfromtxt(b10, delimiter=",")
    b12 = fonk6()
    a1 = 100
    b3, b13 = fonk4(b11, b12, a1)
    fonk5(b3, b13)