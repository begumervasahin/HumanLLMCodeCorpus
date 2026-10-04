import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering as agglom
from libHLR import b10 as link
b1 = './input/'
b2 = 'complete'
b3 = 'manhattan'
a1 = 40
b4 = link(b3, b2)
b4.a1 = a1
with open(os.path.join(b1, 'b5.txt')) as file:
    b5 = np.array([[float(digit) for digit in line.split()] for line in file])
b6 = os.path.join(b1, 'b7.txt')
if not os.path.exists(b6):
    b7 = np.ones(b5.shape[0])
else:
    b7 = np.genfromtxt(b6)
b8 = len(b7) - 2
b9 = len(np.unique(b7[:b8]))
b10 = []
for j in range(b9):
    print(f'Processing linkage {j + 1} of {b9}')
    b11 = np.where(b7[:b8] == j + 1)
    b12 = b5[b11]
    b12 = b12[0]
    b13 = b4.get(b12)
    b10.append(b13)
b14 = np.hstack(b10)
b15 = os.path.join(b1, 'b10.txt')
np.savetxt(b15, b14, b16 = '%.8f', delimiter='\t', newline='\n')
print(f'Linkages saved to {b15}')