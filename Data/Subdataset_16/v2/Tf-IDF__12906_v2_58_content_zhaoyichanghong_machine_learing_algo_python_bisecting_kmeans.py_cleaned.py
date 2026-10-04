import numpy as np
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, b11, a1):
        b1 = b11.shape[0]
        b2 = [np.arange(b1)]
        while len(b2) < a1:
            b3 = [np.var(b11[cluster]) for cluster in b2]
            b4 = np.argmax(b3)
            b5 = b11[b2[b4]]
            b6 = KMeans(a1=2, random_state=0)
            b7 = b6.fit_predict(b5)
            b8 = [b2[b4][b7 == i] for i in range(2)]
            b2[b4] = b8[0]
            b2.append(b8[1])
        b9 = np.zeros(b1, dtype=int)
        for i, cluster in enumerate(b2):
            b9[cluster] = i
        return b9
if b10 = = "__main__":
    np.random.seed(42)
    b11 = np.random.rand(100, 2)
    b12 = class1()
    a1 = 3
    b7 = b12.fonk1(b11, a1)
    print("Cluster b7:", b7)