import numpy as np
from sklearn.cluster import KMeans
b1 = True
def fonk1(X):
    xmin, b2 = min(X, key=lambda a:a[0])[0], max(X,key=lambda a:a[0])[0]
    ymin, b3 = min(X, key=lambda a:a[1])[1], max(X,key=lambda a:a[1])[1]
    return (xmin,b2), (ymin,b3)
def fonk2(data, centers, b11):
    a1 = 0.0
    for i in range(len(data)):
        b4 = b11.item(i)
        a1 += np.linalg.norm(centers[b4] - data[i])**2
    return a1
def fonk3(data, b5 = 30, sampleTrials=10, b1=True):
    numData, b6 = data.shape
    b7 = [[min(data[:,dim]), max(data[:,dim])] \
                for dim in range(b6)]
    b8 = np.zeros(b5)
    b9 = np.zeros(b5)
    for k in range(b5):
        b10 = KMeans(n_clusters=(k + 1))
        b11 = b10.fit_predict(data)
        b12 = np.log(fonk2(data, b10.cluster_centers_, b11))
        b13 = np.zeros(sampleTrials)
        for trial in range(sampleTrials):
            b14 = np.zeros((numData, b6))
            for sample in range(numData):
                b14[sample] = [np.random.uniform(b7[dim][0], \
                                     b7[dim][1]) for dim in range(b6)]
            b15 = b10.fit_predict(b14)
            b13[trial] = \
                np.log(fonk2(b14, b10.cluster_centers_, \
                                         b15))
        b8[k] = sum(b13 - b12)**2 / sampleTrials
        b16 = sum(b13) / sampleTrials
        b17 = np.sqrt(sum((b13 - b16)**2) / sampleTrials)
        b9[k] = np.sqrt(1 + 1/sampleTrials) * b17
        if b1:
            print("Gap value at ", k, "clusters: ", b8[k - 1])
            print("Need to beat ", b8[k] - b9[k - 1])
        if k > 1 and b8[k - 1] > b8[k] - b9[k - 1]:
            return b11
    return b11