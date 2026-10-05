import numpy as np
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = np.matrix(b1)
print("Shape of the matrix:", b2.shape)
print("Element at (0,1):", b2[0, 1])
print("Element at (2,3):", b2[2, 3])
b2[0, 1] = -8
print("Modified matrix:")
print(b2)
print("Second column:")
print(b2[:, 1])