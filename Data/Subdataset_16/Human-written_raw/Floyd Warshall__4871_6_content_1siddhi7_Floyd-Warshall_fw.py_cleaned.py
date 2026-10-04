import numpy as np
np.set_printoptions(b1 = 2)
np.set_printoptions(b2 = True)
import math
b3 = math.inf
def fonk1():
    b4 = int(input("Enter number of vertices: "))
    print("Enter the values of adjacency matrix row-wise")
    b5 = np.zeros((b4,b4))
    for i in range(b4):
        for j in range(b4):
            b5[i][j] = int(input())
    return b4, b5
def fonk2(b5, n):
    print("\n\n")
    print("D[0] :\n ", b5)
    print("\n")
    for k in range(n):
            for i in range(n):
                for j in range(n):
                    b5[i][j] = min(b5[i][j] , b5[i][k]+ b5[k][j])
            print("D[%d] :\n " %(k+1), b5)
            print("\n")