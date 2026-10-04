import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def generate_synthetic_data(size, params):
    return [np.random.normal(loc=loc, scale=scale, size=size) for loc, scale in params]
def combine_data_sets(data_sets, proportions, size):
    combined_data = np.concatenate([
        random.sample(list(data_set), int(prop * size))
        for data_set, prop in zip(data_sets, proportions)
    ])
    return combined_data
def plot_gmm(data):
    gmm = mixture.GaussianMixture(n_components=3)
    gmm.fit(data.reshape(-1, 1))
    y = gmm.predict(data.reshape(-1, 1))
    plt.scatter(data, y, c=y, cmap='viridis', marker='o', edgecolor='k')
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data')
    plt.ylabel('Cluster')
    plt.show()
def main():
    size = 500
    proportions = [0.25, 0.5, 0.25]
    params1 = [(1, 0.1), (1.5, 0.1), (2, 0.2)]
    params2 = [(1, 0.3), (1.5, 0.4), (2, 0.3)]
    data_sets1 = generate_synthetic_data(size, params1)
    dset1 = combine_data_sets(data_sets1, proportions, size)
    data_sets2 = generate_synthetic_data(size, params2)
    dset2 = combine_data_sets(data_sets2, proportions, size)
    plot_gmm(dset1)
if __name__ == "__main__":
    main()