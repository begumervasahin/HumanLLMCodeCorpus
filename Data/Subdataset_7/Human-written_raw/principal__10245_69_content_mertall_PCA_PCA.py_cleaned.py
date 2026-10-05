from mpl_toolkits import mplot3d
from scipy.sparse.linalg import svds
from scipy.sparse import rand, coo_matrix
import numpy as np
from matplotlib import pyplot
def fonk1(b9,n):
    b1 = rand(b9, n, density=0.1)
    b2 = min(b1.shape) - 1
    return b1, b2
def fonk2(b1,b2):
    U, S, b3 = svds(b1,b2=b2)
    b4 = np.dot(U,np.diag(S))
    return b4
def fonk3(b1,b4):
    b5 = pyplot.figure()
    b6 = pyplot.axes(projection='3d')
    b6.scatter(b4[:,0],b4[:,1])
    b7 = pyplot.figure()
    b8 = pyplot.axes(projection='3d')
    b8.plot3D(b4[:,0],b4[:,1])
    print(b4)
    pyplot.show()
def fonk4():
    b9 = int(input('Choose the number of rows in your sparse random matrix:\n'))
    print('For now there is only 3 dimensional capability, in the future there will be added functionality for higher dimensions.')
    b1,b2 = fonk1(b9,3)
    b4 = fonk2(b1,b2)
    print('Now a graph will be displayed with your singular vectors plotted along with the singular value matrix')
    fonk3(b1,b4)
if b10 = = '__main__':
    fonk4()