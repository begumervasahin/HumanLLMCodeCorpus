import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.ExcelFile('mice_protein.xlsx')
b2 = b1.parse('Data_Cortex_Nuclear')
b3 = b2.iloc[:, 1:78]
b4 = b3.apply(lambda v1: v1.fillna(v1.mean()), axis=0)
b5 = np.cov(b4.transpose())
eigen_value, b6 = np.linalg.eig(b5)
b7 = b6[:, :2]
b8 = b7.transpose()
b9 = b4.transpose()
b10 = np.dot(b8, b9)
b11 = b10.transpose()
b12 = b11[:, 0]
b13 = b11[:, 1]
plt.plot(b10[0, 0:149], b10[1, 0:149], '*', b14 = 3, color='blue', alpha=0.5, label='c-CS-m')
plt.plot(b10[0, 150:299], b10[1, 150:299], '*', b14 = 3, color='red', alpha=0.5, label='c-SC-m')
plt.plot(b10[0, 300:434], b10[1, 300:434], '*', b14 = 3, color='green', alpha=0.5, label='c-CS-s')
plt.plot(b10[0, 435:569], b10[1, 435:569], '*', b14 = 3, color='yellow', alpha=0.5, label='c-SC-s')
plt.plot(b10[0, 570:704], b10[1, 570:704], '*', b14 = 3, color='orange', alpha=0.5, label='t-CS-m')
plt.plot(b10[0, 705:839], b10[1, 705:839], '*', b14 = 3, color='pink', alpha=0.5, label='t-SC-m')
plt.plot(b10[0, 840:944], b10[1, 840:944], '*', b14 = 3, color='black', alpha=0.5, label='t-CS-s')
plt.plot(b10[0, 945:1079], b10[1, 945:1079], '*', b14 = 3, color='brown', alpha=0.5, label='t-SC-s')
plt.title("Scatter Plot")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()