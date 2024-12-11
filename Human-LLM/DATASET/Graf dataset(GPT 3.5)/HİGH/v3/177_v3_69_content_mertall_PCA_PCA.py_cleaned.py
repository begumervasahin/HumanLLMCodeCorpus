import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import rand
import matplotlib.pyplot as plt
def fonk1(b6, a1):
    return rand(b6, a1, b1 = 0.1)
def fonk2(b7, b8):
    U, S, b2 = svds(b7, k=b8)
    return U.dot(np.diag(S))
def fonk3(b9):
    b3 = plt.figure()
    b4 = b3.add_subplot(111, projection='3d')
    b4.scatter(b9[:, 0], b9[:, 1], b9[:, 2], b5 = 'r', marker='o')
    b4.set_xlabel('X')
    b4.set_ylabel('Y')
    b4.set_zlabel('Z')
    plt.title('Singular Vectors Plot')
    plt.show()
def fonk4():
    b6 = int(input('Enter the number of rows in your sparse random matrix: '))
    a1 = 3
    print('Note: Currently, the program supports only 3-dimensional data. Higher dimensions will be supported in the future.')
    b7 = fonk1(b6, a1)
    b8 = min(b7.shape) - 1
    b9 = fonk2(b7, b8)
    print('A 3D graph will be displayed with your singular vectors.')
    fonk3(b9)
if b10 = = '__main__':
    fonk4()