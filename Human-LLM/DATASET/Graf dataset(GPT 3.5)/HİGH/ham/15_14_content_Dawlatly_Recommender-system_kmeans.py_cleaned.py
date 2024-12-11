14. Repository: Dawlatly/Recommender-system
   File: b12.py
   URL: https:
   Code Content:
import numpy as np
np.set_printoptions(b1 = np.inf)
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
b2 = pd.read_csv('FYP.csv')
b3 = b2.iloc[:, [10]].values
b4 = b2.iloc[:, [9]].values
b5 = LabelEncoder()
b3 = b5.fit_transform(b3[:,0])
b6 = LabelEncoder()
b4 = b6.fit_transform(b4[:,0])
b7 = np.vstack((b4,b3)).T
b8 = OneHotEncoder(categorical_features="all")
b7 = b8.fit_transform(b7).toarray()
from sklearn.decomposition import PCA
b9 = PCA(n_components=2)
b7 = b9.fit_transform(b7)
b10 = b9.explained_variance_ratio_
from sklearn.cluster import KMeans
b11 = []
for i in range(1, 11):
    b12 = KMeans(n_clusters = i, init = 'k-means++', max_iter = 1000, n_init = 10)
    b12.fit(b7)
    b11.append(b12.inertia_)
plt.plot(range(1, 11), b11)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
b12 = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 1000, n_init = 10)
b13 = b12.fit_predict(b7)
plt.scatter(b7[b13 = = 0, 0], b7[b13 == 0, 1], b14 = 100, c = 'red', label = 'Cluster 1')
plt.scatter(b7[b13 = = 1, 0], b7[b13 == 1, 1], b14 = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(b7[b13 = = 2, 0], b7[b13 == 2, 1], b14 = 100, c = 'green', label = 'Cluster 3')
plt.scatter(b12.cluster_centers_[:, 0], b12.cluster_centers_[:, 1], b14 = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()
   README Content:
This is an online store developed using Django that makes use of k-means clustering and Apriori algorithms to make recommendations to its user. It is a part of my Bachelor'b14 graduation thesis.
The training data is present in the `FYP.csv` file. It consists of 9400 sample orders. The scripts for k-means clustering and apriori algorithm are present in `k-means.py` and `apriori.py` files resepectively.
The environment is as follows:
- Python 3.6.7
- Anaconda 4.6.14
- Django 1.11.3
To train the data, please see the files mentioned above and execute them. To run the website, execute the code `python manage.py runserver` within the directory in the command line. Then on your browser, visit `http:
