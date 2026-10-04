import os
import numpy as np
from libHLR import b5 as link
b1 = './input/'
b2 = 'complete'
b3 = 'manhattan'
a1 = 40
def fonk1(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def fonk2(input_path):
    b4 = os.path.join(input_path, 'b13.txt')
    if os.path.exists(b4):
        return np.genfromtxt(b4)
    else:
        return np.ones(b12.shape[0])
def fonk3(b12, b13, b15, b10):
    b5 = []
    for j in range(b15):
        print(f'Processing linkage {j + 1} of {b15}')
        b6 = np.where(b13[:b14] == j + 1)
        b7 = b12[b6][0]
        b8 = b10.get(b7)
        b5.append(b8)
    return np.hstack(b5)
def fonk4(b5, output_file):
    np.savetxt(output_file, b5, b9 = '%.8f', delimiter='\t', newline='\n')
    print(f'Linkages saved to {output_file}')
def fonk5():
    b10 = link(b3, b2)
    b10.b11 = a1
    b12 = fonk1(os.path.join(b1, 'b12.txt'))
    b13 = fonk2(b1)
    b14 = len(b13) - 2
    b15 = len(np.unique(b13[:b14]))
    b5 = fonk3(b12, b13, b15, b10)
    fonk4(b5, os.path.join(b1, 'b5.txt'))
if b16 = = "__main__":
    fonk5()