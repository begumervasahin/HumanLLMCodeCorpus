
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
b1 = pd.read_csv('endometrial.csv')
b2 = b1.dropna()
b2.head()
b3 = b2.iloc[:,1:]
b3.head()
b4 = preprocessing.scale(b3.T)
b5 = TSNE(n_components=2, n_iter=2500, random_state=0)
b6 = b5.fit_transform(b4)
plt.scatter(b6[:,0], b6[:,1])
plt.show()
