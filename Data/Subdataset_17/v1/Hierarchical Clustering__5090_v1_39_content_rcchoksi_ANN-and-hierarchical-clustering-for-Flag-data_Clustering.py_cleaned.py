import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
def load_and_scale_data(file_path):
    df = pd.read_csv(file_path)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    return scaled_data
def perform_hierarchical_clustering(data, method='average'):
    z = linkage(data, method)
    coph_corr, coph_dists = cophenet(z, pdist(data))
    max_distances = maxdists(z)
    return z, coph_corr, coph_dists, max_distances
def plot_dendrogram(z, title, truncate_mode=None, p=None):
    plt.figure(figsize=(30, 15))
    plt.title(title)
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    dendrogram(
        z,
        leaf_rotation=90.,
        leaf_font_size=10.,
        truncate_mode=truncate_mode,
        p=p,
        show_contracted=True if truncate_mode else False
    )
    plt.show()
def main():
    file_path = 'Flagdata.csv'
    scaled_data = load_and_scale_data(file_path)
    z, coph_corr, coph_dists, max_distances = perform_hierarchical_clustering(scaled_data)
    print(f'Cophenet Correlation Coefficient: {coph_corr}')
    print(f'Cophenet Pairwise Distances: {coph_dists}')
    print(f'First Cluster: {z[0]}')
    print(f'Distance Array: {max_distances}')
    plot_dendrogram(z, 'Dendrogram for Flag Data')
    plot_dendrogram(z, 'Truncated Dendrogram (Last 12 Merged Clusters)', truncate_mode='lastp', p=12)
if __name__ == "__main__":
    main()