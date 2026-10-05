import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
def load_data(file_path):
    with open(file_path) as f:
        return np.array([list(map(float, line.split())) for line in f])
def perform_pca(data):
    cov_matrix = np.cov(data.T)
    eigenvalues, eigenvectors = eig(cov_matrix)
    sorted_indices = np.argsort(eigenvalues)
    pca1_idx, pca2_idx = sorted_indices[-2:]
    pc1, pc2 = eigenvectors[pca1_idx], eigenvectors[pca2_idx]
    transformation_matrix = np.array([pc1, pc2])
    return np.dot(data, transformation_matrix.T)
def plot_scatter(data):
    plt.scatter(data[:, 0], data[:, 1], alpha=0.2)
    plt.title('Principal Component Analysis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
def initialize_gmm(data, num_clusters):
    probabilities = np.random.rand(len(data), num_clusters)
    probabilities /= np.sum(probabilities, axis=1)[:, None]
    means = np.array([data[np.random.randint(0, len(data))] for _ in range(num_clusters)])
    covariances = np.array([[[1, 0.1], [0.1, 1]]] * num_clusters)
    weights = np.ones(num_clusters) / num_clusters
    return probabilities, means, covariances, weights
def plot_gmm(means, covariances):
    plt.figure(figsize=(8, 6))
    for k in range(len(means)):
        x, y = np.mgrid[-4:10:.5, -6:6:.5]
        pos = np.empty(x.shape + (2,))
        pos[:, :, 0] = x
        pos[:, :, 1] = y
        rv = multivariate_normal(means[k], covariances[k])
        plt.contour(x, y, rv.pdf(pos), alpha=0.5)
        plt.scatter(means[k][0], means[k][1], s=300, c='black', marker="d", alpha=0.5)
    plt.show()
def check_convergence(prev_likelihood, data, means, covariances, weights):
    curr_likelihood = 0.0
    for i in range(len(data)):
        likelihood = sum(weights[k] * multivariate_normal.pdf(data[i], means[k], covariances[k]) for k in range(len(means)))
        curr_likelihood += np.log(likelihood)
    return abs(curr_likelihood - prev_likelihood) <= 0.001
def train_gmm(data, num_clusters):
    probabilities, means, covariances, weights = initialize_gmm(data, num_clusters)
    max_epochs = 2001
    prev_likelihood = 0
    for epoch in range(max_epochs):
        if check_convergence(prev_likelihood, data, means, covariances, weights):
            break
        for i in range(len(data)):
            for k in range(num_clusters):
                probabilities[i][k] = weights[k] * multivariate_normal.pdf(data[i], means[k], covariances[k])
            probabilities[i] /= np.sum(probabilities[i])
        for k in range(num_clusters):
            means[k] = np.dot(probabilities[:, k], data) / np.sum(probabilities[:, k])
            covariances[k] = np.dot((probabilities[:, k] * (data - means[k])).T, (data - means[k])) / np.sum(probabilities[:, k])
            weights[k] = np.sum(probabilities[:, k]) / len(data)
        if epoch % 100 == 0:
            plot_gmm(means, covariances)
            print("Epoch:", epoch)
    plot_gmm(means, covariances)
    for k in range(num_clusters):
        print("Cluster", k, "probability sum =", np.sum(probabilities[:, k]))
data = load_data('data_online.txt')
trans_data = perform_pca(data)
plot_scatter(trans_data)
train_gmm(trans_data, num_clusters=3)