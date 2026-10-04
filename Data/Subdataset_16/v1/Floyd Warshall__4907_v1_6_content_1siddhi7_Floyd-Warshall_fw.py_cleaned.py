import numpy as np
import math
np.set_printoptions(b1 = 2, suppress=True)
b2 = math.inf
def fonk1():
    b3 = int(input("Enter number of vertices: "))
    print("Enter the values of adjacency matrix row-wise:")
    b4 = np.zeros((b3, b3))
    for i in range(b3):
        for j in range(b3):
            b4[i][j] = int(input())
    return b3, b4
def fonk2(b4, n):
    print("\n\n")
    print("D[0] :\n", b4)
    print("\n")
    for k in range(n):
        for i in range(n):
            for j in range(n):
                b4[i][j] = min(b4[i][j], b4[i][k] + b4[k][j])
        print(f"D[{k+1}] :\n", b4)
        print("\n")
def fonk3():
    b3, b4 = fonk1()
    fonk2(b4, b3)
if b5 = = '__main__':
    fonk3()