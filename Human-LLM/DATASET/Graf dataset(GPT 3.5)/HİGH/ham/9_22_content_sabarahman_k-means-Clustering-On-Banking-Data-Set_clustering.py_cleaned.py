import numpy as np
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
import pandas as pd
b1 = pd.read_csv("Churn_Modelling.csv")
b2 = b1.iloc[:,[8,12]].values
b3 = []
for i in range(1,16):
    b4 = KMeans(n_clusters=i,init='k-means++',random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
plot.plot(range(1,16),b3)
plot.title('Elbow Method')
plot.xlabel('Number Of Clusters')
plot.ylabel('b3')
plot.show()
b4 = KMeans(n_clusters=4,init='k-means++',random_state=0)
b5 = b4.fit_predict(b2)
plot.scatter(b2[b5 = =0,0],b2[b5==0,1],b6=25,c='red',label='cluster1')
plot.scatter(b2[b5 = =1,0],b2[b5==1,1],b6=25,c='blue',label='cluster2')
plot.scatter(b2[b5 = =2,0],b2[b5==2,1],b6=25,c='green',label='cluster3')
plot.scatter(b2[b5 = =3,0],b2[b5==3,1],b6=25,c='pink',label='cluster4')
plot.scatter(b4.cluster_centers_[:,0],b4.cluster_centers_[:,1],b6 = 25,c='yellow',label='centroid')
plot.title('KMeans Clustering')
plot.xlabel('Balance')
plot.ylabel('Estimated Salary in $')
plot.legend()
plot.show()