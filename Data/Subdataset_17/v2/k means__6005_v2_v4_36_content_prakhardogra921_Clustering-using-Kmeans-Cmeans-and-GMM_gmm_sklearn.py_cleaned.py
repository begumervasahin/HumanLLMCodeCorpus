import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def generate_synthetic_data(size, loc1, scale1, loc2, scale2, loc3, scale3):
    set1 = np.random.normal(loc=loc1, scale=scale1, size=size)
    set2 = np.random.normal(loc=loc2, scale=scale2, size=size)
    set3 = np.random.normal(loc=loc3, scale=scale3, size=size)
    return set1, set2, set3
def combine_data_sets(set1, set2, set3, p1, p2, p3, size):
    combined_data = np.array(
        random.sample(list(set1), int(p1 * size)) +
        random.sample(list(set2), int(p2 * size)) +
        random.sample(list(set3), int(p3 * size))
    )
    return combined_data
def generate_gmm(data):
    gmm = mixture.GaussianMixture(n_components=3)
    gmm.fit(data.reshape(-1, 1))
    y = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, y, c=y, cmap='viridis', marker='o', edgecolor='k')
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data')
    plt.ylabel('Cluster')
    plt.show()
size = 500
p1, p2, p3 = 0.25, 0.5, 0.25
set1, set2, set3 = generate_synthetic_data(size, 1, 0.1, 1.5, 0.1, 2, 0.2)
dset = combine_data_sets(set1, set2, set3, p1, p2, p3, size)
set4, set5, set6 = generate_synthetic_data(size, 1, 0.3, 1.5, 0.4, 2, 0.3)
dset2 = combine_data_sets(set4, set5, set6, p1, p2, p3, size)
generate_gmm(dset)
