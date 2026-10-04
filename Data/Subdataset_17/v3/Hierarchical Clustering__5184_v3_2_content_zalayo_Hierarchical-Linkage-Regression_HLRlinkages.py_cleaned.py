import os
import numpy as np
from libHLR import linkages as link
INPUT_PATH = './input/'
LINK_TYPE = 'complete'
DISTANCE_METRIC = 'manhattan'
RADIUS = 40
def load_data(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def initialize_kx(input_path):
    kx_file_path = os.path.join(input_path, 'kx.txt')
    if os.path.exists(kx_file_path):
        return np.genfromtxt(kx_file_path)
    else:
        return np.ones(X.shape[0])
def process_clusters(X, kx, K, x_link):
    linkages = []
    for j in range(K):
        print(f'Processing linkage {j + 1} of {K}')
        cluster_indices = np.where(kx[:last_index] == j + 1)
        cluster_data = X[cluster_indices][0]
        linkage_result = x_link.get(cluster_data)
        linkages.append(linkage_result)
    return np.hstack(linkages)
def save_linkages(linkages, output_file):
    np.savetxt(output_file, linkages, fmt='%.8f', delimiter='\t', newline='\n')
    print(f'Linkages saved to {output_file}')
def main():
    x_link = link(DISTANCE_METRIC, LINK_TYPE)
    x_link.R = RADIUS
    X = load_data(os.path.join(INPUT_PATH, 'X.txt'))
    kx = initialize_kx(INPUT_PATH)
    last_index = len(kx) - 2
    K = len(np.unique(kx[:last_index]))
    linkages = process_clusters(X, kx, K, x_link)
    save_linkages(linkages, os.path.join(INPUT_PATH, 'linkages.txt'))
if __name__ == "__main__":
    main()