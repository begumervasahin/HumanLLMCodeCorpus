import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def generate_synthetic_data(loc, scale, size):
    return np.random.normal(loc=loc, scale=scale, size=size)
def combine_data_sets(sets, proportions, size):
    combined_data = []
    for data_set, proportion in zip(sets, proportions):
        combined_data.extend(random.sample(list(data_set), int(proportion * size)))
    return np.array(combined_data)
def generate_gmm_plot(data, n_components=3):
    gmm = mixture.GaussianMixture(n_components=n_components)
    gmm.fit(data.reshape(-1, 1))
    clusters = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, clusters)
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data Points')
    plt.ylabel('Cluster')
    plt.show()
size = 500
proportions = [0.25, 0.5, 0.25]
set1 = generate_synthetic_data(loc=1, scale=0.1, size=size)
set2 = generate_synthetic_data(loc=1.5, scale=0.1, size=size)
set3 = generate_synthetic_data(loc=2, scale=0.2, size=size)
dset = combine_data_sets([set1, set2, set3], proportions, size)
generate_gmm_plot(dset)
set4 = generate_synthetic_data(loc=1, scale=0.3, size=size)
set5 = generate_synthetic_data(loc=1.5, scale=0.4, size=size)
set6 = generate_synthetic_data(loc=2, scale=0.3, size=size)
dset2 = combine_data_sets([set4, set5, set6], proportions, size)
