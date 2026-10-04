import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_file=pd.ExcelFile('mice_protein.xlsx')
df1 =data_file.parse('Data_Cortex_Nuclear')
v1_null=df1.iloc[:, 1:78]
mean= v1_null.mean(axis=0)
v1_null.isnull().sum()
modified_v1 = []
modified_v1 = v1_null.apply(lambda v1 : v1.fillna(v1.mean()),axis=0)
covariance_v1 = np.cov(modified_v1.transpose())
eigen_value, eigen_vector = np.linalg.eig(covariance_v1)
eig_1=[]
eig_1 = eigen_vector[:,:2]
eig_2 = eig_1.transpose()
z1=modified_v1.transpose()
z2=[]
for i in range(1080):
     z2=np.dot(eig_2,z1)
     z3=z2.transpose()
pc1= z3[:,0]
pc2= z3[:,1]
y=df1.iloc[:,81]
plt.plot(z2[0,0:149], z2[1,0:149], '*',  markersize=3, color='blue', alpha=0.5, label='c-CS-m')
plt.plot(z2[0,150:299], z2[1,150:299], '*', markersize=3, color='red', alpha=0.5, label='c-SC-m')
plt.plot(z2[0,300:434], z2[1,300:434], '*', markersize=3, color='green', alpha=0.5, label='c-CS-s')
plt.plot(z2[0,435:569], z2[1,435:569], '*', markersize=3, color='yellow', alpha=0.5, label='c-SC-s')
plt.plot(z2[0,570:704], z2[1,570:704], '*', markersize=3, color='orange', alpha=0.5, label='t-CS-m')
plt.plot(z2[0,705:839], z2[1,705:839], '*', markersize=3, color='pink', alpha=0.5, label='t-SC-m')
plt.plot(z2[0,840:944], z2[1,840:944], '*', markersize=3, color='black', alpha=0.5, label='t-CS-s')
plt.plot(z2[0,945:1079], z2[1,945:1079], '*', markersize=3, color='brown', alpha=0.5, label='t-SC-s')
plt.title("Scatter Plot")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()