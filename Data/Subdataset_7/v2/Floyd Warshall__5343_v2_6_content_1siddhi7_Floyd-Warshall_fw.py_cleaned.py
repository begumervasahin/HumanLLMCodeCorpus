import numpy as np
import math
np.set_printoptions(b1 = 2)
np.set_printoptions(b2 = True)
b3 = math.inf
def fonk1():
    b4 = int(input("Enter the number of vertices: "))
    print("Enter the values of the adjacency matrix row-wise:")
    b5 = np.zeros((b4, b4))
    for i in range(b4):
        b5[i] = list(map(int, input().split()))
    return b4, b5
def fonk2(b5, b4):
    print("\n\n")
    print("Initial Matrix (D[0]):\n", b5)
    print("\n")
    for k in range(b4):
        for i in range(b4):
            for j in range(b4):
                b5[i][j] = min(b5[i][j], b5[i][k] + b5[k][j])
        print("Matrix after iteration %d (D[%d]):\n" % (k + 1, k + 1), b5)
        print("\n")
b4, b5 = fonk1()
fonk2(b5, b4)