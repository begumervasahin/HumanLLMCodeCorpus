import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
size = 500
set1 = np.random.normal(loc=1, scale=0.1, size=size)
set2 = np.random.normal(loc=1.5, scale=0.1, size=size)
set3 = np.random.normal(loc=2, scale=0.2, size=size)
p1 = 0.25
p2 = 0.5
p3 = 0.25
dset = np.array(random.sample(list(set1), int(p1*size)) +
                random.sample(list(set2), int(p2*size)) +
                random.sample(list(set3), int(p3*size)))
set4 = np.random.normal(loc=1, scale=0.3, size=size)
set5 = np.random.normal(loc=1.5, scale=0.4, size=size)
set6 = np.random.normal(loc=2, scale=0.3, size=size)
dset2 = np.array(random.sample(list(set4), int(p1*size)) +
                 random.sample(list(set5), int(p2*size)) +
                 random.sample(list(set6), int(p3*size)))
def generate_gmm(set):
    gmm = mixture.GaussianMixture(n_components=3)
    gmm.fit(set.reshape(-1, 1))
    y = gmm.predict(set.reshape(-1, 1))
    plt.scatter(set, y)
    plt.title('GMM')
    plt.show()
generate_gmm(dset)
