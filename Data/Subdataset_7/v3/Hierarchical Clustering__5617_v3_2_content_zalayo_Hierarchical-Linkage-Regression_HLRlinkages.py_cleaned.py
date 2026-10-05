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
    b5 = np.array([[float(digit) for digit in line.split()] for line in file])
if os.path.exists(os.path.join(b1, 'b6.txt')):
    b6 = np.genfromtxt(os.path.join(b1, 'b6.txt'))
else:
    b6 = np.ones((b5.shape[0],))
b7 = len(b6) - 2
b8 = len(np.unique(b6[:b7]))
b9 = np.array([])
for j in range(b8):
    print(f'Processing b12 {j + 1} of {b8}')
    b10 = np.where(b6[:b7] == j + 1)[0]
    b11 = b5[b10]
    b12 = b4.get(b11)
    b9 = np.concatenate((b9, b12))
b9 = np.hsplit(b9, b8)
np.savetxt(os.path.join(b1, 'linkages.txt'), b9, b13 = '%.8f', delimiter='\t', newline='\n')