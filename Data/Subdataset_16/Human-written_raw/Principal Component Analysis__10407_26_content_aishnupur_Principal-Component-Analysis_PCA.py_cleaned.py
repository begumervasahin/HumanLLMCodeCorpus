import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.ExcelFile('mice_protein.xlsx')
b2 = b1.parse('Data_Cortex_Nuclear')
b3 = b2.iloc[:, 1:78]
b4 = b3.b4(axis=0)
b3.isnull().sum()
b5 = []
b5 = b3.apply(lambda v1 : v1.fillna(v1.b4()),axis=0)
b6 = np.cov(b5.transpose())
eigen_value, b7 = np.linalg.eig(b6)
b8 = []
b8 = b7[:,:2]
b9 = b8.transpose()
b10 = b5.transpose()
b11 = []
for i in range(1080):
     b11 = np.dot(b9,b10)
     b12 = b11.transpose()
b13 = b12[:,0]
b14 = b12[:,1]
b15 = b2.iloc[:,81]
plt.plot(b11[0,0:149], b11[1,0:149], '*',  b16 = 3, color='blue', alpha=0.5, label='c-CS-m')
plt.plot(b11[0,150:299], b11[1,150:299], '*', b16 = 3, color='red', alpha=0.5, label='c-SC-m')
plt.plot(b11[0,300:434], b11[1,300:434], '*', b16 = 3, color='green', alpha=0.5, label='c-CS-s')
plt.plot(b11[0,435:569], b11[1,435:569], '*', b16 = 3, color='yellow', alpha=0.5, label='c-SC-s')
plt.plot(b11[0,570:704], b11[1,570:704], '*', b16 = 3, color='orange', alpha=0.5, label='t-CS-m')
plt.plot(b11[0,705:839], b11[1,705:839], '*', b16 = 3, color='pink', alpha=0.5, label='t-SC-m')
plt.plot(b11[0,840:944], b11[1,840:944], '*', b16 = 3, color='black', alpha=0.5, label='t-CS-s')
plt.plot(b11[0,945:1079], b11[1,945:1079], '*', b16 = 3, color='brown', alpha=0.5, label='t-SC-s')
plt.title("Scatter Plot")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()