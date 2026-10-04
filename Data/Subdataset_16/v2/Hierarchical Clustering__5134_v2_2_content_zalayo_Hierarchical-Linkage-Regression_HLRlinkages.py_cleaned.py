import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as agglom
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
b11 = []
for j in range(b10):
    print(f'Processing linkage {j + 1} of {b10}')
    b12 = np.where(b8[:b9] == j + 1)
    b13 = b6[b12][0]
    b14 = b4.get(b13)
    b11.append(b14)
b15 = np.hstack(b11)
b16 = os.path.join(b1, 'linkages.txt')
np.savetxt(b16, b15, b17 = '%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {b16}')