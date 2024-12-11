import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
plt.style.use('ggplot')
def fonk1(b1 = 1, max_val=20):
    return random.randint(b1, max_val)
def fonk2(b5, b8, b7):
    b2 = ["g.", "r.", "c.", "y."]
    for i in range(len(b5)):
        plt.plot(b5[i][0], b5[i][1], b2[b8[i]], b3 = 10)
    plt.scatter(b7[:, 0], b7[:, 1], b4 = "x", s=150, linewidths=5, zorder=10)
    plt.show()
b5 = np.array([[fonk1(), fonk1()] for _ in range(6)])
b6 = KMeans(n_clusters=2)
b6.fit(b5)
b7 = b6.cluster_centers_
b8 = b6.labels_
fonk2(b5, b8, b7)