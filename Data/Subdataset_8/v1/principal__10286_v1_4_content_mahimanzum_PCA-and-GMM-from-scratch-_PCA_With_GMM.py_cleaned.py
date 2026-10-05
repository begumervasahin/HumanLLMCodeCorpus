import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
with open('data_online.txt') as f:
    train_data = []
    for line in f:
        train_data.append([float(x) for x in line.split()])
train_data = np.array(train_data)
cov_matrix = np.cov(train_data.T)
values, vectors = eig(cov_matrix)
vectors = vectors.T
indx = [i for i in range(len(values))]
sort_list = zip(values, indx)
sort_list = sorted(sort_list, key=lambda t: t[0])
pca1_idx = sort_list[-1][1]
pca2_idx = sort_list[-2][1]
pc1 = vectors[pca1_idx]
pc2 = vectors[pca2_idx]
transform = np.array([pc1, pc2])
trans_data = np.dot(train_data, transform.T)
def draw_main():
    plt.scatter(trans_data[:, 0], trans_data[:, 1], alpha=0.2)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
draw_main()
n_clusters = 3
P = np.random.rand(len(trans_data), n_clusters)
P /= np.sum(P, axis=1)[:, None]
mu = np.array([[0.0, 0.0]] * n_clusters)
for k in range(n_clusters):
    mu[k] = trans_data[np.random.randint(0, len(trans_data))]
sigma = np.array([[[1, 0.1], [0.1, 1]]] * n_clusters)
w = np.ones(n_clusters) / n_clusters
def draw():
    plt.figure(figsize=(8, 6))
    for k in range(n_clusters):
        x, y = np.mgrid[-4:10:.5, -6:6:.5]
        pos = np.empty(x.shape + (2,))
        pos[:, :, 0] = x
        pos[:, :, 1] = y
        rv = multivariate_normal(mu[k], sigma[k])
        plt.contour(x, y, rv.pdf(pos), alpha=0.5)
        plt.scatter(mu[k][0], mu[k][1], s=300, c='black', marker="d", alpha=0.5)
    plt.show()
draw()
prev = 0
def converged():
    global prev
    prob_sum = 0.0
    prob = 0.0
    for i in range(len(trans_data)):
        for k in range(n_clusters):
            prob_sum += w[k] * multivariate_normal.pdf(trans_data[i], mu[k], sigma[k])
        prob += np.log(prob_sum)
    if abs(prob - prev) <= 0.001:
        return True
    prev = prob
    return False
n_epochs = 2001
for epoch in range(n_epochs):
    if converged():
        break
    for i in range(len(trans_data)):
        for k in range(n_clusters):
            P[i][k] = w[k] * multivariate_normal.pdf(trans_data[i], mu[k], sigma[k])
        P[i] /= np.sum(P[i])
    for k in range(n_clusters):
        mu[k] = np.dot(P[:, k], trans_data) / np.sum(P[:, k])
        sigma[k] = np.dot((P[:, k] * (trans_data - mu[k])).T, (trans_data - mu[k])) / np.sum(P[:, k])
        w[k] = np.sum(P[:, k]) / len(trans_data)
    if epoch % 100 == 0:
        draw()
        print("Epoch:", epoch)
draw()
for k in range(n_clusters):
    print("Cluster ", k, " probability sum = ", np.sum(P[:, k]))