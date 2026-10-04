import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename):
    with open(filename, 'rb') as f:
        b1 = f.read()
    b1 = bytearray(b1)
    b1 = np.array(b1[16:], dtype='float64') > 100.
    return b1
def fonk2(filename):
    with open(filename, 'rb') as f:
        b2 = f.read()
    b2 = bytearray(b2)
    b2 = np.array(b2[8:])
    return b2
def fonk3(b1, b3 = 400, cols=20):
    b4 = 28 * 28
    b5 = b3
    b6 = plt.figure(figsize=(10, 10))
    for a1 in range(b3):
        b7 = b6.add_subplot(b5, cols, a1 + 1)
        plt.imshow(b1[a1*b4:(a1+1)*b4].reshape(28, 28), b8 = plt.cm.bone)
        b7.set_axis_off()
    plt.show()
def fonk4(b2, b18):
    b9 = np.bincount(b2, minlength=b18)
    b10 = b9 / len(b2)
    b11 = np.log10(b10)
    return b11
def fonk5(b1, b2, b18, num_features):
    b12 = np.zeros((b18, num_features), dtype='float64')
    for i in range(b18):
        b13 = (b2 == i)
        b12[i] = (np.sum(b1[b13], b14 = 0, dtype='float64') + 1.) / (np.sum(b13) + b18)
    b15 = np.log10(b12)
    b16 = np.log10(1. - b12)
    return b15, b16
def fonk6(b26, b25, b15, b16):
    b17 = b26.shape[0]
    b18 = b25.shape[0]
    b19 = np.zeros(b17, dtype=int)
    for i in range(b17):
        b20 = np.sum(b15[:, b26[i].reshape(-1)], b14=1) + \
                         np.sum(b16[:, np.logical_not(b26[i].reshape(-1))], b14 = 1)
        b21 = b25 + b20
        b19[i] = np.argmax(b21)
    return b19
def fonk7():
    b22 = fonk1('train-b1.idx3-ubyte')
    b23 = fonk2('train-b2.idx1-ubyte')
    fonk3(b22)
    b4 = 28 * 28
    b24 = b22.shape[0]
    b22 = b22.reshape(int(b24), b4)
    a1 = 10
    b25 = fonk4(b23, a1)
    b15, b16 = fonk5(b22, b23, a1, b4)
    b26 = fonk1('t10k-b1.idx3-ubyte')
    b27 = fonk2('t10k-b2.idx1-ubyte')
    b28 = b26.shape[0]
    b26 = b26.reshape(int(b28), b4)
    b29 = fonk6(b26, b25, b15, b16)
    b30 = np.mean(b27 == b29)
    print("Naive Bayes classifier classification b30:", b30 * 100., '%')
if b31 = = "__main__":
    fonk7()