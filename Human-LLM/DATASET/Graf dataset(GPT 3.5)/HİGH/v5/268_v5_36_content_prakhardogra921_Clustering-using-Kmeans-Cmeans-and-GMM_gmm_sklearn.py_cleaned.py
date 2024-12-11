import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
a1 = 500
b1 = np.random.normal(loc=1, scale=0.1, a1=a1)
b2 = np.random.normal(loc=1.5, scale=0.1, a1=a1)
b3 = np.random.normal(loc=2, scale=0.2, a1=a1)
b4 = [0.25, 0.5, 0.25]
b5 = np.concatenate([
    random.sample(list(b1), int(p * a1))
    for set_, p in zip([b1, b2, b3], b4)
])
def fonk1(data):
    b6 = mixture.GaussianMixture(n_components=3)
    b6.fit(data.reshape(-1, 1))
    b7 = b6.predict(data.reshape(-1, 1))
    plt.scatter(data, b7)
    plt.title('GMM')
    plt.show()
fonk1(b5)