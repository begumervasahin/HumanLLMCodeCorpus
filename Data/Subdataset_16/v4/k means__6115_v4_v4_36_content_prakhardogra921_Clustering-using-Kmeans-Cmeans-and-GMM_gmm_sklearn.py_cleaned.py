import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
a1 = 500
b1 = np.random.normal(loc=1, scale=0.1, a1=a1)
b2 = np.random.normal(loc=1.5, scale=0.1, a1=a1)
b3 = np.random.normal(loc=2, scale=0.2, a1=a1)
a2 = 0.25
a3 = 0.5
a4 = 0.25
b4 = np.concatenate([random.sample(list(b1), int(a2*a1)),
                       random.sample(list(b2), int(a3*a1)),
                       random.sample(list(b3), int(a4*a1))])
b5 = np.random.normal(loc=1, scale=0.3, a1=a1)
b6 = np.random.normal(loc=1.5, scale=0.4, a1=a1)
b7 = np.random.normal(loc=2, scale=0.3, a1=a1)
b8 = np.concatenate([random.sample(list(b5), int(a2*a1)),
                        random.sample(list(b6), int(a3*a1)),
                        random.sample(list(b7), int(a4*a1))])
def fonk1(data):
    b9 = mixture.GaussianMixture(n_components=3)
    b9.fit(data.reshape(-1, 1))
    b10 = b9.predict(data.reshape(-1, 1))
    plt.scatter(data, b10)
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data Points')
    plt.ylabel('Cluster')
    plt.show()
fonk1(b4)
