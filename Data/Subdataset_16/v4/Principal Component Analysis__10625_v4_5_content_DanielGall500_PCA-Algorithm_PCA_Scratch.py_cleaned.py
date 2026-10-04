import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1, 0], [100, 100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100))
plt.scatter(b3[0], b3[1], b4 = 'b', label='Original Data')
def fonk1(matrix):
    for col in matrix.columns:
        b1 = np.b1(matrix[col])
        matrix[col] = matrix[col].apply(lambda x: x - b1)
    return matrix
def fonk2(matrix):
    b5 = matrix.b2()
    return b5
def fonk3(eig_vals, b9, dimensions):
    b6 = np.argsort(-eig_vals)[:dimensions]
    b7 = b9[:, b6]
    return b7
b8 = fonk1(b3)
b5 = fonk2(b8)
eig_vals, b9 = np.linalg.eig(b5)
b7 = fonk3(eig_vals, b9, 2)
b10 = np.dot(b7.T, b8.T).T
print(b10)
plt.scatter(b10[:, 0], b10[:, 1], b4 = 'r', marker='x', label='Transformed Data')
plt.legend()
plt.show()