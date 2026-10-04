14. Repository: Dawlatly/Recommender-system
   File: kmeans.py
   URL: https:
   Code Content:
import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
dataset = pd.read_csv('FYP.csv')
X = dataset.iloc[:, [10]].values
Y=dataset.iloc[:, [9]].values
labelencoder_X = LabelEncoder()
X=labelencoder_X.fit_transform(X[:,0])
labelencoder_Y = LabelEncoder()
Y=labelencoder_Y.fit_transform(Y[:,0])
done = np.vstack((Y,X)).T
onehotencoder_done = OneHotEncoder(categorical_features="all")
done = onehotencoder_done.fit_transform(done).toarray()
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
done = pca.fit_transform(done)
explained_variance = pca.explained_variance_ratio_
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 1000, n_init = 10)
    kmeans.fit(done)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 1000, n_init = 10)
y_kmeans = kmeans.fit_predict(done)
plt.scatter(done[y_kmeans == 0, 0], done[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(done[y_kmeans == 1, 0], done[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(done[y_kmeans == 2, 0], done[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()
   README Content:
This is an online store developed using Django that makes use of k-means clustering and Apriori algorithms to make recommendations to its user. It is a part of my Bachelor's graduation thesis.
The training data is present in the `FYP.csv` file. It consists of 9400 sample orders. The scripts for k-means clustering and apriori algorithm are present in `k-means.py` and `apriori.py` files resepectively.
The environment is as follows:
- Python 3.6.7
- Anaconda 4.6.14
- Django 1.11.3
To train the data, please see the files mentioned above and execute them. To run the website, execute the code `python manage.py runserver` within the directory in the command line. Then on your browser, visit `http:
