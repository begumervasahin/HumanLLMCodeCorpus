from sklearn.neighbors import NearestNeighbors
import numpy as np
def fonk1():
    return np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
def fonk2(b3):
    b1 = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
    b1.fit(b3)
    return b1
def fonk3(b1, b3):
    distances, b2 = b1.kneighbors(b3)
    return distances, b2
def fonk4():
    b3 = fonk1()
    b1 = fonk2(b3)
    print("Fitted NearestNeighbors model:\n", b1)
    distances, b2 = fonk3(b1, b3)
    print("\nDistances to nearest neighbors:\n", distances)
    print("\nIndices of nearest neighbors:\n", b2)
if b4 = = "__main__":
    fonk4()