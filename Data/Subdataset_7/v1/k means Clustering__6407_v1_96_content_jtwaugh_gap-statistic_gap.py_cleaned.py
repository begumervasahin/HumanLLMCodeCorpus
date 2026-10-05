import numpy as np
from sklearn.cluster import KMeans
def fonk1(X):
    xmin, b1 = min(X, key=lambda a: a[0])[0], max(X, key=lambda a: a[0])[0]
    ymin, b2 = min(X, key=lambda a: a[1])[1], max(X, key=lambda a: a[1])[1]
    return (xmin, b1), (ymin, b2)
def fonk2(b18, centers, b10):
    a1 = 0.0
    for i in range(len(b18)):
        b3 = b10.item(i)
        a1 += np.linalg.norm(centers[b3] - b18[i])**2
    return a1
def fonk3(b18, b4 = 30, sampleTrials=10, printResults=True):
    numData, b5 = b18.shape
    b6 = [[min(b18[:, dim]), max(b18[:, dim])] for dim in range(b5)]
    b7 = np.zeros(b4)
    b8 = np.zeros(b4)
    for k in range(b4):
        b9 = KMeans(n_clusters=(k + 1))
        b10 = b9.fit_predict(b18)
        b11 = np.log(fonk2(b18, b9.cluster_centers_, b10))
        b12 = np.zeros(sampleTrials)
        for trial in range(sampleTrials):
            b13 = np.zeros((numData, b5))
            for sample in range(numData):
                b13[sample] = [np.random.uniform(b6[dim][0], b6[dim][1]) for dim in range(b5)]
            b14 = b9.fit_predict(b13)
            b12[trial] = np.log(fonk2(b13, b9.cluster_centers_, b14))
        b7[k] = sum(b12 - b11)**2 / sampleTrials
        b15 = sum(b12) / sampleTrials
        b16 = np.sqrt(sum((b12 - b15)**2) / sampleTrials)
        b8[k] = np.sqrt(1 + 1/sampleTrials) * b16
        if printResults:
            if k > 0:
                print("Gap value at", k, "clusters:", b7[k - 1])
                print("Need to beat", b7[k] - b8[k - 1])
        if k > 0 and b7[k - 1] > b7[k] - b8[k - 1]:
            return b10
    return b10
if b17 = = "__main__":
    np.random.seed(0)
    b18 = np.random.rand(100, 2)
    b10 = fonk3(b18)
    print("Final b10:", b10)