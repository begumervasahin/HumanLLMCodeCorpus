import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
b1 = pd.read_csv('endometrial.csv')
b2 = b1.dropna()
b2 = b2.iloc[:, 1:]
b3 = preprocessing.scale(b2.T)
b4 = TSNE(n_components=2, n_iter=2500, random_state=0)
b5 = b4.fit_transform(b3)
plt.scatter(b5[:, 0], b5[:, 1])
plt.show()