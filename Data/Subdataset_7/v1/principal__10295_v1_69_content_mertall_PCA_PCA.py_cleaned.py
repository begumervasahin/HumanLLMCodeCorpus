import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import rand
import matplotlib.pyplot as plt
def fonk1(b7, a1):
    b1 = rand(b7, a1, density=0.1)
    return b1
def fonk2(b1, b8):
    U, S, b2 = svds(b1, b8=b8)
    b3 = U.dot(np.diag(S))
    return b3
def fonk3(b3):
    b4 = plt.figure()
    b5 = b4.add_subplot(111, projection='3d')
    b5.scatter(b3[:,0], b3[:,1], b3[:,2], b6 = 'r', marker='o')
    b5.set_xlabel('b1')
    b5.set_ylabel('Y')
    b5.set_zlabel('Z')
    plt.title('Singular Vectors Plot')
    plt.show()
def fonk4():
    b7 = int(input('Enter the number of rows in your sparse random matrix: '))
    a1 = 3
    print('For now, there is only 3-dimensional capability. Higher dimensions will be supported in the future.')
    b1 = fonk1(b7, a1)
    b8 = min(b1.shape) - 1
    b3 = fonk2(b1, b8)
    print('A graph will be displayed with your singular vectors plotted along with the singular value matrix.')
    fonk3(b3)
if b9 = = '__main__':
    fonk4()