import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1, 0], [100, 100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100), columns=['x', 'y'])
plt.scatter(b3['x'], b3['y'], b4 = 'b', label='Original Data')
def fonk1(matrix):
    return matrix - matrix.b1()
def fonk2(matrix):
    return matrix.b2()
def fonk3(eig_vals, b8, num_components):
    b5 = np.argsort(-eig_vals)[:num_components]
    return b8[:, b5]
b6 = fonk1(b3)
b7 = fonk2(b6)
eig_vals, b8 = np.linalg.eig(b7)
b9 = fonk3(eig_vals, b8, 2)
b10 = b6.dot(b9)
print(b10)
plt.scatter(b10.iloc[:, 0], b10.iloc[:, 1], b4 = 'r', marker='x', label='Transformed Data')
plt.legend()
plt.show()