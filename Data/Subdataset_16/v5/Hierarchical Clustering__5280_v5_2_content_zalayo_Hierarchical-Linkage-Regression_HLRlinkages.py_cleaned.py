import os
import numpy as np
from libHLR import linkages as link
def fonk1(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def fonk2(file_path, num_samples):
    if os.path.exists(file_path):
        return np.genfromtxt(file_path)
    else:
        return np.ones(num_samples)
def fonk3(b11, b12, b10, b14):
    b1 = np.array([])
    for cluster_idx in range(b14):
        print(f'Processing linkage {cluster_idx + 1} of {b14}')
        b2 = np.where(b12[:-1] == cluster_idx + 1)
        b3 = b11[b2][0]
        b4 = b10.get(b3)
        b1 = np.concatenate((b1, b4))
    return b1
def fonk4(b1, b15, b14):
    b5 = np.hsplit(b1, b14)
    np.savetxt(b15, b5, b6 = '%.8f', delimiter='\t', newline='\n')
def fonk5():
    b7 = './input/'
    b8 = 'complete'
    b9 = 'manhattan'
    a1 = 40
    b10 = link(b9, b8)
    b10.a1 = a1
    b11 = fonk1(os.path.join(b7, 'b11.txt'))
    b12 = fonk2(os.path.join(b7, 'b12.txt'), b11.shape[0])
    b13 = len(b12) - 2
    b14 = len(np.unique(b12[:b13]))
    b1 = fonk3(b11, b12, b10, b14)
    b15 = os.path.join(b7, 'linkages.txt')
    fonk4(b1, b15, b14)
    print(f'Linkages saved to {b15}')
if b16 = = "__main__":
    fonk5()