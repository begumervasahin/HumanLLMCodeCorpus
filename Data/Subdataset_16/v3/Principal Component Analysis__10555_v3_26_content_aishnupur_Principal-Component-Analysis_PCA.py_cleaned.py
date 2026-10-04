import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.ExcelFile('mice_protein.xlsx')
b2 = b1.parse('Data_Cortex_Nuclear')
b3 = b2.iloc[:, 1:78]
b4 = b3.apply(lambda col: col.fillna(col.mean()), axis=0)
b5 = np.cov(b4.transpose())
eigenvalues, b6 = np.linalg.eig(b5)
b7 = b6[:, :2]
b8 = np.dot(b7.T, b4.transpose()).transpose()
b9 = b8[:, 0]
b10 = b8[:, 1]
b11 = {
    'c-CS-m': (0, 149, 'blue'),
    'c-SC-m': (150, 299, 'red'),
    'c-CS-s': (300, 434, 'green'),
    'c-SC-s': (435, 569, 'yellow'),
    't-CS-m': (570, 704, 'orange'),
    't-SC-m': (705, 839, 'pink'),
    't-CS-s': (840, 944, 'black'),
    't-SC-s': (945, 1079, 'brown')
}
plt.figure(b12 = (10, 8))
for label, (start, end, color) in b11.items():
    plt.plot(b9[start:end], b10[start:end], '*', b13 = 3, color=color, alpha=0.5, label=label)
plt.title("Scatter Plot of Principal Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()