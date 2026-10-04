import numpy as np
mat = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graphMat = np.matrix(mat)
print("Matrix shape:", graphMat.shape)
element_0_1 = graphMat[0, 1]
element_2_3 = graphMat[2, 3]
print("Element at (0,1):", element_0_1)
print("Element at (2,3):", element_2_3)
graphMat[0, 1] = -8
second_row = graphMat[1]
print("Second row:", second_row)
second_column = graphMat[:, 1]
print("Second column:", second_column)