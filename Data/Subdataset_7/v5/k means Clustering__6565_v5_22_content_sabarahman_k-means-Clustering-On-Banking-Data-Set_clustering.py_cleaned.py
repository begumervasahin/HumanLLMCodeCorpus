
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
b1 = pd.read_csv("Churn_Modelling.csv")
b2 = [8, 12]
b3 = b1.iloc[:, b2].values
b4 = []
for num_clusters in range(1, 16):
    b5 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    b5.fit(b3)
    b4.append(b5.inertia_)
plt.plot(range(1, 16), b4)
plt.title('Elbow Method')
plt.xlabel('Number Of Clusters')
plt.ylabel('WCSS')
plt.show()
a1 = 4
b5 = KMeans(n_clusters=a1, init='k-means++', random_state=0)
b6 = b5.fit_predict(b3)
b7 = ['red', 'blue', 'green', 'pink']
for cluster_num, color in zip(range(a1), b7):
    plt.scatter(b3[b6 = = cluster_num, 0], b3[b6 == cluster_num, 1], b8=25, c=color, label=f'Cluster {cluster_num+1}')
plt.scatter(b5.cluster_centers_[:, 0], b5.cluster_centers_[:, 1], b8 = 25, c='yellow', label='Centroid')
plt.title('KMeans Clustering')
plt.xlabel('Balance')
plt.ylabel('Estimated Salary in $')
plt.legend()
plt.show()