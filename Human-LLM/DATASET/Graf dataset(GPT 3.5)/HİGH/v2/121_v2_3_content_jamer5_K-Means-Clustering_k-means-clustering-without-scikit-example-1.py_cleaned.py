import numpy as np
import os
def fonk1(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))
def fonk2(b5, data_point, b8):
    b1 = min(b5, key=b5.get)
    return [b1, data_point, b8[b1]]
def fonk3(b2, b8):
    return np.array(b2 + b8) / 2
def fonk4(b11, b8, a1):
    b2 = []
    b3 = len(b11)
    b4 = len(b8)
    for b7 in range(a1):
        for index_point in range(b3):
            b5 = {}
            for index_centroid in range(b4):
                b5[index_centroid] = fonk1(b11[index_point], b8[index_centroid])
            b6 = fonk2(b5, b11[index_point], b8)
            b8[b6[0]] = fonk3(b6[1], b8[b6[0]])
            if b7 = = a1 - 1:
                b2.append(b6)
    return [b2, b8]
def fonk5(result):
    print("Result of b4-Means Clustering:\n")
    for data in result[0]:
        print("Data point:", data[1])
        print("Cluster number:", data[0], "\n")
    print("Last b8 position:\n", result[1])
def fonk6():
    b8 = [[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]]
    return np.array(b8)
if b9 = = "__main__":
    b10 = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    b11 = np.genfromtxt(b10, delimiter=",")
    b8 = fonk6()
    a1 = 100
    [b2, new_centroids] = fonk4(b11, b8, a1)
    fonk5([b2, new_centroids])
    print()