import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv("Mall_Customers.csv")
b2 = b1.iloc[:,[3,4]].values
import scipy.cluster.hierarchy as sch
b3 = sch.b3(sch.linkage(b2,method='ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidian Distance')
plt.legend()
plt.show()
from sklearn.cluster import AgglomerativeClustering
b4 = AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = =0,0],b2[b5==0,b6],s=100,c='red',label='Carefull')
plt.scatter(b2[b5 = =b6,0],b2[b5==b6,b6],s=100,c='blue',label='Standard')
plt.scatter(b2[b5 = =2,0],b2[b5==2,b6],s=100,c='green',label='Target')
plt.scatter(b2[b5 = =3,0],b2[b5==3,b6],s=100,c='cyan',label='Careless')
plt.scatter(b2[b5 = =4,0],b2[b5==4,b6],s=100,c='magenta',label='Sensible')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(b6 = 100)')
plt.legend()
plt.show()