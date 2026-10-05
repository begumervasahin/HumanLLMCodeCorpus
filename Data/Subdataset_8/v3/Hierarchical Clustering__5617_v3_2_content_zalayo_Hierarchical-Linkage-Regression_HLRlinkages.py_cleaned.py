import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as AgglomClustering
from libHLR import linkages as Linkages
INPUT_PATH = './input/'
LINK_TYPE = 'complete'
DISTANCE = 'manhattan'
R = 40
linkage_object = Linkages(DISTANCE, LINK_TYPE)
linkage_object.R = R
with open(os.path.join(INPUT_PATH, 'X.txt')) as file:
    X = np.array([[float(digit) for digit in line.split()] for line in file])
if os.path.exists(os.path.join(INPUT_PATH, 'kx.txt')):
    kx = np.genfromtxt(os.path.join(INPUT_PATH, 'kx.txt'))
else:
    kx = np.ones((X.shape[0],))
last_index = len(kx) - 2
K = len(np.unique(kx[:last_index]))
L = np.array([])
for j in range(K):
    print(f'Processing linkage {j + 1} of {K}')
    idx = np.where(kx[:last_index] == j + 1)[0]
    Xi = X[idx]
    linkage = linkage_object.get(Xi)
    L = np.concatenate((L, linkage))
L = np.hsplit(L, K)
np.savetxt(os.path.join(INPUT_PATH, 'linkages.txt'), L, fmt='%.8f', delimiter='\t', newline='\n')