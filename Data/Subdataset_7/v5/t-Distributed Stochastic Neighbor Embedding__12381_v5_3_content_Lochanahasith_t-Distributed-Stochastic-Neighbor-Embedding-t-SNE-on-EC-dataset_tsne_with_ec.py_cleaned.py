import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
b1 = pd.read_csv('endometrial.csv').dropna()
b1 = b1.iloc[:, 1:]
b2 = preprocessing.scale(b1.T)
b3 = TSNE(n_components=2, n_iter=2500, random_state=0)
b4 = b3.fit_transform(b2)
plt.scatter(b4[:, 0], b4[:, 1])
plt.show()