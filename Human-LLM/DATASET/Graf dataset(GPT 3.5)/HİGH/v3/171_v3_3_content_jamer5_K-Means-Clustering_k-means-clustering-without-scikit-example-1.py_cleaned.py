import numpy as np
import os
def fonk1(point, centroid):
    return np.linalg.norm(point - centroid)
def fonk2(b6, data_point, b12):
    b1 = min(b6, key=b6.get)
    return [b1, data_point, b12[b1]]
def fonk3(b3, b12):
    return np.mean(b3 + b12, b2 = 0)
def fonk4(b11, b12, a1):
    b3 = []
    b4 = len(b11)
    b5 = len(b12)
    for b8 in range(a1):
        for index_point in range(b4):
            b6 = {}
            for index_centroid in range(b5):
                b6[index_centroid] = fonk1(b11[index_point], b12[index_centroid])
            b7 = fonk2(b6, b11[index_point], b12)
            b12[b7[0]] = fonk3(b7[1], b12[b7[0]])
            if b8 = = a1 - 1:
                b3.append(b7)
    return [b3, b12]
def fonk5(result):
    print("Result of b5-Means Clustering:\n")
    for data in result[0]:
        print("Data point:", data[1])
        print("Cluster number:", data[0], "\n")
    print("Last b12 position:\n", result[1])
def fonk6():
    return np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
if b9 = = "__main__":
    b10 = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    b11 = np.genfromtxt(b10, delimiter=",")
    b12 = fonk6()
    a1 = 100
    [b3, new_centroids] = fonk4(b11, b12, a1)
    fonk5([b3, new_centroids])
    print()