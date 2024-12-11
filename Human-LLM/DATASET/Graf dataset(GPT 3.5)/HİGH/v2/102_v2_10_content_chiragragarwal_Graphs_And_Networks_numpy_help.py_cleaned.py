import numpy as np
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = np.b2(b1)
print("The b2 has a shape of:", b2.shape)
print("The element at row 0, column 1 is:", b2[0, 1])
print("The element at row 2, column 3 is:", b2[2, 3])
b2[0, 1] = -8
print("Modified b2:")
print(b2)
print("The second column of the b2 is:")
print(b2[:, 1])