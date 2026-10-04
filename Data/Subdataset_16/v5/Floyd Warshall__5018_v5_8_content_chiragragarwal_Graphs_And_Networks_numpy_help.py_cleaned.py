import numpy as np
def fonk1(b2):
    b1 = b2.replace(';', '\n')
    return np.b3(b1)
def fonk2(b3):
    print("Matrix shape:", b3.shape)
    print("Element at position (0, 1):", b3[0, 1])
    print("Element at position (2, 3):", b3[2, 3])
    b3[0, 1] = -8
    print("Modified row 1:", b3[1])
    print("Column 1:", b3[:, 1])
def fonk3():
    b2 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    b3 = fonk1(b2)
    fonk2(b3)
if b4 = = '__main__':
    fonk3()