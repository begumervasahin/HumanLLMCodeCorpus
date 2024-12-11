import numpy as np
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = np.matrix(b1)
b3 = b2.shape
b4 = b2[0, 1]
b5 = b2[2, 3]
b2[0, 1] = -8
b6 = b2[1]
b7 = b2[:, 1]
