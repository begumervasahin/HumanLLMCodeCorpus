import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = '~/yourdata'
b2 = pd.read_excel(b1, sheet_name='sheet')
b3 = np.mean(b2, axis=0)
b4 = np.var(b2, axis=0)
num_rows, b5 = b2.shape
b6 = b2 - b3
b7 = np.dot(b6.T, b6) / (num_rows - 1)
b10, b8 = np.linalg.eig(b7)
for eigvec in b8:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(eigvec))
    print('Eigenvectors are unit vectors.')
b9 = b10.argsort()[::-1]
b10 = b10[b9]
b8 = b8[:, b9]
b11 = sum(b10)
b12 = [eigval / b11 * 100 for eigval in b10]
b13 = np.cumsum(b12)
b14 = ['PC%s' % i for i in range(1, len(b10) + 1)]
plt.scatter(b12, b14, b15 = 0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
a1 = 3
b16 = b8[:, :a1]
b17 = np.dot(b6, b16)
b18 = np.dot(b17, b16.T)
b19 = b18 + b3.values
b20 = b2 - b19