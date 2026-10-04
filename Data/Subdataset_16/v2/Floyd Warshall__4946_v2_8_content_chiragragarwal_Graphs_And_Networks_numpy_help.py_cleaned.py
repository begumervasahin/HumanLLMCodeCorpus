import numpy as np
def fonk1():
    b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    b2 = b1.replace(';', '\n')
    b3 = np.b3(b2)
    print(f"Matrix shape: {b3.shape}")
    print(f"Element at position (0, 1): {b3[0, 1]}")
    print(f"Element at position (2, 3): {b3[2, 3]}")
    b3[0, 1] = -8
    print(f"Modified row 1: {b3[1]}")
    print(f"Column 1: {b3[:, 1]}")
if b4 = = '__main__':
    fonk1()