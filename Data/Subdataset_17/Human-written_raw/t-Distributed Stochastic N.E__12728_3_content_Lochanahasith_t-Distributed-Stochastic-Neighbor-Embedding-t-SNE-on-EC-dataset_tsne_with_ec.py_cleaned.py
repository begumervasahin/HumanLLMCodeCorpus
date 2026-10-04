
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
datawithnan= pd.read_csv('endometrial.csv')
data1 = datawithnan.dropna()
data1.head()
data = data1.iloc[:,1:]
data.head()
scaled_data = preprocessing.scale(data.T)
tsne = TSNE(n_components=2, n_iter=2500, random_state=0)
tsne_data = tsne.fit_transform(scaled_data)
plt.scatter(tsne_data[:,0], tsne_data[:,1])
plt.show()
