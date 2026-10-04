import numpy as np
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = np.matrix(b1)
print("Matrix shape:", b2.shape)
b3 = b2[0, 1]
b4 = b2[2, 3]
print("Element at position (0, 1):", b3)
print("Element at position (2, 3):", b4)
b2[0, 1] = -8
print("Matrix after modifying element (0, 1):\n", b2)
b5 = b2[1]
b6 = b2[:, 1]
print("Row 1:\n", b5)
print("Column 1:\n", b6)