import numpy as np
from sklearn.cluster import KMeans
def bounding_box(X):
    xmin, xmax = min(X, key=lambda a: a[0])[0], max(X, key=lambda a: a[0])[0]
    ymin, ymax = min(X, key=lambda a: a[1])[1], max(X, key=lambda a: a[1])[1]
    return (xmin, xmax), (ymin, ymax)
def compactness(data, centers, labels):
    kSum = 0.0
    for i in range(len(data)):
        clusterNum = labels.item(i)
        kSum += np.linalg.norm(centers[clusterNum] - data[i])**2
    return kSum
def gapKMeans(data, kRange=30, sampleTrials=10, printResults=True):
    numData, numFeatures = data.shape
    extrema = [[min(data[:, dim]), max(data[:, dim])] for dim in range(numFeatures)]
    gap = np.zeros(kRange)
    s = np.zeros(kRange)
    for k in range(kRange):
        kclusters = KMeans(n_clusters=(k + 1))
        labels = kclusters.fit_predict(data)
        kCompactness = np.log(compactness(data, kclusters.cluster_centers_, labels))
        trialCompactness = np.zeros(sampleTrials)
        for trial in range(sampleTrials):
            samples = np.zeros((numData, numFeatures))
            for sample in range(numData):
                samples[sample] = [np.random.uniform(extrema[dim][0], extrema[dim][1]) for dim in range(numFeatures)]
            sampleLabels = kclusters.fit_predict(samples)
            trialCompactness[trial] = np.log(compactness(samples, kclusters.cluster_centers_, sampleLabels))
        gap[k] = sum(trialCompactness - kCompactness)**2 / sampleTrials
        wbar = sum(trialCompactness) / sampleTrials
        sd = np.sqrt(sum((trialCompactness - wbar)**2) / sampleTrials)
        s[k] = np.sqrt(1 + 1/sampleTrials) * sd
        if printResults:
            if k > 0:
                print("Gap value at", k, "clusters:", gap[k - 1])
                print("Need to beat", gap[k] - s[k - 1])
        if k > 0 and gap[k - 1] > gap[k] - s[k - 1]:
            return labels
    return labels
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(100, 2)
    labels = gapKMeans(data)
    print("Final labels:", labels)