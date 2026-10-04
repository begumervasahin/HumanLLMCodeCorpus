import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
def load_data(filepath):
    data = pd.read_csv(filepath)
    coordinates = data[['x-coord', 'y-coord']].values
    country_names = data['CountryName'].values
    return coordinates, country_names
def plot_countries(coordinates, country_names):
    plt.figure(figsize=(8, 10))
    plt.subplot(211)
    for (x, y), name in zip(coordinates, country_names):
        plt.scatter(x, y, color='black')
        plt.text(x, y, name, fontsize=6)
    plt.title('Countries')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
def perform_clustering(coordinates, num_clusters=4):
    distance_matrix = pdist(coordinates, 'euclidean')
    linkage_matrix = linkage(distance_matrix, method='single')
    clusters = fcluster(linkage_matrix, t=num_clusters, criterion='maxclust')
    return clusters
def plot_clusters(coordinates, clusters):
    cluster_colors = ['r', 'g', 'b', 'm']
    plt.subplot(212)
    for color, cluster_id in zip(cluster_colors, np.unique(clusters)):
        cluster_points = clusters == cluster_id
        plt.scatter(coordinates[cluster_points, 0], coordinates[cluster_points, 1], c=color, label=f'Cluster {cluster_id}')
    plt.title('Clusters')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
    plt.legend()
def main(filepath):
    coordinates, country_names = load_data(filepath)
    plot_countries(coordinates, country_names)
    clusters = perform_clustering(coordinates)
    plot_clusters(coordinates, clusters)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    filepath = 'final_countries_data.csv'
    main(filepath)