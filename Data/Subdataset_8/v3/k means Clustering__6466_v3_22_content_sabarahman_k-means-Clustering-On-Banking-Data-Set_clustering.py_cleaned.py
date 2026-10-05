import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
def load_dataset(file_path):
    return pd.read_csv(file_path)
def select_features(data):
    return data.iloc[:, [8, 12]].values
def perform_elbow_method(features, max_clusters=15):
    wcss = []
    for num_clusters in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        kmeans.fit(features)
        wcss.append(kmeans.inertia_)
    return wcss
def plot_elbow_method(wcss):
    plt.plot(range(1, len(wcss) + 1), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number Of Clusters')
    plt.ylabel('WCSS')
    plt.show()
def apply_kmeans(features, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    return kmeans.fit_predict(features), kmeans.cluster_centers_
def visualize_clusters(features, cluster_labels, centroids):
    colors = ['red', 'blue', 'green', 'pink']
    for i in range(len(colors)):
        plt.scatter(features[cluster_labels == i, 0], features[cluster_labels == i, 1],
                    s=25, c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=25, c='yellow', label='Centroids')
    plt.title('K-Means Clustering')
    plt.xlabel('Balance')
    plt.ylabel('Estimated Salary in $')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    dataset = load_dataset("Churn_Modelling.csv")
    features = select_features(dataset)
    wcss = perform_elbow_method(features)
    plot_elbow_method(wcss)
    optimal_num_clusters = 4
    cluster_labels, centroids = apply_kmeans(features, optimal_num_clusters)
    visualize_clusters(features, cluster_labels, centroids)