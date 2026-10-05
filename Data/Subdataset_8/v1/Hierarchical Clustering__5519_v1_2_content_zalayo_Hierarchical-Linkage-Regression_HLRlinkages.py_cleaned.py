import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as agglom
from libHLR import linkages as link
input_path = './input/'
link_type = 'complete'
distance = 'manhattan'
R = 40
xLink = link(distance, link_type)
xLink.R = R
with open(input_path + 'X.txt') as file:
    X = np.array([[float(digit) for digit in line.split()] for line in file])
if not os.path.exists(input_path + 'kx.txt'):
    kx = np.ones((np.shape(X)[0],))
else:
    kx = np.genfromtxt(input_path + 'kx.txt')
last_indx = len(kx) - 2
K = len(np.unique(kx[0:last_indx]))
idx = 0
L = np.asarray([])
for j in range(K):
    print('Processing linkage %d of %d' % (j + 1, K))
    idx = np.where(kx[0:last_indx] == j + 1)
    Xi = X[idx, :][0]
    L = np.concatenate((L, xLink.get(Xi)))
L = np.hsplit(L, K)
np.savetxt(input_path + 'linkages.txt', L, fmt='%.8f', delimiter='\t', newline='\n')