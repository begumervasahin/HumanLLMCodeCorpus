import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
def fonk1(a1, loc_scale_pairs, b14):
    b1 = [np.random.normal(loc=loc, scale=scale, a1=a1) for loc, scale in loc_scale_pairs]
    b2 = np.concatenate([random.sample(list(subset), int(p * a1)) for subset, p in zip(b1, b14)])
    return b2
def fonk2(b2, b3 = 3):
    b4 = mixture.GaussianMixture(b3=b3)
    b4.fit(b2.reshape(-1, 1))
    b5 = b4.predict(b2.reshape(-1, 1))
    plt.scatter(b2, b5)
    plt.title('GMM Clustering')
    plt.show()
def fonk3(data, b3 = 2):
    b4 = mixture.GaussianMixture(b3=b3)
    b4.fit(data.reshape(-1, 1))
    b5 = b4.predict(data.reshape(-1, 1))
    fig, b6 = plt.subplots()
    b7 = itertools.cycle(['navy', 'turquoise', 'cornflowerblue', 'darkorange'])
    for i, (mean, cov, color) in enumerate(zip(b4.means_, b4.covariances_, b7)):
        if not np.any(b5 = = i):
            continue
        plt.scatter(data[b5 = = i], np.zeros_like(data[b5 == i]), 0.8, color=color)
        b10, b8 = linalg.eigh(cov)
        b9 = np.arctan2(b8[0][1], b8[0][0])
        b9 = 180. * b9 / np.pi
        b10 = 2. * np.sqrt(2.) * np.sqrt(b10)
        b11 = mpl.patches.Ellipse(mean, b10[0], b10[1], 180. + b9, color=color)
        b11.set_clip_box(b6.bbox)
        b11.set_alpha(0.5)
        b6.add_artist(b11)
    plt.xticks(())
    plt.yticks(())
    plt.title('GMM with Ellipses')
    plt.show()
a1 = 500
b12 = [(1, 0.1), (1.5, 0.1), (2, 0.2)]
b13 = [(1, 0.3), (1.5, 0.4), (2, 0.3)]
b14 = [0.25, 0.5, 0.25]
b15 = fonk1(a1, b12, b14)
b16 = fonk1(a1, b13, b14)
fonk2(b15)
fonk3(b15)