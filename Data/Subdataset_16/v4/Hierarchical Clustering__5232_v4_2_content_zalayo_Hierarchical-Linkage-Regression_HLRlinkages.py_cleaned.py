import os
import numpy as np
from libHLR import linkages as link
b1 = './input/'
b2 = 'complete'
b3 = 'manhattan'
a1 = 40
b4 = link(b3, b2)
b4.a1 = a1
b5 = os.path.join(b1, 'b6.txt')
with open(b5) as file:
    b6 = np.array([[float(value) for value in line.split()] for line in file])
b7 = os.path.join(b1, 'b8.txt')
if os.path.exists(b7):
    b8 = np.genfromtxt(b7)
else:
    b8 = np.ones(b6.shape[0])
b9 = len(b8) - 2
b10 = len(np.unique(b8[:b9]))
b11 = np.asarray([])
for cluster_idx in range(b10):
    print(f'Processing linkage {cluster_idx + 1} of {b10}')
    b12 = np.where(b8[:b9] == cluster_idx + 1)
    b13 = b6[b12]
    b13 = b13[0]
    b14 = b4.get(b13)
    b11 = np.concatenate((b11, b14))
b11 = np.hsplit(b11, b10)
b15 = os.path.join(b1, 'linkages.txt')
np.savetxt(b15, b11, b16 = '%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {b15}')