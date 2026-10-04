import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
def load_and_standardize_data(file_path):
    data = pd.read_csv(file_path)
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)
    return standardized_data
def perform_hierarchical_clustering(data, method='average'):
    linkage_matrix = linkage(data, method=method)
    cophenet_corr, cophenet_distances = cophenet(linkage_matrix, pdist(data))
    max_distances = maxdists(linkage_matrix)
    return linkage_matrix, cophenet_corr, cophenet_distances, max_distances
def plot_dendrogram(linkage_matrix, title, truncate_mode=None, p=None):
    plt.figure(figsize=(30, 15) if not truncate_mode else (20, 10))
    plt.title(title)
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    dendrogram(
        linkage_matrix,
        leaf_rotation=90.,
        leaf_font_size=10. if not truncate_mode else 12.,
        truncate_mode=truncate_mode,
        p=p,
        show_contracted=bool(truncate_mode)
    )
    plt.show()
def display_clustering_metrics(cophenet_corr, linkage_matrix, cophenet_distances, max_distances):
    print(f'Cophenet Correlation Coefficient: {cophenet_corr:.3f}')
    print(f'First Cluster Merged: {linkage_matrix[0]}')
    print(f'First 10 Cophenet Pairwise Distances: {cophenet_distances[:10]}')
    print(f'First 10 Max Cluster Distances: {max_distances[:10]}')
def main():
    file_path = 'Flagdata.csv'
    standardized_data = load_and_standardize_data(file_path)
    linkage_matrix, cophenet_corr, cophenet_distances, max_distances = perform_hierarchical_clustering(standardized_data)
    display_clustering_metrics(cophenet_corr, linkage_matrix, cophenet_distances, max_distances)
    plot_dendrogram(linkage_matrix, 'Dendrogram for Flag Data')
    plot_dendrogram(linkage_matrix, 'Truncated Dendrogram (Last 12 Merged Clusters)', truncate_mode='lastp', p=12)
if __name__ == "__main__":
    main()