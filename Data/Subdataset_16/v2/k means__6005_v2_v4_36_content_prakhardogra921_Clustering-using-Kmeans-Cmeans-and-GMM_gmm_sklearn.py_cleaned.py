import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def fonk1(a1, loc1, scale1, loc2, scale2, loc3, scale3):
    b1 = np.random.normal(loc=loc1, scale=scale1, a1=a1)
    b2 = np.random.normal(loc=loc2, scale=scale2, a1=a1)
    b3 = np.random.normal(loc=loc3, scale=scale3, a1=a1)
    return b1, b2, b3
def fonk2(b1, b2, b3, p1, p2, b8, a1):
    b4 = np.array(
        random.sample(list(b1), int(p1 * a1)) +
        random.sample(list(b2), int(p2 * a1)) +
        random.sample(list(b3), int(b8 * a1))
    )
    return b4
def fonk3(data):
    b5 = mixture.GaussianMixture(n_components=3)
    b5.fit(data.reshape(-1, 1))
    b6 = b5.predict(data.reshape(-1, 1))
    plt.scatter(data, b6, b7 = b6, cmap='viridis', marker='o', edgecolor='k')
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data')
    plt.ylabel('Cluster')
    plt.show()
a1 = 500
p1, p2, b8 = 0.25, 0.5, 0.25
b1, b2, b3 = fonk1(a1, 1, 0.1, 1.5, 0.1, 2, 0.2)
b9 = fonk2(b1, b2, b3, p1, p2, b8, a1)
set4, set5, b10 = fonk1(a1, 1, 0.3, 1.5, 0.4, 2, 0.3)
b11 = fonk2(set4, set5, b10, p1, p2, b8, a1)
fonk3(b9)
