
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def load_data(file_path):
    columns_to_use = ['latitude', 'longitude', 'reviewCount', 'checkins']
    data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
    return data[columns_to_use]
def scale_features(data, features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[features])
    return scaled_features
def perform_kmeans_clustering(scaled_features, num_clusters=4):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(scaled_features)
    cluster_labels = kmeans.predict(scaled_features)
    centroids = kmeans.cluster_centers_
    return kmeans, cluster_labels, centroids
def print_cluster_info(kmeans, centroids):
    print(f"Within-cluster sum of squares: {kmeans.inertia_:.2f}")
    for i, centroid in enumerate(centroids, 1):
        print(f"Centroid {i}: Latitude = {centroid[0]:.4f}, Longitude = {centroid[1]:.4f}")
def plot_clusters(data, cluster_labels, centroids):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['latitude'], data['longitude'], c=cluster_labels, s=50, cmap='viridis', label='Cluster Points')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5, label='Centroids')
    plt.title("Cluster Visualization of Yelp Data")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.legend()
    plt.savefig('Latitude-Longitude.jpg')
    plt.show()
def main():
    file_path = "./yelp.csv"
    data = load_data(file_path)
    scaled_features = scale_features(data, ['latitude', 'longitude'])
    kmeans, cluster_labels, centroids = perform_kmeans_clustering(scaled_features)
    print_cluster_info(kmeans, centroids)
    plot_clusters(data, cluster_labels, centroids)
if __name__ == "__main__":
    main()