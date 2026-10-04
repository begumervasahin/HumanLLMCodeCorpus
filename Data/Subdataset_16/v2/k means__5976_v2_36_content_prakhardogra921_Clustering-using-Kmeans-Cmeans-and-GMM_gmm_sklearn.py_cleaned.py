import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
from scipy import linalg
import itertools
import matplotlib as mpl
import random
def fonk1(a1, loc1, scale1, loc2, scale2, loc3, scale3, p1, p2, b14):
    b1 = np.random.normal(loc=loc1, scale=scale1, a1=a1)
    b2 = np.random.normal(loc=loc2, scale=scale2, a1=a1)
    b3 = np.random.normal(loc=loc3, scale=scale3, a1=a1)
    b4 = np.array(
        random.sample(list(b1), int(p1 * a1)) +
        random.sample(list(b2), int(p2 * a1)) +
        random.sample(list(b3), int(b14 * a1))
    )
    return b4
def fonk2(b4, b5 = 3):
    b6 = mixture.GaussianMixture(b5=b5)
    b6.fit(b4.reshape(-1, 1))
    b7 = b6.predict(b4.reshape(-1, 1))
    plt.scatter(b4, b7)
    plt.title('GMM')
    plt.show()
def fonk3(data, b5 = 2):
    b6 = mixture.GaussianMixture(b5=b5)
    b6.fit(data.reshape(-1, 1))
    b7 = b6.predict(data.reshape(-1, 1))
    fig, b8 = plt.subplots()
    b9 = itertools.cycle(['navy', 'turquoise', 'cornflowerblue', 'darkorange'])
    for i, (mean, cov, color) in enumerate(zip(b6.means_, b6.covariances_, b9)):
        if not np.any(b7 = = i):
            continue
        plt.scatter(data[b7 = = i], np.zeros_like(data[b7 == i]), 0.8, color=color)
        b12, b10 = linalg.eigh(cov)
        b11 = np.arctan2(b10[0][1], b10[0][0])
        b11 = 180. * b11 / np.pi
        b12 = 2. * np.sqrt(2.) * np.sqrt(b12)
        b13 = mpl.patches.Ellipse(mean, b12[0], b12[1], 180. + b11, color=color)
        b13.set_clip_box(b8.bbox)
        b13.set_alpha(0.5)
        b8.add_artist(b13)
    plt.xticks(())
    plt.yticks(())
    plt.title('GMM with Ellipses')
    plt.show()
a1 = 500
p1, p2, b14 = 0.25, 0.5, 0.25
b15 = fonk1(a1, loc1=1, scale1=0.1, loc2=1.5, scale2=0.1, loc3=2, scale3=0.2, p1=p1, p2=p2, b14=b14)
b16 = fonk1(a1, loc1=1, scale1=0.3, loc2=1.5, scale2=0.4, loc3=2, scale3=0.3, p1=p1, p2=p2, b14=b14)
fonk2(b15)
fonk3(b15)