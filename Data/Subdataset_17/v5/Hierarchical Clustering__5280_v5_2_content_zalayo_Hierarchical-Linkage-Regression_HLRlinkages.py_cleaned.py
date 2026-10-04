import os
import numpy as np
from libHLR import linkages as link
def load_data(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def initialize_kx(file_path, num_samples):
    if os.path.exists(file_path):
        return np.genfromtxt(file_path)
    else:
        return np.ones(num_samples)
def compute_linkages(X, kx, linkage_obj, num_clusters):
    linkage_results = np.array([])
    for cluster_idx in range(num_clusters):
        print(f'Processing linkage {cluster_idx + 1} of {num_clusters}')
        cluster_indices = np.where(kx[:-1] == cluster_idx + 1)
        cluster_data = X[cluster_indices][0]
        linkage_result = linkage_obj.get(cluster_data)
        linkage_results = np.concatenate((linkage_results, linkage_result))
    return linkage_results
def save_linkages(linkage_results, output_file, num_clusters):
    linkage_results_split = np.hsplit(linkage_results, num_clusters)
    np.savetxt(output_file, linkage_results_split, fmt='%.8f', delimiter='\t', newline='\n')
def main():
    input_path = './input/'
    link_type = 'complete'
    distance_metric = 'manhattan'
    R = 40
    linkage_obj = link(distance_metric, link_type)
    linkage_obj.R = R
    X = load_data(os.path.join(input_path, 'X.txt'))
    kx = initialize_kx(os.path.join(input_path, 'kx.txt'), X.shape[0])
    last_index = len(kx) - 2
    num_clusters = len(np.unique(kx[:last_index]))
    linkage_results = compute_linkages(X, kx, linkage_obj, num_clusters)
    output_file = os.path.join(input_path, 'linkages.txt')
    save_linkages(linkage_results, output_file, num_clusters)
    print(f'Linkages saved to {output_file}')
if __name__ == "__main__":
    main()