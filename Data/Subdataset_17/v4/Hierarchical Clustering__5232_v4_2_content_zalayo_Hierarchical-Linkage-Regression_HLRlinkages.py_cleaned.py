import os
import numpy as np
from libHLR import linkages as link
input_path = './input/'
link_type = 'complete'
distance_metric = 'manhattan'
R = 40
linkage_obj = link(distance_metric, link_type)
linkage_obj.R = R
x_file_path = os.path.join(input_path, 'X.txt')
with open(x_file_path) as file:
    X = np.array([[float(value) for value in line.split()] for line in file])
kx_file_path = os.path.join(input_path, 'kx.txt')
if os.path.exists(kx_file_path):
    kx = np.genfromtxt(kx_file_path)
else:
    kx = np.ones(X.shape[0])
last_index = len(kx) - 2
num_clusters = len(np.unique(kx[:last_index]))
linkage_results = np.asarray([])
for cluster_idx in range(num_clusters):
    print(f'Processing linkage {cluster_idx + 1} of {num_clusters}')
    indices = np.where(kx[:last_index] == cluster_idx + 1)
    cluster_data = X[indices]
    cluster_data = cluster_data[0]
    linkage_result = linkage_obj.get(cluster_data)
    linkage_results = np.concatenate((linkage_results, linkage_result))
linkage_results = np.hsplit(linkage_results, num_clusters)
output_file = os.path.join(input_path, 'linkages.txt')
np.savetxt(output_file, linkage_results, fmt='%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {output_file}')