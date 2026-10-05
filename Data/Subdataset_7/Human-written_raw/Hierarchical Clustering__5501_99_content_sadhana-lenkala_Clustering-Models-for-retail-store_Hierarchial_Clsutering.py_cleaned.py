import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:,[3,4]].values
import scipy.cluster.hierarchy as sch
b3 = sch.dendrogram(sch.linkage(b2,method ='ward',metric = 'euclidean'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance using ward method')
plt.show()
from sklearn.cluster import AgglomerativeClustering
b4 = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean',linkage = 'ward')
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = = 0 , 0],b2[b5 == 0,1],color = 'red', label = 'Low spenders', s = 100)
plt.scatter(b2[b5 = = 1 , 0],b2[b5 == 1,1],color = 'blue', label = 'standard', s = 100)
plt.scatter(b2[b5 = = 2 , 0],b2[b5 == 2,1],color = 'green', label = 'Target', s = 100)
plt.scatter(b2[b5 = = 3 , 0],b2[b5 == 3,1],color = 'magenta', label = 'Low earners', s = 100)
plt.scatter(b2[b5 = = 4 , 0],b2[b5 == 4,1],color = 'cyan', label = 'out of target', s = 100)
plt.title('cluster of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()