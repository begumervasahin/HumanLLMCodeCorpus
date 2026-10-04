from sklearn.neighbors import NearestNeighbors
import numpy as np
def fonk1():
    return np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
def fonk2(b4, b1 = 2, algorithm='ball_tree'):
    b2 = NearestNeighbors(b1=b1, algorithm=algorithm)
    b2.fit(b4)
    return b2
def fonk3(b2, b4):
    distances, b3 = b2.kneighbors(b4)
    return distances, b3
def fonk4(b2, distances, b3):
    print("Trained NearestNeighbors b2:\n", b2)
    print("\nDistances to nearest neighbors:\n", distances)
    print("\nIndices of nearest neighbors:\n", b3)
def fonk5():
    b4 = fonk1()
    b2 = fonk2(b4)
    distances, b3 = fonk3(b2, b4)
    fonk4(b2, distances, b3)
if b5 = = "__main__":
    fonk5()