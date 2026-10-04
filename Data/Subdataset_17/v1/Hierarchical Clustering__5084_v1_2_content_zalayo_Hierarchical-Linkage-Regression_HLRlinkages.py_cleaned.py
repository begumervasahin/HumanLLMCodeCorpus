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
with open(os.path.join(input_path, 'X.txt')) as file:
    X = np.array([[float(digit) for digit in line.split()] for line in file])
kx_path = os.path.join(input_path, 'kx.txt')
if not os.path.exists(kx_path):
    kx = np.ones(X.shape[0])
else:
    kx = np.genfromtxt(kx_path)
last_index = len(kx) - 2
K = len(np.unique(kx[:last_index]))
linkages = []
for j in range(K):
    print(f'Processing linkage {j + 1} of {K}')
    idx = np.where(kx[:last_index] == j + 1)
    Xi = X[idx]
    Xi = Xi[0]
    linkage_result = x_link.get(Xi)
    linkages.append(linkage_result)
linkages_array = np.hstack(linkages)
output_file = os.path.join(input_path, 'linkages.txt')
np.savetxt(output_file, linkages_array, fmt='%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {output_file}')