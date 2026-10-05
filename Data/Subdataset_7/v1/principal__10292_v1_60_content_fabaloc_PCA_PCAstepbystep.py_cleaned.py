import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = '~/yourdata'
b2 = pd.read_excel(b1, sheet_name='sheet')
b2 = pd.DataFrame(b2)
b3 = np.mean(b2, axis=0)
b4 = np.var(b2, axis=0)
n, b5 = b2.shape
b6 = b2 - b3
b7 = (b6.T.dot(b6)) / (n - 1)
b10, b8 = np.linalg.eig(b7)
for i in b8:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(i))
    print('Everything ok!')
b9 = b10.argsort()[::-1]
b10 = b10[b9]
b8 = b8[:, b9]
b11 = sum(b10)
b12 = [i / b11 * 100 for i in sorted(b10, reverse=True)]
b13 = np.cumsum(b12)
b14 = ['b14%s' % s for s in range(1, len(b10) + 1)]
plt.scatter(b12, b14, b15 = 0.5)
plt.title('Explained variance')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance (%)')
plt.show()
a1 = 3
b16 = b8[:, :a1]
b17 = b6.dot(b16)
b18 = b17.dot(b16.T)
b19 = b18 + b3.values
b20 = b2 - b19