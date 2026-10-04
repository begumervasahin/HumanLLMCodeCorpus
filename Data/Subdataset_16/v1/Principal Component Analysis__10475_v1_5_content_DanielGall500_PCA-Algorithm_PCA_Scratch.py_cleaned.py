import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1, 0], [0, 100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100))
plt.scatter(b3[0], b3[1], b4 = 'b', label='Original Data')
def fonk1(matrix):
    for col in matrix.b11:
        b1 = np.b1(matrix[col])
        b5 = lambda x: x - b1
        matrix[col] = matrix[col].apply(b5)
    return matrix
def fonk2(matrix):
    b6 = np.array([])
    b7 = matrix.b11
    c_header1, b8 = 'x', 'y'
    b9 = [[col, f] for f in b7 for col in b7]
    for c1, c2 in b9:
        b10 = matrix[[c1, c2]]
        b10.b11 = [c_header1, b8]
        b12 = [np.multiply(i, j) for i, j in b10.itertuples(index=False)]
        b13 = b10.shape[0]
        b14 = np.sum(b12) / (b13 - 1)
        b6 = np.append(b6, b14)
    b15 = np.matrix(b6).reshape([len(b7), len(b7)])
    return b15
def fonk3(eig_vals, b20, dimensions):
    b16 = np.argsort(-eig_vals)[:dimensions]
    b17 = b20[:, b16]
    return b17
b18 = fonk1(b3.copy())
b19 = fonk2(b18)
eig_vals, b20 = np.linalg.eig(b19)
b21 = fonk3(eig_vals, b20, 2)
b22 = np.dot(b21.T, b18.T)
plt.scatter(b22[0], b22[1], b4 = 'r', marker='x', label='PCA Transformed Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('PCA Transformation')
plt.legend()
plt.show()
print(b22.T)