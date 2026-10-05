
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
def load_data(file_path):
    return pd.read_csv(file_path)
def preprocess_data(dataset):
    categories = dataset.iloc[:, [10]].values
    subcategories = dataset.iloc[:, [9]].values
    label_encoder = LabelEncoder()
    categories_encoded = label_encoder.fit_transform(categories[:, 0])
    subcategories_encoded = label_encoder.fit_transform(subcategories[:, 0])
    encoded_data = np.vstack((subcategories_encoded, categories_encoded)).T
    onehot_encoder = OneHotEncoder(categories='auto')
    encoded_data = onehot_encoder.fit_transform(encoded_data).toarray()
    return encoded_data
def apply_pca(data, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)
def find_optimal_clusters(data):
    wcss = []
    for num_clusters in range(1, 11):
        kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=1000, n_init=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss
def visualize_clusters(data, cluster_labels, centroids):
    for cluster_num in range(len(centroids)):
        plt.scatter(data[cluster_labels == cluster_num, 0], data[cluster_labels == cluster_num, 1],
                    s=100, label=f'Cluster {cluster_num + 1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', label='Centroids')
    plt.title('Clusters of customers')
    plt.xlabel('Category')
    plt.ylabel('Subcategory')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    dataset = load_data('FYP.csv')
    encoded_data = preprocess_data(dataset)
    reduced_data = apply_pca(encoded_data)
    wcss = find_optimal_clusters(reduced_data)
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
    optimal_num_clusters = 3
    kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', max_iter=1000, n_init=10)
    cluster_labels = kmeans.fit_predict(reduced_data)
    visualize_clusters(reduced_data, cluster_labels, kmeans.cluster_centers_)