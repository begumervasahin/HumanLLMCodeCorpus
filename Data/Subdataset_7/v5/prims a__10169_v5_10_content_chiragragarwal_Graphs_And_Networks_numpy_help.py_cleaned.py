import numpy as np
b1 = '1 2 3 4; 5 6 7 8; 0 1 2 3'
b2 = np.b2(b1)
b3 = b2.b3
print("Shape of the b2:", b3)
b4 = b2[0, 1]
b5 = b2[2, 3]
print("Element at [0, 1]:", b4)
print("Element at [2, 3]:", b5)
b2[0, 1] = -8
b6 = b2[:, 1]
print("Column 1 of the b2:")
print(b6)