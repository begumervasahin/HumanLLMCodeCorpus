from mpl_toolkits import mplot3d
from scipy.sparse.linalg import svds
from scipy.sparse import rand, coo_matrix
import numpy as np
from matplotlib import pyplot
def data(m,n):
    X = rand(m, n, density=0.1)
    k = min(X.shape) - 1
    return X, k
def svd(X,k):
    U, S, V = svds(X,k=k)
    singular_values = np.dot(U,np.diag(S))
    return singular_values
def graph(X,singular_values):
    fig = pyplot.figure()
    ax = pyplot.axes(projection='3d')
    ax.scatter(singular_values[:,0],singular_values[:,1])
    fig2 = pyplot.figure()
    ax1 =pyplot.axes(projection='3d')
    ax1.plot3D(singular_values[:,0],singular_values[:,1])
    print(singular_values)
    pyplot.show()
def main():
    m = int(input('Choose the number of rows in your sparse random matrix:\n'))
    print('For now there is only 3 dimensional capability, in the future there will be added functionality for higher dimensions.')
    X,k = data(m,3)
    singular_values = svd(X,k)
    print('Now a graph will be displayed with your singular vectors plotted along with the singular value matrix')
    graph(X,singular_values)
if __name__ == '__main__':
    main()