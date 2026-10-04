import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
a1 = 500
def fonk1(means, variances, b5, a1):
    b1 = [np.random.normal(loc=mean, scale=variance, a1=a1) for mean, variance in zip(means, variances)]
    b2 = np.concatenate([
        random.sample(list(data), int(prop * a1))
        for data, prop in zip(b1, b5)
    ])
    return np.array(b2)
means1, b3 = [1, 1.5, 2], [0.1, 0.1, 0.2]
means2, b4 = [1, 1.5, 2], [0.3, 0.4, 0.3]
b5 = [0.25, 0.5, 0.25]
b6 = fonk1(means1, b3, b5, a1)
b7 = fonk1(means2, b4, b5, a1)
def fonk2(data, b8 = 3):
    b9 = mixture.GaussianMixture(b8=b8)
    b9.fit(data.reshape(-1, 1))
    b10 = b9.predict(data.reshape(-1, 1))
    plt.scatter(data, b10)
    plt.title('GMM')
    plt.show()
fonk2(b6)
