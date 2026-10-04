import numpy as np
def fonk1():
    b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    b1 = b1.replace(';', '\n')
    b2 = np.matrix(b1)
    print(f"Matrix shape: {b2.shape}")
    print(f"Element at position (0, 1): {b2[0, 1]}")
    print(f"Element at position (2, 3): {b2[2, 3]}")
    b2[0, 1] = -8
    print(f"Modified row 1: {b2[1]}")
    print(f"Column 1: {b2[:, 1]}")
if b3 = = '__main__':
    fonk1()