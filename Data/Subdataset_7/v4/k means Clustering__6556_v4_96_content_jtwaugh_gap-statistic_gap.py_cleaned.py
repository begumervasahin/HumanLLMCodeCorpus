import numpy as np
from sklearn.cluster import KMeans
def fonk1(data):
    xmin, b1 = min(data, key=lambda a: a[0])[0], max(data, key=lambda a: a[0])[0]
    ymin, b2 = min(data, key=lambda a: a[1])[1], max(data, key=lambda a: a[1])[1]
    return (xmin, b1), (ymin, b2)
def fonk2(data, centers, b10):
    a1 = 0.0
    for i in range(len(data)):
        b3 = b10.item(i)
        a1 += np.linalg.norm(centers[b3] - data[i]) ** 2
    return a1
def fonk3(data, b4 = 30, sample_trials=10, print_results=True):
    num_data, b5 = data.shape
    b6 = [[min(data[:, dim]), max(data[:, dim])] for dim in range(b5)]
    b7 = np.zeros(b4)
    b8 = np.zeros(b4)
    for k in range(b4):
        b9 = KMeans(n_clusters=(k + 1))
        b10 = b9.fit_predict(data)
        b11 = np.log(fonk2(data, b9.cluster_centers_, b10))
        b12 = np.zeros(sample_trials)
        for trial in range(sample_trials):
            b13 = np.zeros((num_data, b5))
            for sample in range(num_data):
                b13[sample] = [np.random.uniform(b6[dim][0], b6[dim][1])
                                   for dim in range(b5)]
            b14 = b9.fit_predict(b13)
            b12[trial] = np.log(fonk2(b13, b9.cluster_centers_, b14))
        b7[k] = sum(b12 - b11) ** 2 / sample_trials
        b15 = sum(b12) / sample_trials
        b16 = np.sqrt(sum((b12 - b15) ** 2) / sample_trials)
        b8[k] = np.sqrt(1 + 1 / sample_trials) * b16
        if print_results:
            if k > 0:
                print("Gap value at", k, "clusters:", b7[k - 1])
                print("Need to beat", b7[k] - b8[k - 1])
        if k > 0 and b7[k - 1] > b7[k] - b8[k - 1]:
            return b10
    return b10