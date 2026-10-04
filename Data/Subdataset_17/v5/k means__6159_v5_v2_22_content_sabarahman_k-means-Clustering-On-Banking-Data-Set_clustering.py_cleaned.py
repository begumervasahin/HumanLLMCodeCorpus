import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path)
def select_features(dataset, feature_indices):
    return dataset.iloc[:, feature_indices].values
def calculate_wcss(features, max_clusters=15):
    wcss = []
    for num_clusters in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        kmeans.fit(features)
        wcss.append(kmeans.inertia_)
    return wcss
def plot_elbow_method(wcss):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(wcss) + 1), wcss, marker='o', linestyle='--', color='b')
    plt.title('Elbow Method to Determine Optimal Number of Clusters')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.grid(True)
    plt.show()
def apply_kmeans(features, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    return kmeans.fit_predict(features), kmeans.cluster_centers_
def plot_clusters(features, cluster_labels, cluster_centers):
    plt.figure(figsize=(10, 6))
    colors = ['red', 'blue', 'green', 'purple']
    for i in range(len(colors)):
        plt.scatter(features[cluster_labels == i, 0], features[cluster_labels == i, 1],
                    s=50, c=colors[i], label=f'Cluster {i + 1}')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
                s=200, c='yellow', marker='X', label='Centroids')
    plt.title('K-Means Clustering of Customers')
    plt.xlabel('Balance ($)')
    plt.ylabel('Estimated Salary ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
file_path = "Churn_Modelling.csv"
feature_indices = [8, 12]
optimal_num_clusters = 4
dataset = load_data(file_path)
features = select_features(dataset, feature_indices)
wcss = calculate_wcss(features)
plot_elbow_method(wcss)
cluster_labels, cluster_centers = apply_kmeans(features, optimal_num_clusters)
plot_clusters(features, cluster_labels, cluster_centers)