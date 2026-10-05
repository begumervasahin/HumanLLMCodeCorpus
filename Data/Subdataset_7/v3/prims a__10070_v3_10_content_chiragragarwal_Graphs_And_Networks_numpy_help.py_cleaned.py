import numpy as np
b1 = '1 2 3 4; 5 6 7 8; 0 1 2 3'
b2 = np.b2(b1)
print("Shape of the b2:", b2.shape)
b3 = b2[0, 1]
b4 = b2[2, 3]
print(f"Element at row 0, column 1: {b3}")
print(f"Element at row 2, column 3: {b4}")
b2[0, 1] = -8
print("Modified b2:")
print(b2)
b5 = b2[:, 1]
print("Second column of the b2:")
print(b5)