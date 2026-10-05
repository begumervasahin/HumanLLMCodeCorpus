import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
from scipy.stats import multivariate_normal
def load_data(file_path):
    data = []
    with open(file_path) as file:
        for line in file:
            data.append([float(x) for x in line.split()])
    return np.array(data)
def perform_pca(data):
    cov_matrix = np.cov(data.T)
    values, vectors = eig(cov_matrix)
    vectors = vectors.T
    pca1_idx, pca2_idx = np.argsort(values)[-2:]
    pc1, pc2 = vectors[pca1_idx], vectors[pca2_idx]
    transform = np.array([pc1, pc2])
    return np.dot(data, transform.T)
def plot_scatter(data):
    plt.scatter(data[:, 0], data[:, 1], alpha=0.2)
    plt.title('Initial Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
def initialize_clusters(data, num_clusters):
    mean_x, mean_y = np.mean(data, axis=0)
    mean_shift = 0.5
    initial_means = np.array([[mean_x + (np.random.rand() - 0.5) * mean_shift,
                               mean_y + (np.random.rand() - 0.5) * mean_shift]
                               for _ in range(num_clusters)])
    initial_covariances = np.array([[[1, 0.1], [0.1, 1.0]] for _ in range(num_clusters)])
    initial_weights = np.full(num_clusters, 1 / num_clusters)
    return initial_means, initial_covariances, initial_weights
def plot_clusters(data, means, covariances):
    colors = ['red', 'blue', 'green', 'black']
    for k in range(len(means)):
        plt.scatter(data[:, 0], data[:, 1], c='grey', alpha=0.2)
        x, y = np.mgrid[-4:10:.5, -6:6:.5]
        pos = np.empty(x.shape + (2,))
        pos[:, :, 0] = x
        pos[:, :, 1] = y
        rv = multivariate_normal(means[k], covariances[k])
        plt.contour(x, y, rv.pdf(pos), colors=colors[k], alpha=0.5)
    plt.show()
def has_converged(prev, current):
    return np.abs(current - prev) <= 0.001
train_data = load_data('data_online.txt')
trans_data = perform_pca(train_data)
plot_scatter(trans_data)
num_clusters = 4
mu, sigma, w = initialize_clusters(trans_data, num_clusters)
plot_clusters(trans_data, mu, sigma)
prev_log_likelihood = 0
num_epochs = 2001
for epoch in range(num_epochs):
    for i in range(len(trans_data)):
        for k in range(num_clusters):
            P[i][k] = w[k] * multivariate_normal.pdf(trans_data[i], mu[k], sigma[k])
        P[i] /= np.sum(P[i])
    for k in range(num_clusters):
        mu[k] = np.dot(P[:, k], trans_data) / np.sum(P[:, k])
        X = trans_data - mu[k]
        sigma[k] = np.dot(P[:, k] * X.T, X) / np.sum(P[:, k])
        w[k] = np.sum(P[:, k]) / len(trans_data)
    current_log_likelihood = sum(np.log(sum(w[k] * multivariate_normal.pdf(trans_data[i], mu[k], sigma[k]) for k in range(num_clusters))) for i in range(len(trans_data)))
    if has_converged(prev_log_likelihood, current_log_likelihood):
        break
    prev_log_likelihood = current_log_likelihood
    if epoch % 1 == 0:
        plot_clusters(trans_data, mu, sigma)
        print("Means at epoch ", epoch, ":", mu)
for k in range(num_clusters):
    print("Cluster ", k, " probability sum = ", np.sum(P[:, k]))