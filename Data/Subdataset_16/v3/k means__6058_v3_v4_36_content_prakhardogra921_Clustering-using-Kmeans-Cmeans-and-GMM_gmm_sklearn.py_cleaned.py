import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def fonk1(a1, params):
    return [np.random.normal(b1 = b1, scale=scale, a1=a1) for b1, scale in params]
def fonk2(data_sets, b6, a1):
    b2 = np.concatenate([
        random.sample(list(data_set), int(prop * a1))
        for data_set, prop in zip(data_sets, b6)
    ])
    return b2
def fonk3(data):
    b3 = mixture.GaussianMixture(n_components=3)
    b3.fit(data.reshape(-1, 1))
    b4 = b3.predict(data.reshape(-1, 1))
    plt.scatter(data, b4, b5 = b4, cmap='viridis', marker='o', edgecolor='k')
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data')
    plt.ylabel('Cluster')
    plt.show()
def fonk4():
    a1 = 500
    b6 = [0.25, 0.5, 0.25]
    b7 = [(1, 0.1), (1.5, 0.1), (2, 0.2)]
    b8 = [(1, 0.3), (1.5, 0.4), (2, 0.3)]
    b9 = fonk1(a1, b7)
    b10 = fonk2(b9, b6, a1)
    b11 = fonk1(a1, b8)
    b12 = fonk2(b11, b6, a1)
    fonk3(b10)
if b13 = = "__main__":
    fonk4()