import random
import sys
import numpy as np
import scipy.stats
import scipy.cluster.vq as vq
import scipy.spatial.distance as norms
import data
import math
__author__ = "Yashaswi Mohanty"
__email__ = "ymohanty@colby.edu"
__version__ = "2/21/2016"
def kmeans_init(d, K, categories=None):
    means = []
    A = d
    N = A.shape[0]
    if categories is None:
        for i in range(K):
            means.append(A[np.random.randint(0, N)].tolist()[0])
    else:
        if K != max(categories) + 1:
            print("The highest category label and specified clusters should be the same")
            return
        for i in range(K):
            sum = np.zeros(A.shape[1])
            num_elem = 0
            for j in range(len(categories)):
                if categories[j] == i:
                    sum = np.add(sum, A[j].tolist()[0])
                    num_elem += 1
            sum = 1 / float(num_elem) * sum
            means.append(sum)
    return np.matrix(means)
def kmeans_classify(A, means, metric):
    data_classes = []
    data_metrics = []
    dist = sys.maxsize
    for v in A:
        index = 0
        for i in range(len(means.tolist())):
            m = means.tolist()[i]
            norm_matrix = np.vstack((v, m))
            if norms.pdist(norm_matrix, metric)[0] < dist:
                dist = norms.pdist(norm_matrix, metric)[0]
                index = i
        data_classes.append([index])
        data_metrics.append([dist])
        dist = sys.maxsize
    return np.matrix(data_classes), np.matrix(data_metrics)
def kmeans_algorithm(A, means, metric):
    MIN_CHANGE = 1e-7
    MAX_ITERATIONS = 100
    D = means.shape[1]
    K = means.shape[0]
    N = A.shape[0]
    for i in range(MAX_ITERATIONS):
        codes, errors = kmeans_classify(A, means, metric)
        newmeans = np.zeros_like(means)
        counts = np.zeros((K, 1))
        for j in range(N):
            newmeans[codes[j, 0], :] += A[j, :]
            counts[codes[j, 0], 0] += 1.0
        for j in range(K):
            if counts[j, 0] > 0.0:
                newmeans[j, :] /= counts[j, 0]
            else:
                newmeans[j, :] = A[random.randint(0, A.shape[0]), :]
        diff = np.sum(np.square(means - newmeans))
        means = newmeans
        if diff < MIN_CHANGE:
            break
    codes, errors = kmeans_classify(A, means, metric)
    return means, codes, errors
def kmeans(d, headers, K, metric, whiten=True, categories=None):
    try:
        A = d.get_data(headers)
    except AttributeError:
        A = d
    if whiten:
        W = vq.whiten(A)
    else:
        W = A
    codebook = kmeans_init(W, K, categories)
    codebook, codes, errors = kmeans_algorithm(W, codebook, metric)
    return codebook, codes, errors
if __name__ == '__main__':
    d = data.Data("clusterdata.csv")
    means = kmeans_init(d, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    print(kmeans_classify(d, means))