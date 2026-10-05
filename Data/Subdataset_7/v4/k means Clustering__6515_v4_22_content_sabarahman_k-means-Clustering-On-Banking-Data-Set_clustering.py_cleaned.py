
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
b1 = pd.read_csv("Churn_Modelling.csv")
b2 = b1.iloc[:, [8, 12]].values
b3 = []
for i in range(1, 16):
    b4 = KMeans(n_clusters=i, init='k-means++', random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
plt.plot(range(1, 16), b3)
plt.title('Elbow Method')
plt.xlabel('Number Of Clusters')
plt.ylabel('WCSS')
plt.show()
b4 = KMeans(n_clusters=4, init='k-means++', random_state=0)
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = = 0, 0], b2[b5 == 0, 1], b6=25, c='red', label='Cluster 1')
plt.scatter(b2[b5 = = 1, 0], b2[b5 == 1, 1], b6=25, c='blue', label='Cluster 2')
plt.scatter(b2[b5 = = 2, 0], b2[b5 == 2, 1], b6=25, c='green', label='Cluster 3')
plt.scatter(b2[b5 = = 3, 0], b2[b5 == 3, 1], b6=25, c='pink', label='Cluster 4')
plt.scatter(b4.cluster_centers_[:, 0], b4.cluster_centers_[:, 1], b6 = 25, c='yellow', label='Centroid')
plt.title('KMeans Clustering')
plt.xlabel('Balance')
plt.ylabel('Estimated Salary in $')
plt.legend()
plt.show()