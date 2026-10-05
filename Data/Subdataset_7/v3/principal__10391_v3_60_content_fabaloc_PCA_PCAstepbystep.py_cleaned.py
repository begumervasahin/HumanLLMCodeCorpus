import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = '~/yourdata'
b2 = pd.read_excel(b1, sheet_name='sheet')
b3 = pd.DataFrame(b2)
b4 = b3.mean()
b5 = b3 - b4
b6 = np.cov(b5, rowvar=False)
eigenvalues, b7 = np.linalg.eig(b6)
b8 = np.argsort(eigenvalues)[::-1]
b9 = eigenvalues[b8]
b10 = b7[:, b8]
b11 = np.sum(b9)
b12 = (b9 / b11) * 100
b13 = len(b9)
b14 = [f'PC{i}' for i in range(1, b13 + 1)]
plt.scatter(b12, b14, b15 = 0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
a1 = 3
b16 = b10[:, :a1]
b17 = b5.dot(b16)
b18 = b17.dot(b16.T) + b4.values
b19 = b3 - b18