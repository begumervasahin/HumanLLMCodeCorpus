import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as AgglomClustering
from libHLR import linkages as Linkages
b1 = './input/'
b2 = 'complete'
b3 = 'manhattan'
a1 = 40
b4 = Linkages(b3, b2)
b4.a1 = a1
with open(os.path.join(b1, 'b5.txt')) as file:
    b5 = np.loadtxt(file)
b6 = os.path.join(b1, 'b7.txt')
if not os.path.exists(b6):
    b7 = np.ones(b5.shape[0])
else:
    b7 = np.loadtxt(b6)
b8 = len(b7) - 2
b9 = len(np.unique(b7[:b8]))
b10 = np.array([])
for j in range(b9):
    print(f'Processing linkage {j + 1} of {b9}')
    b11 = np.where(b7[:b8] == j + 1)[0]
    b12 = b5[b11]
    b10 = np.concatenate((b10, b4.get(b12)))
b10 = np.hsplit(b10, b9)
b13 = os.path.join(b1, 'linkages.txt')
np.savetxt(b13, b10, b14 = '%.8f', delimiter='\t', newline='\n')