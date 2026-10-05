import numpy as np
mat = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graphMat = np.matrix(mat)
print("Shape of the matrix:", graphMat.shape)
print("Element at (0,1):", graphMat[0, 1])
print("Element at (2,3):", graphMat[2, 3])
graphMat[0, 1] = -8
print("Modified matrix:")
print(graphMat)
print("Second column:")
print(graphMat[:, 1])