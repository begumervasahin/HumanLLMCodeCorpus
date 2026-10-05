
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = '~/yourdata'
b2 = pd.read_excel(b1, sheet_name='sheet')
b3 = pd.DataFrame(b2)
b4 = np.mean(b3, axis=0)
b5 = np.var(b3, axis=0)
num_rows, b6 = b3.shape
b7 = b3 - b4
b8 = (b7.T.dot(b7)) / (num_rows - 1)
eigenvalues, b9 = np.linalg.eig(b8)
for vector in b9:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(vector))
    print('Eigenvectors are unit vectors.')
b10 = eigenvalues.argsort()[::-1]
b11 = eigenvalues[b10]
b12 = b9[:, b10]
b13 = sum(b11)
b14 = [(value / b13) * 100 for value in b11]
b15 = np.cumsum(b14)
b16 = ['PC%s' % index for index in range(1, len(b11) + 1)]
plt.scatter(b14, b16, b17 = 0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
a1 = 3
b18 = b12[:, :a1]
b19 = b7.dot(b18)
b20 = b19.dot(b18.T)
b20 += b4.values
b21 = b3 - b20