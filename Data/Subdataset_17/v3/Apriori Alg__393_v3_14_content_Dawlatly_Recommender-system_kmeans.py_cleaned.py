
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
def load_dataset(file_path):
    return pd.read_csv(file_path)
def preprocess_data(dataset):
    X = dataset.iloc[:, [10]].values
    Y = dataset.iloc[:, [9]].values
    labelencoder_X = LabelEncoder()
    X = labelencoder_X.fit_transform(X[:, 0])
    labelencoder_Y = LabelEncoder()
    Y = labelencoder_Y.fit_transform(Y[:, 0])
    combined = np.vstack((Y, X)).T
    onehotencoder = OneHotEncoder()
    combined = onehotencoder.fit_transform(combined).toarray()
    return combined
def apply_pca(data, n_components=2):
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(data)
    explained_variance = pca.explained_variance_ratio_
    return reduced_data, explained_variance
def plot_elbow_method(data):
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
def fit_kmeans(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=1000, n_init=10)
    y_kmeans = kmeans.fit_predict(data)
    return kmeans, y_kmeans
def plot_clusters(data, kmeans, y_kmeans):
    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
    plt.title('Clusters of customers')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
def main():
    file_path = 'FYP.csv'
    dataset = load_dataset(file_path)
    print(dataset.head())
    preprocessed_data = preprocess_data(dataset)
    reduced_data, explained_variance = apply_pca(preprocessed_data)
    print("Explained Variance Ratio:", explained_variance)
    plot_elbow_method(reduced_data)
    kmeans, y_kmeans = fit_kmeans(reduced_data)
    plot_clusters(reduced_data, kmeans, y_kmeans)
if __name__ == "__main__":
    main()