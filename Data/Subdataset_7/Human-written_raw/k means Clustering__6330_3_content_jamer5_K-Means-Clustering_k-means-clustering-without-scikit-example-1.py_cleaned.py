import numpy as np
import os
def fonk1(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))
def fonk2(b6, data_point, b8):
    b1 = min(b6, key=b6.get)
    return [b1, data_point, b8[b1]]
def fonk3(b3, b8):
    return np.array(b3 + b8)/2
def fonk4(b11, b8, a1):
    b2 = []
    b3 = []
    b4 = len(b11)
    b5 = len(b8)
    for b7 in range(0, a1):
        for index_point in range(0, b4):
            b6 = {}
            for index_centroid in range(0, b5):
                b6[index_centroid] = fonk1(b11[index_point], b8[index_centroid])
            b2 = fonk2(b6, b11[index_point], b8)
            b8[b2[0]] = fonk3(b2[1], b8[b2[0]])
            if b7 = = (a1 - 1):
                b3.append(b2)
    return [b3, b8]
def fonk5(result):
    print("Result of b5-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last b8 position: \n {}".format(result[1]))
def fonk6():
    b8 = []
    b8.append([5.0, 0.0])
    b8.append([45.0, 70.0])
    b8.append([50.0, 90.0])
    return np.array(b8)
if b9 = = "__main__":
    b10 = os.path.dirname(__file__) + "\data-example-1.csv"
    b11 = np.genfromtxt(b10, delimiter=",")
    b8 = fonk6()
    a1 = 100
    [b3, new_centroids] = fonk4(b11, b8, a1)
    fonk5([b3, new_centroids])
    print()