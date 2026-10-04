import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
size = 500
def generate_dataset(means, variances, proportions, size):
    sets = [np.random.normal(loc=mean, scale=variance, size=size) for mean, variance in zip(means, variances)]
    dataset = np.concatenate([
        random.sample(list(data), int(prop * size))
        for data, prop in zip(sets, proportions)
    ])
    return np.array(dataset)
means1, variances1 = [1, 1.5, 2], [0.1, 0.1, 0.2]
means2, variances2 = [1, 1.5, 2], [0.3, 0.4, 0.3]
proportions = [0.25, 0.5, 0.25]
dset1 = generate_dataset(means1, variances1, proportions, size)
dset2 = generate_dataset(means2, variances2, proportions, size)
def generate_gmm(data, n_components=3):
    gmm = mixture.GaussianMixture(n_components=n_components)
    gmm.fit(data.reshape(-1, 1))
    y = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, y)
    plt.title('GMM')
    plt.show()
generate_gmm(dset1)
