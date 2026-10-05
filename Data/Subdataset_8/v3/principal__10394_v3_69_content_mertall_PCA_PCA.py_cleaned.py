import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import rand
import matplotlib.pyplot as plt
def generate_sparse_matrix(num_rows, num_columns):
    return rand(num_rows, num_columns, density=0.1)
def perform_svd(sparse_matrix, num_singular_values):
    U, S, _ = svds(sparse_matrix, k=num_singular_values)
    return U.dot(np.diag(S))
def plot_singular_vectors(singular_vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(singular_vectors[:, 0], singular_vectors[:, 1], singular_vectors[:, 2], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Singular Vectors Plot')
    plt.show()
def main():
    num_rows = int(input('Enter the number of rows in your sparse random matrix: '))
    num_columns = 3
    print('Note: Currently, the program supports only 3-dimensional data. Higher dimensions will be supported in the future.')
    sparse_matrix = generate_sparse_matrix(num_rows, num_columns)
    num_singular_values = min(sparse_matrix.shape) - 1
    singular_vectors = perform_svd(sparse_matrix, num_singular_values)
    print('A 3D graph will be displayed with your singular vectors.')
    plot_singular_vectors(singular_vectors)
if __name__ == '__main__':
    main()