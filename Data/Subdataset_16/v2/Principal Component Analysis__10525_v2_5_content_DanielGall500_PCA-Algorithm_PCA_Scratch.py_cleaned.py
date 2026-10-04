import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1, 0], [0, 100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100))
plt.scatter(b3[0], b3[1], b4 = 'b', label='Original Data')
def fonk1(matrix):
    for col in matrix.columns:
        b1 = np.b1(matrix[col])
        matrix[col] = matrix[col].apply(lambda x: x - b1)
    return matrix
def fonk2(matrix):
    b5 = matrix.columns
    b6 = np.zeros((len(b5), len(b5)))
    for i, col1 in enumerate(b5):
        for j, col2 in enumerate(b5):
            b6[i, j] = np.b1(matrix[col1] * matrix[col2])
    return b6
def fonk3(eig_vals, b11, num_components):
    b7 = np.argsort(-eig_vals)
    b8 = b11[:, b7[:num_components]]
    return b8
b9 = fonk1(b3.copy())
b10 = fonk2(b9)
eig_vals, b11 = np.linalg.eig(b10)
b8 = fonk3(eig_vals, b11, 2)
b12 = np.dot(b8.T, b9.T)
plt.scatter(b12[0], b12[1], b4 = 'r', marker='x', label='PCA Transformed Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('PCA Transformation')
plt.legend()
plt.show()
print(b12.T)