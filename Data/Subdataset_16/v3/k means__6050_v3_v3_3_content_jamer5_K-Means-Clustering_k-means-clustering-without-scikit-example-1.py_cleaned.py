import numpy as np
import os
def fonk1(point, centroid):
    return np.linalg.norm(point - centroid)
def fonk2(b6, data_point, b8):
    b1 = min(b6, key=b6.get)
    return [b1, data_point, b8[b1]]
def fonk3(b5, b8):
    b2 = []
    for i in range(len(b8)):
        b3 = [data[1] for data in b5 if data[0] == i]
        if b3:
            b4 = np.mean(b3, axis=0)
        else:
            b4 = b8[i]
        b2.append(b4)
    return np.array(b2)
def fonk4(b13, b8, total_iterations):
    for iteration in range(total_iterations):
        b5 = []
        for point in b13:
            b6 = {i: fonk1(point, b8[i]) for i in range(len(b8))}
            b7 = fonk2(b6, point, b8)
            b5.append(b7)
        b8 = fonk3(b5, b8)
    return b5, b8
def fonk5(results):
    b5, b9 = results
    print("Result of k-Means Clustering:\n")
    for b7 in b5:
        print(f"Data point: {b7[1]}")
        print(f"Cluster number: {b7[0]}\n")
    print("Final b8 position:\n", b9)
def fonk6():
    return np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
def fonk7(b12):
    return np.genfromtxt(b12, b10 = ",")
if b11 = = "__main__":
    b12 = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    b13 = fonk7(b12)
    b14 = fonk6()
    a1 = 100
    b15 = fonk4(b13, b14, a1)
    fonk5(b15)