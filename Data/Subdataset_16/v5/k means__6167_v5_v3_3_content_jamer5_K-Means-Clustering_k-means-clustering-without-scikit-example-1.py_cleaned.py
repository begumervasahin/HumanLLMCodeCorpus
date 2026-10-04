import numpy as np
import os
def fonk1(point, centroid):
    return np.linalg.norm(point - centroid)
def fonk2(b5):
    return min(b5, b1 = b5.get)
def fonk3(cluster_points):
    return np.mean(cluster_points, b2 = 0)
def fonk4(b10, b11, a1):
    b3 = len(b11)
    for _ in range(a1):
        b4 = {i: [] for i in range(b3)}
        for data_point in b10:
            b5 = {i: fonk1(data_point, b11[i]) for i in range(b3)}
            b6 = fonk2(b5)
            b4[b6].append(data_point)
        for i in range(b3):
            if b4[i]:
                b11[i] = fonk3(b4[i])
    b7 = []
    for data_point in b10:
        b5 = {i: fonk1(data_point, b11[i]) for i in range(b3)}
        b6 = fonk2(b5)
        b7.append((b6, data_point, b11[b6]))
    return b7, b11
def fonk5(b7, b11):
    print("Result of b3-Means Clustering:\n")
    for label in b7:
        print("Data point:", label[1])
        print("Cluster number:", label[0], "\n")
    print("Last b11 position:\n", b11)
def fonk6():
    return np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
if b8 = = "__main__":
    b9 = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    b10 = np.genfromtxt(b9, delimiter=",")
    b11 = fonk6()
    a1 = 100
    b7, b12 = fonk4(b10, b11, a1)
    fonk5(b7, b12)