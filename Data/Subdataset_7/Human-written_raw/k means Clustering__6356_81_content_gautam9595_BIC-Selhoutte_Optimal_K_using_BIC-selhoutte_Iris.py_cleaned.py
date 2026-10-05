import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
b1 = load_iris()
dir(b1)
from sklearn.cluster import KMeans
def fonk1(kmeans,X):
    b2 = [kmeans.cluster_centers_]
    b3 = kmeans.labels_
    b4 = kmeans.n_clusters
    b5 = np.bincount(b3)
    N, b6 = X.shape
    b7 = (1.0/(N - b4)/b6)*sum([sum(distance.cdist(X[np.where(b3==i)],[b2[0][i]],'euclidean')**2) for i in range(b4)])
    b8 = 0.5*b4*np.log(N)*(b6+1)
    b9 = np.sum([b5[i]*np.log(b5[i])-b5[i]*np.log(N)-((b5[i]*b6)/2)*np.log(2*np.pi*b7)-((b5[i]-1)*b6/2) for i in range(b4)])-b8
    return(b9)
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
b9 = []
for i in range(2,int(math.sqrt(len(b1.data)))):
    b10 = KMeans(n_clusters=i)
    b11 = b10.fit_predict(b1.data)
    b9.append(fonk1(b10,b1.data)/silhouette_score(b1.data,b11))
print(b9)
plt.plot(range(2,int(math.sqrt(len(b1.data)))),b9)