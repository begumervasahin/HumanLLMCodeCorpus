import numpy as np
from sklearn.cluster import KMeans
def fonk1(data):
    b1 = min(data[:, 0])
    b2 = max(data[:, 0])
    b3 = min(data[:, 1])
    b4 = max(data[:, 1])
    return (b1, b2), (b3, b4)
def fonk2(data, centers, b12):
    a1 = 0.0
    for i in range(len(data)):
        b5 = b12.item(i)
        a1 += np.linalg.norm(centers[b5] - data[i]) ** 2
    return a1
def fonk3(data, b6 = 30, sample_trials=10, print_results=True):
    num_data, b7 = data.shape
    b8 = [[min(data[:, dim]), max(data[:, dim])] for dim in range(b7)]
    b9 = np.zeros(b6)
    b10 = np.zeros(b6)
    for k in range(b6):
        b11 = KMeans(n_clusters=(k + 1))
        b12 = b11.fit_predict(data)
        b13 = np.log(fonk2(data, b11.cluster_centers_, b12))
        b14 = np.zeros(sample_trials)
        for trial in range(sample_trials):
            b15 = np.zeros((num_data, b7))
            for sample in range(num_data):
                b15[sample] = [np.random.uniform(b8[dim][0], b8[dim][1])
                                   for dim in range(b7)]
            b16 = b11.fit_predict(b15)
            b14[trial] = np.log(fonk2(b15, b11.cluster_centers_, b16))
        b9[k] = sum(b14 - b13) ** 2 / sample_trials
        b17 = sum(b14) / sample_trials
        b18 = np.sqrt(sum((b14 - b17) ** 2) / sample_trials)
        b10[k] = np.sqrt(1 + 1 / sample_trials) * b18
        if print_results and k > 0:
            print("Gap value at", k, "clusters:", b9[k - 1])
            print("Need to beat", b9[k] - b10[k - 1])
        if k > 0 and b9[k - 1] > b9[k] - b10[k - 1]:
            return b12
    return b12