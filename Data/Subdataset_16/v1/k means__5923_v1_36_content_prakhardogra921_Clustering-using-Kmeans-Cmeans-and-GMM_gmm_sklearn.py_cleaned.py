import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
a1 = 500
b1 = np.random.normal(loc=1, scale=0.1, a1=a1)
b2 = np.random.normal(loc=1.5, scale=0.1, a1=a1)
b3 = np.random.normal(loc=2, scale=0.2, a1=a1)
a2 = 0.25
a3 = 0.5
a4 = 0.25
b4 = np.array(random.sample(list(b1), int(a2*a1)) +
                random.sample(list(b2), int(a3*a1)) +
                random.sample(list(b3), int(a4*a1)))
b5 = np.random.normal(loc=1, scale=0.3, a1=a1)
b6 = np.random.normal(loc=1.5, scale=0.4, a1=a1)
b7 = np.random.normal(loc=2, scale=0.3, a1=a1)
b8 = np.array(random.sample(list(b5), int(a2*a1)) +
                 random.sample(list(b6), int(a3*a1)) +
                 random.sample(list(b7), int(a4*a1)))
def fonk1(b4):
    b9 = mixture.GaussianMixture(n_components=3)
    b9.fit(b4.reshape(-1, 1))
    b10 = b9.predict(b4.reshape(-1, 1))
    plt.scatter(b4, b10)
    plt.title('GMM')
    plt.show()
fonk1(b4)
def fonk2(b1):
    b9 = mixture.GaussianMixture(n_components=2)
    b9.fit(b1.reshape(-1, 1))
    b11 = b9.predict(b1.reshape(-1, 1))
    b12 = plt.subplot(2, 1, 2)
    b13 = itertools.cycle(['navy', 'turquoise', 'cornflowerblue', 'darkorange'])
    for i, (mean, cov, color) in enumerate(zip(b9.means_, b9.covariances_, b13)):
        b16, b14 = linalg.eigh(cov)
        if not np.any(b11 = = i):
            continue
        plt.scatter(b1[b11 = = i, 0], np.zeros_like(b1[b11 == i]), .8, color=color)
        b15 = np.arctan2(b14[0][1], b14[0][0])
        b15 = 180. * b15 / np.pi
        b16 = 2. * np.sqrt(2.) * np.sqrt(b16)
        b17 = mpl.patches.Ellipse(mean, b16[0], b16[1], 180. + b15, color=color)
        b17.set_clip_box(b12.bbox)
        b17.set_alpha(.5)
        b12.add_artist(b17)
    plt.xticks(())
    plt.yticks(())
    plt.title('GMM with Ellipses')
    plt.subplots_adjust(b18 = .35, bottom=.02)
    plt.show()
fonk2(b1.reshape(-1, 1))