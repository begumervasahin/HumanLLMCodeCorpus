import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.sparse import rand
from scipy.sparse.linalg import svds
def fonk1(b8, cols):
    b1 = rand(b8, cols, density=0.1)
    b2 = min(b1.shape) - 1
    return b1, b2
def fonk2(b1, b2):
    U, S, b3 = svds(b1, b2=b2)
    b4 = np.dot(U, np.diag(S))
    return b4
def fonk3(b4):
    b5 = plt.figure(figsize=(12, 6))
    b6 = b5.add_subplot(121, projection='3d')
    b6.scatter(b4[:, 0], b4[:, 1], b4[:, 2])
    b6.set_title('Singular Values Scatter Plot')
    b7 = b5.add_subplot(122, projection='3d')
    b7.plot3D(b4[:, 0], b4[:, 1], b4[:, 2])
    b7.set_title('Singular Values 3D Line Plot')
    plt.show()
def fonk4():
    b8 = int(input('Enter the number of b8 for your sparse random matrix:\n'))
    print('Currently, the program supports 3-dimensional plots. More dimensions will be supported in the future.')
    b1, b2 = fonk1(b8, 3)
    b4 = fonk2(b1, b2)
    print('Displaying a graph with your singular vectors plotted along with the singular value matrix...')
    fonk3(b4)
if b9 = = '__main__':
    fonk4()