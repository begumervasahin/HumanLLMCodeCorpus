import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
size = 500
set1 = np.random.normal(loc=1, scale=0.1, size=size)
set2 = np.random.normal(loc=1.5, scale=0.1, size=size)
set3 = np.random.normal(loc=2, scale=0.2, size=size)
mixture_proportions = [0.25, 0.5, 0.25]
dset = np.concatenate([
    random.sample(list(set1), int(p * size))
    for set_, p in zip([set1, set2, set3], mixture_proportions)
])
def plot_gmm(data):
    gmm = mixture.GaussianMixture(n_components=3)
    gmm.fit(data.reshape(-1, 1))
    y = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, y)
    plt.title('GMM')
    plt.show()
plot_gmm(dset)