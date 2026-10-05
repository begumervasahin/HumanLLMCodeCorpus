import math
import numpy as np
import matplotlib.pyplot as plt
DATA = np.loadtxt("data_kmeans.txt")
OBS, FEATURES = DATA.shape
def form_cluster(clusters):
    threshold = 1000000000
    cluster_observations = np.zeros((OBS, clusters))
    centroids = np.random.uniform(low=-10, high=10, size=(clusters, FEATURES))
    while True:
        for obs_idx in range(OBS):
            for cluster_idx in range(clusters):
                sum_of_squares = 0
                for feature_idx in range(FEATURES):
                    diff = math.pow((DATA[obs_idx][feature_idx] - centroids[cluster_idx][feature_idx]), 2)
                    sum_of_squares += diff
                cluster_observations[obs_idx][cluster_idx] = sum_of_squares
        cluster_assignment = cluster_observations.argmin(axis=1)
        loss = calculate_loss(cluster_observations, cluster_assignment)
        if loss <= threshold:
            break
        else:
            threshold = loss
            centroids = re_evaluate(clusters, cluster_assignment)
    return cluster_observations, cluster_assignment
def re_evaluate(clusters, cluster_assignment):
    centroids = np.zeros((clusters, FEATURES))
    for cluster_idx in range(clusters):
        count = 0
        cluster_sum = np.zeros(FEATURES)
        for obs_idx in range(OBS):
            if cluster_assignment[obs_idx] == cluster_idx:
                for feature_idx in range(FEATURES):
                    cluster_sum[feature_idx] += DATA[obs_idx][feature_idx]
                count += 1
        for feature_idx in range(FEATURES):
            centroids[cluster_idx][feature_idx] = cluster_sum[feature_idx] / count
    return centroids
def calculate_loss(cluster_observations, cluster_assignment):
    total_loss = 0
    for obs_idx in range(OBS):
        total_loss += cluster_observations[obs_idx][int(cluster_assignment[obs_idx])]
    return total_loss
def draw_plot(cluster_observations, cluster_assignment):
    x_pos = DATA[:, 0]
    y_pos = DATA[:, 1]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for i in range(len(DATA)):
        ax.scatter(x_pos[i], y_pos[i], color=colors[int(cluster_assignment[i])])
    plt.show()
def main():
    cluster_observations, cluster_assignment = form_cluster(2)
    draw_plot(cluster_observations, cluster_assignment)
if __name__ == '__main__':
    main()