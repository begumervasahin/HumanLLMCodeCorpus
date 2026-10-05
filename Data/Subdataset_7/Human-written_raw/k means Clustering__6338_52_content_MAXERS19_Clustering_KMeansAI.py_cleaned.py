
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3,4]].values
from sklearn.cluster import KMeans
b3 = []
for i in range (1,11):
    b4 = KMeans(n_clusters = i, init='k-means++' , max_iter = 300, n_init = 10 , random_state = 0)
    b4.fit(b2)
    b3.append(b4.inertia_)
b4 = KMeans(n_clusters = 5, init='k-means++' , max_iter = 300, n_init = 10 , random_state = 0)
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = = 0, 0] ,b2[b5 == 0, 1], s = 100 ,c= 'red' , label ='Cluseter 1')
plt.scatter(b2[b5 = = 1, 0] ,b2[b5 == 1, 1], s = 100 ,c= 'blue' , label ='Cluseter 2')
plt.scatter(b2[b5 = = 2, 0] ,b2[b5 == 2, 1], s = 100 ,c= 'black' , label ='Cluseter 3')
plt.scatter(b2[b5 = = 3, 0] ,b2[b5 == 3, 1], s = 100 ,c= 'green' , label ='Cluseter 4')
plt.scatter(b2[b5 = = 4, 0] ,b2[b5 == 4, 1], s = 100 ,c= 'yellow' , label ='Cluseter 5')