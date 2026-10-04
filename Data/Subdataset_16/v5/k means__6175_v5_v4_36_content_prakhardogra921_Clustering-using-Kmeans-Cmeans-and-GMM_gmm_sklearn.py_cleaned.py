import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import random
def fonk1(b1, scale, a1):
    return np.random.normal(b1 = b1, scale=scale, a1=a1)
def fonk2(sets, b6, a1):
    b2 = []
    for data_set, proportion in zip(sets, b6):
        b2.extend(random.sample(list(data_set), int(proportion * a1)))
    return np.array(b2)
def fonk3(data, b3 = 3):
    b4 = mixture.GaussianMixture(b3=b3)
    b4.fit(data.reshape(-1, 1))
    b5 = b4.predict(data.reshape(-1, 1))
    plt.scatter(data, b5)
    plt.title('Gaussian Mixture Model')
    plt.xlabel('Data Points')
    plt.ylabel('Cluster')
    plt.show()
a1 = 500
b6 = [0.25, 0.5, 0.25]
b7 = fonk1(b1=1, scale=0.1, a1=a1)
b8 = fonk1(b1=1.5, scale=0.1, a1=a1)
b9 = fonk1(b1=2, scale=0.2, a1=a1)
b10 = fonk2([b7, b8, b9], b6, a1)
fonk3(b10)
b11 = fonk1(b1=1, scale=0.3, a1=a1)
b12 = fonk1(b1=1.5, scale=0.4, a1=a1)
b13 = fonk1(b1=2, scale=0.3, a1=a1)
b14 = fonk2([b11, b12, b13], b6, a1)
