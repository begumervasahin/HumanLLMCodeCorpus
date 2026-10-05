import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import rand
import matplotlib.pyplot as plt
def generate_sparse_matrix(m, n):
    X = rand(m, n, density=0.1)
    return X
def perform_svd(X, k):
    U, S, Vt = svds(X, k=k)
    singular_values = U.dot(np.diag(S))
    return singular_values
def plot_singular_vectors(singular_values):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(singular_values[:,0], singular_values[:,1], singular_values[:,2], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Singular Vectors Plot')
    plt.show()
def main():
    m = int(input('Enter the number of rows in your sparse random matrix: '))
    n = 3
    print('For now, there is only 3-dimensional capability. Higher dimensions will be supported in the future.')
    X = generate_sparse_matrix(m, n)
    k = min(X.shape) - 1
    singular_values = perform_svd(X, k)
    print('A graph will be displayed with your singular vectors plotted along with the singular value matrix.')
    plot_singular_vectors(singular_values)
if __name__ == '__main__':
    main()