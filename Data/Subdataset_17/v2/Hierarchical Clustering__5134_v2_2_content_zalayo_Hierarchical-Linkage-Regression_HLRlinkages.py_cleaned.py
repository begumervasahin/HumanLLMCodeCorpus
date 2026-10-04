import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as agglom
from libHLR import linkages as link
input_path = './input/'
link_type = 'complete'
distance_metric = 'manhattan'
R = 40
x_link = link(distance_metric, link_type)
x_link.R = R
x_file_path = os.path.join(input_path, 'X.txt')
with open(x_file_path) as file:
    X = np.array([[float(value) for value in line.split()] for line in file])
kx_file_path = os.path.join(input_path, 'kx.txt')
if os.path.exists(kx_file_path):
    kx = np.genfromtxt(kx_file_path)
else:
    kx = np.ones(X.shape[0])
last_index = len(kx) - 2
K = len(np.unique(kx[:last_index]))
linkage_results = []
for j in range(K):
    print(f'Processing linkage {j + 1} of {K}')
    cluster_indices = np.where(kx[:last_index] == j + 1)
    cluster_data = X[cluster_indices][0]
    linkage_result = x_link.get(cluster_data)
    linkage_results.append(linkage_result)
linkages_array = np.hstack(linkage_results)
output_file = os.path.join(input_path, 'linkages.txt')
np.savetxt(output_file, linkages_array, fmt='%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {output_file}')