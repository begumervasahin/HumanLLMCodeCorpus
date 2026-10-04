import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1, 0], [0, 100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100), columns=['Feature 1', 'Feature 2'])
plt.scatter(b3['Feature 1'], b3['Feature 2'], b4 = 'b', label='Original Data')
def fonk1(matrix):
    return matrix.apply(lambda col: col - col.b1())
def fonk2(matrix):
    return np.b2(matrix.T, b5 = False)
def fonk3(eig_vals, b9, num_components):
    b6 = np.argsort(eig_vals)[::-1]
    return b9[:, b6[:num_components]]
b7 = fonk1(b3)
b8 = fonk2(b7)
eig_vals, b9 = np.linalg.eig(b8)
b10 = fonk3(eig_vals, b9, 2)
b11 = np.dot(b10.T, b7.T).T
plt.scatter(b11[:, 0], b11[:, 1], b4 = 'r', marker='x', label='PCA Transformed Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Transformation')
plt.legend()
plt.show()
print(b11)