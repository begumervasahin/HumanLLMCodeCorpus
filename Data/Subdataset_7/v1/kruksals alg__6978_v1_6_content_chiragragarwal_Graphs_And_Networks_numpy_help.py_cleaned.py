import numpy as np
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = np.matrix(b1)
print("Shape of the matrix:", b2.shape)
print("Element at position (0, 1):", b2[0, 1])
print("Element at position (2, 3):", b2[2, 3])
b2[0, 1] = -8
print("Modified row 1:", b2[1])
print("Column 2:", b2[:, 1])