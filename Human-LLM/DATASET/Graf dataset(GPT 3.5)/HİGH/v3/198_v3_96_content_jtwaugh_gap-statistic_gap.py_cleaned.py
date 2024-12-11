import numpy as np
from sklearn.cluster import KMeans
def fonk1(points):
    b1 = min(points, key=lambda a: a[0])[0]
    b2 = max(points, key=lambda a: a[0])[0]
    b3 = min(points, key=lambda a: a[1])[1]
    b4 = max(points, key=lambda a: a[1])[1]
    return (b1, b2), (b3, b4)
def fonk2(b20, centers, b12):
    a1 = 0.0
    for i in range(len(b20)):
        b5 = b12.item(i)
        a1 += np.linalg.norm(centers[b5] - b20[i])**2
    return a1
def fonk3(b20, b6 = 30, sample_trials=10, print_results=True):
    num_data, b7 = b20.shape
    b8 = [[min(b20[:, dim]), max(b20[:, dim])] for dim in range(b7)]
    b9 = np.zeros(b6)
    b10 = np.zeros(b6)
    for k in range(b6):
        b11 = KMeans(n_clusters=(k + 1))
        b12 = b11.fit_predict(b20)
        b13 = np.log(fonk2(b20, b11.cluster_centers_, b12))
        b14 = np.zeros(sample_trials)
        for trial in range(sample_trials):
            b15 = np.zeros((num_data, b7))
            for sample in range(num_data):
                b15[sample] = [np.random.uniform(b8[dim][0], b8[dim][1]) for dim in range(b7)]
            b16 = b11.fit_predict(b15)
            b14[trial] = np.log(fonk2(b15, b11.cluster_centers_, b16))
        b9[k] = sum(b14 - b13)**2 / sample_trials
        b17 = sum(b14) / sample_trials
        b18 = np.sqrt(sum((b14 - b17)**2) / sample_trials)
        b10[k] = np.sqrt(1 + 1/sample_trials) * b18
        if print_results and k > 0:
            print("Gap value at", k, "clusters:", b9[k - 1])
            print("Need to beat", b9[k] - b10[k - 1])
        if k > 0 and b9[k - 1] > b9[k] - b10[k - 1]:
            return b12
    return b12
if b19 = = "__main__":
    np.random.seed(0)
    b20 = np.random.rand(100, 2)
    b12 = fonk3(b20)
    print("Final b12:", b12)