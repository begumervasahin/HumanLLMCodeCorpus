import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
size = 500
set1 = np.random.normal(loc=1, scale=0.1, size=size)
set2 = np.random.normal(loc=1.5, scale=0.1, size=size)
set3 = np.random.normal(loc=2, scale=0.2, size=size)
p1, p2, p3 = 0.25, 0.5, 0.25
dset = np.concatenate((
    random.sample(set1.tolist(), int(p1*size)),
    random.sample(set2.tolist(), int(p2*size)),
    random.sample(set3.tolist(), int(p3*size))
))
set4 = np.random.normal(loc=1, scale=0.3, size=size)
set5 = np.random.normal(loc=1.5, scale=0.4, size=size)
set6 = np.random.normal(loc=2, scale=0.3, size=size)
dset2 = np.concatenate((
    random.sample(set4.tolist(), int(p1*size)),
    random.sample(set5.tolist(), int(p2*size)),
    random.sample(set6.tolist(), int(p3*size))
))
def generate_gmm(data):
    gmm = mixture.GaussianMixture(n_components=3)
    gmm.fit(data.reshape(-1, 1))
    clusters = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, clusters)
    plt.title('GMM')
    plt.show()
generate_gmm(dset)
