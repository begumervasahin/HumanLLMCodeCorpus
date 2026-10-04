import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.ExcelFile('mice_protein.xlsx')
b2 = b1.parse('Data_Cortex_Nuclear')
b3 = b2.iloc[:, 1:78]
b4 = b3.apply(lambda col: col.fillna(col.mean()), axis=0)
b5 = np.cov(b4.transpose())
eigen_values, b6 = np.linalg.eig(b5)
b7 = b6[:, :2]
b8 = np.dot(b7.T, b4.transpose()).transpose()
b9 = b8[:, 0]
b10 = b8[:, 1]
plt.figure(b11 = (10, 8))
plt.plot(b9[0:149], b10[0:149], '*', b12 = 3, color='blue', alpha=0.5, label='c-CS-m')
plt.plot(b9[150:299], b10[150:299], '*', b12 = 3, color='red', alpha=0.5, label='c-SC-m')
plt.plot(b9[300:434], b10[300:434], '*', b12 = 3, color='green', alpha=0.5, label='c-CS-s')
plt.plot(b9[435:569], b10[435:569], '*', b12 = 3, color='yellow', alpha=0.5, label='c-SC-s')
plt.plot(b9[570:704], b10[570:704], '*', b12 = 3, color='orange', alpha=0.5, label='t-CS-m')
plt.plot(b9[705:839], b10[705:839], '*', b12 = 3, color='pink', alpha=0.5, label='t-SC-m')
plt.plot(b9[840:944], b10[840:944], '*', b12 = 3, color='black', alpha=0.5, label='t-CS-s')
plt.plot(b9[945:1079], b10[945:1079], '*', b12 = 3, color='brown', alpha=0.5, label='t-SC-s')
plt.title("Scatter Plot of Principal Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()