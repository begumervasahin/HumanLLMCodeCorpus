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
with open(b1 + 'b5.txt') as file:
    b5 = np.array([[float(digit) for digit in line.split()] for line in file])
if not os.path.exists(b1 + 'b6.txt'):
    b6 = np.ones((np.shape(b5)[0],))
else:
    b6 = np.genfromtxt(b1 + 'b6.txt')
b7 = len(b6) - 2
b8 = len(np.unique(b6[0:b7]))
a2 = 0
b9 = np.asarray([])
for j in range(b8):
    print('Processing linkage %d' % (j + 1), ' of %d' % b8)
    a2 = np.where(b6[0:b7] == j + 1)
    b10 = b5[a2, :]
    b10 = b10[0, :, :]
    b9 = np.concatenate((b9, b4.get(b10)))
b9 = np.hsplit(b9, b8)
np.savetxt(b1 + 'linkages.txt', b9, b11 = '%.8f',
                                b12 = '\t',newline='\n')