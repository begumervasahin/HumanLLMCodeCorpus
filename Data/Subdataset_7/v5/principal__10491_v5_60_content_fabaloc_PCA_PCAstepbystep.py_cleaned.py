import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = '~/yourdata'
b2 = 'sheet'
b3 = pd.read_excel(b1, b2=b2)
b4 = np.mean(b3, axis=0)
b5 = np.var(b3, axis=0)
b6 = b3 - b4
num_rows, b7 = b3.shape
b8 = np.dot(b6.T, b6) / (num_rows - 1)
b11, b9 = np.linalg.eig(b8)
for eigvec in b9:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(eigvec))
print('Eigenvectors are unit vectors.')
b10 = b11.argsort()[::-1]
b11 = b11[b10]
b9 = b9[:, b10]
b12 = sum(b11)
b13 = [(eigval / b12) * 100 for eigval in b11]
b14 = np.cumsum(b13)
b15 = len(b11)
b16 = ['PC%s' % (i + 1) for i in range(b15)]
plt.scatter(b13, b16, b17 = 0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
a1 = 3
b18 = b9[:, :a1]
b19 = np.dot(b6, b18)
b20 = np.dot(b19, b18.T)
b21 = b20 + b4.values
b22 = b3 - b21