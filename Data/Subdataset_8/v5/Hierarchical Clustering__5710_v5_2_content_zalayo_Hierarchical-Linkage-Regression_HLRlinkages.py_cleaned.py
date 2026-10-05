import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as AgglomClustering
from libHLR import linkages as Linkages
input_path = './input/'
link_type = 'complete'
distance = 'manhattan'
R = 40
linkage_object = Linkages(distance, link_type)
linkage_object.R = R
with open(os.path.join(input_path, 'X.txt')) as file:
    X = np.loadtxt(file)
kx_file_path = os.path.join(input_path, 'kx.txt')
if not os.path.exists(kx_file_path):
    kx = np.ones(X.shape[0])
else:
    kx = np.loadtxt(kx_file_path)
last_index = len(kx) - 2
K = len(np.unique(kx[:last_index]))
L = np.array([])
for j in range(K):
    print(f'Processing linkage {j + 1} of {K}')
    idx = np.where(kx[:last_index] == j + 1)[0]
    Xi = X[idx]
    L = np.concatenate((L, linkage_object.get(Xi)))
L = np.hsplit(L, K)
linkages_file_path = os.path.join(input_path, 'linkages.txt')
np.savetxt(linkages_file_path, L, fmt='%.8f', delimiter='\t', newline='\n')