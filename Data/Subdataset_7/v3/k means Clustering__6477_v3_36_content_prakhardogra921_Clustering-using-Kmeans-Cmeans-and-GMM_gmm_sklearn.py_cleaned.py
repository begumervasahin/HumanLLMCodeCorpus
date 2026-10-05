import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
a1 = 500
b1 = np.random.normal(loc=1, scale=0.1, a1=a1)
b2 = np.random.normal(loc=1.5, scale=0.1, a1=a1)
b3 = np.random.normal(loc=2, scale=0.2, a1=a1)
p1, p2, b4 = 0.25, 0.5, 0.25
b5 = np.concatenate((
    random.sample(b1.tolist(), int(p1*a1)),
    random.sample(b2.tolist(), int(p2*a1)),
    random.sample(b3.tolist(), int(b4*a1))
))
b6 = np.random.normal(loc=1, scale=0.3, a1=a1)
b7 = np.random.normal(loc=1.5, scale=0.4, a1=a1)
b8 = np.random.normal(loc=2, scale=0.3, a1=a1)
b9 = np.concatenate((
    random.sample(b6.tolist(), int(p1*a1)),
    random.sample(b7.tolist(), int(p2*a1)),
    random.sample(b8.tolist(), int(b4*a1))
))
def fonk1(data):
    b10 = mixture.GaussianMixture(n_components=3)
    b10.fit(data.reshape(-1, 1))
    b11 = b10.predict(data.reshape(-1, 1))
    plt.scatter(data, b11)
    plt.title('GMM')
    plt.show()
fonk1(b5)
